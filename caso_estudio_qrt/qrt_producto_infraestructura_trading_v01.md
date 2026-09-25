# qrt | infraestructura de trading

Propuesta de producto v0.1 · 24 de septiembre de 2026

Estado: propuesta para definir la oferta. Capacidades, precios, plazos y compromisos de soporte pendientes de validación interna. No reemplaza el ADN de marca ni constituye una oferta contractual.

## 1. La idea del producto

**Diseñar, construir y transferir la infraestructura que conecta datos, investigación y ejecución de trading.**

El cliente compra una mejora concreta en su forma de trabajar: procesos conectados, controles explícitos, pruebas reproducibles y conocimiento que su equipo pueda conservar.

La oportunidad para qrt es convertir su experiencia técnica en una forma de entrega reconocible. El producto abarca el recorrido completo, pero cada contratación resuelve un problema delimitado.

Nombre recomendado: **qrt | infraestructura de trading**. Mantenerlo bajo la marca principal permite acumular reputación y evita introducir una marca nueva antes de validar la oferta.

Promesa propuesta:

> Conectamos tus datos, herramientas y procesos para construir una infraestructura de trading que puedas entender, verificar y mantener.

Esta es una decisión de posicionamiento derivada de la investigación y del ADN de qrt. No es una demanda comercial ya demostrada.

## 2. Qué expresa de la nueva etapa

La empresa pasa de describir capacidades a mostrar cómo esas capacidades se convierten en una entrega. El vínculo con el laboratorio de trading permanece: aprender, poner a prueba y documentar antes de proponer una solución al cliente.

| Principio de marca | Manifestación en el producto |
|---|---|
| Mostrar el trabajo | Arquitectura, supuestos, decisiones y resultados de pruebas disponibles para el cliente. |
| Dudar de lo que funciona | Pruebas de fallos, revisión de dependencias y criterios de revalidación. |
| Operar antes de recomendar | Evidencia de los componentes efectivamente probados; diferencias explícitas entre laboratorio, piloto y producción. |

El laboratorio aporta credibilidad cuando podemos mostrar su alcance. Haber usado un componente internamente no demuestra que toda una arquitectura esté validada para cualquier cliente.

## 3. Tres recorridos de cliente

Los tres perfiles comparten método y estándares de entrega. Cambian el problema inicial, la complejidad y las responsabilidades.

| Perfil | Situación de entrada | Primera entrega adecuada | Condición de encaje |
|---|---|---|---|
| Instituciones y equipos de inversión | Datos y herramientas dispersos; investigación difícil de reproducir; paso a producción frágil. | Diagnóstico de un flujo y diseño de su arquitectura objetivo. | Responsable interno, acceso a sistemas y problema acotable. |
| Brokers y plataformas | Necesidad de conectar proveedores, plataformas, controles o conciliación. | Diagnóstico de una integración y prueba de viabilidad. | Acceso técnico autorizado, interlocutor operativo y dependencias identificadas. |
| Traders independientes avanzados y pequeños equipos | Scripts manuales, despliegue inestable o dependencia de una sola persona. | Revisión técnica y profesionalización de un flujo sobre herramientas existentes. | Estrategia definida, presupuesto de ingeniería y capacidad para operar lo entregado. |

En la web usar «traders independientes» en lugar de «retail»: la marca también tiene una vertical vinculada al consumo, y ambos significados podrían confundirse.

**Foco inicial recomendado:** clientes con un proceso existente y un cuello de botella identificable, dentro de plataformas que qrt domine. La investigación no demuestra todavía que brokers conviertan mejor que instituciones. La prioridad comercial debe combinar acceso real a compradores, experiencia comprobable y complejidad asumible.

## 4. Una oferta con tres etapas contratables

### 01 · Diagnóstico y arquitectura

**Pregunta que resuelve:** qué necesitamos cambiar, por qué y en qué orden.

Incluye entrevistas técnicas, inventario de sistemas y dependencias, revisión de un flujo, identificación de fallos relevantes y evaluación de construir, integrar o adquirir componentes.

Entregables:

- Mapa de la situación actual y arquitectura propuesta.
- Lista priorizada de problemas, con evidencia y consecuencias operativas.
- Alternativas con ventajas, límites y costos por confirmar.
- Hoja de ruta, alcance del primer módulo y criterios de aceptación.
- Estimación de esfuerzo, dependencias y responsables.

La conversación inicial sirve para determinar encaje. El diagnóstico es un trabajo remunerado, con entregables propios y útil aunque el cliente implemente con otro proveedor.

### 02 · Construcción e integración

**Pregunta que resuelve:** cómo convertir la arquitectura elegida en un sistema verificable.

