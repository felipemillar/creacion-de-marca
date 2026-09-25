# Tres opciones para qrt | infraestructura de trading

Fecha: 24 de septiembre de 2026  
Estado: diseño aprobado para revisión previa a implementación

## Objetivo

Crear tres prototipos de página completa para presentar el producto de consultoría e infraestructura de trading. Las propuestas deben comunicar la investigación reciente sin introducir un lenguaje visual ajeno al sitio vigente.

Los prototipos servirán para comparar tres arquitecturas narrativas. No reemplazarán `index.html`, `soluciones-finanzas.html` ni otros archivos de producción.

## Fuente de verdad visual

Las tres opciones utilizarán el sistema existente en `assets/qrt.css`, el comportamiento compartido de `assets/qrt.js` y las reglas de `caso_estudio_qrt/manual_de_marca_logo.md`.

Reglas obligatorias:

- Paleta monocromática del sitio y sus variables actuales. El cian `#00B4D8` se reserva para foco o señal puntual; no será un color decorativo dominante.
- Logotipo `qrt^` en minúsculas, Sora 700 para las letras y Sora 500 para el exponente. Se conserva el despliegue a `(quantitative research trading)^` al desplazarse.
- Sora para titulares de identidad, Space Grotesk para jerarquías editoriales, Inter para cuerpo y Fira Code para etiquetas, índices y metadatos.
- Cuadrícula de fondo, bordes de un píxel, botones rectangulares sin radio, modo claro/oscuro, cursor `_` y transiciones con `cubic-bezier(0.16, 1, 0.3, 1)`.
- Se reutilizan cabecera, navegación, selector de idioma, control de tema, pie y menú móvil actuales.
- Sin gradientes, sombras expresivas, fotografías genéricas, tarjetas redondeadas, colores adicionales, ilustración tridimensional ni recursos de estética fintech convencional.
- Todo gráfico será SVG lineal y utilizará `currentColor`, las variables actuales y las proporciones del resto del sitio.

## Principios de contenido

La página presenta una capacidad de ingeniería, no resultados financieros. El copy no promete rentabilidad, infalibilidad, cumplimiento automático ni ausencia de fallos.

Los tres perfiles son:

- instituciones y equipos de inversión;
- brokers y plataformas;
- traders independientes avanzados y equipos pequeños.

La oferta común tiene tres etapas:

1. diagnóstico y arquitectura;
2. construcción e integración;
3. continuidad técnica opcional.

Los cuatro ámbitos de trabajo son datos y trazabilidad, investigación reproducible, ejecución e integraciones, y supervisión y continuidad.

Los precios, márgenes, plazos cerrados, SLA de quince minutos, porcentajes de código reutilizable y prioridad comercial de brokers no aparecerán como hechos. Las tecnologías se mostrarán como ejemplos sujetos al caso, no como una arquitectura universal.

El llamado principal será `conversemos sobre tu infraestructura`. El contacto inicial no se confundirá con el diagnóstico pagado.

## Estructura compartida

Cada opción será un HTML autónomo dentro de `demos/`, enlazado desde un índice de comparación. Compartirá una hoja de estilos de extensión pequeña y un script específico, cargados después de `assets/qrt.css` y `assets/qrt.js`.

Las páginas tendrán:

1. barra discreta de comparación de propuestas;
2. cabecera oficial de qrt;
3. hero de producto;
4. cuerpo narrativo particular de la opción;
5. bloque de alcance y entregables;
6. llamada final;
7. pie oficial.

La barra de comparación se identificará como herramienta de prototipo, tendrá menor jerarquía que el sitio y no modificará la identidad de la página.

## Opción 01 · del modelo a la operación

### Tesis

La infraestructura de trading es la expresión comercial más directa del ciclo `q_ r_ t_`. Esta opción conecta el producto nuevo con la filosofía ya reconocible de qrt y es la recomendada.

### Hero

Etiqueta: `finanzas / infraestructura de trading_`

Título:

> del modelo a la operación.

Entrada:

> conectamos datos, investigación y ejecución para construir sistemas que tu equipo pueda entender, verificar y mantener.

CTA: `conversemos sobre tu infraestructura →`

### Relato

El cuerpo será un recorrido vertical de cuatro movimientos:

- `q_ / datos`: convertir fuentes dispersas en un flujo trazable;
- `r_ / investigación`: registrar hipótesis, parámetros y pruebas reproducibles;
- `t_ / ejecución`: integrar herramientas y proveedores con controles definidos;
- `^_ / continuidad`: observar, documentar y mejorar lo que vuelve de la operación.

Cada movimiento usa el componente `.block`, alterna texto y SVG, e incorpora una letra de fondo de baja opacidad. El cuarto movimiento usa `^` para cerrar el bucle y devolver visualmente a `q_`.

### Entregables

Una rejilla 2 × 2 presenta:

- arquitectura y prioridades;
- implementación por módulos;
- pruebas y criterios de aceptación;
- documentación y transferencia.

### Diferencia visual

El SVG central será un circuito continuo que atraviesa los cuatro movimientos y vuelve a su origen. La animación dibuja el trazo al entrar en pantalla. Respeta el lenguaje lineal y monocromático existente.

### Ventaja

Es la opción más propia de qrt, ofrece continuidad con la home y explica por qué esta empresa puede entregar el producto.

### Riesgo

Puede resultar abstracta para compradores que llegan con un problema inmediato. Se corrige con ejemplos operativos breves y entregables concretos en cada movimiento.

## Opción 02 · una infraestructura, tres operaciones

### Tesis

Los tres tipos de cliente comparten una arquitectura básica, pero entran por problemas diferentes. La página permite identificarse antes de explicar el método.

