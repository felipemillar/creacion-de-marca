# 🤖 Agentes de Automatización de Investigación (NotebookLM)

Esta carpeta contiene los scripts ("agentes") de Python que automatizan la conexión, carga de documentos, búsquedas en la web e interrogación de cuadernos de **NotebookLM** utilizando la API de `notebooklm_mcp`.

---

## 📋 Requisitos de Ejecución

Los scripts están diseñados para ejecutarse de forma nativa utilizando el entorno de Python aislado de la herramienta `notebooklm-mcp-server` de tu sistema. Esto evita conflictos de librerías y garantiza que `notebooklm_mcp` esté disponible.

### 1. Entorno de Python
Para ejecutar cualquier script, utiliza el entorno virtual donde esté instalado `notebooklm_mcp` (por ejemplo con `uv` o el venv del proyecto):
```bash
# Con uv (entorno aislado del MCP server):
uv run --with notebooklm-mcp python agentes/[nombre_del_script.py]

# O directamente con python en tu entorno activo:
python agentes/[nombre_del_script.py]
```

### 2. Autenticación y Credenciales
Los agentes se conectan a tu cuenta de Google NotebookLM utilizando los tokens de sesión cacheados por el servidor.
*   **Archivo de Tokens:** Los scripts buscan las credenciales en `~/.notebooklm-mcp/auth.json`.
*   **Renovación:** Si los tokens expiran y los scripts muestran errores de autorización, ejecuta el siguiente comando en tu terminal para actualizar la sesión en tu navegador y renovar los tokens cacheados:
    ```bash
    notebooklm-mcp-auth
    ```

---

## 🛠️ Descripción de los Agentes

### 1. 📂 `notebook_research.py`
Este script inicializa el cuaderno principal de la metodología en NotebookLM y le suministra la documentación base teórica del proyecto.
*   **Propósito:** Crear el cuaderno de trabajo y cargar los archivos fuente iniciales para consultarlos.
*   **Acciones:**
    1.  Verifica si existe el cuaderno `"Metodología y Método para la Creación de Marca"`; si no existe, lo crea.
    2.  Lee los archivos teóricos locales desde `investigacion/fuentes_maestras/`:
        *   `Neurociencia y Creación de Marca_ Investigación Profunda.md`
        *   `Técnicas Modernas de Creación de Marca_ Teoría.md`
    3.  Los carga automáticamente en el cuaderno como fuentes de texto (`add_text_source`).
    4.  Ejecuta 4 consultas teóricas base y guarda las respuestas estructuradas en la carpeta `investigacion/` (archivos `resumen_*.md`).
*   **Comando de Ejecución:**
    ```bash
    python agentes/notebook_research.py
    ```

---

### 2. 🔍 `notebook_research_expand.py`
Este agente expande de forma autónoma la base teórica de la marca realizando búsquedas en internet y creando nuevos cuadernos específicos de investigación.
*   **Propósito:** Recopilar nuevas fuentes web de manera automatizada y guardarlas en NotebookLM.
*   **Acciones:**
    1.  Crea dos nuevos cuadernos dedicados:
        *   `"Investigación: Neurobranding y Biometría"`
        *   `"Investigación: Brand Optimization for Agents (BOA)"`
    2.  Lanza búsquedas en la web mediante el comando de investigación de NotebookLM (`start_research` en modo rápido).
    3.  Monitorea el progreso de la búsqueda en la web mediante polling.
    4.  Importa automáticamente las 10 fuentes web más relevantes descubiertas por el motor de NotebookLM a cada cuaderno correspondiente.
    5.  Registra un historial en la bitácora [registro_nuevos_cuadernos.md](file:///Users/fmillar/Proyectos_Desarrollo/Creacion%20de%20marca/investigacion/registro_nuevos_cuadernos.md).
*   **Comando de Ejecución:**
    ```bash
    python agentes/notebook_research_expand.py
    ```

---

### 3. 💬 `query_new_notebooks.py`
Este script se encarga de interrogar a los nuevos cuadernos creados por el agente de expansión para extraer insights específicos.
*   **Propósito:** Obtener la síntesis estructurada de las nuevas fuentes web sin necesidad de ingresar al navegador.
*   **Acciones:**
    1.  Se conecta simultáneamente a los dos nuevos cuadernos creados mediante sus IDs correspondientes.
    2.  Realiza consultas sobre metodologías biométricas específicas, detalles de casos de estudio corporativos, directrices de cumplimiento ético de neuroderechos, plantillas de apilamiento de esquemas JSON-LD, y optimizaciones GEO en 2026.
    3.  Guarda los resultados estructurados en formato Markdown en la carpeta `investigacion/` (archivos [insights_neurobranding.md](file:///Users/fmillar/Proyectos_Desarrollo/Creacion%20de%20marca/investigacion/insights_neurobranding.md) e [insights_boa.md](file:///Users/fmillar/Proyectos_Desarrollo/Creacion%20de%20marca/investigacion/insights_boa.md)).
*   **Comando de Ejecución:**
    ```bash
    python agentes/query_new_notebooks.py
    ```

---

## 📈 Flujo de Integración Teórica

```
 ┌───────────────────────────┐      ┌───────────────────────────┐      ┌───────────────────────────┐
 │  notebook_research.py     │ ───> │ notebook_research_exp...  │ ───> │  query_new_notebooks.py   │
 │                           │      │                           │      │                           │
 │ • Carga docs del workspace│      │ • Crea 2 cuadernos nuevos │      │ • Extrae los tecnicismos  │
 │ • Resuelve bases teóricas │      │ • Rastrea la web (20 docs)│      │   y benchmarks avanzados  │
 └───────────────────────────┘      └───────────────────────────┘      └───────────────────────────┘
               │                                                                      │
               ▼                                                                      ▼
 ┌───────────────────────────┐                                          ┌───────────────────────────┐
 │    resumen_*.md           │                                          │     insights_*.md         │
 │  (Teoría y Neuro-bases)   │                                          │  (Métricas de biometría)  │
 └───────────────────────────┘                                          └───────────────────────────┘
```

> [!TIP]
> **Extensibilidad:** Si deseas investigar un nuevo tema (por ejemplo, *Branding en el Metaverso*), puedes editar la lista `researches` en `notebook_research_expand.py` con un nuevo título y consulta. Al ejecutarlo, se creará el cuaderno, se buscarán fuentes en la web y se importarán automáticamente.