Se contrata por módulos y por hitos. Incluye implementación, pruebas, despliegue acordado, documentación y transferencia al equipo del cliente.

El cierre exige evidencias de aceptación, dependencias conocidas y un procedimiento operativo. Los cambios de alcance se estiman antes de ejecutarse. El cliente controla las autorizaciones para producción.

### 03 · Continuidad técnica

**Pregunta que resuelve:** cómo mantener y evolucionar lo entregado.

Servicio opcional para mantenimiento de conectores, revisión de incidentes, actualizaciones y mejoras delimitadas. El acuerdo distingue horario de cobertura, tiempo de respuesta, capacidad reservada y qué requiere presupuesto adicional.

No fijar todavía disponibilidad permanente ni respuestas de 15 minutos: dependen del equipo, turnos y herramientas realmente disponibles. El acompañamiento técnico no implica decidir operaciones de inversión por el cliente.

## 5. Cuatro módulos para organizar las capacidades

Son familias de trabajo dentro del producto; su publicación depende de confirmar capacidad de entrega.

| Módulo | Qué construimos | Evidencia de entrega |
|---|---|---|
| Datos y trazabilidad | Ingesta, normalización, almacenamiento y controles de calidad del flujo acordado. | Origen y versiones identificados; incidencias de datos detectables. |
| Investigación reproducible | Entorno de experimentación, registro de versiones y pruebas de estrategias suministradas. | Un experimento puede repetirse con sus datos, parámetros y limitaciones. |
| Ejecución e integraciones | Conectores y coordinación entre herramientas, APIs o protocolos adecuados al caso. | Pruebas de órdenes, rechazos, reconexión y conciliación del flujo incluido. |
| Supervisión y continuidad | Registros, alertas, controles técnicos y procedimientos de recuperación. | Fallos definidos se detectan y el equipo conoce la respuesta prevista. |

La arquitectura se elige por restricciones y necesidades del cliente. FIX, MT5, Python, C++, Rust o una base de datos determinada no son requisitos universales ni capacidades confirmadas de qrt por aparecer en el notebook.

## 6. Primer piloto propuesto

**Profesionalizar un flujo existente, de extremo a extremo.**

Alcance orientativo: una estrategia o proceso suministrado por el cliente, un mercado, una conexión a broker y un entorno de prueba. Seleccionar el piloto dentro de las plataformas ya dominadas por qrt. Si la mayor fortaleza actual es datos o investigación, aplicar el mismo formato a ese flujo sin incluir ejecución.

Ejemplo: pasar de un script que requiere supervisión manual a un despliegue documentado con registros, alertas y recuperación ante desconexiones.

Criterios de aceptación acordados antes de construir:

1. El despliegue se reproduce con instrucciones y dependencias registradas.
2. Las acciones del sistema y sus respuestas quedan trazadas.
3. Los escenarios de desconexión y reintento definidos no generan duplicaciones en las pruebas.
4. El estado local se contrasta con el del proveedor en los escenarios incluidos.
5. Las alertas llegan al responsable y se prueba el procedimiento de recuperación.
6. El cliente recibe documentación, capacitación y registro de problemas pendientes.

Los umbrales de rendimiento y el período de observación se pactan según el caso. Una prueba aprobada no demuestra ausencia de fallos en cualquier condición. La activación real requiere aceptación del cliente y un plan específico; no se prescribe una asignación de capital.

## 7. Modelo comercial propuesto

| Etapa | Modalidad | Base del presupuesto |
|---|---|---|
| Diagnóstico | Precio por alcance definido. | Sistemas incluidos, profundidad de revisión y entregables. |
| Implementación | Proyecto por módulos e hitos aceptables. | Esfuerzo por rol, integraciones, pruebas, dependencias y transferencia. |
| Continuidad | Acuerdo periódico opcional. | Cobertura, capacidad reservada, criticidad y mantenimiento incluido. |

Separar honorarios qrt de infraestructura, datos, licencias y cargos de terceros. Describir qué código se desarrolla para el cliente, qué componentes previos se licencian y qué dependencias tienen sus propias condiciones.

**No adoptar aún los precios del notebook.** USD 15.000 por diagnóstico y USD 4.000–7.500 mensuales son supuestos del estudio, sin validación suficiente para convertirse en tarifa de qrt. Tampoco los márgenes proyectados acreditan rentabilidad.

Antes de cotizar, construir una estimación con horas y costo completo por rol, pruebas, gestión, preventa, retrabajo, soporte y terceros. Contrastar esa estimación con conversaciones y propuestas reales. La disponibilidad para dos proyectos simultáneos y varios contratos de soporte debe comprobarse con carga de trabajo concreta.

