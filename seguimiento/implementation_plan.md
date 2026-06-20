# Plan: Segunda Iteración - Reestructuración de Espacio de Trabajo y Enriquecimiento Metodológico

Este plan detalla el proceso para estructurar todo el material del proyecto en la carpeta activa (`/Users/fmillar/Proyectos_Desarrollo/Creacion de marca`) e incorporar los insights técnicos recopilados en las investigaciones avanzadas sobre **Neurobranding y Biometría** y **Brand Optimization for Agents (BOA)**.

---

## User Review Required

> [!IMPORTANT]
> **Reestructuración Física de la Carpeta Activa:**
> Copiaremos todos los scripts de automatización ("agentes"), resúmenes teóricos y bitácoras de investigación (actualmente en el directorio de la aplicación) en subdirectorios organizados de la carpeta activa para asegurar que conserves todo el ecosistema de trabajo en un solo lugar.
>
> **Nuevas Carpetas en el Workspace:**
> *   `agentes/`: Contendrá los scripts de Python para interactuar con NotebookLM.
> *   `investigacion/`: Contendrá todas las notas de investigación e insights sintetizados de la web.
> *   `seguimiento/`: Contendrá los activos de control (`task.md`, `implementation_plan.md`, `walkthrough.md`).
>
> **Enriquecimiento del Playbook (Fase 4 e Hilo Conductor):**
> Actualizaremos las bases teóricas y procedimentales del Playbook con protocolos biometrícos profundos, casos corporativos minuciosos y estrategias técnicas de optimización semántica agéntica (esquemas apilados JSON-LD de 2026, WebMCP, y métricas de SoM).

---

## Proposed Changes

### Componente: Estructura de Archivos del Espacio de Trabajo

