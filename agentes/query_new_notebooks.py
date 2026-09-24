import os
import sys
import json
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
    print(f"Error importando la librería notebooklm_mcp: {type(err).__name__} (detalles omitidos por seguridad)")
    sys.exit(1)

def run_queries(client, notebook_id, queries):
    results = {}
    for key, q in queries.items():
        print(f"  Consultando: '{q}'...")
        try:
            response = client.query(notebook_id, query_text=q)
            results[key] = response.get("answer", "No answer received.")
        except Exception as err:
            print(f"  Error en consulta '{key}': {type(err).__name__} (detalles omitidos por seguridad)")
            results[key] = f"Error querying: {type(err).__name__}"
    return results

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

    # Notebook 1: Neurobranding & Biometría
    # ID parametrizable por variable de entorno si se desea
    nb1_id = os.environ.get("NOTEBOOK_NEUROBRANDING_ID", "501f20f3-1941-4617-9204-7f2380b77d6e")
    queries_nb1 = {
        "metodologias_biometricas": "What are the specific methodologies, metrics, and protocols for using EEG, eye-tracking, and GSR in branding/packaging design? Explain how they are combined (cross-modal synergy).",
        "casos_estudio": "Provide details on the neuromarketing case studies of Frito-Lay (Cheetos/packaging), Campbell's Soup, and Hyundai. What were the exact biological measurements and business results?",
        "cumplimiento_neuroderechos": "What are the latest compliance guidelines, ethical standards, and legal requirements for protecting user cognitive liberty and neuro-data (neurorights), particularly regarding Chile and Emotiv case?"
    }
    
    print("\n=== Consultando Cuaderno: Neurobranding y Biometría ===")
    results_nb1 = run_queries(client, nb1_id, queries_nb1)

    # Notebook 2: Brand Optimization for Agents (BOA)
    nb2_id = os.environ.get("NOTEBOOK_BOA_ID", "4d97cf8e-c44e-4662-a917-e4c15da97ee5")
    queries_nb2 = {
        "optimizacion_agentes_geo": "What are the technical guidelines, metrics, and optimization techniques for Generative Engine Optimization (GEO) and Brand Optimization for Agents (BOA) in 2026? How do LLMs rank/cite brands?",
        "marcado_esquemas_datos": "Explain the role of Schema Markup and structured data for AI search engine indexability. What specific schemas are recommended in 2026?",
        "auditorias_y_alucinaciones": "How do brands audit their visibility on AI search platforms (ChatGPT, Perplexity, Adobe Brand Visibility) and what strategies prevent/mitigate AI hallucinations?"
    }

    print("\n=== Consultando Cuaderno: Brand Optimization for Agents (BOA) ===")
    results_nb2 = run_queries(client, nb2_id, queries_nb2)

    # Guardar resultados en investigacion/
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    md_path_nb1 = OUTPUT_DIR / "insights_neurobranding.md"
    print(f"\nGuardando insights de Neurobranding en: {md_path_nb1.name}...")
    with open(md_path_nb1, "w", encoding="utf-8") as f:
        f.write("# Insights de Neurobranding y Biometría\n\n")
        for key, val in results_nb1.items():
            f.write(f"## {key.replace('_', ' ').title()}\n\n")
            f.write(f"{val}\n\n")

    md_path_nb2 = OUTPUT_DIR / "insights_boa.md"
    print(f"\nGuardando insights de BOA en: {md_path_nb2.name}...")
    with open(md_path_nb2, "w", encoding="utf-8") as f:
        f.write("# Insights de Brand Optimization for Agents (BOA)\n\n")
        for key, val in results_nb2.items():
            f.write(f"## {key.replace('_', ' ').title()}\n\n")
            f.write(f"{val}\n\n")

    print("\n¡Proceso de consulta de cuadernos completado!")

if __name__ == "__main__":
    main()
