# El nexo: de la filosofía q_ r_ t_ a las industrias

Documento de razonamiento. Resuelve el problema estructural del sitio: cómo evitar que
la filosofía de marca (`quantitative`, `research`, `trading`) y las verticales de negocio
(minería, retail, finanzas) queden como dos bloques pegados sin relación argumental.

Complementa a [qrt_adn_y_mensajes.md](qrt_adn_y_mensajes.md), que fija el ADN y la voz.

---

## 1. Primer movimiento: q_ r_ t_ no son tres áreas, son un ciclo

Hoy el sitio los presenta como tres pilares en paralelo. Presentados así son una
declaración de identidad, y una declaración no se puede aplicar a nada.

Presentados como **un bucle cerrado**, se convierten en un procedimiento — y un
procedimiento sí viaja a otra industria:

```
        ┌─────────────────────────────────────────┐
        │                                         │
        ▼                                         │
   ┌─────────┐      ┌──────────┐      ┌─────────┐ │
   │   q_    │ ───▶ │    r_    │ ───▶ │   t_    │─┘
   │  medir  │      │ descubrir│      │ ejecutar│
   └─────────┘      └──────────┘      └─────────┘
   qué cuenta       qué patrón        qué pasa cuando
   como evidencia   predice esa       hay costo real
   y cómo se mide   medida            de por medio
```

- **q_ — el estándar de prueba.** Antes de modelar hay que definir qué es una buena
  decisión en este dominio y en qué unidad se mide. Sin esto, todo lo demás es opinión.
- **r_ — el motor de descubrimiento.** Formular la hipótesis y validarla fuera de la
  muestra donde nació. Aquí se decide en qué se puede confiar.
- **t_ — la consecuencia.** Someter la regularidad a costo real. Es lo único que
  distingue un hallazgo de una coincidencia.

El resultado de `t_` regresa a `q_` como dato nuevo. El bucle nunca termina: es la
traducción operativa del valor *dudar de lo que funciona*.

---

## 2. Segundo movimiento: por qué el trading le enseña algo a un minero

La respuesta fácil —"somos rigurosos"— no convence a un C-level. La respuesta real es
estructural.

Todo problema de decisión tiene cuatro propiedades. El trading es el único entorno donde
las cuatro están al máximo a la vez. Por eso es un caso límite, y por eso un método que
sobrevive ahí queda sobre-entrenado para el resto.

| Entorno | Incertidumbre | Consecuencia por decisión | Frecuencia | Velocidad de feedback |
| :--- | :--- | :--- | :--- | :--- |
| **trading propio** | alta | media | altísima | segundos |
| **finanzas institucional** | alta | alta | alta | días |
| **minería** | alta | **altísima** | **baja** | **meses** |
| **marcas y consumo** | media | baja | altísima | semanas |

Minería no es "finanzas con piedras": es el problema **invertido**. Cada decisión cuesta
muchísimo más, se toma mucho menos seguido y el resultado tarda un año en aparecer.
No se puede aprender por ensayo y error cuando cada error cuesta millones.

De ahí sale la formulación central del nexo:

> **En trading el ciclo de aprendizaje se cierra en segundos.
> En su industria se cierra en meses. Nuestro trabajo es acortarlo.**

---

## 3. Tercer movimiento: el cuello de botella define el servicio

Cada industria falla en una propiedad distinta del cuadro anterior. Eso —y no la
preferencia comercial— determina qué se vende en cada vertical.

### minería — el cuello es la frecuencia de observación
La decisión es rara y cara. Hay que **fabricar repetición**: en vez de decidir una vez al
año cuándo intervenir un equipo, se mide de forma continua y se decide con evidencia
acumulada. Una decisión anual se convierte en miles de micro-observaciones.

→ Se resuelve con **modelos predictivos + infraestructura de datos**.

*Nexo técnico con el core:* una serie de vibración de un molino y una serie de precios
comparten estructura estadística — ruido, cambios de régimen, señales débiles y un costo
marcadamente asimétrico entre el falso positivo (parar la planta sin necesidad) y el
falso negativo (falla catastrófica). Eso es gestión de riesgo, no minería.

### finanzas — el cuello es la latencia humana
La señal existe y el feedback es rápido. Lo que falla es que un comité no reacciona a la
velocidad del mercado, y al crecer el volumen el riesgo deja de ser medible.

→ Se resuelve con **infraestructura, automatización y modelos de riesgo**.

### marcas y consumo — el cuello es la calidad de la señal
Hay repetición de sobra y feedback razonable. El problema es que **el sujeto miente**:
la gente no sabe por qué elige, y las encuestas capturan la racionalización posterior del
Sistema 2, no la decisión real del Sistema 1.

