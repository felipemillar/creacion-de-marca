import os
import sys
import time

# Asegurar que importamos del path correcto de anaconda3
sys.path.insert(0, "/opt/anaconda3/lib/python3.12/site-packages")

try:
    from notebooklm_mcp.auth import load_cached_tokens
    from notebooklm_mcp.api_client import NotebookLMClient
except ImportError as e:
    print(f"Error importando notebooklm_mcp: {e}")
    sys.exit(1)

def main():
    print("Cargando tokens de autenticación...")
    tokens = load_cached_tokens()
    if not tokens:
        print("Error: No se encontraron tokens guardados. Ejecuta 'notebooklm-mcp-auth' primero.")
        sys.exit(1)
        
    print("Inicializando NotebookLMClient...")
    client = NotebookLMClient(
        cookies=tokens.cookies,
        csrf_token=tokens.csrf_token,
        session_id=tokens.session_id
    )
    
    notebook_title = "Metodología y Método para la Creación de Marca"
    print(f"Buscando si existe el cuaderno '{notebook_title}'...")
    notebooks = client.list_notebooks()
    target_nb = None
    for nb in notebooks:
        if nb.title == notebook_title:
            target_nb = nb
            break
            
    if target_nb:
        print(f"Cuaderno existente encontrado. ID: {target_nb.id}")
    else:
        print(f"Creando nuevo cuaderno '{notebook_title}'...")
        target_nb = client.create_notebook(title=notebook_title)
        if not target_nb:
            print("Error creando el cuaderno.")
            sys.exit(1)
        print(f"Cuaderno creado. ID: {target_nb.id}")
        
    # Obtener fuentes actuales del cuaderno
    print("Obteniendo fuentes del cuaderno...")
    sources = client.get_notebook_sources_with_types(target_nb.id)
    existing_titles = [src["title"] for src in sources]
    print(f"Fuentes actuales: {existing_titles}")
    
    # Cargar documento 1
    doc1_title = "Neurociencia y Creación de Marca - Investigación Profunda"
    doc1_path = "/Users/fmillar/Proyectos_Desarrollo/Creacion de marca/Neurociencia y Creación de Marca_ Investigación Profunda.md"
    if doc1_title in existing_titles:
        print(f"La fuente '{doc1_title}' ya existe en el cuaderno.")
    else:
        print(f"Leyendo e importando '{doc1_title}'...")
        if os.path.exists(doc1_path):
            with open(doc1_path, "r", encoding="utf-8") as f:
                text = f.read()
            res = client.add_text_source(target_nb.id, text=text, title=doc1_title)
            print(f"Fuente agregada: {res}")
            time.sleep(2)  # Pausa de seguridad
        else:
            print(f"Error: No se encontró el archivo en {doc1_path}")
            
    # Cargar documento 2
    doc2_title = "Técnicas Modernas de Creación de Marca - Teoría"
    doc2_path = "/Users/fmillar/Proyectos_Desarrollo/Creacion de marca/Técnicas Modernas de Creación de Marca_ Teoría.md"
    if doc2_title in existing_titles:
        print(f"La fuente '{doc2_title}' ya existe en el cuaderno.")
    else:
        print(f"Leyendo e importando '{doc2_title}'...")
        if os.path.exists(doc2_path):
            with open(doc2_path, "r", encoding="utf-8") as f:
                text = f.read()
            res = client.add_text_source(target_nb.id, text=text, title=doc2_title)
            print(f"Fuente agregada: {res}")
            time.sleep(2)  # Pausa de seguridad
        else:
            print(f"Error: No se encontró el archivo en {doc2_path}")

    # Consultar para extraer información valiosa
    print("\n--- Ejecutando consultas de investigación teórica ---")
    
    queries = {
        "resumen_neurociencia": "Explica la hipótesis del marcador somático de Damasio, el papel de la amígdala y corteza prefrontal ventromedial, y cómo se relaciona con el Sistema 1 del consumidor. Extrae también los detalles del caso Frito-Lay (mate vs brillante, y el test de Cheetos de venganza en la lavandería) y Hyundai (biometría EEG del cerebro límbico).",
        "resumen_marcas_teoria": "Resume los marcos de Kevin Lane Keller (CBBE), Lógica Dominante de Servicio (S-D Logic) y cocreación de Vargo y Lusch, Teoría de Identidad Social y Identity Signaling de Jonah Berger, y las Comunidades de Marca de Muniz y O'Guinn (conciencia compartida, rituales, responsabilidad moral).",
        "resumen_estetica_y_ux": "Resume las Leyes de UX (Hick, Jakob, Prägnanz, Fitts) aplicadas al branding visual y digital, y el Branding Sensorial (Martin Lindstrom) con la sinergia intermodal (incluyendo las refracciones del color de Coca-Cola y el olfato).",
        "resumen_arquetipos_y_activacion": "Resume los Arquetipos de Marca de Mark & Pearson alineados con los cuatro vectores de motivación humana (Exploración, Cambio, Conexión, Estructura). Explica también la optimización de marcas para agentes de IA (indexabilidad semántica conversacional) y las consideraciones éticas de Neuroderechos (Rafael Yuste)."
    }
    
    scratch_dir = "/Users/fmillar/.gemini/antigravity-ide/brain/11be0cf2-22c5-4aee-afdc-f19c56155c20/scratch"
    os.makedirs(scratch_dir, exist_ok=True)
    
    for key, query_text in queries.items():
        out_file = os.path.join(scratch_dir, f"{key}.md")
        if os.path.exists(out_file) and os.path.getsize(out_file) > 1000:
            print(f"La consulta '{key}' ya ha sido guardada anteriormente.")
            continue
            
        print(f"Consultando NotebookLM sobre '{key}'...")
        res = client.query(target_nb.id, query_text=query_text, timeout=180)
        if res and isinstance(res, dict) and "answer" in res:
            answer = res["answer"]
            with open(out_file, "w", encoding="utf-8") as out_f:
                out_f.write(f"# Consulta: {key}\n\n{answer}\n")
            print(f"Resultado guardado en {out_file}")
            time.sleep(3)  # Pausa de seguridad
        else:
            print(f"Error consultando '{key}': {res}")

    print("\n¡Proceso de investigación autónoma de NotebookLM completado con éxito!")

if __name__ == "__main__":
    main()
