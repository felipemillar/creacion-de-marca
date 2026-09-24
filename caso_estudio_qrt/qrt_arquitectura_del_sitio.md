# Arquitectura del sitio: resolución del eje de navegación

Documento de decisión. Resuelve el conflicto entre las dos estructuras de sitio que
proponen los documentos anteriores, y fija el mapa definitivo antes de escribir más HTML.

Complementa a [qrt_adn_y_mensajes.md](qrt_adn_y_mensajes.md) (ADN y voz) y a
[qrt_nexo_filosofia_industrias.md](qrt_nexo_filosofia_industrias.md) (el nexo).
Donde este documento contradiga la estructura del §5 del ADN, gana este documento.

---

## 1. El conflicto

Hay dos mapas del sitio escritos en dos momentos distintos, y no coinciden.

| Origen | Eje | Páginas |
| :--- | :--- | :--- |
| ADN §5 (30 jul) | **audiencia** | `que-hacemos`, `como-trabajamos`, `tecnologia` |
| Nexo §6 + lo construido (2 ago) | **industria** | `soluciones-finanzas`, `-mineria`, `-retail`, `neurociencia` |

Hoy conviven a medias: la navegación implementada usa el eje de industria, y el eje de
audiencia no existe en ninguna parte. El resultado es que una de las tres audiencias
—el talento técnico— no tiene puerta de entrada.

Elegir "uno de los dos" es la respuesta equivocada. La correcta es notar que **un eje
absorbe al otro sólo parcialmente**, y construir únicamente lo que queda fuera.

---

## 2. El criterio de resolución

Una página se justifica si responde una pregunta que ninguna otra responde. Aplicado a
las tres audiencias del ADN §5:

| Audiencia | Qué necesita creer | ¿Lo cubre una vertical? |
| :--- | :--- | :--- |
| C-level financiero institucional | Que esto reduce riesgo y es defendible ante un directorio | **Sí** — `soluciones-finanzas` ya lo hace: capacidades + clientes con nombre |
| Empresas fuera de finanzas | Que su problema de decisión se parece al de un mercado | **Parcialmente** — la vertical muestra el *qué*, pero el *por qué* es el argumento del nexo y no cabe ahí |
| Talento técnico | Que aquí hay problemas difíciles y estándares reales | **No** — un quant no entra por "minería" |

De ahí salen exactamente dos páginas nuevas, no tres:

- **`metodo.html`** — el argumento del nexo completo, que hoy sólo vive en un `.md`.
- **`tecnologia.html`** — la única audiencia sin puerta.

Y una que se descarta: `que-hacemos.html`.

---

## 3. Por qué se descarta `que-hacemos.html`

Los servicios ya están distribuidos en las verticales, como bloque 3 de la plantilla
("qué hacemos aquí"). En finanzas son cuatro: modelos y señales, infraestructura de
mercado, riesgo y cumplimiento, asesoría patrimonial automatizada.

Una página de servicios genérica los volvería a listar sin industria. Eso destruye el
hallazgo central del nexo §3 —**el cuello de botella de cada industria determina qué se
vende ahí**— y produce justo la lectura que el ADN §7 manda evitar: la de una consultora
generalista con un catálogo.

El catálogo se lee mejor desde el problema del cliente que desde la oferta.

---

## 4. Por qué `metodo.html` no duplica a la home

Es la objeción obvia: la home ya recorre `q_ r_ t_`. La respuesta está en el marco que el
propio nexo §7.2 usa para decidir el visual de `^_`.

| | home | `metodo.html` |
| :--- | :--- | :--- |
| Sistema | 1 — forma, ritmo, scroll | 2 — argumento, tablas, lectura |
| Función | que el lector *sienta* el ciclo | que el lector *pueda defenderlo* ante su jefe |
| Formato | scrollytelling animado | prosa lineal y estructurada |
| Extensión | una frase por etapa | el desarrollo completo |
| Citable por un LLM | mal — texto animado, sin estructura | **bien** — es el objetivo de la página |

La home convence. `metodo.html` da los argumentos con los que el convencido convence a
otro. Son funciones distintas del mismo contenido, no repetición.

Su contenido ya está escrito: son las secciones 1 a 5 de
[qrt_nexo_filosofia_industrias.md](qrt_nexo_filosofia_industrias.md) —el ciclo, la tabla
de las cuatro propiedades, el cuello de botella por industria, el tick, y la matriz.
Es el material más valioso del proyecto y hoy no está en el sitio.

**Nota de GEO:** es la página que debe llevar el `HowTo` en JSON-LD del nexo §7.5, no la
home. Un recomendador de IA extrae mejor de prosa estructurada que de una animación.

---

## 5. El mapa del sitio