## 8. Diferenciación que podemos construir

La combinación propuesta es: experiencia de dominio demostrable, integración adaptada al cliente, pruebas visibles y transferencia de conocimiento.

La independencia técnica debe explicarse mediante entregables y condiciones de salida. «Propiedad absoluta del código» no describe bien una solución que combina componentes propios, desarrollos específicos y terceros.

También hay alternativas abiertas: LEAN permite ejecutarse con infraestructura propia, y Devexperts contempla entrega de código fuente. Por eso la apertura por sí sola no demuestra exclusividad competitiva. La diferenciación de qrt debe acreditarse en cómo diseña, entrega y acompaña. Fuentes: [QuantConnect, Algorithm Engine](https://www.quantconnect.com/docs/v2/writing-algorithms/key-concepts/algorithm-engine) y [Devexperts, soluciones para brokers](https://devexperts.com/solutions-for-equity-brokerages/).

El programa de consultores independientes de QuantConnect confirma que existe un formato de consultoría, desarrollo y enseñanza alrededor de estas herramientas. No demuestra el precio, la demanda local ni una acreditación de qrt. [Fuente oficial](https://www.quantconnect.com/docs/v2/cloud-platform/community/integration-partners).

## 9. Traducción a la página web

### Texto principal propuesto

Etiqueta: `infraestructura de trading_`

**La infraestructura detrás de tu operación.**

Conectamos datos, investigación y ejecución. Diseñamos e implementamos sistemas con pruebas, documentación y controles definidos para tu operación.

Para instituciones, brokers y traders independientes avanzados.

CTA principal: **Conversemos sobre tu infraestructura**.

### Secuencia de la sección

1. **Tu punto de partida.** Tres entradas por perfil, con un problema reconocible por cada una.
2. **El sistema que conectamos.** Diagrama datos → investigación → ejecución, con supervisión transversal.
3. **Lo que recibes.** Arquitectura, implementación validada, documentación y transferencia.
4. **Cómo avanzamos.** Diagnóstico → construcción → continuidad opcional.
5. **Evidencia.** Caso real autorizado o demostración de laboratorio claramente identificada.
6. **Conversación inicial.** Perfil, herramientas actuales, problema y objetivo.

El detalle de lenguajes, proveedores y protocolos aparece después de explicar el resultado. Los números, certificaciones y logos se publican cuando tengan evidencia y autorización de uso.

### Dirección visual recomendada

Desarrollar la opción editorial clara de las tres muestras como base. Mantener espacios generosos, tipografía legible, minúsculas de marca y un acento técnico moderado. Incorporar un diagrama del sistema inspirado en la opción laboratorio; las rutas por perfil pueden tomar la interacción de la opción institucional.

La demostración visual más útil es un flujo de datos o una incidencia con su respuesta. Debe mostrar cómo piensa qrt y qué entrega. Evitar que un gráfico de rentabilidad ficticio se interprete como evidencia de resultados.

### Texto de las tres entradas

**Instituciones** — Conecta investigación y operación con procesos trazables y responsabilidades claras.

**Brokers y plataformas** — Integra herramientas y proveedores con controles y pruebas definidos.

**Traders independientes** — Profesionaliza tus herramientas con una infraestructura que puedas mantener.

## 10. Evidencia y decisiones pendientes

Se leyeron los siete documentos de síntesis del [notebook de investigación](https://notebook.google.com/notebook/c8701907-dc93-4dd7-ac8d-92f8a84f658a). Se contrastaron afirmaciones competitivas clave con tres páginas oficiales. Esto no equivale a una auditoría completa de todas las fuentes externas.

La interfaz contiene 40 entradas: 37 utilizables y 3 con error. Siete entradas son los propios documentos de síntesis. El índice declara 48 fuentes, cifra que no se reproduce en el inventario disponible. La [nota de verificación](../investigacion/verificacion_notebook_trading_2026-09-24.md) documenta las diferencias.

Antes de presentar esta oferta como capacidad disponible, resolver:

- **Capacidad:** plataformas, proyectos y componentes que qrt puede demostrar hoy.
- **Cliente inicial:** problemas y compradores a los que ya tiene acceso.
- **Entrega:** responsables, disponibilidad, pruebas y cobertura real de soporte.
- **Economía:** costos, esfuerzo y disposición a pagar por un alcance concreto.
- **Prueba de marca:** caso o demostración que puede mostrarse con autorización.

El siguiente hito recomendado es definir una ficha de diagnóstico y un piloto en una tecnología dominada, probarlos en conversaciones comerciales y ajustar el alcance con evidencia. El sitio puede comunicar esta estructura cuando se confirme qué módulos están listos para contratar.