→ Se resuelve **midiendo conducta en lugar de preguntar**. Aquí la neurociencia deja de
ser un adorno y pasa a ser el instrumento que le faltaba a este vertical.

> **Observación importante:** este marco no se construyó para justificar el catálogo.
> Se deriva de la estructura del problema y produce, por sí solo, la mezcla de servicios
> que la empresa ya presta. El posicionamiento es descriptivo, no aspiracional.

---

## 4. Cuarto movimiento: cada industria tiene su tick

En el mercado nunca se pregunta por qué alguien compró. Se mira el flujo. El precio es la
única declaración honesta, y llega miles de veces por segundo.

Toda industria tiene su equivalente: una señal de alta frecuencia que revela la verdad
sin que nadie la declare.

| Industria | Su tick |
| :--- | :--- |
| finanzas | el precio |
| minería | la vibración, la temperatura, la ley del mineral |
| marcas y consumo | la fijación ocular, la respuesta galvánica, la transacción |
| neurociencia (I+D) | la respuesta neural preconsciente, antes de la racionalización |

**El trabajo de qrt^ es encontrar el tick de cada industria y construir el sistema que
lo escucha.**

Es el mismo principio epistemológico en los cuatro casos: preferencia revelada por
encima de preferencia declarada. Mirar lo que se hace, no lo que se dice.

---

## 5. La matriz: q_ r_ t_ traducido a cada industria

Este es el material directo para el componente que se repite en cada página de vertical.

| | **q_** — qué se mide | **r_** — cómo se valida | **t_** — dónde se paga el error |
| :--- | :--- | :--- | :--- |
| **finanzas** | Retorno ajustado por riesgo, exposición, capacidad | Backtesting fuera de muestra, walk-forward | Capital propio en el mercado |
| **minería** | Probabilidad de falla, costo esperado de parada, ley recuperada | Validación contra el histórico de fallas | La planta se detiene o no se detiene |
| **marcas y consumo** | Atención medida, elasticidad, conversión incremental | Test controlado con grupo de resguardo | Presupuesto de campaña e inventario |
| **neurociencia** (I+D) | Valencia, carga cognitiva, tiempo a la primera fijación | Protocolo experimental con grupo control | La pieza sale o no sale a producción |

---

## 6. Cómo se implementa esto en el sitio

### 6.1 El componente puente, repetido en cada vertical
Una banda de tres columnas —`q_`, `r_`, `t_`— con el contenido de la matriz de la
sección 5. Siempre la misma forma, distinto contenido. Es el nexo hecho visible: el
lector reconoce la estructura de la home y ve su traducción concreta.

Va entre el bloque de capacidades y el de la prueba, y responde a la pregunta que el
lector se está haciendo justo ahí: *¿esto es realmente el mismo método o solo lo dicen?*

### 6.2 En la home
Un bloque nuevo tras `t_`, antes del pie: las cuatro industrias con su tick. Cierra el
scrollytelling llevando de la filosofía a la aplicación, y le da destino al menú
`soluciones`.

### 6.3 En el hero de cada vertical
El titular de cada vertical debe nombrar el cuello de botella de esa industria, no el
método. El método ya se demostró en la home; la vertical tiene que demostrar
**comprensión del problema del cliente**.

- finanzas → *el mercado no perdona el criterio* (latencia)
- minería → apunta a la frecuencia: se decide poco, se paga caro, se sabe tarde
- retail → apunta a la señal: preguntar no sirve

### 6.4 Corrección pendiente en la home
El scrollytelling actual presenta `q_ r_ t_` como tres pilares paralelos. Para que este
marco funcione hay que dejar visible que son **un ciclo**: basta con que el copy de `t_`
devuelva explícitamente a `q_` ("y el resultado vuelve a la mesa de medición"), o con un
conector visual entre la última sección y la primera.

---

## 7. Especificación de la sección de cierre `^_`

Sección nueva en la home, después de `t_` y antes del bloque de industrias.
Cada decisión de aquí está justificada con una fuente del propio proyecto.

### 7.1 Por qué esta sección debe existir

Dos marcos del playbook detectan el mismo hueco por caminos distintos:

- **CBBE (Keller)** — la pirámide sube Prominencia → Significado → Juicios → **Resonancia**.
  La home entrega los tres primeros y se corta antes del cuarto. Resonancia exige que el
  lector se vea a sí mismo en la marca.
- **Branding Cultural (Holt)** — la narrativa va Tensión → Mito → Guía → **Transformación**.
  El hero da la tensión y `q_ r_ t_` dan el mito. Falta el beat en que el estado somático
  del lector pasa de ansioso a con control.