```
home  index.html
│  hero → q_ → r_ → t_ → ^_ → las cuatro industrias
│
├─ el método  metodo.html
│     el ciclo · por qué el trading viaja · el tick de cada industria · la matriz
│
├─ soluciones/                              ← eje primario de entrada
│  ├─ finanzas    soluciones-finanzas.html    ✅ construida
│  ├─ minería     soluciones-mineria.html
│  └─ retail      soluciones-retail.html
│
├─ investigación  neurociencia.html         ← I+D, no se vende
│
├─ tecnología     tecnologia.html           ← puerta del talento técnico
├─ nosotros       nosotros.html             ← trayectoria y legitimidad
└─ contacto       contacto.html             ← destino único de conversión
```

Ocho páginas más la home. Siete por construir, y el doble de archivos por el espejo en
inglés del §7: **nueve pares, dieciocho archivos.**

### 5.1 Las dos páginas que ningún documento anterior había pedido

**`nosotros.html`.** Las tres audiencias necesitan lo mismo antes de creer cualquier otra
cosa: saber quién está detrás. Hoy el sitio no lo dice en ninguna parte. Además es el
único lugar donde el valor *operar antes de recomendar* (ADN §3.3) se puede demostrar
como historia y no como afirmación: la empresa nació operando capital propio.

**`contacto.html`.** El sitio no tiene destino de conversión. El único botón destacado de
la navegación es `login`, que no convierte a nadie que no sea ya cliente. Un sitio B2B que
le habla a un C-level y no le ofrece una vía de contacto no está terminado.

---

## 6. La navegación

```
qrt^  |  inicio  filosofía ▾  soluciones ▾  tecnología  nosotros  |  ES|EN  login  [contacto]
```

```
filosofía ▾                    soluciones ▾
  quantitative                   finanzas
  research                       minería
  trading                        retail
  ─────────────                  ─────────────
  el ciclo ^                     neurociencia · I+D
  el método
```

Cinco elementos visibles. Cumple la Ley de Hick sin esconder nada relevante.

### 6.1 Tres cambios respecto de lo implementado hoy

1. **`el método` entra bajo `filosofía`**, después de una línea. El desplegable pasa a
   espejar la estructura de la home: las tres letras, el ciclo que las cierra, y la
   lectura profunda al final. La navegación enseña el argumento antes de que lo lean.
2. **`neurociencia` se etiqueta `neurociencia · I+D`**, no sólo separada por una línea.
   El ADN §7 decidió dejarla en el submenú de soluciones; se respeta, pero la línea sola
   es una señal demasiado débil. Estando bajo `soluciones` sin etiqueta, el lector asume
   que está en venta — y el ADN es explícito en que no lo está.
3. **`login` deja de ser el botón destacado.** El portal de clientes existe y se mantiene,
   pero baja a enlace discreto: sirve a quien ya es cliente, no a quien está decidiendo.
   El slot de mayor jerarquía visual va para `contacto`, que es el que convierte.
   Pendiente: la URL real del portal, hoy es `href="#"`.

### 6.2 Orden de las verticales

Hoy el submenú y el footer las listan `minería · retail · finanzas`, y en el footer no
hay divisor antes de neurociencia. Debe ser `finanzas · minería · retail` en los dos:
finanzas primero porque es la única respaldada por el core operativo, la única construida
y la que le habla a la audiencia primaria. El orden de un menú es una jerarquía.

---

## 7. URLs e idioma

Decidir esto ahora es barato; retrofitearlo con ocho páginas publicadas rompe enlaces y
posicionamiento.

**URLs.** Se mantiene el esquema plano con guion —`soluciones-finanzas.html`— que ya está
implementado. No hay build ni servidor que justifique directorios, y renombrar lo
existente no compra nada.

**Idioma: espejo completo.** Decidido el 2026-08-02. Las nueve páginas existen en ambos
idiomas. El esquema actual no soporta eso: `en.html` es la home inglesa y el conmutador de
`soluciones-finanzas.html` apunta a la home inglesa, no a su traducción.

Esquema: plano, prefijo `en-`, **slug en inglés**. El slug traducido es lo que posiciona
en inglés; `en-soluciones-finanzas.html` no lo hace. El TODO que ya está en el archivo
—`crear solutions-finance.html`— apuntaba a esto.

| es | en |
| :--- | :--- |
| `index.html` | `en.html` |
| `metodo.html` | `en-method.html` |
| `soluciones-finanzas.html` | `en-solutions-finance.html` |
| `soluciones-mineria.html` | `en-solutions-mining.html` |
| `soluciones-retail.html` | `en-solutions-retail.html` |
| `neurociencia.html` | `en-neuroscience.html` |
| `tecnologia.html` | `en-technology.html` |
| `nosotros.html` | `en-about.html` |
| `contacto.html` | `en-contact.html` |

