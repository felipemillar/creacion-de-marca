# 🤖 Agente: Extractor de Insights (Insights Extractor Agent)

Este documento define la estructura, rol, especificaciones técnicas y de operación del **Agente Extractor de Insights**.

---

## 📋 Ficha de Identificación del Agente

*   **Nombre Oficial:** Agente Extractor de Insights (`insights-extractor-agent`)
*   **Script de Control:** [query_new_notebooks.py](file:///Users/fmillar/Proyectos_Desarrollo/Creacion%20de%20marca/agentes/query_new_notebooks.py)
*   **Plataforma Destino:** Google NotebookLM
*   **Cuadernos Consultados:**
    1.  `"Investigación: Neurobranding y Biometría"` (ID: `501f20f3-1941-4617-9204-7f2380b77d6e`)
    2.  `"Investigación: Brand Optimization for Agents (BOA)"` (ID: `4d97cf8e-c44e-4662-a917-e4c15da97ee5`)
*   **Objetivo Primario:** Interrogar los cuadernos temáticos de investigación y sintetizar las respuestas en archivos de insights técnicos.

---

## 1. Definición y Propósito

El **Agente Extractor de Insights** es la herramienta analítica final de la recolección teórica. Su propósito es interrogar simultáneamente las fuentes web importadas en los cuadernos de investigación y extraer resúmenes estructurados sobre temas muy específicos (protocolos de preprocesamiento de EEG, casos de neuromarketing reales, mitigación de alucinaciones de IA y plantillas JSON-LD de 2026).

Al automatizar la consulta y síntesis, el agente evita que el usuario tenga que ingresar a la interfaz de NotebookLM y redactar múltiples preguntas, estructurando la salida en archivos Markdown directamente en el espacio de trabajo local para alimentar y actualizar el Playbook Metodológico.

---

## 2. Arquitectura de Datos e Integración

### Inputs (Entradas)
*   **Tokens de Autenticación:** Cookies y CSRF desde `~/.notebooklm-mcp/auth.json`.
*   **IDs de Cuadernos Destino:** Los identificadores únicos de los cuadernos de investigación creados previamente.
*   **Preguntas Estructuradas:** Consultas enfocadas a extraer la parte técnica (métricas biométricas, optimización GEO, y marcado estructurado).

### Procesamiento de API (Llamadas `notebooklm_mcp`)
*   `query(notebook_id, query_text)`: Ejecuta las consultas en cada cuaderno específico para recuperar los resúmenes del conocimiento indexado.

### Outputs (Salidas en `/investigacion/`)
Genera dos archivos Markdown detallados de insights:
*   [insights_neurobranding.md](file:///Users/fmillar/Proyectos_Desarrollo/Creacion%20de%20marca/investigacion/insights_neurobranding.md): Contiene las metodologías biométricas cruzadas (EEG + Eye tracking + GSR), benchmarks del punto de venta y pautas éticas de neurodatos.
*   [insights_boa.md](file:///Users/fmillar/Proyectos_Desarrollo/Creacion%20de%20marca/investigacion/insights_boa.md): Contiene las directrices de optimización para buscadores de IA, esquemas JSON-LD stacked y auditorías de alucinaciones de RAG.

---

## 3. Flujo de Trabajo del Agente

```
   [Inicio] ──> Cargar auth.json ──> Inicializar Cliente
                                         │
                                         ▼
                             Consultas Cuaderno 1:
                             - Metodologías Biométricas
                             - Casos de Estudio Reales
                             - Cumplimiento de Neuroderechos
                                         │
                                         ▼
                             Consultas Cuaderno 2:
                             - GEO y Pautas de LLMs
                             - Esquemas de Datos Stacked
                             - Auditoría y Alucinaciones
                                         │
                                         ▼
                               Guardar Respuestas:
                         - insights_neurobranding.md
                         - insights_boa.md ───────────────> [Fin]
```

---

## 4. Manual de Operación y Comandos

### Ejecución Estándar
Para iniciar el agente y generar los reportes de insights en tu carpeta de investigación, ejecuta en tu terminal:
```bash
/Users/fmillar/.local/share/uv/tools/notebooklm-mcp-server/bin/python agentes/query_new_notebooks.py
```

### Modificación de las Preguntas Técnicas
Puedes modificar o añadir preguntas en los diccionarios `queries_nb1` (Línea 43) y `queries_nb2` (Línea 53) dentro del script para cambiar la información solicitada al modelo de lenguaje.

---

## 5. Manejo de Excepciones y Solución de Problemas

*   **Error: `NotebookLMClient object has no attribute 'notebook_query'`**
    *   *Causa:* Estás ejecutando una versión antigua del script que intentaba llamar al método erróneo de la API.
    *   *Solución:* Asegúrate de que el script llame a `client.query(notebook_id, query_text=q)` (el error ha sido subsanado en la última versión).
*   **Error: IDs de Cuadernos Incorrectos (Notebook Not Found):**
    *   *Causa:* Los IDs de los cuadernos indicados en el script (`nb1_id` y `nb2_id`) no existen o fueron eliminados en la nube.
    *   *Solución:* Verifica los IDs en tu interfaz web de NotebookLM o revisa la bitácora `registro_nuevos_cuadernos.md` y actualiza las constantes en el script.
*   **Error: Respuestas Vacías o Incompletas:**
    *   *Causa:* El servidor RAG de NotebookLM falló al recuperar la información en el momento de la consulta.
    *   *Solución:* Vuelve a ejecutar el script. Las consultas son independientes y se sobrescribirán de forma limpia en los archivos de salida.
