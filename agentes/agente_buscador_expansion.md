# 🤖 Agente: Buscador y Expansión de Fuentes (Search & Expansion Agent)

Este documento define la estructura, rol, especificaciones técnicas y de operación del **Agente Buscador y Expansión de Fuentes**.

---

## 📋 Ficha de Identificación del Agente

*   **Nombre Oficial:** Agente Buscador y Expansión de Fuentes (`search-expansion-agent`)
*   **Script de Control:** [notebook_research_expand.py](file:///Users/fmillar/Proyectos_Desarrollo/Creacion%20de%20marca/agentes/notebook_research_expand.py)
*   **Plataforma Destino:** Google NotebookLM
*   **Cuadernos Creados:**
    1.  `"Investigación: Neurobranding y Biometría"` (ID: `501f20f3-1941-4617-9204-7f2380b77d6e`)
    2.  `"Investigación: Brand Optimization for Agents (BOA)"` (ID: `4d97cf8e-c44e-4662-a917-e4c15da97ee5`)
*   **Objetivo Primario:** Expandir el ecosistema teórico mediante búsquedas web automatizadas e importación autónoma de fuentes externas en NotebookLM.

---

## 1. Definición y Propósito

El **Agente Buscador y Expansión de Fuentes** es una herramienta de enriquecimiento de conocimiento secundario. Su propósito es identificar brechas de información o requerimientos de ampliación sobre temas avanzados de marca, buscar fuentes actualizadas en la web mediante el motor de búsqueda y RAG de NotebookLM, e importar las fuentes descubiertas a cuadernos temáticos independientes.

Este agente permite mantener la metodología al día con el estado del arte técnico (por ejemplo, directrices de buscadores de IA de 2026 o metodologías de preprocesamiento de ondas de EEG), eliminando el tiempo de navegación y filtrado manual del usuario en internet.

---

## 2. Arquitectura de Datos e Integración

### Inputs (Entradas)
*   **Tokens de Autenticación:** Cookies y CSRF desde `~/.notebooklm-mcp/auth.json`.
*   **Configuración de Búsqueda:** Diccionario con títulos de cuadernos y las cadenas de términos clave en inglés para optimizar el motor de búsqueda (ej: `"Brand Optimization for Agents BOA AI search engine..."`).

### Procesamiento de API (Llamadas `notebooklm_mcp`)
*   `create_notebook(title)`: Inicializa el cuaderno de investigación específico.
*   `start_research(notebook_id, query, source="web", mode="fast")`: Dispara la búsqueda web en NotebookLM sobre los términos indicados. Retorna un `task_id` único.
*   `poll_research(notebook_id, target_task_id)`: Consulta repetitiva del estado de la búsqueda en segundo plano hasta que el estado sea `"completed"`.
*   `import_research_sources(notebook_id, task_id, sources)`: Toma las fuentes web descubiertas y las asimila formalmente como documentos del cuaderno.

### Outputs (Salidas en `/investigacion/`)
*   **Cuadernos en la Nube:** Dos cuadernos de NotebookLM provistos de 10 fuentes web de alta relevancia en cada uno.
*   **Registro Histórico (Bitácora):** Escribe el log [registro_nuevos_cuadernos.md](file:///Users/fmillar/Proyectos_Desarrollo/Creacion%20de%20marca/investigacion/registro_nuevos_cuadernos.md) detallando los IDs de los cuadernos, URLs y la lista de títulos de las fuentes web importadas con éxito.

---

## 3. Flujo de Trabajo del Agente

```
   [Inicio] ──> Cargar auth.json ──> Inicializar Cliente
                                         │
                                         ▼
                             Bucle por cada Investigación:
                                         │
                                         ▼
                                  Crear Cuaderno
                                         │
                                         ▼
                               Lanzar Búsqueda Web
                                         │
                                         ▼
                           Bucle de Polling (15s c/u):
                             - Consultar Estado
                             - ¿Completado? ── (No, reintentar)
                                  │ (Sí)
                                  ▼
                              Importar Fuentes
                                         │
                                         ▼
                        Fin Bucle de Investigaciones
                                         │
                                         ▼
                       Generar Bitácora en Markdown ──> [Fin]
```

---

## 4. Manual de Operación y Comandos

### Ejecución Estándar
Para iniciar el agente y realizar las búsquedas web con importación automática, ejecuta en tu terminal:
```bash
/Users/fmillar/.local/share/uv/tools/notebooklm-mcp-server/bin/python agentes/notebook_research_expand.py
```

### Configuración de Nuevas Investigaciones (Extensibilidad)
Para agregar nuevos temas de investigación, edita la lista `researches` al inicio de la función `main()` en el script:
```python
researches = [
    {
        "title": "Investigación: [Nuevo Tema]",
        "query": "[Términos de búsqueda detallados en inglés]"
    }
]
```

---

## 5. Manejo de Excepciones y Solución de Problemas

*   **Error: Tiempo de espera agotado (Timeout en Polling):**
    *   *Causa:* El motor de investigación web de NotebookLM está tardando más de 3.5 minutos en consolidar los resultados de la búsqueda.
    *   *Solución:* Puedes incrementar la variable `max_attempts` (por defecto `15`) en el script para permitir un mayor tiempo de espera si la red está lenta.
*   **Error: Fuentes Importadas en Cero:**
    *   *Causa:* La consulta de términos clave (`query`) fue demasiado restrictiva o no arrojó resultados válidos en la web.
    *   *Solución:* Modifica la consulta en el script para utilizar términos más amplios o generales y vuelve a ejecutar el agente.
*   **Duplicación de Cuadernos:**
    *   *Causa:* Si ejecutas el script múltiples veces, se crearán nuevos cuadernos independientes con el mismo título.
    *   *Solución:* Esto es por diseño para asegurar una recolección limpia. Puedes eliminar los cuadernos duplicados manualmente en la interfaz web de NotebookLM si lo deseas.
