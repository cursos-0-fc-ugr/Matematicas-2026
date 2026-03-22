---
title: Fracciones y potencias
title-block-banner: true
lang: es
format: 
  html: 
    include-in-header: includes-header.html
    toc: true
    fontsize: 1.2em
    page-layout: full
    format-links: true
    html-math-method:
            method: mathjax
            url: "https://cdn.jsdelivr.net/npm/mathjax@4/tex-svg.js"
---

## Fracciones


Una fracción es el cociente entre dos números enteros: $\dfrac{a}{b}$ con $b\not = 0$, el número en la parte superior se denomina *numerador* y el de la inferior *denominador*. Las fracciones se usan para expresar cantidades que no corresponden a número enteros, pero también éstos pueden representarse mediante fracciones. Distintas fracciones pueden representar a la misma cantidad, entonces se llaman *fracciones equivalentes*; entre todas las fracciones que representan a la misma cantidad hay solamente una que tiene la propiedad de que $\operatorname{mcd}(a,b)=1$, es decir, numerador y denominador son primos relativos, este tipo de fracciones se llaman *irreducibles*.

Partiendo de la fracción $\dfrac{5}{6}$ podemos construir fracciones equivalentes multiplicando numerador y denominador por el mismo número, por ejemplo, multiplicando por $2$ obtenemos $\dfrac{10}{12}$ y por $3$ nos da $\dfrac{15}{18}$. Las tres son fracciones equivalentes, es decir, representan a la misma cantidad y por tanto podemos escribir $$\frac{5}{6}=\frac{10}{12}=\frac{15}{18}.$$ De entre estas tres fracciones la primera es la fracción irreducible puesto que $5$ y $6$ son primos relativos.

Para obtener la fracción irreducible equivalente a una dada podemos utilizar el $\operatorname{mcd}$ de numerador y denominador. Por ejemplo, para calcular la fracción irreducible equivalente con $\dfrac{198}{825}$ usamos que $\operatorname{mcd}(198,825)=33$ y así tanto numerador como denominador pueden escribirse como múltiplos de ese número y la fracción puede ser simplificada eliminando el mismo factor en numerador y denominador: $$\dfrac{198}{825}= \dfrac{33\cdot 6}{33\cdot 25}= \dfrac{\require{cancel}\cancel{33}\cdot 6}{\cancel{ 33}\cdot 25}=\dfrac{6}{25}.$$ La fracción resultante es irreducible puesto que se han eliminado todos los factores primos comunes de numerador y denominador.

## Suma y resta de fracciones


Para realizar la suma o resta de cantidades necesitamos representarlas mediante fracciones que tengan el mismo denominador, para ello basta elegir entre todas las fracciones equivalentes las adecuadas en cada caso. La forma más habitual es calcular el $\operatorname{mcm}$ de todos los denominadores que tengamos. Una vez que las fracciones tienen el mismo denominador las operaciones de suma y resta se efectúan sobre los numeradores.

Si queremos calcular $$\dfrac{5}{6} + 2 - \dfrac{4}{9},$$ debemos sustituir cada uno de los números por una fracción equivalente de forma que las tres tengan el mismo denominador. En primer lugar observemos que $2=\dfrac{2}{1}$, así que tenemos los denominadores $6,1,9$; el $\operatorname{mcm}(6,1,9)=18$, que será el denominador común que necesitamos. Ahora cada una de las cantidades debe representarse por la fracción equivalente que tiene denominador $18$; para $\dfrac{5}{6}$ calculamos el cociente entre $18$ y el denominador original $6$, que es $3$ (siempre resultará entero, porque el $\operatorname{mcm}$ es un múltiplo como su nombre indica), por tanto, para que la fracción sea equivalente debemos multiplicar numerador y denominador por $3$ $$\dfrac{5}{6}=\dfrac{5\cdot 3}{6\cdot 3}=\dfrac{15}{18}.$$ Del mismo modo, $$2=\dfrac{2}{1}=\dfrac{2\cdot 18}{1\cdot 18}=\dfrac{36}{18}$$ y $$\dfrac{4}{9}=\dfrac{4\cdot 2}{9\cdot 2}=\dfrac{8}{18}.$$ Ahora volvemos a escribir la operación a realizar $$\dfrac{15}{18} + \dfrac{36}{18} - \dfrac{8}{18}=\dfrac{15+36-8}{18}=\dfrac{43}{18}.$$