#### [NEW] Carpetas y Archivos en la Carpeta Activa
*   **`agentes/`**
    *   [notebook_research.py](file:///Users/fmillar/Proyectos_Desarrollo/Creacion%20de%20marca/agentes/notebook_research.py)
    *   [notebook_research_expand.py](file:///Users/fmillar/Proyectos_Desarrollo/Creacion%20de%20marca/agentes/notebook_research_expand.py)
    *   [query_new_notebooks.py](file:///Users/fmillar/Proyectos_Desarrollo/Creacion%20de%20marca/agentes/query_new_notebooks.py)
*   **`investigacion/`**
    *   [registro_nuevos_cuadernos.md](file:///Users/fmillar/Proyectos_Desarrollo/Creacion%20de%20marca/investigacion/registro_nuevos_cuadernos.md)
    *   [resumen_neurociencia.md](file:///Users/fmillar/Proyectos_Desarrollo/Creacion%20de%20marca/investigacion/resumen_neurociencia.md)
    *   [resumen_marcas_teoria.md](file:///Users/fmillar/Proyectos_Desarrollo/Creacion%20de%20marca/investigacion/resumen_marcas_teoria.md)
    *   [resumen_estetica_y_ux.md](file:///Users/fmillar/Proyectos_Desarrollo/Creacion%20de%20marca/investigacion/resumen_estetica_y_ux.md)
    *   [resumen_arquetipos_y_activacion.md](file:///Users/fmillar/Proyectos_Desarrollo/Creacion%20de%20marca/investigacion/resumen_arquetipos_y_activacion.md)
    *   [insights_neurobranding.md](file:///Users/fmillar/Proyectos_Desarrollo/Creacion%20de%20marca/investigacion/insights_neurobranding.md)
    *   [insights_boa.md](file:///Users/fmillar/Proyectos_Desarrollo/Creacion%20de%20marca/investigacion/insights_boa.md)
*   **`seguimiento/`**
    *   [task.md](file:///Users/fmillar/Proyectos_Desarrollo/Creacion%20de%20marca/seguimiento/task.md)
    *   [implementation_plan.md](file:///Users/fmillar/Proyectos_Desarrollo/Creacion%20de%20marca/seguimiento/implementation_plan.md)
    *   [walkthrough.md](file:///Users/fmillar/Proyectos_Desarrollo/Creacion%20de%20marca/seguimiento/walkthrough.md)

---

### Componente: Playbook Metodológico de Marca

#### [MODIFY] [README.md](file:///Users/fmillar/Proyectos_Desarrollo/Creacion%20de%20marca/README.md)
*   Actualizar la sección de estructura para documentar e indexar las carpetas `agentes/`, `investigacion/` y `seguimiento/`, integrando enlaces directos funcionales.

#### [MODIFY] [00_fundamentos.md](file:///Users/fmillar/Proyectos_Desarrollo/Creacion%20de%20marca/00_fundamentos.md)
*   **EEG Avanzado:** Agregar especificaciones técnicas de preprocesamiento (DC offset, filtros IIR 0.5–50 Hz, filtro notch 50 Hz, transformada wavelet Daubechies "db7"/"db4" para remoción de ruido) y localización (electrodo Fp1 para prefrontal en diademas de bajo coste). KPI's detallados: Valence (> 5.0) y Cognitive Load (< 5.0), Detrended Fluctuation Analysis (DFA) y parámetros Hjorth.
*   **Eye Tracking:** Incorporar métricas clave: TTFF (Time to First Fixation) con benchmark POS < 0.5s para packshot, y TFD (Total Fixation Duration) con benchmark > 1.0s para eslóganes.
*   **GSR:** Agregar métricas de picos SCR y amplitud correlacionados con el modelo de excitación de Mehrabian-Russell.
*   **Sinergia Cross-Modal:** Explicar con un diagrama la triangulación multimodal (Sincronía Espacio-Cognitiva, Integración Valence-Arousal y Triangulación de Metáfora de Marca).
*   **Era Agéntica (BOA y GEO):** Desglosar las etapas de evaluación de LLMs (Query, Parsing, Cross-reference, Selection). Explicar la trinidad algorítmica (LLM, Knowledge Graphs, search) y las señales de consenso (unlinked mentions, Wikidata/Wikipedia). Requerimientos técnicos de renderizado en servidor (evitar CSR en rastreadores de IA) y WebMCP (`<link rel="model-context-protocol" href="/mcp">`).

#### [MODIFY] [04_activacion_y_experiencia.md](file:///Users/fmillar/Proyectos_Desarrollo/Creacion%20de%20marca/04_activacion_y_experiencia.md)
*   **Casos Corporativos Detallados:** Incorporar las métricas biológicas y resultados de Frito-Lay (mate vs brillante, y el test del comercial Cheetos), Campbell's Soup (rediseño de etiqueta basado en EEG y biometría galvánica/pupilometría con 1500 sujetos), e Hyundai (diseño de curvas y simetría evaluado por EEG).
*   **Directrices de Auditoría GEO/BOA:** Añadir requisitos de IndexNow y robots.txt.
*   **Estrategia JSON-LD 2026 (Schema Stacking):** Crear una plantilla de código lista para usar con esquemas anidados (Organization, Product, FAQPage, HowTo, Service, Speakable, Review, ItemList).
*   **Mitigación de Alucinaciones:** Explicar la remediación a nivel de origen (Wikidata/Wikipedia, consistencia NAP en LinkedIn/local listings) y control de sentimiento (Five Blocks AIQ / impact.com).
*   **Métricas de Visibilidad de IA:** Detallar Share of Model (SoM), Citation Frequency, Tráfico Referido de IA (GA4), Citation Pathing, Consistencia de Señal de Consenso y Citation ROI.

---

## Verification Plan

### Manual Verification
*   Confirmar que todos los archivos se encuentran copiados y enlazados de manera correcta en el workspace activo de marca.
*   Ejecutar pruebas del formato del Playbook en markdown para asegurar legibilidad.
*   Validar que no existan enlaces rotos.
