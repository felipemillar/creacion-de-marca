# Manual de Identidad de Marca Digital: Logotipo qrt^

Este manual establece los lineamientos técnicos, estéticos y de usabilidad para la implementación del logotipo de **qrt^** (Quantitative Research & Trading). Como una marca de corte científico, técnico y minimalista, el logotipo debe tratarse con rigurosa precisión geométrica y respeto a sus reglas de legibilidad y adaptabilidad.

---

## 📐 1. Concepto y Filosofía Visual

El logotipo de **qrt^** representa la convergencia entre el rigor académico y la velocidad de ejecución.

*   **Minúsculas Obligatorias:** El acrónimo `q`, `r`, `t` se escribe exclusivamente en minúsculas. Esto elimina el "ego" corporativo tradicional, alineándose con la sobriedad editorial suiza y la notación de variables en la física y las matemáticas avanzadas.
*   **El Exponente (`^`):** Simboliza la elevación matemática al núcleo (core), denotando crecimiento exponencial y la trascendencia de los modelos cuantitativos.
*   **Versión Expandida:** En entornos interactivos de scrollytelling, el logotipo se despliega horizontalmente para revelar los pilares de la marca: `(quantitative research trading)^`.

---

## 🎨 2. Especificaciones de Color (Paleta Cromática)

El sistema visual es de alto contraste (monocromático) para optimizar el procesamiento cognitivo y transmitir rigor técnico y neutralidad.

| Aplicación | Nombre de Color | Formato HEX | Formato RGB | Formato HSL |
| :--- | :--- | :--- | :--- | :--- |
| **Fondo Principal Claro / Logo Positivo** | Negro Corporativo | `#0D0D0D` | `13, 13, 13` | `0, 0%, 5%` |
| **Fondo Principal Oscuro / Logo Negativo** | Blanco Puro | `#FFFFFF` | `255, 255, 255` | `0, 0%, 100%` |
| **Textos Secundarios e Indicadores** | Gris Técnico (Muted) | `#6E6E73` | `110, 110, 115` | `240, 1%, 44%` |
| **Resaltado y Enfoque de IA** | Cian Eléctrico | `#00B4D8` | `0, 180, 216` | `190, 100%, 42%` |

---

## 🔠 3. Tipografía de Marca

El logotipo está construido con la tipografía **Sora**, un tipo de letra geométrico sans-serif de Google Fonts con remates limpios e industriales.

*   **Tipografía del Logotipo (`q`, `r`, `t`):** `Sora`, peso **700 (Bold)**.
*   **Tipografía del Exponente (`^`):** `Sora`, peso **500 (Medium)**.
*   **Separación del Kerning Colapsado:** Cuando el logotipo está cerrado (`qrt^`), se debe aplicar una separación técnica al carácter `t` (`margin-left: 0.06em` en CSS o `dx: 2px` en SVG) para evitar colisiones visuales entre el trazo de la `r` y el trazo transversal de la `t`.

---

## 📏 4. Logometría y Área de Exclusión

Para garantizar el impacto visual y evitar interferencias con otros elementos de la interfaz, el logotipo debe mantener siempre un área de protección o zona de exclusión.

### Área de Protección (Clear Space)
La zona de protección mínima alrededor del logotipo se define a partir de la altura **X** (x-height) de la letra `q`. Ningún elemento gráfico, borde de pantalla o bloque de texto puede ingresar en este espacio protector.
```text
      +-------------------------------------------+
      |                 Área X                    |
      |          +---------------------+          |
      |   Área X |   q   r  t   ^      | Área X   |
      |          +---------------------+          |
      |                 Área X                    |
      +-------------------------------------------+
```

### Tamaños Mínimos en Interfaces Digitales
*   **Escritorio (Desktop):** Altura mínima de **24px** (aproximadamente `2.2rem` en el CSS de navegación).
*   **Móvil (Mobile):** Altura mínima de **18px** (aproximadamente `1.15rem` en cabecera colapsada).

---

## 🚫 5. Usos Correctos e Incorrectos

### Usos Correctos (Do's)
*   Utilizar la versión negra (`#0D0D0D`) sobre fondos claros.
*   Utilizar la versión blanca (`#FFFFFF`) sobre fondos oscuros o imágenes de baja densidad atenuadas.
*   Mantener las transiciones dinámicas fluidas (`0.8s cubic-bezier(0.16, 1, 0.3, 1)`) al expandir o contraer las letras colapsables.

