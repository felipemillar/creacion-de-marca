# 🤖 Agente: Investigador Principal (Primary Research Agent)

Este documento define la estructura, rol, especificaciones técnicas y de operación del **Agente Investigador Principal**.

---

## 📋 Ficha de Identificación del Agente

*   **Nombre Oficial:** Agente Investigador Principal (`primary-research-agent`)
*   **Script de Control:** [notebook_research.py](file:///Users/fmillar/Proyectos_Desarrollo/Creacion%20de%20marca/agentes/notebook_research.py)
*   **Plataforma Destino:** Google NotebookLM
*   **Cuaderno de Destino:** `"Metodología y Método para la Creación de Marca"`
*   **Objetivo Primario:** Centralizar la base teórica local y extraer los fundamentos del Playbook de marca mediante consultas estructuradas en NotebookLM.

---

## 1. Definición y Propósito

El **Agente Investigador Principal** es el responsable de establecer la base conceptual del proyecto en la nube. Su propósito es digitalizar los documentos teóricos locales recopilados en el espacio de trabajo, subirlos a un cuaderno único en NotebookLM, y realizar la extracción inicial de la información estructurada que servirá de insumo para los redactores de la metodología de marca.

Al automatizar este paso, el agente elimina el proceso manual de copiar/pegar textos en la interfaz web de NotebookLM, garantizando que no se pierdan secciones teóricas clave y estructurando la salida en archivos Markdown listos para ser consumidos por el Playbook.

---

## 2. Arquitectura de Datos e Integración

### Inputs (Entradas)
*   **Tokens de Autenticación:** Carga dinámicamente las cookies y el token CSRF desde `~/.notebooklm-mcp/auth.json`.
*   **Documentos Locales (Fuentes):**
    *   [Neurociencia y Creación de Marca_ Investigación Profunda.md](file:///Users/fmillar/Proyectos_Desarrollo/Creacion%20de%20marca/Neurociencia%20y%20Creaci%C3%B3n%20de%20Marca_%20Investigaci%C3%B3n%20Profunda.md)
    *   [Técnicas Modernas de Creación de Marca_ Teoría.md](file:///Users/fmillar/Proyectos_Desarrollo/Creacion%20de%20marca/T%C3%A9cnicas%20Modernas%20de%20Creaci%C3%B3n%20de%20Marca_%20Teor%C3%ADa.md)

### Procesamiento de API (Llamadas `notebooklm_mcp`)
*   `list_notebooks()`: Busca el cuaderno metodológico existente.
*   `create_notebook(title)`: Crea el cuaderno si no está presente en la cuenta.
*   `get_notebook_sources_with_types(notebook_id)`: Verifica qué fuentes ya han sido cargadas.
*   `add_text_source(notebook_id, text, title)`: Sube el contenido de los Markdown locales como fuentes nativas de NotebookLM.
*   `query(notebook_id, query_text, timeout)`: Ejecuta las consultas teóricas para la recopilación de bases.

### Outputs (Salidas en `/investigacion/`)
Genera 4 archivos Markdown con respuestas estructuradas:
*   `resumen_neurociencia.md`: Síntesis de Damasio, CPFvm, amígdala, Frito-Lay y Hyundai.
*   `resumen_marcas_teoria.md`: Modelos de Keller (CBBE), Vargo y Lusch (S-D Logic), Berger (Señalización) y Muniz/O'Guinn (Comunidades).
*   `resumen_estetica_y_ux.md`: Sinergia de Lindstrom, olfato y color, y Leyes de UX (Hick, Jakob, Prägnanz, Fitts).
*   `resumen_arquetipos_y_activacion.md`: Arquetipos de Mark & Pearson, indexabilidad para agentes y Neuroderechos (Yuste).

---

## 3. Flujo de Trabajo del Agente

```
   [Inicio] ──> Cargar auth.json ──> ¿Tokens Válidos?
                                         │
                 ┌───────────────────────┴───────────────────────┐
                 ▼ (Sí)                                          ▼ (No)
        Buscar/Crear Cuaderno                           Lanzar Error de Auth
                 │
                 ▼
        Escanear Fuentes Actuales
                 │
                 ▼
       ¿Docs locales subidos?
                 │
         ┌───────┴───────┐
         ▼ (No)          ▼ (Sí)
      Subir Textos     Omitir Carga
         │               │
         └───────┬───────┘
                 │
                 ▼
      Ejecutar 4 Consultas RAG
                 │
                 ▼
      Guardar Resúmenes en MD ──> [Fin]
```

---

## 4. Manual de Operación y Comandos

### Ejecución Estándar
Para iniciar el agente y cargar/sincronizar el cuaderno metodológico base, ejecuta en tu consola:
```bash
/Users/fmillar/.local/share/uv/tools/notebooklm-mcp-server/bin/python agentes/notebook_research.py
```

### Parámetros Modificables (en el script)
*   **`notebook_title` (Línea 29):** Título del cuaderno a buscar o crear en tu cuenta.
*   **`queries` (Línea 89):** Diccionario con las preguntas estructuradas que el agente le hará a NotebookLM. Puedes modificar los textos para cambiar el enfoque de los resúmenes generados.

---

## 5. Manejo de Excepciones y Solución de Problemas

*   **Error: `ModuleNotFoundError: No module named 'notebooklm_mcp'`**
    *   *Causa:* Estás ejecutando el script con el binario de Python global del sistema o de Conda, el cual no tiene la librería instalada.
    *   *Solución:* Asegúrate de anteponer la ruta de Python de uv: `/Users/fmillar/.local/share/uv/tools/notebooklm-mcp-server/bin/python`.
*   **Error: `load_cached_tokens returned None`**
    *   *Causa:* El archivo de autenticación local no existe o se ha corrompido.
    *   *Solución:* Ejecuta `notebooklm-mcp-auth` en la terminal para iniciar sesión en tu cuenta de Google y regenerar las credenciales.
*   **Error de Timeout en Consultas:**
    *   *Causa:* Las consultas de NotebookLM pueden tardar cuando los servidores están congestionados.
    *   *Solución:* El agente tiene un tiempo de espera de 180 segundos por defecto (`timeout=180`), lo cual es seguro. Si falla, vuelve a ejecutar el script (el agente omitirá la carga de textos ya existentes y continuará directamente con las consultas pendientes).
