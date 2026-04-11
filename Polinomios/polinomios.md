---
title: Polinomios
title-block-banner: true
lang: es
format: 
  html: 
    # include-in-header: includes-header.html
    theme: [night, custom.scss]
    fontsize: 1.2em
    toc: true
    page-layout: full
    format-links: true
    html-math-method:
            method: mathjax
            url: "https://cdn.jsdelivr.net/npm/mathjax@4/tex-svg.js"
---

## Monomios y polinomios

En Álgebra se utilizan expresiones en las que se combinan números con símbolos que representan elementos no determinados a los que llamamos según las situaciones *incógnitas* (en el contexto de ecuaciones), *variables* en el contexto de funciones, o en el caso de polinomios *indeterminadas*. Los *polinomios* son un tipo de expresiones algebraicas donde se combinan las indeterminadas con números, a los que llamamos también *coeficientes*, usando solo las operaciones suma y producto. La indeterminada (a veces son varias, pero trataremos aquí solo el caso de polinomios en una indeterminada) suele nombrarse por la letra $x$ (aunque también es bastante usual la $t$) y no puede operarse con los coeficientes, así que la expresión $1+x$ no puede simplificarse; sin embargo, algunas operaciones en las que aparece la indeterminada admiten una escritura resumida:

$$x+x+x=3x; \,\, x\cdot 2x = 2x^2; \,\, 3x^4-5x^4=-2x^4.$$

así, podemos escribir potencias (enteras positivas) de la indeterminada y aparecen lo que se llaman *monomios*, que son términos de la forma $ax^m$ donde $a$ representa un coeficiente y el exponente $m$ se llama el *grado* del monomio. Un polinomio, que es una suma finita de monomios, se escribe agrupando todos los monomios del mismo grado hasta tener una expresión de la forma

$$a_0+a_1x+a_2x^2+ \dots +a_nx^n=\sum_{i=0}^n a_i x^i,$$

con $a_0, \dots ,a_n$ números; el mayor índice $n$ para el que $a_n\not = 0$ se llama el *grado del polinomio* y el correspondiente coeficiente, $a_n$ es el *coeficiente líder*. Los números distintos de cero pueden considerarse polinomios de grado $0$, y se suele decir que el grado del polinomio $0$ es $- \infty$.

- $2-x-x^3$ es un polinomio de grado 3, todos sus coeficientes son números enteros, su coeficiente líder es $-1$.

- $-\dfrac{1}{3}+\dfrac{2}{7}x+2x^2$ es un polinomio de grado 2 con coeficiente líder $2$ y sus coeficientes son números racionales.

- $x+\sqrt{2}x^3-\pi x^6$ es un polinomio de grado 6 con coeficiente líder $-\pi$ y sus coeficientes son números reales.

Se suelen escribir los polinomios ordenando los monomios por el grado, bien en sentido ascendente como en $-\dfrac{1}{3}+\dfrac{2}{7}x+2x^2$ o bien en sentido descendente como en $-10 x^4 - 3 x^2 + 2 x - 2$.

## Suma y resta de polinomios

Para sumar polinomios debemos sumar los coeficientes asociados a una misma potencia de $x$ tal como se muestra en el ejemplo siguiente:

$$
\begin{align*}
(-10 x^4 - 3 x^2 + 2 x - 2) + (x^3 + x^2 + x + 1) & = (-10 + 0) x^4 + (0 + 1) x^3 + (-3 + 1) x^2 + (2 + 1) x + (-2 + 1) \\
&= -10 x^4 + x^3 -2 x^2 + 3 x - 1.
\end{align*}
$$