## Producto, fracción inversa y división


Para multiplicar dos fracciones se multiplican ambos numeradores y ambos denominadores: $$\dfrac{a}{b}\cdot \dfrac{c}{d}= \dfrac{a\cdot c}{b \cdot d}.$$

La *fracción inversa* de una dada es la que tiene por numerador al denominador de la primera y viceversa. La fracción inversa de $\dfrac{a}{b}$ es $\dfrac{b}{a}$, es decir, la fracción inversa es aquella que al multiplicarla por la dada nos da como resultado el número 1.

$$\dfrac{a}{b}\cdot \dfrac{b}{a}= \dfrac{a\cdot b}{b\cdot a}=\dfrac{\cancel{a}\cdot \cancel{b}\cdot 1}{\cancel{a}\cdot \cancel{b}\cdot 1}=\dfrac{1}{1}=1.$$

Observemos que el número $0=\dfrac{0}{1}$ no tiene fracción inversa puesto que $0$ no es admitido como denominador.

Para dividir dos fracciones se puede usar la regla de multiplicar en cruz o sustituir la división por el producto con la fracción inversa del divisor, es decir:

$$\dfrac{a}{b}\colon \dfrac{c}{d}= \dfrac{\frac{a}{b}}{\frac{c}{d}}= \dfrac{a}{b}\cdot \dfrac{d}{c}=\dfrac{a\cdot d}{b \cdot c}.$$

## Operaciones con fracciones, uso de paréntesis y signos

Ahora ejercitaremos las operaciones recordando que el producto tiene prioridad sobre la suma pero que esta prioridad puede cambiarse mediante el uso de paréntesis. También prestaremos atención a los signos que aparecen.

Efectuaremos las operaciones

1.  $\dfrac{2}{5}\cdot \dfrac{1}{3}- \dfrac{1}{4}$

2.  $\dfrac{2}{5}\cdot \left( \dfrac{1}{3}- \dfrac{1}{4}\right)$

y comprobaremos que los resultados son diferentes. En la primera se efectúa en primer lugar el producto y después la resta: $$\dfrac{2}{5}\cdot \dfrac{1}{3}- \dfrac{1}{4}=\dfrac{2\cdot 1}{5\cdot 3}-\dfrac{1}{4}=\dfrac{2}{15}-\dfrac{1}{4}= \dfrac{8-15}{60}=-\dfrac{7}{60}.$$ En la segunda primero se efectúa la operación entre paréntesis y después el producto: $$\dfrac{2}{5}\cdot \left( \dfrac{1}{3}- \dfrac{1}{4}\right)=\dfrac{2}{5}\cdot \left( \dfrac{4-3}{12}\right)=\dfrac{2}{5}\cdot \dfrac{1}{12}=\dfrac{2}{60}=\dfrac{1}{30}.$$

Los signos se manejan como en los números enteros, teniendo en cuenta que siempre podemos elegir que el signo del denominador sea positivo sin más multiplicar, si es necesario, arriba y abajo por $-1$. 
$$\left( -\dfrac{1}{3}\right)\colon \left( \dfrac{2}{5}-\dfrac{1}{2}\right)=
\left( -\dfrac{1}{3}\right)\colon \left( \dfrac{4-5}{10}\right)
=\left( -\dfrac{1}{3}\right)\colon \left( -\dfrac{1}{10}\right)=
\left( -\dfrac{1}{3}\right)\cdot \left(- \dfrac{10}{1}\right)= \dfrac{10}{3}.$$

