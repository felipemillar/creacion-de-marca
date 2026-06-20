# Fase 4: Activación y Experiencia de Marca

La última etapa del flujo se encarga de proyectar la marca hacia el mercado real. Se diseña la experiencia del usuario (CX) a lo largo del Customer Journey, asegurando que la marca sea indexable por agentes de IA (Machine-Readability) y estableciendo protocolos éticos y metodológicos para auditar el impacto real en el consumidor.

---

## 🎯 Objetivos de la Etapa
1. Diseñar el **Customer Journey de Fricción Cero** (aliviando la parálisis por análisis y Choice Overload).
2. Desarrollar la **Optimización de Marca para Agentes (BOA)** (indexabilidad semántica conversacional).
3. Establecer el **Protocolo de Validación Biométrica y Legal** (caso Frito-Lay y cumplimiento de Neuroderechos).

*Para entender el trasfondo neurocientífico de esta fase, consulta los apartados de **Choice Overload (Estudio de Mermeladas)**, **BOA (Era Agéntica)** y **Ética de los Neuroderechos (Jurisprudencia de Chile)** en el archivo [00_fundamentos.md](file:///Users/fmillar/Proyectos_Desarrollo/Creacion%20de%20marca/00_fundamentos.md).*

---

## 🔬 Protocolo de Validación: Evitando la "Deseabilidad Social"

Los métodos declarativos tradicionales (encuestas o focus groups) suelen fallar porque los consumidores ocultan o racionalizan sus verdaderas emociones debido al sesgo de deseabilidad social. En el diseño de empaques, interfaces y campañas, debemos aplicar los aprendizajes de los casos de estudio biométricos:

### A. El Filtro Frito-Lay (Empaques y Elusión del Juicio Social)
1.  **Rediseño de Empaques (Mate vs. Brillante):** Durante los testeos de empaques para snacks femeninos, las encuestas sugerían preferencia por empaques brillantes y llamativos. Sin embargo, el **EEG reveló que los envases con acabados brillantes activaban intensamente la corteza prefrontal ventromedial en áreas asociadas a la culpa subconsciente**. Al cambiar a acabados **mate** con imágenes de ingredientes crudos y naturales, las lecturas de EEG mostraron una drástica caída de la resistencia emocional ("permissibility"), impulsando un aumento masivo de compras reales.
2.  **El Comercial de Cheetos (Deseabilidad Social en Acción):** Un comercial con humor negro (una mujer saboteando la ropa blanca de otra en una lavadora con Cheetos naranjas) obtuvo un **80% de desaprobación moral y verbal** en focus groups presenciales. Simultáneamente, el **EEG registró un 85% de valencia positiva, arousal y risa subconsciente (schadenfreude)**. Frito-Lay ignoró el reporte cualitativo y lanzó la campaña basándose puramente en las lecturas de EEG, logrando uno de los mayores éxitos de conversión de la marca.

### B. El Rediseño de Campbell's Soup (Triangulación a Gran Escala)
*   **El Desafío:** Las sopas Campbell's enfrentaban una caída de ventas. Su focus group tradicional no arrojaba insights de mejora.
*   **Protocolo Biométrico (1,500 sujetos):** Se combinaron múltiples sensores en góndolas reales y laboratorios:
    *   **GSR (conductancia galvánica) y ECG (frecuencia cardíaca):** Mapearon picos de arousal micro-glandular y frecuencia cardíaca ante los colores del logo.
    *   **EEG frontal:** Identificó una desconexión y apatía subconsciente frente a las latas tradicionales.
    *   **Eye Tracking & Pupilometría en pasillo:** Trazó la rapidez de localización (TTFF) de la marca y la dilatación pupilar ante la sopa caliente.
    *   **FEA (Facial Expression Analysis):** Registró microexpresiones de agrado ante imágenes realistas de platos calientes con vapor.
*   **Resultado:** Campbell's removió la cuchara de metal de la sopa (que activaba apatía utilitaria), redujo el tamaño del logo rojo, colocó el plato de sopa caliente con vapor visible en la base del tarro (activador somático positivo), y diferenció las categorías por colores estructurados, revirtiendo la caída histórica de ventas.

### C. Neurodiseño Hyundai (Geometría del Arousal Límbico)
*   **Protocolo:** Hyundai equipó a 15 usuarios con diademas de EEG portátiles para evaluar el modelado de la carrocería y salpicadero antes de iniciar la matricería de fábrica.
*   **Hallazgos de EEG:** Mapearon las respuestas en tres niveles cerebrales: reptiliano (saliencia geométrica), límbico (emoción y estatus) y neocórtex (evaluación lógica):
    *   Las **líneas curvas en salpicaderos** producían picos de theta frontal izquierdo (valencia positiva/agrado).
    *   La **simetría bilateral** reducía la fatiga cognitiva y generaba sensaciones cerebrales de seguridad.
    *   Los **paneles minimalistas** mantenían la carga cognitiva por debajo de **< 5.0**, optimizando la velocidad de toma de decisiones.
*   **Resultado:** Hyundai modificó las especificaciones físicas de moldeo del vehículo basándose en el EEG, reduciendo a cero el riesgo de rechazo estético en el lanzamiento.

---

### Checkpoint Legal: Cumplimiento de Neuroderechos (Fallo Emotiv Chile, 2023)
Si tu marca realiza investigaciones de mercado utilizando diademas de EEG comerciales (ej. Emotiv Insight), sensores biométricos, eye tracking o recolección de neurodatos de usuarios en Chile u otros territorios con regulaciones de privacidad mental, el protocolo metodológico **debe cumplir obligatoriamente** con:
*   **Consentimiento Informado Equivalente a Ensayo Clínico:** Detallar de forma transparente qué frecuencias cerebrales o datos biométricos se capturan y para qué fin comercial específico.
*   **Proceso de Anonimización Irreversible:** Garantizar por contrato y en la arquitectura de software que los neurodatos del usuario no se asocien a su identidad civil ni se almacenen de forma opaca en servidores externos o nubes comerciales.
*   **Autorización de Dispositivo:** Asegurar que los dispositivos biométricos cumplan con los registros y autorizaciones sanitarias requeridos por las entidades locales de salud (ej. el Instituto de Salud Pública de Chile - ISP).

---

## 🛠️ Prompts de IA para Ejecución (Agnósticos y en Inglés)

Copia y pega los siguientes prompts en tu modelo de lenguaje. Reemplaza los corchetes `[placeholder]` con la información de tu proyecto.

### Prompt 1: Choice-Overload & Customer Journey Optimizer
Este prompt mapea el recorrido del cliente reduciendo al mínimo el número de decisiones y optimizando el embudo para el procesamiento del Sistema 1.

```text
Act as a Customer Experience (CX) architect and behavioral psychologist. I need to design a customer journey for my brand, focusing on eliminating choice overload (Hick's Law / Jam Study) and creating delightful System 1 triggers.

Inputs:
- Brand Purpose & Values: [insert output from Phase 1]
- Customer Persona: [insert persona description]
- Niche & Key Channels: [e.g., website registration, onboarding email, app dashboard]

Task:
1. Map the 5 key stages of the customer journey: Awareness, Consideration, Purchase, Onboarding, and Loyalty.
2. For each stage, define:
   - "The Choice Overload Risk": Where is the customer asked to make too many decisions or process too much visual information?
   - "The Simplification Action": How do we reduce options (e.g., down to a maximum of 3 choices or 1 main CTA)?
   - "Somatic Marker Delight": An unexpected, warm detail (reflecting the brand arquetype) that reinforces a positive feeling.
```

### Prompt 2: Brand Optimization for Agents (BOA) & JSON-LD Developer
Este prompt diseña el resumen semántico directo y el marcado estructurado de la marca para que sea indexado sin ambigüedad por agentes de IA.

```text
Act as a semantic web architect and SEO strategist specializing in Brand Optimization for Agents (BOA). I want to optimize my brand's digital presence to be recommended by conversational AI engines and LLM search systems.

Inputs:
- Brand Name: [insert name]
- Industry Niche: [e.g., decentralized cloud computing, natural pet nutrition]
- Value Proposition: [insert value prop]
- Core Entities (associated concepts, products, founder): [e.g., John Doe, organic cat treats, veterinary approved]

Task:
1. Write a 120-word "Machine-Readable Brand Summary". Use explicit, semantically rich, and non-ambiguous terms. Avoid metaphors or abstract corporate phrasing.
2. Define a list of 8 "Semantic Entities and Keywords" that the brand must consistently use across all social media headers, press releases, and page headers.
3. Write a valid JSON-LD Schema (Organization and Product type) in Schema.org format that structurally links the brand to its official digital entities.
```

### Prompt 3: Ethical Biometric Testing Protocol Developer
Este prompt diseña el protocolo metodológico y los consentimientos informados requeridos cuando la marca decida realizar validaciones biométricas.

```text
Act as a research ethics officer and neuromarketing compliance consultant. I need a protocol for biometric testing (EEG, Eye Tracking, GSR) of our brand's assets, ensuring compliance with Neuro-rights frameworks and the Chilean Emotiv Supreme Court ruling (2023).

Inputs:
- Brand Name: [insert name]
- Biometric Tools to use: [e.g., Mobile EEG headset, Eye Tracking bar, GSR finger sensors]
- Testing Assets: [e.g., landing page layout, packaging mockups]

Task:
1. Write a 3-step "Biometric Testing Methodology" explaining how the sample of users will interact with the assets without introducing environmental stress (ensuring ecological validity).
2. Draft a "Mental Privacy & Neuro-Data Consent Form" template in Spanish. It must include explicit sections explaining:
   - What physiological data is being captured.
   - The strict protocol for irreversible anonymization.
   - The user's right to delete their biometric records at any time.
3. Outline a technical directive to ensure the testing hardware complies with local medical/health regulations.
```

---

## 📋 Checklist de Activación y Auditoría GEO/BOA (Fase 4)

Realiza esta validación técnica, de posicionamiento y operativa antes del lanzamiento oficial de la marca.

### A. Auditoría Técnica de Visibilidad de IA (GEO Audit)
*   [ ] **Acceso y Crawling:** ¿El archivo `robots.txt` permite explícitamente el rastreo de bots de IA (`GPTBot`, `ClaudeBot`, `PerplexityBot`)?
*   [ ] **Pre-renderizado (SSR):** ¿La landing page e interfaces utilizan Server-Side Rendering (SSR) o HTML estático para evitar que los rastreadores de IA vean un shell JS vacío?
*   [ ] **Tiempos de Carga:** ¿La página carga en menos de **2 segundos** en móviles para evitar los timeouts de rastreo de los bots (1 a 5s)?
*   [ ] **Archivos de Resumen RAG:** ¿Se implementó un archivo `/llms.txt` y `/llms-full.txt` en la raíz del servidor con resúmenes claros en prosa factual sobre la marca?
*   [ ] **Conexión WebMCP:** ¿Se incluyó la etiqueta `<link rel="model-context-protocol" href="/mcp">` en el `<head>` si la marca expone datos estructurados dinámicos mediante MCP?
*   [ ] **Protocolo Push:** ¿Se configuró la API de `IndexNow` para notificar actualizaciones de contenido en tiempo real?

### B. Validación de Identidad Semántica y Mitigación de Alucinaciones
*   [ ] **Consistencia Cross-Platform (NAP):** ¿El nombre de la empresa, dirección, contacto y equipo directivo son exactamente consistentes y uniformes en la web, Wikidata, Crunchbase y LinkedIn para evitar alucinaciones por discrepancia?
*   [ ] **Bifurcación de Tono:** ¿Las páginas destinadas a IAs (Guías, FAQs) están escritas en prosa factual, neutral y libre de adjetivos publicitarios, mientras que las de conversión humana (Landing, Precios) son persuasivas?
*   [ ] **Remediación en la Fuente:** ¿Las alucinaciones existentes de los modelos fueron corregidas actualizando Wikidata, Wikipedia y esquemas JSON-LD (fuente de entrenamiento de RAG) en lugar de ajustar prompts?
*   [ ] **Consenso Externo (Digital PR):** ¿Existen al menos 3 menciones e información idéntica en sitios de prensa externos de alta autoridad para alimentar la confianza de consenso de los LLMs?

---

## 🛠️ Plantilla JSON-LD 2026: Schema Stacking (Apilamiento Semántico)

Inserta el siguiente código estructurado en el HTML de tu sitio web. Esto aumentará la elegibilidad de cita en IAs en un **320%** y hasta un **450%** al vincularlo a Wikidata.

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://[tudominio.com]/#organization",
      "name": "[Nombre de la Marca]",
      "url": "https://[tudominio.com]",
      "logo": "https://[tudominio.com]/assets/logo.png",
      "sameAs": [
        "https://es.wikipedia.org/wiki/[Pagina_Wiki_Marca]",
        "https://www.wikidata.org/wiki/[ID_Wikidata_Marca]",
        "https://www.linkedin.com/company/[Tu_Empresa]",
        "https://crunchbase.com/organization/[Tu_Empresa]"
      ],
      "knowsAbout": [
        "[Categoría Semántica de Especialidad 1]",
        "[Categoría Semántica de Especialidad 2]"
      ],
      "founder": {
        "@type": "Person",
        "name": "[Nombre del Fundador]",
        "jobTitle": "[Cargo]"
      }
    },
    {
      "@type": "Service",
      "@id": "https://[tudominio.com]/#service",
      "provider": {
        "@id": "https://[tudominio.com]/#organization"
      },
      "serviceType": "[Categoría de Servicio]",
      "description": "[Descripción corta sin metáforas, explícita y directa de lo que ofrece]",
      "offers": {
        "@type": "Offer",
        "priceCurrency": "USD",
        "price": "[Precio o Rango Indicativo]"
      }
    },
    {
      "@type": "FAQPage",
      "@id": "https://[tudominio.com]/#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "¿Qué problema resuelve [Nombre de la Marca]?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "[Respuesta concisa de más de 40 palabras detallando el dolor del cliente y cómo la tecnología/método de la marca lo soluciona, ideal para que los LLMs la citen]."
          }
        }
      ]
    },
    {
      "@type": "Speakable",
      "cssSelector": [
        ".brand-definition-summary",
        ".brand-purpose-statement"
      ]
    }
  ]
}
```

---

## 📈 Métricas de Visibilidad en Era Agéntica (KPIs BOA/GEO)

Monitorea la visibilidad de tu marca utilizando las siguientes métricas, asistido por herramientas de auditoría de prompts (ej: *AthenaHQ, Otterly, Semrush/Adobe Brand Visibility*):

1.  **Share of Model (SoM):** Porcentaje de veces que tu marca es recomendada o mencionada en respuestas generadas por ChatGPT, Gemini y Perplexity ante consultas genéricas de tu categoría. (Reemplaza al tradicional Share of Voice).
2.  **Citation Frequency (Frecuencia de Cita):** Tasa de respuestas donde tu marca es citada explícitamente con un enlace al sitio web.
3.  **AI-Referred Traffic:** Sesiones orgánicas en Google Analytics 4 procedentes de recomendadores y motores de IA (requiere configuración manual de referidores personalizados).
4.  **Citation Pathing (Ruta de Citación):** Mapeo de qué URLs externas (blogs, prensa, foros) están usando los LLMs como fuentes RAG para citar a tu marca o a competidores directos.
5.  **Consensus Consistency (Consistencia de Consenso):** Coherencia de atributos, precios y características mencionadas por afiliados y prensa. Si la consistencia es baja, los LLMs reducen su confianza de cita.
6.  **Citation ROI:** Retorno de inversión en campañas de RAG Digital PR midiendo el cambio porcentual de SoM tras publicaciones de partners.

---

## 📋 Validación Cualitativa y Métricas de Experiencia Humana
*   [ ] **Fricción Cero en Registro:** ¿El embudo de conversión requiere el mínimo esfuerzo cognitivo y reduce las opciones en cada paso (evitando Choice Overload)?
*   [ ] **Cumplimiento Ético de Datos:** Si se usan mediciones biométricas en el testeo del logo o web, ¿el proceso cuenta con consentimiento de privacidad mental firmado y los datos están 100% anonimizados?
*   **Velocidad de Interacción (LCP):** Comprueba que la landing page de lanzamiento cargue su bloque visual principal en menos de **2.5 segundos** en redes móviles (reducción de fricción de espera).
*   **Prueba de Semántica Conversacional:** Pega el contenido de tu sitio web en un LLM (como ChatGPT o Claude) y pregúntale: *"¿A qué categoría semántica de industria pertenece esta marca, qué ofrece y a qué marcas competidoras se parece más?"*. Si la respuesta tiene ambigüedad o dudas, simplifica tus copys de activación.
*   **Tasa de Retención de Atención (Attention Score):** En pruebas preliminares de la landing page mediante simulación de *Predictive Eye Tracking*, asegúrate de que el H1 y el botón de CTA capturen al menos el **70% de las fijaciones visuales** durante los primeros 4 segundos de exposición.