Cada par lleva `hreflang` recíproco más `x-default` apuntando al español. Con el espejo
completo el conmutador ya nunca miente: siempre existe la contraparte.

Se descartó el directorio `en/` con slugs limpios, que es el estándar. Obliga a rutas
`../assets/` y a que el hosting sirva índices de directorio, y el sitio es demasiado
pequeño para pagar eso. Si más adelante hay hosting con URLs limpias, migrar es un
renombrado y una tabla de redirecciones.

### 7.1 El espejo completo obliga a un paso de construcción

Esta es la consecuencia que hay que aceptar antes de seguir. Dieciocho archivos con la
cabecera, la navegación, el desplegable y el pie copiados a mano no se mantienen
sincronizados. No es una hipótesis: **ya está pasando con dos**. En
`soluciones-finanzas.html` el submenú ordena las verticales `minería · retail · finanzas`
y el pie las ordena distinto y omite el divisor de neurociencia, en el mismo archivo.

Tres salidas:

| Opción | Veredicto |
| :--- | :--- |
| Copiar y pegar en 18 archivos | Descartada. Cada cambio de menú son 18 ediciones y la deriva es segura |
| Inyectar cabecera y pie con JavaScript | **Descartada, y es importante por qué.** Un crawler o un recuperador de IA que no ejecuta JS no ve la navegación ni los enlaces. El sitio está optimizado para ser citado por LLMs; esto lo rompería justo ahí |
| Paso de construcción con parciales | **Elegida.** Un script corto ensambla las páginas desde `partials/` y emite HTML estático plano. Se conserva todo el beneficio de SEO/GEO y la navegación se edita una vez |

El resultado sigue siendo el mismo sitio estático de hoy. Lo único que cambia es que
`header`, `nav`, `footer` y el conmutador de idioma pasan a existir una sola vez por
idioma, y que las cadenas de traducción quedan en un solo lugar en vez de dispersas en
nueve archivos.

---

## 8. Decisiones tomadas el 2026-08-02

| # | Decisión | Resolución |
| :--- | :--- | :--- |
| 1 | `login` | El portal existe. Se mantiene como enlace discreto; `contacto` toma el botón destacado. **Falta la URL real** |
| 2 | Alcance del inglés | Espejo completo, nueve pares. Obliga al paso de construcción del §7.1 |
| 3 | Nombre del argumento del nexo | `metodo.html`, etiqueta `el método` |

---

## 9. Insumos bloqueantes

Dos de las páginas nuevas no se pueden escribir sin datos que sólo tiene el cliente. Ya
estaban en el ADN §10 y siguen pendientes:

| Página | Insumo que falta |
| :--- | :--- |
| `nosotros.html` | Año de fundación, origen, 2 o 3 hitos con fecha |
| `tecnologia.html` | Lenguajes, infraestructura de cómputo, volumen y frecuencia de datos, herramientas de backtesting y monitoreo |
| `soluciones-*.html` | Permiso de uso de marca, sobre todo de BHP y Antofagasta Minerals |
| footer (todas) | Ciudad y país de la casa matriz |

`metodo.html` y las dos verticales restantes **no** están bloqueadas: su contenido ya está
escrito en los documentos de estrategia.

---

## 10. Orden de construcción

El criterio es no escribir dos veces la misma pieza.

| # | Trabajo | Por qué en este lugar |
| :--- | :--- | :--- |
| 1 | Paso de construcción con parciales, y extraer el CSS/JS de `index.html` a `assets/` | Con dieciocho archivos esto deja de ser higiene y pasa a ser condición previa. Toda página nueva hereda de aquí |
| 2 | Cerrar la home: sección `^_`, bloque de industrias, ajuste de una frase en `t_` | Es el destino del menú `soluciones` y el clímax narrativo que hoy falta |
| 3 | `metodo.html` | Contenido ya escrito en el nexo §1–5. Da destino al desplegable `filosofía` |
| 4 | Componente puente `q_ r_ t_` en finanzas, con la matriz del nexo §5 | Se diseña una vez y se replica en las otras dos verticales |
| 5 | `soluciones-mineria.html` y `soluciones-retail.html` | Repiten plantilla y puente ya probados. Cierran los enlaces rotos |
| 6 | `contacto.html` | Barata y desbloquea la conversión |
| 7 | `neurociencia.html` | Sin bloque de prueba, según el ADN §7 |
| 8 | `nosotros.html` y `tecnologia.html` | Bloqueadas por insumos |
| 9 | Espejo en inglés de las nueve | Último por una razón concreta: cada página en español que cambia después de traducida es trabajo hecho dos veces. Se traduce sobre contenido congelado |

El espejo va al final **como fase**, no como pensamiento tardío. La estructura que lo
soporta —parciales, cadenas separadas, `hreflang`— entra en el paso 1.