::: {#exr-1}

Calcula y devuelve el resultado como fracción irreducible.

1.  $\left(-2+\dfrac{1}{3}\right)\left(\dfrac{7}{5}-1\right) - \dfrac{1}{5}\left(\dfrac{2}{3}-\dfrac{1}{4}\right)$
    [
    $= -\dfrac{3}{4}$
    ]{#solucion-e1-1 .collapse}.
    <button id="e1-1" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>


2.  $\dfrac{\left( -\dfrac{3}{5}\right)\left(-\dfrac{5}{6}\right)}{\dfrac{1}{3}-\dfrac{1}{2}-\dfrac{1}{5}}$
    [
    $= -\dfrac{15}{11}$
    ]{#solucion-e1-2 .collapse}.
    <button id="e1-2" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>

3.  $\left(\dfrac{1}{5}+\dfrac{1}{2}\right)\colon \left( \left(\dfrac{2}{3}-\dfrac{4}{5}\right)+ \dfrac{1}{4}\left(\dfrac{1}{5}-\dfrac{2}{3}\right)\right)$
    [
    $= -\dfrac{14}{5}$
    ]{#solucion-e1-3 .collapse}.
    <button id="e1-3" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>

4.  $1+\dfrac{2}{\dfrac{4}2}$
    [
    $= 1+\dfrac{2}2= 2$
    ]{#solucion-e1-4 .collapse}.
    <button id="e1-4" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>

5.  $\dfrac{\dfrac{2}4}{2}+2$
    [
    $= 2+\dfrac{1}2\dfrac{1}2 =2+ \dfrac{1}4= \dfrac{9}4$
    ]{#solucion-e1-5 .collapse}.
    <button id="e1-5" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>

La división no es \"asociativa\". No podemos por tanto escribir $2/3/4$, puesto que no es lo mismo $\dfrac{2}{\dfrac{3}4}$ que $\dfrac{\dfrac{2}3}4$.
:::


## Potencias

El concepto inicial de potencia es una forma de denotar a un producto en el que todos los factores son idénticos, por ejemplo si queremos expresar el producto $2\times 2 \times 2 \times 2 \times 2$ usaremos la expresión $2^5$, es decir, se escribe el factor que se repite, al que llamaremos *base de la potencia*, en este caso $2$, y se le añade como superíndice el número de veces que aparece en el producto, a lo que llamaremos *exponente*, en este caso $5$. En general escribimos

$$\overbrace{a\cdot a\cdot \dots \cdot a}^{\mbox{n veces}}=a^n.$$

Como convenio, para cualquier número $a$ distinto de cero, $a^0=1$. Observemos que si la base es un número negativo es necesario usar paréntesis para indicar su potencia, por ejemplo $(-2)^4=16$ mientras que $-2^4=-16$.

1.  $a^n \cdot a^m = a^{n+m}$.

2.  $(a\cdot b)^n=a^n \cdot b^n$.

3.  $(a^n)^m=a^{n\cdot m}$.

4.  $\dfrac{a^n}{a^m}=a^{n-m}$.

5.  $a^{-n}=\dfrac{1}{a^n}$.

6.  $\left(\dfrac{a}{b}\right)^n=\dfrac{a^n}{b^n}$.

Calculamos 
$$\left( -\dfrac{1}{2} \right)^{-2}= \dfrac{1}{\left( -\dfrac{1}{2} \right)^{2}}= \dfrac{1}{ \dfrac{(-1)^2}{2^2}}= 1\cdot \dfrac{2^2}{1}=2^2.$$

Usamos las propiedades anteriores y la simplificación de fracciones para obtener una expresión simplificada de una dada: $$a^2\cdot b^3\cdot \left(\dfrac{1}{ab^2}\right)^2= a^2\cdot b^3\cdot \dfrac{1^2}{(ab^2)^2}= \dfrac{\cancel{a^2}\cdot b^3}{\cancel{a^2}\cdot b^4}= b^{3-4}=b^{-1}= \dfrac{1}{b}.$$ Podemos observar que la cancelación de $a^2$ también podría realizarse haciendo uso de las propiedades de las potencias, puesto que $$\dfrac{a^2}{a^2}=a^{2-2}=a^0 = 1.$$


::: {#exr-2}

Simplifica las siguientes expresiones


1.  $\dfrac{a^2}{(a^2)^{-3}\cdot a^4}$
    [
    $= a^4$
    ]{#solucion-e2-1 .collapse}.
    <button id="e2-1" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>

2.  $\dfrac{(a^5\cdot a^{-2})^3}{a^{-3}}$
    [
    $= a^{12}$
    ]{#solucion-e2-2 .collapse}.
    <button id="e2-2" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>


3.  $\left(\dfrac{a}{b}\right)^3\cdot\left(\dfrac{b}{a}\right)^{-2}\cdot \left(\dfrac{1}{a}\right)^{-1}$
    [
    $= \dfrac{a^{6}}{b^5}$
    ]{#solucion-e2-3 .collapse}.
    <button id="e2-3" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>


\"Elevar a\" no es asociativo. No tiene sentido escribir ${2^3}^4$, pues no es lo mismo $2^{(3^4)}$ que $(2^3)^4$ (el primero vale $2417851639229258349412352$ y el segundo $4096$).
:::


## Radicales


Definimos la raiz n-ésima de un número no negativo $a$ como aquella cantidad no negativa $x$ tal que $x^n=a$, y la denotaremos por $\sqrt[n]{a}$: 
$$\sqrt[n]{a}=x \text{ implica que } x^n=a.$$

Estamos escogiendo raíces no negativas, si quitamos esa restricción, puede que exista más de una. Por ejemplo, existen dos raíces cuadradas de $1$, pues tanto $(-1)^2$ como $1^2$ valen $1$. También estamos considerando raíces de números no negativos. Como el cuadrado de un número real es siempre no negativo, no podemos encontrar una raíz real cuadrada de un número negativo. Sin embargo, sí podemos encontrar una cúbica. Por ejemplo, $(-1)^3=-1$, por lo que $-1$ es una raíz cúbica de $-1$.

La expresión de los radicales también puede realizarse mediante potencias, si $x=\sqrt[n]{a}$, entonces $x=a^{\frac{1}{n}}$ puesto que 
$$x^n= (a^{\frac{1}{n}})^n= a^{\frac{n}{n}}=a^1 = a.$$

La expresión de radicales como potencias con exponentes fraccionarios tiene las mismas propiedades, usando las operaciones correspondientes con dichos números.

Podemos escribir en forma de potencia la siguiente expresión

$$\left(\sqrt[12]{a^4b^8}\right)^3  = \left( (a^4 b^8)^{\frac{1}{12}} \right)^3 = \left( a^{\frac{4}{12}}b^{\frac{8}{12}} \right)^3 =a^{\frac{4\cdot 3}{12}}b^{\frac{8\cdot 3}{12}} = ab^2.$$

::: {#exr-3}

Simplifica las siguientes expresiones:

1.  $\sqrt[3]{\sqrt{a^5 a^7}}$
    [
    $= a^2$
    ]{#solucion-e3-1 .collapse}.
    <button id="e3-1" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>

2.  $\left(\sqrt[3]{\sqrt[7]{\sqrt{8a^3}}}\right)^7$
    [
    $= \sqrt{2a}$
    ]{#solucion-e3-2 .collapse}.
    <button id="e3-2" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>

3.  $\dfrac{(\sqrt{x})^3}{\left(\sqrt[3]{\sqrt[4]{x}}\right)^6}$
    [
    $= x^{3}$
    ]{#solucion-e3-3 .collapse}.
    <button id="e3-3" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>
:::

------------------------------------------------------------------------

[Esta página está basada en las transparencias de Jerónimo Alaminos Prats, José Extremera Lizana y Pilar Muñoz Rivas para el Curso Cero de la ETSIIT de la Universidad de Granada.]{.small}