`^_` es simultáneamente la Resonancia de Keller y la Transformación de Holt.

### 7.2 El visual: espiral, no diagrama

Se descartó el diagrama de llaves anotado. **No pasa la Ley de Prägnanz** ni el test del
borroso de la Fase 3: demasiados elementos, exige lectura secuencial y por lo tanto activa
Sistema 2 en el primer contacto, desperdiciando el canal visual que procesa 60.000 veces
más rápido que el texto.

La forma elegida es una **espiral de trazo continuo**:

| Forma | Significado | Veredicto |
| :--- | :--- | :--- |
| Círculo | Repetir sin avanzar | Contradice el mensaje |
| Diagrama anotado | Explícito pero complejo | Falla Prägnanz |
| **Espiral** | Repetir acumulando | **Elegida** |

Ventajas: contorno simple y continuo, sobrevive el desenfoque, y rima con la espiral de
Fibonacci de `r_`, que también se genera iterando una regla a escala creciente.

**Revelado en dos capas**, aprovechando el motor de typewriter ya construido:
1. *Sistema 1* — la espiral se dibuja sola. Forma pura, sin texto.
2. *Sistema 2* — aparecen `q`, `r`, `t` en tres posiciones angulares, repetidas en cada
   vuelta a radio creciente. El `^` cierra en el extremo exterior.

### 7.3 Copy (validado contra las reglas HeyHuman)

Título: `^` + cursor `_`. La cuarta "letra" de la serie es el propio exponente.

> **No es una secuencia. Es un exponente.**
>
> Las tres letras no son tres áreas. Son tres etapas de un mismo bucle.
>
> Medimos, descubrimos, ejecutamos. Y lo que la ejecución devuelve vuelve a la medición.
>
> Su organización ya hace las tres cosas. Lo que suele faltar es el registro que las conecta.
>
> Repetir sin registro es dar vueltas. Repetir con registro es acumular.
>
> Por eso el logo agrupa las tres letras entre paréntesis. Y por eso lleva un exponente.

Cumplimiento: todas las oraciones bajo 15 palabras, párrafos de 2 frases, voz activa,
sin jerga corporativa. El giro de "nosotros" a "su organización" en el tercer párrafo es
el movimiento de resonancia.

### 7.4 Una sola llamada a la acción

Por **Ley de Hick** y por el estudio de las mermeladas de Columbia citado en
[00_fundamentos.md](00_fundamentos.md): un único enlace, hacia las industrias. No agregar
contacto ni método en el mismo bloque.

### 7.5 Marcado semántico (Fase 4)

El ciclo de cuatro pasos es el contenido más citable del sitio para recomendadores de IA.
Se marca como `HowTo` en JSON-LD, con un `HowToStep` por etapa (`q_`, `r_`, `t_`, y el
retorno a la medición). Es el tipo de estructura que un LLM extrae y cita textualmente.

### 7.6 Brecha declarada, no resuelta

La Fase 3 exige una firma sonora de 3 segundos y el sitio no tiene ninguna. `^_` es su
lugar natural por ser el clímax narrativo. **No se implementa ahora:** la Ley de Jakob
establece que la innovación nunca debe ir en la usabilidad fundamental, y el audio
automático rompe esa expectativa. Queda como brecha abierta de la Fase 3.

### 7.7 Ajuste requerido en `t_`

La sección `t_` cierra hoy en *"Optimizamos decisiones complejas donde la velocidad y la
precisión son fundamentales"*. Es un final, no una entrega. Debe devolver a la medición
para que el ciclo se sienta antes de enunciarse. Es un cambio de una frase.

---

## 8. Qué está respaldado y qué es oferta

Distinción obligatoria antes de escribir cualquier página:

| Afirmación | Estado |
| :--- | :--- |
| Modelos predictivos e infraestructura de datos en minería | **Respaldado** — Antofagasta Minerals, BHP |
| Las cuatro capacidades en finanzas | **Respaldado** — BEC, Pepperstone, Mercados G, Patrimore |
| Trabajo en marcas y consumo | **Respaldado**, naturaleza por confirmar — CHEIL, Sixbell |
| Neurociencia aplicada a decisiones de marca | **No respaldado** — I+D propia, sin cliente. No prometer entrega |
| "Acortamos el ciclo de aprendizaje" como resultado medido | **No respaldado** — es el argumento del método, no un dato. No cuantificar |

La tabla de la sección 5 describe **cómo se trabaja**, no resultados obtenidos. Ninguna
celda debe redactarse como caso de éxito sin dato que lo sostenga.
