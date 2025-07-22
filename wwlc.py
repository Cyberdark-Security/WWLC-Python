#!/usr/bin/env python3
import argparse
import re
import sys
import io
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import requests # <-- Re-añadimos requests

try:
    from playwright.sync_api import sync_playwright, Error
    from pypdf import PdfReader
except ImportError:
    print("[-] Faltan librerías. Ejecuta 'pip install -r requirements.txt'", file=sys.stderr)
    sys.exit(1)


# ... (Las funciones clean_and_split_words, split_compound_words, generate_variations, y process_document_metadata no cambian)...
def clean_and_split_words(text):
    text = str(text).lower()
    words = re.findall(r'[a-zA-Z0-9_-]+', text)
    filtered_words = [
        word for word in words 
        if not word.isdigit() and 3 <= len(word) <= 50
    ]
    return filtered_words

def split_compound_words(word, min_part_length=3):
    parts = [word] if len(word) < 6 else [word] + [p for i in range(min_part_length, len(word) - min_part_length + 1) for p in [word[:i], word[i:]] if len(p) >= min_part_length]
    return list(dict.fromkeys(parts))

def generate_variations(word):
    variations = {word}
    if word.endswith('s') and len(word) > 4: variations.add(word[:-1])
    if word.endswith('ed') and len(word) > 5: variations.add(word[:-2])
    if word.endswith('ing') and len(word) > 6: variations.add(word[:-3])
    for num in ['1', '2', '3', '2024', '2025']: variations.add(word + num)
    return list(variations)

def process_document_metadata(url, content, found_meta_data):
    if not url.endswith('.pdf'): return
    print(f"[+] Analizando metadatos de PDF: {url}")
    try:
        pdf_file = io.BytesIO(content)
        reader = PdfReader(pdf_file)
        meta = reader.metadata
        if meta.author:
            print(f"    -> Autor encontrado: {meta.author}")
            found_meta_data.add(meta.author.strip())
        if meta.creator:
            print(f"    -> Creador encontrado: {meta.creator}")
            found_meta_data.add(meta.creator.strip())
    except Exception as e:
        print(f"    -> No se pudo procesar el PDF: {e}", file=sys.stderr)