::: {#exr-1}
Realiza las siguientes sumas.

1.  $(2 + 3 x - \dfrac{2}{5} x^3 - 11 x^4) + (\dfrac{3}{4} - \dfrac{2}{3} x + x^2 + 13 x^4)$
    [
    $= 2x^4 - \dfrac{2 x^3}5 + x^2 + \dfrac{7 x}3 + \dfrac{11}4$
    ]{#solucion-e1-1 .collapse}.
    <button id="e1-1" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>

2.  $(-3 x + 3 x^3 + 3 x^4) + (5 + 3 x - 2 x^2 + 4 x^3 - 3 x^4)$
    [
    $= 7 x^3 - 2 x^2 + 5$
    ]{#solucion-e1-2 .collapse}.
    <button id="e1-2" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>

:::

## Multiplicación de polinomios

La multiplicación de polinomios se basa en la consideración de la variable como un "número indeterminado", por lo que está sujeta a las reglas aritméticas numéricas. La regla que se emplea es la del producto de potencias de igual base, es decir, $x^i x^j = x^{i+j}$. De esta forma la multiplicación se realiza usando la propiedad distributiva y el producto de cada monomio. Veamos un ejemplo que puede ser suficientemente significativo.

Multipliquemos $3x^3 + 5x^2 - 3x + 1$ por $x^4 + 7 x - 2$, lo que hacemos multiplicando el primero por cada uno de los términos del segundo, así

$$
\begin{split}
-2(3x^3 + 5x^2 - 3x + 1) &= -6 x^3 - 10 x^2 + 6 x - 2,\\
7x (3x^3 + 5x^2 - 3x + 1) &= 21 x^4 + 35 x^3 - 21 x^2 + 7 x, \\
x^4 (3x^3 + 5x^2 - 3x + 1) &= 3x^7 + 5 x^6 - 3 x^5 + x^4,
\end{split}
$$


y sumando los resultados parciales obtenemos el resultado,

$$
\begin{align*}
(3x^3 + 5x^2 - 3x + 1) (x^4 + 7 x - 2) & = (3x^7 + 5 x^6 - 3 x^5 + x^4) + (21 x^4 + 35 x^3 - 21 x^2 + 7 x) + (-6 x^3 - 10 x^2 + 6 x - 2) \\
 & = 3x^7 + 5 x^6 - 3 x^5 + 22 x^4 + 29 x^3 -31 x^2 + 13 x -2.
\end{align*}
$$

Podemos describir la multiplicación mediante el siguiente diagrama:

$$
\begin{array}{rrrrrrrr}
& & & & 3x^3 & + 5x^2 & - 3x & + 1 \\
\times & & & & & x^4 & + 7 x & - 2 \\
\hline
& & & & -6 x^3 & - 10 x^2 & + 6 x & - 2 \\
& & & 21 x^4 & + 35 x^3 & - 21 x^2 & + 7 x & \\
3x^7 & + 5 x^6 & - 3 x^5 & + x^4 & & & & \\
\hline
3x^7 & + 5 x^6 & - 3 x^5 & + 22 x^4 & + 29 x^3 & -31 x^2 & + 13 x & -2
\end{array}
$$

::: {#exr-2}
Realiza las siguientes multiplicaciones.

1.  $\left(x^5 - \dfrac{1}{5}x^4 - 2 x^3 + 4 x - \dfrac{2}{3}\right) \times \left(\dfrac{3}{5} x^2 - 2 x + \dfrac{1}{2}\right)$
    [
    $= \dfrac{3 x^7}5 - \dfrac{53 x^6}{25} - \dfrac{3 x^5}{10} + \dfrac{39 x^4}{10} + \dfrac{7 x^3}5 - \dfrac{42 x^2}5 + \dfrac{10 x}3 - \frac{1}3$
    ]{#solucion-e2-1 .collapse}. 
    <button id="e2-1" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>

2.  $(-3 x^4 - 2 x^3 - 4 x^2 - 2 x - 7) \times (-2 x^4 - 3 x^2 - 4 x - 5)$
    [
    $= 6 x^8 + 4 x^7 + 17 x^6 + 22 x^5 + 49 x^4 + 32 x^3 + 49 x^2 + 38 x + 35$
    ]{#solucion-e2-2 .collapse}.
    <button id="e2-2" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>
:::

## División de polinomios {#división-de-polinomios.}

La división de polinomios con coeficientes racionales (o reales) se basa en el siguiente resultado.

::: {.callout-note title="Propiedad" icon=false}
Dados polinomios $f,g$ con $g \neq 0$ existen polinomios $q$ y $r$ tales que $f = qg + r$ y $\operatorname{grado}(r) < \operatorname{grado}(g)$.
:::

La división es un proceso iterativo. Supongamos que el término líder de $f$ es $a_n x^n$, el término líder de $g$ es $b_m x^m$ y $n \geq m$. Entonces el término líder de $\frac{a_n}{b_m} x^{n-m} g$ es también $a_n x^n$, luego el grado de $f_1 = f -\frac{a_n}{b_m} x^{n-m} g$ es menor que $n$. De esta forma tenemos que $\frac{a_n}{b_m} x^{n-m}$ es parte del cociente, para completar el cociente y conocer el resto debemos dividir $f_1$ entre $g$. Veámoslo en un ejemplo.

Vamos a dividir $f=3x^4 + 3 x^2 - \dfrac{2}{3} x + 1$ entre $g=2x^2 + x$. Debemos multiplicar el divisor por [$\frac{3}{2} x^2$]{style="color:cornflowerblue"} para igualar el término líder de $f$, con lo cual debemos calcular $f - \frac{3}{2} x^2 (2x^2 + x)= -\frac{3}{2} x^3 + 3 x^2 - \frac{2}{3} x + 1$. Gráficamente,

<style>
td{
    white-space: nowrap;
    padding: 0px;
    width: 3em;

}
table {
    border: 0px;
}
</style>
<table>
<tbody>
<tr><td style="text-align:right; color: darkred;">$3x^4$</td><td></td><td style="text-align: right; color:darkgoldenrod;"> <span>$+ 3 x^2$</td><td style="text-align: right; color: coral;"><span>$− \frac{2}3 x$</td><td style="text-align: right; color: chocolate;">$+ 1$</td><td></td><td style="font-size: large; text-align: left; border-bottom-style: solid; border-bottom-width:3px; border-left-style: solid; border-left-width:3px;">$\ 2x^2+x$</td></tr>

<tr><td style="text-align: right; color: cornflowerblue; border-bottom-style: solid;  border-bottom-width: 1px;">$-3 x^4$</td><td style="text-align: right; color: cornflowerblue; border-bottom-style: solid; border-bottom-width: 1px;">$-\frac{3}2 x^3$</td> <td></td><td></td><td></td><td></td><td><span style="color:cornflowerblue">$\frac{3}2 x^2$</span><span style="color:yellowgreen"> $-\frac{3}4x$</span><span style="color:slateblue">$+\frac{15}{8}$</span></td></tr>

<tr><td></td><td style="text-align: right; color: darkorange;">$−\frac{3}2 x^3$</td>
</tbody>
</table>

Con este nuevo dividendo necesitamos multiplicar el divisor por [$-\frac{3}{4}x$]{style="color:yellowgreen"} con el fin de igualar el término líder. De forma análoga al anterior tenemos que el nuevo dividendo es $\frac{15}{4}x^2-\frac{2}{3}x + 1$, o gráficamente

<table>
<tbody>
    <tr><td style="text-align:right; color: darkred;">$3x^4$</td><td></td><td style="text-align: right; color:darkgoldenrod;"> <span>$+ 3 x^2$</td><td style="text-align: right; color: coral;"><span>$− \frac{2}3 x$</td><td style="text-align: right; color: chocolate;">$+ 1$</td><td></td><td style="font-size: large; text-align: left; border-bottom-style: solid; border-bottom-width:3px; border-left-style: solid; border-left-width:3px;">$\ 2x^2+x$</td></tr>

    <tr><td style="text-align: right; color: cornflowerblue; border-bottom-style: solid;  border-bottom-width: 1px;">$-3 x^4$</td><td style="text-align: right; color: cornflowerblue; border-bottom-style: solid; border-bottom-width: 1px;">$-\frac{3}2 x^3$</td> <td></td><td></td><td></td><td></td><td><span style="color:cornflowerblue">$\frac{3}2 x^2$</span><span style="color:yellowgreen"> $-\frac{3}4x$</span><span style="color:slateblue">$+\frac{15}{8}$</span></td></tr>

    <tr><td></td><td style="text-align: right; color: darkorange;">$−\frac{3}2 x^3$</td><td style="text-align: right; color: darkgoldenrod;"></td><td style="text-align: right; color: coral;"></td><td style="text-align: right; color: chocolate;"></td></tr>

    <tr><td></td><td style="text-align: right; color: yellowgreen; border-bottom-style: solid; border-bottom-width: 1px;">$\frac{3}2 x^3$</td><td style="text-align: right; color: yellowgreen; border-bottom-style: solid; border-bottom-width: 1px;">$+\frac{3}{4}x^2$</td></tr><tr><td style="height: 0.8em;"></td></tr>

    <tr><td></td><td></td><td style="text-align: right; color: darkgoldenrod;">$\frac{15}4 x^2$</td></tr>
    </tbody>
</table>

Finalmente necesitamos multiplicar el divisor $g$ por [$\frac{15}{8}$]{.math style="color:slateblue;"} para igualar los términos líderes, lo que nos lleva a completar el cociente y a llegar al resto:

<table>
<tbody>
    <tr><td style="text-align:right; color: darkred;">$3x^4$</td><td></td><td style="text-align: right; color:darkgoldenrod;"> <span>$+ 3 x^2$</td><td style="text-align: right; color: coral;"><span>$− \frac{2}3 x$</td><td style="text-align: right; color: chocolate;">$+ 1$</td><td></td><td style="font-size: large; text-align: left; border-bottom-style: solid; border-bottom-width:3px; border-left-style: solid; border-left-width:3px;">$\ 2x^2+x$</td></tr>

    <tr><td style="text-align: right; color: cornflowerblue; border-bottom-style: solid;  border-bottom-width: 1px;">$-3 x^4$</td><td style="text-align: right; color: cornflowerblue; border-bottom-style: solid; border-bottom-width: 1px;">$-\frac{3}2 x^3$</td> <td></td><td></td><td></td><td></td><td><span style="color:cornflowerblue">$\frac{3}2 x^2$</span><span style="color:yellowgreen"> $-\frac{3}4x$</span><span style="color:slateblue">$+\frac{15}{8}$</span></td></tr>

    <tr><td></td><td style="text-align: right; color: darkorange;">$−\frac{3}2 x^3$</td><td style="text-align: right; color: darkgoldenrod;"></td><td style="text-align: right; color: coral;"></td><td style="text-align: right; color: chocolate;"></td></tr>

    <tr><td></td><td style="text-align: right; color: yellowgreen; border-bottom-style: solid; border-bottom-width: 1px;">$\frac{3}2 x^3$</td><td style="text-align: right; color: yellowgreen; border-bottom-style: solid; border-bottom-width: 1px;">$+\frac{3}{4}x^2$</td></tr><tr><td style="height: 0.8em;"></td></tr>

    <tr><td></td><td></td><td style="text-align: right; color: darkgoldenrod;">$\frac{15}4 x^2$</td></tr>

    <tr><td></td><td></td><td style="text-align: right; color: slateblue; border-bottom-style: solid; border-bottom-width: 1px;">$-\frac{15}4x^2$</td><td style="text-align: right; color: slateblue; border-bottom-style: solid; border-bottom-width: 1px;">$-\frac{15}8 x$</td></tr>

    <tr><td></td><td></td><td></td><td style="text-align: right; color: coral;"><span>$− \frac{61}{24}x$</td><td style="text-align: right; color: chocolate;">$+ 1$</td><td></td><td colspan="10" style="font-weight: bold; color: red;">←&nbsp;Resto</td></tr>
    </tbody>
</table>


Es decir, el cociente es $\frac{3}{2}x^2 - \frac{3}{4}x + \frac{15}{8}$ y el resto es $-\frac{61}{24}x + 1$:

$$
3x^4+3x^2 -\frac{2}3x+1=(2x^2+x)\left(\frac{3}2x^2-\frac{3}4 x+\frac{15}8\right)-\frac{61}{24}x+1
$$

A continuación mostramos otro ejemplo:

<table>
<tbody>
<tr><td style="text-align: right;" >$5x^4$</td><td style="text-align: right;">$-4x^3$</td><td></td><td  style="text-align: right;">$-x$</td><td  style="text-align:right;">$+2$</td><td></td><td style="font-size:large;text-align:left; border-bottom-style:solid;border-bottom-width:2px;border-left-style: solid; border-left-width:2px;padding:3px;width:9em">$4x^3+2x^2-x-4$ </td></tr>

<tr><td style="text-align: right; border-bottom-style: solid; border-bottom-width:1px;">$-5x^4$</td><td style="text-align: right;border-bottom-style: solid; border-bottom-width:1px;">$-\frac{5}2 x^3$</td><td style="text-align: right;border-bottom-style: solid; border-bottom-width:1px;">$+\frac{5}4x^2$</td><td style="text-align: right;border-bottom-style: solid; border-bottom-width:1px;">$+5x$</td><td></td><td></td><td>$\frac{5}4 x-\frac{13}8$</td>
</tr>

<tr>
<td></td><td style="text-align: right;">$-\frac{13}2 x^3$<td style="text-align: right;">$+\frac{5}4 x^2$</td><td style="text-align: right;">$+4x$</td><td style="text-align: right;">$+2$</td>
</tr>

<tr>
<td></td><td style="text-align: right; border-bottom-style: solid; border-bottom-width:1px;">$\frac{13}2 x^3$<td style="text-align: right;border-bottom-style: solid; border-bottom-width:1px;">$+\frac{13}4 x^2$</td><td style="text-align: right;border-bottom-style: solid; border-bottom-width:1px;">$-\frac{13}8 x$</td><td style="text-align: right;border-bottom-style: solid; border-bottom-width:1px;">$-\frac{13}2$</td>
</tr>

<tr>
<td></td><td></td><td style="text-align: right;">$2 x^2$<td style="text-align: right;">$+\frac{19}8 x$</td><td style="text-align: right;">$-\frac{9}2$</td>
</tr>
</tbody>
</table>


Puedes hacer más ejemplos en [esta página](http://weitz.de/poly/).


## División de polinomios: Método de Ruffini

Este método es especial para dividir un polinomio $a_0 + a_1 x + \dots a_n x^n$ entre un binomio de la forma $x-r$. En este caso el cociente tendrá grado $n-1$ y el resto grado $0$ o $-\infty$, es decir,

$$a_0 + a_1 x + \dots + a_n x^n = (b_0 + b_1 x + \dots + b_{n-1} x^{n-1}) (x-r) + s.$$

Para realizar la división debemos calcular $s, b_0, b_1, \dots, b_{n-1}$. Para calcularlos vamos a desarrollar la multiplicación:

$$\begin{split}
a_0 + a_1 x + \dots + a_n x^n &= (b_0 + b_1 x + \dots + b_{n-1} x^{n-1}) (x-r) + s \\
&= b_0 x + b_1 x^2 + \dots + b_{n-1} x^n - r b_0 - r b_1 x - \dots - r b_{n-1} x^{n-1} + s \\
&= (s - r b_0) + (b_0 - r b_1) x + \dots + (b_{n-2} - r b_{n-1}) x^{n-1} + b_{n-1} x^n.
\end{split}$$

Esto nos da una regla recursiva:

$$\begin{aligned}
b_{n-1} &= a_n \\
b_{n-2} &= a_{n-1} + r b_{n-1} \\
b_{n-3} &= a_{n-2} + r b_{n-2} \\
&\quad \vdots \\
b_1 &= a_2 + r b_2 \\
b_0 &= a_1 + r b_1 \\
s &= a_0 + r b_0.\end{aligned}$$

Este método se recuerda mejor mediante una disposición gráfica que vamos a explicar con un ejemplo

Vamos a dividir $2x^4 - \frac{1}{3} x^3 + \frac{3}{2}x^2 - 1$ entre $x-\frac{2}{3}$. Para ello escribimos los coeficientes según el siguiente gráfico:

![](img-pols/img-1.svg){width="600px" fig-alt="Ruffini"}

El coeficiente líder del cociente coincide con el coeficiente líder del dividendo:

![](img-pols/img-2.svg){width="600px" fig-alt="Ruffini"}

Multiplicamos $2$ por $\frac{2}{3}$

![](img-pols/img-3.svg){width="600px" fig-alt="Ruffini"}

y lo sumamos a $-\frac{1}{3}$

![](img-pols/img-4.svg){width="600px" fig-alt="Ruffini"}

Repetimos el proceso hasta calcular todos los coeficientes del cociente,

![](img-pols/img-5.svg){width="600px" fig-alt="Ruffini"}

Finalmente calculamos el resto con el mismo procedimiento,

![](img-pols/img-6.svg){width="600px" fig-alt="Ruffini"}

Por tanto el cociente es $2x^3 + x^2 + \frac{13}{6}x + \frac{13}{9}$ y el resto $-\frac{1}{27}$.

Algunos ejemplos más.

1.  $-\frac{1}{2}x^3 + \frac{5}{3} x^2 + \frac{3}{7}x + \frac{3}{4}$ entre $x+2$

    ![](img-pols/img-7.svg){width="600px" fig-alt="Ruffini"}

2.  $x^5 - 3x^4 + 2 x^2 - 3 x - 9$ entre $x-3$

    ![](img-pols/img-8.svg){width="300px" fig-alt="Ruffini"}

3.  $x^4 - 4 x^2 +4$ entre $x+1$

    ![](img-pols/img-9.svg){width="300px" fig-alt="Ruffini"}

::: {#exr-3}
Calcula cociente y resto obtenidos al dividir


-   $2x^3 + 5 x^2 - 3 x + 2$ entre $x-2$
    [. El cociente es $2x^2+9x+15$ y el resto $32$]{#solucion-e3-1 .collapse}.
    <button id="e3-1" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>

-   $x^5 + \dfrac{1}{2} x^3 - \dfrac{2}{5} x + \dfrac{4}{3}$ entre $x + \frac{2}{5}$
    [. El cociente es $x^4-\dfrac{2}5 x^3+\dfrac{33}{50} x^2-\dfrac{33}{125}x-\dfrac{184}{625}$ y el resto $\dfrac{11396}{9375}$]{#solucion-e3-2 .collapse}.
    <button id="e3-2" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>

-   $\dfrac{4}{5} x^3 - \dfrac{4}{7} x^2 - 3 x - 2$ entre $x-1$
    [
    . El cociente es $\dfrac{4}5x^2+\dfrac{8}{35}x-\dfrac{97}{35}$ y el resto $-\dfrac{167}{35}$
    ]{#solucion-e3-3 .collapse}.
    <button id="e3-3" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>
:::

## Raíces de un polinomio y factorización

Dado un polinomio $p(x)=a_0+a_1x+a_2x^2+ \dots +a_nx^n$, una *raíz* es un número $\alpha$ tal que al evaluar el polinomio en $\alpha$ (sustituir la indeterminada por dicho valor) el resultado es $0$, es decir, $p(\alpha)=0$.

El siguiente resultado es una aplicación del algoritmo de la división de polinomios, en efecto, la división de $p(x)$ entre $x-\alpha$ nos proporciona la fórmula $$p(x)=q(x)\cdot (x-\alpha) + r$$ donde $r$ es un polinomio de grado menor que 1, es decir, es un número.

Para un polinomio $p(x)$ son equivalentes las siguientes afirmaciones:

1.  $\alpha$ es una raíz de $p$,

2.  $\alpha$ es una solución de la ecuación $p(x)=0$,

3.  $p(x)=q(x)(x-\alpha)$.

A los divisores de la forma $x-\alpha$ de un polinomio se les denomina *factores lineales*. Es de gran utilidad obtener la descomposición en factores lineales de un polinomio, o lo que es lo mismo obtener todas las soluciones de una ecuación polinómica. La resolución de algunos tipos de estas ecuaciones es tratado en el apartado "Ecuaciones polinómicas" de la siguiente sesión, sin embargo, es interesante el siguiente método para calcular las posibles raíces enteras de un polinomio con coeficientes también enteros.

Supongamos que tenemos un polinomio de grado $n$ con coeficientes enteros, digamos

$$a_nx^n +\dots +a_1x+a_0$$

si tuviese una raíz entera, $\alpha$, entonces el polinomio sería exactamente el producto de otro polinomio de grado $n-1$, también con coeficientes enteros, y el factor lineal correspondiente, es decir:

$$a_nx^n +\dots +a_1x+a_0=(x-\alpha)\cdot(a_nx^{n-1}+\dots +b_1x+b_0)$$

El hecho de que los coeficientes del cociente son enteros puede deducirse comprobando que en el método de Ruffini todas las operaciones son sumas y productos de números enteros. Ahora observamos que los términos de grado 0 en ambos miembros de la igualdad deben ser iguales

$$a_0=\alpha \cdot b_0$$

y así la raíz $\alpha$ es un divisor del término independiente, y como un número entero distinto de cero tiene una cantidad finita de divisores, puede explorarse el conjunto completo de divisores en busca de las posibles raíces.

Para encontrar todas las raíces enteras del polinomio $$x^4-7x^2+7x-2$$ observamos que como el término independiente es $-2$, sus posibles divisores son $1,-1,2,-2$ así que probamos si alguno de ellos es raíz. Esto puede hacerse realizando la división por Ruffini o simplemente evaluando el polinomio (es más eficiente Ruffini para evaluar)

$$\begin{array}{l}
p(1)=1^4-7\cdot 1^2+7\cdot 1-2=-1\\
p(-1)=(-1)^4-7\cdot (-1)^2+7\cdot (-1) -2=1-7-7-2=-15\\
p(2)=2^4-7\cdot 2^2+7\cdot 2-2= 16-28+14-2=0\\
p(-2)=(-2)^4-7\cdot (-2)^2+7\cdot (-2)-2= 16-28-14-2=-28\\
\end{array}$$ 

Así que $2$ es raíz del polinomio, para factorizar dividimos por $x-2$:

![](img-pols/img-10.svg){width="300px" fig-alt="Ruffini"}

El cociente es $x^3+2x^2-3x+1$, que solo podría tener como raíces enteras a $1$ y $-1$, y ya hemos comprobado que no lo son del polinomio dado, y por tanto tampoco del cociente.

Dado un polinomio con coeficientes racionales sus raíces son las mismas que las de un polinomio con coeficientes enteros que se obtiene al multiplicar el original por el mínimo comúm múltiplo de todos los denominadores que aparezcan en los coeficientes. Por ejemplo, el polinomio $ x^3+\frac{1}{6}x^2+ \frac{1}{5}x-1$ tiene las mismas raíces que $30x^3+5x^2+6x-30$, así que si tuviese raíces enteras estarían entre los divisores de $30$.

::: {#exr-4}
Factoriza, cuando sea posible, los siguientes polinomios:

1.  $x^3+6x^2+9x$
    [
    $= (x + 3)^2 x$
    ]{#solucion-e4-1 .collapse}.
    <button id="e4-1" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>

2.  $x^4-2x^2+1$
    [
    $= (x + 1)^2 (x - 1)^2$
    ]{#solucion-e4-2 .collapse}.
    <button id="e4-2" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>

3.  $x^3+3x^2-4x-12$
    [
    $= (x + 3)(x + 2)(x - 2)$
    ]{#solucion-e4-3 .collapse}.
    <button id="e4-3" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>

4.  $x^5+20x^3 +100x$
    [
    $= (x^2 + 10)^2 x$
    ]{#solucion-e4-4 .collapse}.
    <button id="e4-4" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>

5.  $2x^5-32x$
    [
    $= 2(x^2 + 4)(x + 2)(x - 2)x$
    ]{#solucion-e4-5 .collapse}.
    <button id="e4-5" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>

6.  $\dfrac{2}{5}x^5- \dfrac{6}{5}x^4+\dfrac{14}{15}x^2$
    [
    $= \dfrac{2}{15}(3 x^3 - 9 x^2 + 7) x^2$
    ]{#solucion-e4-6 .collapse}.
    <button id="e4-6" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>
:::


------------------------------------------------------------------------

[Esta página está basada en las transparencias de Javier Lobillo y Evangelina Santos Aláez para el Curso Cero de la ETSIIT de la Universidad de Granada. Maquetado y javascript por Pedro A. García Sánchez.]{.small}
