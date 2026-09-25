# Reescritura de la opción 02: voz técnica y humana

Fecha: 24 de septiembre de 2026  
Estado: diseño aprobado para revisión previa a implementación

## Objetivo

Reescribir la opción 02 de infraestructura de trading para que suene como un equipo técnico con experiencia hablando con otro equipo. Se mantiene completa la estructura visual y funcional actual.

La voz combina precisión técnica con situaciones reconocibles. Evita construcciones simétricas, lenguaje de consultoría genérica y frases que parecen escritas para completar una plantilla.

## Reglas de escritura

- Frases breves, con sujeto y verbo claros.
- Nombrar problemas observables: archivos dispersos, procesos manuales, desconexiones, estados inconsistentes y dependencia de una persona.
- Una idea por oración.
- Usar palabras cotidianas antes que categorías abstractas.
- Hablar de `tu equipo`, `tu operación` y `lo que ya tienes` sólo cuando aporta claridad.
- Conservar términos técnicos que un comprador reconoce: datos, API, conciliación, producción, despliegue y alertas.
- Evitar `ecosistema`, `solución integral`, `punto de entrada`, `buen encaje`, `estándares de entrega`, `profesionalización`, `trazabilidad` y `responsable` cuando exista una forma más directa.
- No usar paralelismos decorativos ni cadenas de tres conceptos sólo por ritmo.
- No prometer rendimiento, continuidad absoluta, cumplimiento automático ni resultados financieros.

## Hero

Etiqueta:

`infraestructura de trading / instituciones · brokers · traders`

Título:

> partimos de cómo operas hoy.

Entrada:

> Revisamos tus herramientas, detectamos dónde se vuelve frágil el proceso y definimos qué conviene construir primero.

CTA:

`elige tu situación ↓`

## Introducción de perfiles

Título:

> tres operaciones. problemas distintos._

Texto:

> Un fondo, un broker y un trader independiente no necesitan la misma infraestructura. Elige el caso que más se parece al tuyo.

Las etiquetas de cada perfil serán `qué suele pasar`, `por dónde empezamos`, `qué entregamos` y `qué necesitamos de tu equipo`.

## Perfil: instituciones

Título:

> llevar una estrategia a producción todavía requiere demasiado trabajo manual.

Descripción:

> Los datos están en un lugar, las pruebas en otro y el despliegue depende de pocas personas. Antes de construir, seguimos un flujo completo y ubicamos dónde se pierde tiempo o control.

Campos:

- **Qué suele pasar:** El proceso cambia entre investigación y producción. Repetir una prueba o explicar una decisión toma más tiempo del necesario.
- **Por dónde empezamos:** Elegimos una estrategia o proceso y seguimos su recorrido de principio a fin.
- **Qué entregamos:** El mapa actual, los problemas prioritarios y el diseño del primer módulo.
- **Qué necesitamos de tu equipo:** Una persona que conozca el proceso, acceso a las herramientas incluidas y tiempo para revisar las decisiones.

## Perfil: brokers y plataformas

Título:

> las integraciones funcionan hasta que un estado deja de coincidir.

Descripción:

> Una orden pasa por varias plataformas antes de quedar cerrada. Cuando algo falla, el problema puede estar en la conexión, en una regla o en la conciliación. Revisamos el flujo completo antes de tocar código.

Campos:

- **Qué suele pasar:** Los estados no coinciden, la recuperación es manual o los incidentes dependen de revisar varios sistemas.
- **Por dónde empezamos:** Elegimos una integración concreta y definimos los fallos que debe soportar.
- **Qué entregamos:** El flujo documentado, sus dependencias y una prueba de viabilidad del cambio propuesto.
- **Qué necesitamos de tu equipo:** Accesos autorizados, un interlocutor técnico y disponibilidad de los proveedores involucrados.

## Perfil: traders independientes avanzados

Título:

> un script útil no siempre está listo para operar sin supervisión.

Descripción:

> La diferencia aparece cuando se corta una conexión, cambia una API o el proceso debe reiniciarse. Revisamos lo que ya funciona y añadimos sólo la estructura necesaria para sostenerlo.

Campos:

- **Qué suele pasar:** Hay tareas manuales, alertas insuficientes o conocimiento que sólo conserva una persona.
- **Por dónde empezamos:** Elegimos una estrategia y una conexión. Probamos el flujo actual y sus fallos más frecuentes.
- **Qué entregamos:** Un plan técnico, el alcance del primer cambio y la forma de comprobarlo.
- **Qué necesitamos de tu equipo:** Una estrategia definida, cuentas propias y alguien que pueda operar el sistema después de la entrega.

## Sistema compartido

Título:

> construimos sólo el tramo que hace falta._

Texto:

> Podemos trabajar sobre datos, investigación, ejecución o monitoreo. La arquitectura depende del problema y de las herramientas que ya utiliza el equipo.

Módulos:

- **datos:** Fuentes identificadas, transformaciones registradas y controles sobre el flujo acordado.
- **investigación:** Pruebas que pueden repetirse con los mismos datos, parámetros y versiones.
- **ejecución:** Conexiones, órdenes y estados puestos a prueba bajo escenarios definidos.
- **operación:** Registros, alertas, recuperación y documentación para el equipo que queda a cargo.

## Primera contratación

Título:

> antes de construir, revisamos un flujo real._

Introducción:

> La primera conversación sirve para entender el problema. Si existe un alcance claro, el diagnóstico es un trabajo separado y termina con decisiones que el cliente puede usar con qrt o con otro proveedor.

Tarjetas:

- **Institución — una estrategia:** Seguimos el recorrido desde los datos hasta el despliegue y definimos el primer cambio.
- **Broker — una integración:** Revisamos conexiones, estados y conciliación antes de proponer una modificación.
- **Trader avanzado — un proceso:** Probamos lo que ya existe y ordenamos los cambios por impacto y esfuerzo.
- **En todos los casos — una decisión:** El cliente recibe un alcance, una arquitectura y criterios para aceptar el trabajo siguiente.

## Cierre

Declaración:

> no empezamos por la tecnología. empezamos por el lugar donde hoy se rompe el proceso.

Apoyo:

> Cuéntanos qué operas, qué herramientas usas y qué parte todavía depende de trabajo manual.

CTA:

`conversemos sobre tu operación →`

## Alcance de implementación

Se modificará sólo `demos/infraestructura-trading/opcion-02.html`, excepto ajustes mínimos de CSS si una nueva etiqueta requiere más espacio. No cambiarán la composición, las interacciones, el comportamiento responsive ni las otras dos propuestas.

## Verificación

- Revisar que ninguna oración supere 20 palabras salvo cuando dividirla perjudique la comprensión.
- Buscar y eliminar las expresiones prohibidas de esta especificación.
- Comprobar los tres estados del selector de perfiles.
- Revisar escritorio, tablet y móvil para detectar desbordes causados por el nuevo texto.
- Confirmar que la página conserva modo claro, modo oscuro y navegación por teclado.
