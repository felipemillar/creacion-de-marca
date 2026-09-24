import os
import sys
import time
from pathlib import Path

# Paths relativos al proyecto
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "investigacion"

# Soporte opcional para virtualenvs locales
uv_packages = Path.home() / ".local/share/uv/tools/notebooklm-mcp-server/lib/python3.12/site-packages"
if uv_packages.exists():
    sys.path.insert(0, str(uv_packages))

try:
    from notebooklm_mcp.auth import load_cached_tokens
    from notebooklm_mcp.api_client import NotebookLMClient
except ImportError as err:
    print(f"Error importando notebooklm_mcp: {type(err).__name__} (detalles omitidos por seguridad)")
    sys.exit(1)

def run_research_flow(client, title, query):
    print(f"\n========================================\nIniciando proceso para: '{title}'\n========================================")
    
    # 1. Crear cuaderno
    print(f"Creando cuaderno en NotebookLM...")
    nb = client.create_notebook(title=title)
    if not nb:
        print("Error: No se pudo crear el cuaderno.")
        return None
    notebook_id = nb.id
    notebook_url = f"https://notebooklm.google.com/notebook/{notebook_id}"
    print(f"Cuaderno creado exitosamente. ID: {notebook_id} | URL: {notebook_url}")
    
    # 2. Iniciar investigación (modo rápido para optimizar tiempos)
    print(f"Iniciando búsqueda web sobre: '{query}'...")
    res_start = client.start_research(notebook_id, query=query, source="web", mode="fast")
    if not res_start or "task_id" not in res_start:
        print("Error: No se pudo iniciar el proceso de investigación.")
        return {
            "title": title,
            "id": notebook_id,
            "url": notebook_url,
            "status": "failed_start",
            "sources_imported": 0
        }
    task_id = res_start["task_id"]
    print(f"Búsqueda web iniciada. Task ID: {task_id}")
    
    # 3. Monitorear progreso (polling)
    print("Esperando a que se complete la búsqueda (polling)...")
    sources = []
    attempts = 0
    max_attempts = 15  # Máximo de ~3.5 minutos
    
    while attempts < max_attempts:
        time.sleep(15)
        attempts += 1
        print(f"  [Intento {attempts}] Consultando estado...")
        res_poll = client.poll_research(notebook_id, target_task_id=task_id)
        
        if not res_poll:
            print("  [Advertencia] No se obtuvo respuesta del estado (reintentando).")
            continue
            
        status = res_poll.get("status")
        print(f"  Estado actual: {status}")
        
        if status == "completed":
            sources = res_poll.get("sources", [])
            print(f"  Búsqueda completada. Encontradas {len(sources)} fuentes potenciales.")
            break
            
    if not sources:
        print("Error o tiempo de espera agotado. No se descubrieron fuentes.")
        return {
            "title": title,
            "id": notebook_id,
            "url": notebook_url,
            "status": "timeout_or_empty",
            "sources_imported": 0
        }
        
    # 4. Importar fuentes
    print(f"Importando {len(sources)} fuentes descubiertas al cuaderno...")
    imported = client.import_research_sources(notebook_id, task_id, sources)
    print(f"Importación completada. {len(imported)} fuentes importadas con éxito.")
    
    return {
        "title": title,
        "id": notebook_id,
        "url": notebook_url,
        "status": "success",
        "sources_imported": len(imported),
        "imported_list": [s.get("title", "Untitled") for s in imported]
    }

def main():
    print("Cargando credenciales de NotebookLM...")
    tokens = load_cached_tokens()
    if not tokens:
        print("Error: No se encontraron credenciales. Ejecuta 'notebooklm-mcp-auth'.")
        sys.exit(1)
        
    client = NotebookLMClient(
        cookies=tokens.cookies,
        csrf_token=tokens.csrf_token,
        session_id=tokens.session_id
    )
    
    researches = [
        {
            "title": "Investigación: Neurobranding y Biometría",
            "query": "Neuromarketing and neurobranding case studies biometric testing EEG fMRI eye tracking"
        },
        {
            "title": "Investigación: Brand Optimization for Agents (BOA)",
            "query": "Brand Optimization for Agents BOA AI search engine recommendation indexability semántica conversacional"
        }
    ]
    
    resultados = []
    for res_info in researches:
        try:
            res = run_research_flow(client, res_info["title"], res_info["query"])
            if res:
                resultados.append(res)
        except Exception as err:
            print(f"Error procesando '{res_info['title']}': {type(err).__name__} (detalles omitidos por seguridad)")
            resultados.append({
                "title": res_info["title"],
                "status": "error",
                "error": f"Error: {type(err).__name__}"
            })
            
    # Generar bitácora en Markdown
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    bitacora_path = OUTPUT_DIR / "registro_nuevos_cuadernos.md"
    print(f"\nEscribiendo bitácora de resultados en: {bitacora_path.name}...")
    
    with open(bitacora_path, "w", encoding="utf-8") as f:
        f.write("# Bitácora: Nuevos Cuadernos de Investigación Creados\n\n")
        f.write("Esta bitácora registra de forma autónoma los cuadernos de NotebookLM creados e investigados en la web para expandir nuestras fuentes teóricas.\n\n")
        
        for r in resultados:
            f.write(f"## {r['title']}\n")
            if r.get("status") == "success":
                f.write(f"*   **Estado:** Completado exitosamente.\n")
                f.write(f"*   **ID del Cuaderno:** `{r['id']}`\n")
                f.write(f"*   **URL:** [{r['title']}]({r['url']})\n")
                f.write(f"*   **Fuentes Importadas:** {r['sources_imported']}\n\n")
                f.write("### Fuentes Importadas:\n")
                for s_title in r.get("imported_list", []):
                    f.write(f"*   {s_title}\n")
            else:
                f.write(f"*   **Estado:** Fallido.\n")
                f.write(f"*   **Detalle:** {r.get('error', 'Tiempo de espera agotado o sin fuentes.')}\n")
            f.write("\n---\n\n")
            
    print("¡Proceso de investigación expandida completado con éxito!")

if __name__ == "__main__":
    main()