### Hero

Etiqueta: `finanzas / instituciones · brokers · traders_`

Título:

> cada operación empieza en un punto distinto.

Entrada:

> diseñamos el siguiente paso de tu infraestructura a partir de las herramientas, responsabilidades y límites que ya existen.

CTA: `encuentra tu punto de entrada ↓`

### Relato

La primera sección muestra tres paneles editoriales:

- **instituciones**: investigación difícil de reproducir y paso a producción frágil;
- **brokers y plataformas**: integraciones, controles y conciliación entre proveedores;
- **traders independientes**: scripts manuales, despliegues inestables y dependencia de una persona.

Al elegir un perfil se actualizan, dentro del mismo bloque, cuatro campos: situación, primera entrega, evidencia de aceptación y responsabilidad del cliente. La interacción usa texto, bordes y cambios de opacidad; no usa color para crear tres submarcas.

Luego aparece la arquitectura compartida: `datos → investigación → ejecución`, con `supervisión` como capa transversal. El diagrama deja claro que qrt no obliga a comprar el sistema completo.

### Entregables

Tres filas relacionan cada perfil con una primera contratación concreta:

- institución: diagnóstico de un flujo de investigación a producción;
- broker: diagnóstico de una integración y prueba de viabilidad;
- trader avanzado: revisión técnica y profesionalización de un flujo existente.

### Diferencia visual

La letra de fondo cambia entre `i`, `b` y `t` al seleccionar un perfil. Los paneles mantienen la rejilla, tipografía y tratamiento de las capacidades actuales.

### Ventaja

Es la opción más clara para calificar visitas y conducirlas hacia una conversación específica.

### Riesgo

Puede hacer que el producto parezca tres servicios distintos. El diagrama común y la misma secuencia de entrega evitan esa fragmentación.

## Opción 03 · construir con evidencia

### Tesis

El comprador entiende el producto como un proceso de reducción progresiva de incertidumbre: primero se delimita, luego se construye y después se sostiene.

### Hero

Etiqueta: `finanzas / diagnóstico · construcción · continuidad_`

Título:

> construir sólo lo que podemos verificar.

Entrada:

> cada etapa termina con decisiones, entregables y criterios de aceptación visibles para tu equipo.

CTA: `revisemos tu situación actual →`

### Relato

La página se organiza como tres capítulos numerados:

1. **diagnóstico y arquitectura**: mapa actual, riesgos, alternativas y primer alcance;
2. **construcción e integración**: módulos, pruebas, despliegue acordado y transferencia;
3. **continuidad técnica**: mantenimiento delimitado, revisión de incidentes y evolución.

Entre capítulos, una línea vertical muestra qué decisión habilita el paso siguiente. Ninguna etapa obliga a contratar la posterior.

Un bloque de aceptación muestra seis ejemplos de evidencia: despliegue reproducible, trazabilidad de acciones, pruebas de desconexión, conciliación, alertas y documentación. Se presentan como criterios a acordar, no garantías universales.

### Entregables

Cada capítulo incluye `recibís`, `decidís` y `qué queda fuera`. La exclusión visible protege el posicionamiento: licencias, datos, cargos de terceros y decisiones de inversión pertenecen al cliente salvo acuerdo específico.

### Diferencia visual

Los capítulos ocupan la altura completa en escritorio y usan numeración Fira Code de gran escala. Una barra de progreso de un píxel acompaña el desplazamiento y respeta las variables monocromáticas.

### Ventaja

Es la opción más comercial y reduce ambigüedad sobre qué se compra.

### Riesgo

Explica menos la filosofía de qrt. Un bloque final conecta las tres etapas con `q_ r_ t_` para recuperar la identidad.

## Contenido transversal

Las tres opciones cerrarán con este argumento:

> una infraestructura útil no termina cuando el código corre. termina cuando el equipo entiende qué hace, cómo se prueba y dónde están sus límites.

Debajo aparecerán cuatro señales de entrega:

- decisiones de arquitectura documentadas;
- pruebas acordadas antes de construir;
- dependencias y derechos de uso explícitos;
- transferencia al equipo responsable.

No se mostrarán logos de clientes ni casos sin autorización. Si se necesita evidencia visual, se usará una demostración de laboratorio claramente rotulada como tal.

## Accesibilidad y comportamiento adaptable

- Contraste mínimo WCAG AA en ambos temas.
- La interacción por perfiles y capítulos funcionará con teclado y conservará estados de foco visibles.
- `prefers-reduced-motion` eliminará el trazado animado, el desplazamiento suave y las transiciones no esenciales.
- En pantallas menores de 991 px se reutiliza el panel móvil oficial.
- Las rejillas pasan a una columna y el contenido no dependerá de hover.
- Los SVG son decorativos cuando el texto ya comunica el concepto; en ese caso usarán `aria-hidden="true"`.

## Verificación

La implementación se considerará completa cuando:

- las tres páginas carguen sin errores de consola;
- todos los enlaces del selector funcionen;
- navegación, tema, logotipo expansible y menú móvil se comporten como en el sitio actual;
- no aparezcan colores, fuentes o radios ajenos al manual;
- las páginas se revisen a 1440 px, 1024 px, 768 px y 390 px;
- el contenido siga siendo legible sin JavaScript;
- las afirmaciones comerciales respeten la nota de verificación de la investigación;
- ninguna modificación afecte los archivos actuales de producción.

## Recomendación

Implementar las tres para compararlas, pero usar **Opción 01 · del modelo a la operación** como candidata principal. Es la que transforma la investigación en producto sin perder el activo más distintivo de qrt: el ciclo `q_ r_ t_` y la idea de que el trading funciona como laboratorio de ingeniería.
