# Integración de soluciones e infraestructura de trading

Fecha: 24 de septiembre de 2026  
Estado: diseño aprobado para revisión previa a implementación

## Objetivo

Incorporar una opción principal `soluciones / solutions` en la navegación del sitio y convertir la opción 02 de infraestructura de trading en una página independiente dentro de la vertical financiera.

La integración mantiene la home como relato de marca. El nuevo producto se descubre desde la navegación o desde la página de finanzas sin interrumpir el scrollytelling `q_ r_ t_`.

## Navegación principal

Orden en español:

`inicio · filosofía⌄ · soluciones⌄ · ES | EN · login`

Orden en inglés:

`home · philosophy⌄ · solutions⌄ · ES | EN · login`

El nuevo elemento usa el mismo componente de menú desplegable que `filosofía`. No introduce otro patrón de interacción, color o icono.

### Menú en español

```text
soluciones
  infraestructura de trading
  ─────────────────────────
  finanzas
  minería
  retail
  ─────────────────────────
  neurociencia · I+D
```

### Menú en inglés

```text
solutions
  trading infrastructure
  ──────────────────────
  finance
  mining
  retail
  ──────────────────────
  neuroscience · R&D
```

`infraestructura de trading` aparece primero porque es el nuevo producto concreto. Las industrias se mantienen juntas después del primer divisor. Neurociencia conserva una separación y una etiqueta que indican que es investigación, no un servicio disponible.

## Rutas nuevas

- Español: `infraestructura-trading.html`.
- Inglés: `en-trading-infrastructure.html`.

Cada página incluye `hreflang` recíproco y `x-default` hacia la versión española. Los metadatos y datos estructurados la presentan como un servicio de ingeniería para infraestructura de trading. No se publicarán precios, márgenes, SLA ni capacidades no confirmadas.

## Página del producto

La página española parte de la opción 02 aprobada y adopta la voz definida en `2026-09-24-qrt-opcion-02-voz-humana-design.md`.

Secuencia:

1. **Hero:** `partimos de cómo operas hoy.`
2. **Tres situaciones:** instituciones, brokers y plataformas, traders independientes avanzados.
3. **Sistema compartido:** datos, investigación, ejecución y operación.
4. **Primera contratación:** revisión de un flujo real antes de construir.
5. **Cierre:** conversación sobre la operación actual.

La selección de perfiles se mantiene interactiva, pero el contenido del primer perfil queda visible sin JavaScript. Los otros dos perfiles también permanecen en el HTML para indexación y accesibilidad.

## Relación con finanzas

En `soluciones-finanzas.html`, la capacidad `infraestructura de mercado` conserva su lugar dentro de la rejilla. La tarjeta incorpora el enlace:

`ver infraestructura de trading →`

Este enlace conduce a `infraestructura-trading.html`. El texto general de finanzas no se duplica dentro de la página del producto.

La página de producto responde `cómo trabajamos sobre la infraestructura`. La vertical financiera responde `qué problemas financieros abordamos`. Esa diferencia evita contenido repetido.

## Relación con la home

La home sólo recibe el nuevo menú. No se agrega la página completa ni otro bloque comercial dentro del scrollytelling.

Podrán añadirse enlaces contextuales desde `research` y `trading` más adelante, cuando se cierre la sección `^_`. No forman parte de esta implementación para evitar modificar el relato principal antes de resolver esa sección.

## Página inglesa

La versión inglesa es una adaptación editorial, no una traducción literal. Mantiene la voz técnica y directa.

Hero:

> **we start with how you operate today.**  
> We review your tools, find where the process becomes fragile, and decide what is worth building first.

Perfiles:

- institutions and investment teams;
- brokers and platforms;
- advanced independent traders.

CTA:

`talk to us about your operation →`

## Archivos alcanzados

- `index.html`: incorporar `soluciones` en la navegación.
- `en.html`: incorporar `solutions` en la navegación.
- `soluciones-finanzas.html`: ordenar el menú y enlazar la capacidad.
- `infraestructura-trading.html`: nueva página española.
- `en-trading-infrastructure.html`: nueva página inglesa.
- `demos/infraestructura-trading/opcion-02.html`: actualizar el prototipo con el lenguaje aprobado.
- `assets/qrt.css`: agregar únicamente estilos compartidos que la página de producto necesite y que no existan.
- `assets/qrt.js`: extender sólo si hace falta para la selección accesible de perfiles.

No se crearán páginas vacías para minería, retail o neurociencia. Los enlaces que todavía no tienen destino se conservarán únicamente donde ya existen; esta implementación no ampliará enlaces rotos.

## Navegación móvil

El nuevo menú aparece expandido dentro del panel móvil, siguiendo el comportamiento actual de `filosofía`. La página de producto debe permitir recorrer los tres perfiles sin depender de hover.

Al elegir un enlace se cierra el panel. Escape y el botón de cierre mantienen el comportamiento compartido existente.

## Accesibilidad y SEO

- `soluciones / solutions` usa un control navegable con teclado y estado accesible.
- La selección de perfiles usa `role="tablist"`, `role="tab"` y `role="tabpanel"`.
- El foco es visible y el contenido no depende únicamente del color.
- La página carga contenido legible sin JavaScript.
- Metadescripción, canonical, `hreflang` y datos estructurados describen el servicio sin promesas financieras.
- El producto se enlaza desde dos páginas internas como mínimo: home y finanzas.

## Verificación

- Comprobar los menús en español e inglés en escritorio y móvil.
- Validar que cada selector de idioma lleve a la misma página en el otro idioma.
- Revisar los tres perfiles con ratón y teclado.
- Probar modo claro y oscuro.
- Confirmar que el enlace desde finanzas llegue al producto.
- Revisar a 1440, 1024, 768 y 390 píxeles.
- Ejecutar comprobación de enlaces locales y JavaScript.
- Confirmar que ninguna afirmación comercial contradiga la verificación del notebook.

## Resultado esperado

El visitante puede descubrir el producto desde la navegación principal, entender si corresponde a su situación y llegar a una conversación sin atravesar contenido que no necesita. La home conserva su papel de presentar la filosofía; finanzas conserva su papel de vertical; infraestructura de trading funciona como producto específico.
