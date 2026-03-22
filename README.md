# Matematicas-2026


## Conversión de cursos cero en html a quarto

1. Convertimos a markdown con 
    ```bash
    pandoc -s --mathjax --wrap=preserve -t markdown 00-conjuntos.html -o conjuntos.md
    ```

2. Eliminamos la cabecera `::: {#header}` (con el consiguiente `:::`). Cambiamos las cabeceras `#` por secciones `##`.

3. Reemplazamos `\[\\\\\((.*?)\\\\\)\]\{.math .inline\}` (con regex) por `$$$1$$`. Comprobamos si se ha quedado algún `.math` por algún salto de línea. 

4. Cambiamos, sin regex, `\\` por `\`.

5. Buscamos las fórmulas centradas `\\\\\[(.*?)\\\\\]` (con regex) y las reemplazamos por `$$$$$1$$$$`.

6. Por si las moscas, `\[(.*?)\]\{.math .inline\}` (con regex) por `$$$1$$`.

7. Quitamos los .display `\[(.*?)\]\{.math .display\}` (con regex) por `$1`.

7. Cambiar `(\` y `\)` por `$`, sin regex.

8. Cambiar `\_` y `\^` por `_` y `^`, sin regex, respectivamente. Lo mismo con `\'`.

8. Revisar espacios entre dólares y texto. Por ejemplo, `$ 5$` por `$5$`, o `$5 $` por `$5$`.

8. Comprobamos si las imágenes están bien, y si no, las reemplazamos por las originales.

9. Hacemos lo mismo con los elementos jsxgraph o similares.

9.  Cambiar cabecera por 

    ```yaml
    ---
    title: Título
    title-block-banner: true
    lang: es
    format: 
      html: 
        include-in-header: includes-header.html
        theme: [night, custom.scss]
        fontsize: 1.2em
        toc: true
        page-layout: full
        format-links: true
        html-math-method:
                method: mathjax
                url: "https://cdn.jsdelivr.net/npm/mathjax@4/tex-svg.js"
    ---
    ```

10. Poner las librerías necesarias en `includes-header.html` (si es necesario).

11. Convertir los ejercicios a `::: {#exr-n} ... :::`.

12. Para usar botones que muestren la solución, como alternativa a `::: {#etiqueta .callout .collapse}`, insertamos en el sitio en el que queramos que aparezca el botón `<button id="e1-1" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>`, donde "e1-1" es un identificador, que debe de ser distinto para cada botón. Después la solución irá en un entorno 

    ```
    ::: {#solucion-e1-1 .callout .collapse}

    Texto de la solución.

    :::
    ```
    La etiqueta de este entorno siempre es de la forma `#solucion-identificador_del_boton`. En este ejemplo, como el identificador del botón es `e1-1`, la etiqueta es `#solucion-e1-1`.

