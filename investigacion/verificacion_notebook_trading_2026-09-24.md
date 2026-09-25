# Verificación del notebook de infraestructura de trading

Fecha: 24 de septiembre de 2026. Propósito: convertir la investigación en una propuesta de producto para qrt.

## Alcance observado

- Notebook: **qrt Investigación del modelo de negocio de infraestructura de trading**.
- [Enlace permanente](https://notebook.google.com/notebook/c8701907-dc93-4dd7-ac8d-92f8a84f658a).
- ID: `c8701907-dc93-4dd7-ac8d-92f8a84f658a`.
- Cuenta activa y propietario verificados visualmente: `felipemillarsilva@gmail.com`.
- 40 entradas de fuentes; 37 disponibles para consulta; 3 con error.
- Entre las 37 disponibles, 7 son documentos derivados y 30 son entradas externas. No se ha verificado la independencia o calidad de todas esas entradas.
- Se leyeron directamente los documentos 1–7: índice, pilares, competencia, arquitectura, productos, economía y recomendación.
- Visibilidad pública y opción de copias activada ya existentes al revisar. Sin cambios de permisos ni publicación por parte de esta ejecución. Acceso anónimo no comprobado.
- Se formuló una consulta de auditoría en el chat del notebook. No se crearon notas, fuentes ni entregables de Studio.

Entradas con error: CloudLogic Financial Data Platforms Guide 2026; SEC Rule 15c3-5 Market Access Rule; Tradovate API Access and Terms. Existe otra entrada sobre la FAQ de la SEC; no confundirla con una recuperación del documento fallido.

## Qué conservar y qué corregir

| Afirmación de la síntesis | Evaluación | Uso en el producto |
|---|---|---|
| Oferta por diagnóstico, implementación y soporte | Arquitectura comercial razonable; recomendación de diseño, no validación de mercado. | Adoptarla como hipótesis de oferta. |
| Brokers como prioridad por ciclos de 1–4 meses | No acreditado con evidencia comercial de qrt. Tiempo de despliegue no equivale a ciclo de venta. | Priorizar según acceso, capacidades y oportunidades reales. |
| Diagnóstico USD 15.000 y soporte USD 4.000–7.500 | Supuestos; no equivalen a disposición a pagar probada. | Estimar esfuerzo y contrastar propuestas antes de fijar tarifas. |
| Márgenes de 53–60% | Escenarios construidos con costos y capacidad no validados. | No presentarlos como rentabilidad esperable o garantizada. |
| Devexperts cerrado al 100% | Contradicho por su página oficial, que incluye entrega de código fuente. | Eliminar esa comparación absoluta. |
| Independencia de plataforma como exclusividad | LEAN permite infraestructura propia. | Diferenciar por entrega, adaptación y transferencia demostrables. |
| Propiedad absoluta del código | La propia síntesis distingue IP previa licenciada y desarrollos cedidos. | Definir derechos por componente. |
| Conectividad regional, equipo de 3 FTE y 60–70% reutilizable | El notebook los presupone; falta inventario verificable de qrt. | Mantenerlos como preguntas internas. |
| SLA de respuesta de 15 minutos y arquitectura universal | No derivados de capacidad operativa acreditada. | Definir por proyecto y cobertura contratada. |
| Cumplimiento normativo automático o garantías de rendimiento | El listado de normas y tecnologías no acredita cumplimiento ni resultados. | No trasladar esas promesas al sitio; evaluar alcance específico. |

El Documento 1 enumera 48 referencias sin reproducir un registro completo con evidencia por afirmación. La interfaz disponible muestra 33 entradas externas, de las cuales tres fallan. No se concluye que las referencias restantes sean inexistentes; sí que su incorporación y evaluación no quedan verificadas aquí.

La respuesta automática a la consulta de auditoría reconoció varias hipótesis, pero también citó el Documento 3 como si fuera evidencia externa de precios y mantuvo la caracterización incorrecta de Devexperts. Se trató como ayuda analítica, no como confirmación independiente.

## Contrastes externos directos

1. [Devexperts — Equities & Derivatives Trading Platform](https://devexperts.com/solutions-for-equity-brokerages/): oferta para brokers, módulos e integraciones; modalidades de entrega que incluyen código fuente. No acredita los precios atribuidos por el notebook.
2. [QuantConnect — Integration Partners](https://www.quantconnect.com/docs/v2/cloud-platform/community/integration-partners): consultores independientes, desarrollo, enseñanza y asesoría; cada proveedor define servicios y precios. No acredita que qrt sea partner.
3. [QuantConnect — Algorithm Engine](https://www.quantconnect.com/docs/v2/writing-algorithms/key-concepts/algorithm-engine): LEAN abierto, ejecutable con infraestructura, datos y conexiones propias. No elimina costos de operación o de terceros.

No se validaron tarifas de todos los competidores, benchmarks, aplicabilidad jurídica ni proyecciones financieras. No reutilizar esas partes de la investigación como hechos comerciales.

## Resultado

[Propuesta de producto v0.1](../caso_estudio_qrt/qrt_producto_infraestructura_trading_v01.md): posicionamiento, segmentos, etapas, módulos, piloto, modelo comercial y sección web. No se modificó el sitio de producción.