def main():
    parser = argparse.ArgumentParser(description='Genera diccionario desde sitios web, sus APIs y documentos.')
    # ... (argumentos no cambian) ...
    parser.add_argument('url', help='URL de la página web a analizar')
    parser.add_argument('-o', '--output', default='wordlist.txt', help='Archivo de salida para la lista de palabras.')
    parser.add_argument('-e', '--email', action='store_true', help='Extraer direcciones de correo electrónico')
    parser.add_argument('--email-file', help='Archivo de salida para los correos electrónicos')
    parser.add_argument('-a', '--meta', action='store_true', help='Extraer metadatos de los archivos (ej: PDF)')
    parser.add_argument('--meta-file', help='Archivo de salida para los datos de metadatos')
    parser.add_argument('--min-length', type=int, default=3, help='Longitud mínima de palabras.')
    parser.add_argument('--max-length', type=int, default=20, help='Longitud máxima de palabras.')
    parser.add_argument('--no-split', action='store_true', help='No dividir palabras compuestas')
    parser.add_argument('--no-variations', action='store_true', help='No generar variaciones adicionales')
    args = parser.parse_args()

    start_url = args.url
    domain_name = urlparse(start_url).netloc
    max_depth = 1
    
    urls_to_visit = [(start_url, 0)]
    visited_urls = set()
    found_words = set()
    found_emails = set()
    found_meta_data = set()
    api_texts = []
    
    email_regex = re.compile(r'\b[a-zA-Z._%+-][a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b')
    
    # Creamos una sesión de Requests para las descargas de archivos
    request_session = requests.Session()
    request_session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})

    print(f"[+] Iniciando análisis de {start_url} con Playwright...")

    with sync_playwright() as p:
        try:
            browser = p.chromium.launch()
            context = browser.new_context(user_agent=request_session.headers['User-Agent'])
            page = context.new_page()

            def handle_response(response):
                if "application/json" in response.headers.get("content-type", ""):
                    print(f"[+] API Response Interceptada: {response.url}")
                    try:
                        api_texts.append(str(response.json()))
                    except Exception:
                        pass

            page.on("response", handle_response)
            
            while urls_to_visit:
                current_url, depth = urls_to_visit.pop(0)
                if current_url in visited_urls:
                    continue
                
                print(f"[+] Rastreado (Profundidad {depth}): {current_url}")
                visited_urls.add(current_url)

                try:
                    page.goto(current_url, wait_until="networkidle", timeout=30000)
                    content = page.content()
                    
                    soup = BeautifulSoup(content, 'html.parser')
                    for script_or_style in soup(["script", "style"]):
                        script_or_style.decompose()

                    html_text = soup.get_text(separator=' ')
                    found_words.update(clean_and_split_words(html_text))

                    if args.email:
                        found_emails.update(email_regex.findall(html_text))

                    if depth < max_depth:
                        links = soup.find_all('a', href=True)
                        for link in links:
                            href = link['href']
                            
                            if args.email and href.startswith('mailto:'):
                                found_emails.add(href.split(':')[1].split('?')[0])
                                continue
                            
                            absolute_link = urljoin(current_url, href)

                            # --- BLOQUE MODIFICADO PARA DESCARGAR PDFS CON REQUESTS ---
                            if args.meta and absolute_link.endswith('.pdf'):
                                if absolute_link not in visited_urls:
                                    download_url = absolute_link
                                    if "github.com" in download_url and "/blob/" in download_url:
                                        download_url = download_url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
                                    
                                    try:
                                        print(f"    -> Descargando documento con requests: {download_url}")
                                        doc_response = request_session.get(download_url, timeout=30)
                                        doc_response.raise_for_status() # Lanza un error si la descarga falla (ej: 404)
                                        process_document_metadata(download_url, doc_response.content, found_meta_data)
                                    except requests.exceptions.RequestException as e:
                                        print(f"    -> Error al descargar {download_url}: {e}", file=sys.stderr)
                                    
                                    visited_urls.add(absolute_link)
                                continue
                            # --- FIN DEL BLOQUE MODIFICADO ---

                            if urlparse(absolute_link).netloc == domain_name and absolute_link not in visited_urls:
                                urls_to_visit.append((absolute_link, depth + 1))
                except Exception as e:
                    print(f"    -> No se pudo procesar la URL {current_url}: {e}", file=sys.stderr)

            print("[+] Extrayendo palabras y correos de las respuestas de las APIs...")
            full_api_text = ' '.join(api_texts)
            found_words.update(clean_and_split_words(full_api_text))
            
            if args.email:
                found_emails.update(email_regex.findall(full_api_text))

            browser.close()
        except Error as e:
            print(f"\n[-] Error de Playwright: {e}", file=sys.stderr)
            sys.exit(1)

    # ... (El resto del script para procesar y guardar los resultados no cambia)...
    print("\n[+] Procesando palabras finales...")
    final_wordlist = set()
    for word in found_words:
        if args.min_length <= len(word) <= args.max_length:
            final_wordlist.add(word)
            if not args.no_split and len(word) >= 6: final_wordlist.update(split_compound_words(word))
            if not args.no_variations: final_wordlist.update(generate_variations(word))
    
    sorted_wordlist = sorted(list(final_wordlist))
    print(f"[+] Palabras totales encontradas (HTML + API): {len(sorted_wordlist)}")
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write('\n'.join(sorted_wordlist))
    print(f"[+] Lista de palabras guardada en: {args.output}")

    if args.email_file and found_emails:
        sorted_emails = sorted(list(found_emails))
        with open(args.email_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(sorted_emails))
        print(f"[+] Correos electrónicos guardados en: {args.email_file}")

    if args.meta_file and found_meta_data:
        processed_meta_words = set()
        
        # Une todas las frases de los metadatos en un solo bloque de texto
        full_meta_text = ' '.join(found_meta_data)
        
        # Usa la misma función que ya tenemos para limpiar y separar en palabras
        cleaned_words = clean_and_split_words(full_meta_text)
        processed_meta_words.update(cleaned_words)
        
        # Guarda la lista de palabras individuales y limpias
        sorted_meta = sorted(list(processed_meta_words))
        with open(args.meta_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(sorted_meta))
        print(f"[+] Metadatos (como diccionario) guardados en: {args.meta_file}")


if __name__ == "__main__":
    main()