### Usos Incorrectos (Don'ts)
*   **NO** alterar la relación de tamaño entre las letras principales y el exponente.
*   **NO** utilizar colores ajenos a la paleta monocromática oficial (por ejemplo, pintar el logotipo con el cian de acento).
*   **NO** aplicar sombras paralelas, contornos (strokes) de colores o texturas dentro de los caracteres del logo.
*   **NO** escribir el logotipo en mayúsculas (`QRT^` es inaceptable).

---

## 💾 6. Descarga y Código de Recursos SVG

Para la máxima fidelidad y velocidad en plataformas web, se proporcionan los siguientes archivos vectoriales optimizados en el espacio de trabajo:

### Versión Logo Positivo (Negro Corporativo)
Archivo: [logo_black.svg](../assets/logos/logo_black.svg)
```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 60" width="180" height="60" fill="none">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Sora:wght@500;700&amp;display=swap');
      .logo-text {
        font-family: 'Sora', sans-serif;
        font-weight: 700;
        font-size: 38px;
        fill: #0d0d0d;
        letter-spacing: -0.04em;
      }
      .logo-exponent {
        font-weight: 500;
        font-size: 32px;
      }
      .word-t {
        dx: 2px;
      }
    </style>
  </defs>
  <text x="10" y="44" class="logo-text">
    <tspan>q</tspan>
    <tspan>r</tspan>
    <tspan class="word-t">t</tspan>
    <tspan class="logo-exponent" dx="2">^</tspan>
  </text>
</svg>
```

### Versión Logo Negativo (Blanco Puro)
Archivo: [logo_white.svg](../assets/logos/logo_white.svg)
```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 60" width="180" height="60" fill="none">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Sora:wght@500;700&amp;display=swap');
      .logo-text {
        font-family: 'Sora', sans-serif;
        font-weight: 700;
        font-size: 38px;
        fill: #ffffff;
        letter-spacing: -0.04em;
      }
      .logo-exponent {
        font-weight: 500;
        font-size: 32px;
      }
      .word-t {
        dx: 2px;
      }
    </style>
  </defs>
  <text x="10" y="44" class="logo-text">
    <tspan>q</tspan>
    <tspan>r</tspan>
    <tspan class="word-t">t</tspan>
    <tspan class="logo-exponent" dx="2">^</tspan>
  </text>
</svg>
```

---

## ⚡ 7. Especificación Técnica de Implementación Web

La cabecera web utiliza un logotipo dinámico y flexible que reacciona al scroll. A continuación, se detalla el marcado semántico y estilos recomendados para su correcta integración:

### Marcado HTML5
```html
<a href="#" class="logo-container" id="logo">
  <span class="logo-parenthesis p-start">(</span>
  <span class="logo-word" id="word-q">
    <span class="logo-always">q</span><span class="logo-collapsible">uantitative</span>
  </span>
  <span class="logo-space"></span>
  <span class="logo-word" id="word-r">
    <span class="logo-always">r</span><span class="logo-collapsible">esearch</span>
  </span>
  <span class="logo-space"></span>
  <span class="logo-word" id="word-t">
    <span class="logo-always">t</span><span class="logo-collapsible">rading</span>
  </span>
  <span class="logo-parenthesis p-end">)</span>
  <span class="logo-always logo-exponent">^</span>
</a>
```

### Reglas CSS3 para Comportamiento Fluido
```css
/* Contenedor del Logo */
.logo-container {
  display: inline-flex;
  align-items: center;
  text-decoration: none;
  color: var(--text-main);
  font-weight: 500;
  font-size: 3.6rem;
  letter-spacing: -0.04em;
  transition: color 0.6s cubic-bezier(0.16, 1, 0.3, 1),
              font-size 0.6s cubic-bezier(0.16, 1, 0.3, 1) 0.8s;
}

header.scrolled .logo-container {
  font-size: 2.2rem;
  transition: color 0.6s cubic-bezier(0.16, 1, 0.3, 1),
              font-size 0.6s cubic-bezier(0.16, 1, 0.3, 1) 0s;
}

/* Palabras Colapsables ( quantitative, research, trading ) */
.logo-collapsible {
  display: inline-block;
  max-width: 0;
  opacity: 0;
  overflow: hidden;
  white-space: nowrap;
  font-weight: 700;
  transform: scaleX(0);
  transform-origin: left center;
  transition: max-width 0.8s cubic-bezier(0.16, 1, 0.3, 1),
              opacity 0.6s ease,
              transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}

header.scrolled .logo-collapsible {
  max-width: 400px;
  opacity: 1;
  transform: scaleX(1);
}

/* Espacio entre Palabras */
.logo-space {
  display: inline-block;
  width: 0;
  transition: all 0.8s cubic-bezier(0.16, 1, 0.3, 1);
}

header.scrolled .logo-space {
  width: 8px;
}
```
