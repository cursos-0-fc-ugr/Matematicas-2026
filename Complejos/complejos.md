---
title: Números complejos
lang: es
format: 
  html: 
    #html-math-method: mathjax
    include-in-header: includes-header.html
    fontsize: 1.2em
    toc: true
    page-layout: full
    format-links: true
    html-math-method:
            method: mathjax
            url: "https://cdn.jsdelivr.net/npm/mathjax@4/tex-svg.js"
            # url: "https://cdn.jsdelivr.net/npm/mathjax@4.0.0-beta.4/tex-mml-chtml.js"

---


## El cuerpo de los números complejos

En el cuerpo de los números reales la ecuación $x^2+1=0$ no tiene solución. Para conseguir soluciones de esta ecuación es necesario, por tanto, ampliar el conjunto de los números reales. El nuevo conjunto de números que resulta de esta ampliación es el conjunto de los números complejos.

**Definición de número complejo.** Llamaremos número complejo a todo par ordenado $(a,b)$ de números reales.

**Igualdad de números complejos.** Dados dos números complejos $z=(a,b)$ y $w=(c,d)$, se tiene que $z=w$ si, y sólo si, $a=c$ y $b=d$.

**Suma y producto de números complejos.** La suma y el producto de dos números complejos $z=(a,b)$ y $w=(c,d)$ vienen dadas por las igualdades: 

$$ \begin{aligned}z+w&=(a+c,b+d), \\
z\,w &=(ac-bd,ad+bc). \end{aligned}
$$


**Propiedades de la suma y el producto de números complejos.**

1.  La suma y el producto de números complejos son operaciones asociativas y conmutativas.

2.  El complejo $(0,0)$ es el elemento neutro de la suma.

3.  Dado un complejo $z=(a,b)$, es obvio que $(-a,-b)$ es su elemento opuesto para la suma. Así pues, denotamos $-z=(-a,-b)$.

4.  El complejo $(1,0)$ es el elemento neutro del producto.

5.  Si $z=(a,b)$ es distinto de $(0,0)$, entonces el número complejo $\left(\frac a{a^2+b^2}\,,\,\frac{-b}{a^2+b^2}\right)$ es el inverso de $z$ para el producto, y se denota por $z^{-1}$ o por $\frac{1}{z}$.

6.  El producto de números complejos cumple la propiedad distributiva respecto de la suma.

7.  Si $z$ y $w$ son números complejos, escribiremos $z-w$ en lugar de $z+(-w)$. Si, además, $w\neq(0,0)$, entonces $\frac{z}{w}$ tendrá el mismo significado que $z\,w^{-1}$.

El conjunto de los números complejos, con las operaciones suma y producto previamente definidas, es un cuerpo, al que llamaremos *cuerpo de los números complejos*, y lo denotaremos por $\mathbb{C}$.

**Forma binómica de un número complejo.** El complejo $(0,1)$ recibe el nombre de *unidad imaginaria* y se denota por $i$. Así,

$$(a,b)=(a,0)+(0,b)=(a,0)+(b,0)(0,1)=a+b\,i,\, \text{ para todo
} (a,b)\in \mathbb{C}.
$$

La expresión $a+b\,i$ es la llamada *forma binómica* del complejo $(a,b)$. La forma binómica es muy útil desde el punto de vista aritmético porque permite aprovechar la estructura de cuerpo de $\mathbb{C}$ a la hora de operar con números complejos. Lo único que hemos de saber es que 

$$i\, i=(0,1)(0,1)=(-1,0)=-1
$$

Ni siquiera es necesario recordar la definición de la suma o el producto en $\mathbb{C}$, pues, dados dos complejos $z=a+b\,i$ y $w=c+d\,i$, obtenemos (aplicando las propiedades de cuerpo de $\mathbb{C}$) que

$$\begin{aligned} &z+w=(a+bi)+(c+di)=(a+c)+(b+d)i\,, \\
&zw=(a+bi)(c+di)=(ac-bd)+(ad+bc)i.\end{aligned}
$$


También de esta forma es fácil considerar $\mathbb R$, el conjunto de los números reales, como subconjunto de $\mathbb C$. Los números reales se corresponden con los números complejos $a+b i$ con $b=0$.

:::: {#exr-1}

Calcula la suma, producto, diferencia y cociente de los pares de números complejos $z_1=(2,1)$ y $z_1=(-2,3).$ Calcula además las mismas operaciones utilizando la forma binómica.  <button id="e1-1" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>  

::::


::: {#solucion-e1-1 .callout .collapse}
La suma y diferencia se hacen coordenada a coordenada a coordenada, por lo que $z_1+z_2=(0,4)$ y $z_1-z_2=(4,-2)$. 

En forma binómica, $z_1+z_2=4i$ y $z_1-z_2=4-2i$. 

El producto es $z_1z_2=(-7,4)$, y en forma binómica, $-7+4i$. Por último, $\dfrac{z_1}{z_2}= \left(-\frac{1}{13},-\frac{8}{13} \right)$, que en forma binómica es $-\dfrac{1}13-\dfrac{8}{13} i.$
:::


::: {.callout title="Solución" collapse=true #e1-1}
La suma y diferencia se hacen coordenada a coordenada a coordenada, por lo que $z_1+z_2=(0,4)$ y $z_1-z_2=(4,-2)$. En forma binómica, $z_1+z_2=4i$ y $z_1-z_2=4-2i$. El producto es $z_1z_2= (-7,4)$, y en forma binómica, $-7+4i$. Por último, $\dfrac{z_1}{z_2}= \left(-\frac{1}{13},-\frac{8}{13} \right)$, que en forma binómica es $-\dfrac{1}13-\dfrac{8}{13} i$.
:::


**Parte real, parte imaginaria, conjugado y módulo de un número complejo.** Sea $z=a+bi$ $\in\mathbb{C}$. Los números reales $a$ y $b$ reciben el nombre de *parte real* y *parte imaginaria*, respectivamente, de $z$. Escribimos $a=\operatorname{Re}(z)$ y $b=\operatorname{Im}(z)$. El complejo $a-bi$ se denomina *conjugado* de $z$ y el número real no negativo $\|z\|=\sqrt{a^2+b^2}$ recibe el nombre de *módulo de* $z$.

Dados $z,w\in\mathbb{C}$. Se tienen las siguientes propiedades:

-   $\overline{\overline{z}}=z$,

-   $\overline{z+w}=\overline{z}+\overline{w}$,

-   $\overline{zw}=\overline{z}\,\overline{w}$,

-   Si $w\neq 0,$ $\overline{(\frac
    zw)}=\frac{\overline{z}}{\overline{w}}$,

-   $\operatorname{Re}(z)=\frac{z+\overline{z}}2$ ,
    $\operatorname{Im}(z)=\frac{z-\overline{z}}{2i}$,

-   $z=\overline{z}\Leftrightarrow z\in \mathbb{R}$,

-   $\|z\|=\|\overline{z}\|=\|-z\|$,

-   $z\overline{z}=\|z\|^2$,

-   $\|zw\|=\|z\|\,\|w\|$,

-   $\|z\|=0\Leftrightarrow z=0$,

-   $\|z+w\|\leq \|z\|+\|w\|$ *(Desigualdad triangular)*,

-   $\big\vert \|z\|-\|w\|\big\vert\leq \|z-w\|$,

-   $\|z+w\|^2+\|z-w\|^2=2(\|z\|^2+\|w\|^2)$
    *(Identidad del paralelogramo)*.

Vamos a ver un método para calcular las potencias enteras de la unidad imaginaria. Observe, en primer lugar, que las potencias de exponente natural de $i$ se vuelven a repetir a partir de la cuarta potencia: 

$$\begin{array}{l} i^0=1, \\ i^1=i, \\
i^2=(0,1)(0,1)=(-1,0)=-1, \\ i^3=i^2\cdot i=-i, \\
i^4=i^2i^2=(-1)(-1)=1, \\ i^5=i^4i=i, \\ \quad\vdots
\end{array}
$$

Dado $n\in\mathbb{N}$, si dividimos $n$ entre $4$, obtenemos que $n=4c+r$ para algún cociente $c\in\mathbb{N}\cup\{0\}$ y un resto $r\in\mathbb{N}\cup\{0\}$ con $0\leq r < 4$. Entonces

$$i^n=i^{4c+r}=(i^4)^c\,i^r=i^r
$$

y, ahora, $i^r$ es una de las cuatro primeras potencias de $i$. En cuanto a las potencias de exponente negativo de $i$, observe que

$$i^{-n}=\frac{1}{i^n}=\frac{1}{i^{4c+r}}=\frac{1}{i^r}=i^{-r}=i^{-r}\,i^4=i^{4-r}.
$$

Como $0 < 4-r\leq 4$, entonces $i^{4-r}$ es una de las primeras potencias de exponente natural de $i$ que hemos calculado antes.

:::: {#exr-2}
1.  Calcula las potencias $155$, $7$, $9$, $23$ y $-19$ de la unidad imaginaria $i=(0,1)$. <button id="e2-1" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>

    ::: {#solucion-e2-1 .callout .collapse}
    El resto de dividir $155$ entre $4$ es $3$, por lo que $i^{155}=i^3=-i$. Lo mismo ocurre con $7$ y $23$. Para exponente $9$, $i^9=i^{2\times 4+1}=i$. 
    
    Por último, $-23=-24+1=-6\times 4+1$, y por tanto $i^{-23}=(i^{4})^{-6}i=1 i=i$.
    :::

2.  Expresa los números complejos $z_1=(-1,1)$, $z_2=(1,2)$ y $z_3=(4,-1)$ en forma binómica y realiza las operaciones siguientes:

    1.  $\dfrac{z_1\overline{z_2}-{z_3}^2}{z_3}$. <button id="e2-2" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>

        ::: {#solucion-e2-2 .callout .collapse}
        $\dfrac{z_1\overline{z_2}-{z_3}^2}{z_3}=-\dfrac{67}{17} +
        \dfrac{30}{17}i$
        :::

    2.  $\dfrac{-(\overline{z_1}){(z_2)}^2+iz_3}{\overline{z_1}+\overline{z_3}}$. <button id="e2-3" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>

        ::: {#solucion-e2-3 .callout .collapse}
        $\dfrac{-(\overline{z_1}){(z_2)}^2+iz_3}{\overline{z_1}+\overline{z_3}}=-2 + \dfrac{5}{3}i$. 
        :::

3.  Resuelve las siguientes ecuaciones con coeficientes complejos:

    1.  $z^2+(-3+2i)z+(5+i)=0$.  <button id="e2-4" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>

        ::: {#solucion-e2-4 .callout .collapse}
        Las soluciones son $\frac{3- 2i \pm \sqrt{-15 - 16i}}2$.
        :::

    2.  $z^6-z^3-2=0$. <button id="e2-5" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>

        ::: {#solucion-e2-5 .callout .collapse}
        Hacemos $x=z^3$, con lo que obtenemos una nueva ecuación $x^x-x-2=0$, cuyas raíces son $x=-1$ y $x=2$. Por tanto, las soluciones de la ecuación original son las raíces cúbicas de $-1$ y $2$. 
        :::

::::

## Representación geométrica de los números complejos 

En esta sección haremos uso de algunas funciones trigonométricas y de algunas funciones arco. Aunque aún no han sido presentadas, suponemos que el alumno está suficientemente habituado a ellas para poder usarlas. En cualquier caso, trataremos estas funciones y sus propiedades en temas posteriores.

**Representación geométrica de los números complejos.** Hagamos corresponder a cada número complejo $z=a+bi$ el punto del plano cuyas coordenadas referidas a un sistema de ejes cartesianos ortogonales son $(a,b)$, como indica el siguiente gráfico. De este modo, se establece una relación biunívoca entre los números complejos y los puntos del plano. En esta representación se llama *eje real* al eje de abscisas y *eje imaginario* al eje de ordenadas.

::: {#box .jxgbox style="width:400px; height:400px;"}
:::

<script type="text/javascript">
    //JXG.Options.text.useMathJax = true;
    function pintac(){
    JXG.Options.axis.ticks.drawLabels = false;
    var board = JXG.JSXGraph.initBoard('box', {boundingbox: [-2,2,2,-2], axis:true, showCopyright:false, showNavigation:false, grid:false});
    //var c = board.create('circle',[[0,0],[0,1]]);
    var z = board.create('point',[1,1.5], {name:"\\(z=(a,b)\\)"});
    var pa = board.create('point', [()=>z.X(),()=>0], {name:"", size:0})
    var pb = board.create('point', [()=>0,()=>z.Y()], {name:"", size:0})
    var a = board.create('segment',[function(){return z}, [function(){return z.X()},0]], {dash:1, strokeColor:"red"})
    var b = board.create('segment',[function(){return z}, [0,function(){return z.Y()}]], {dash:1, strokeColor:"red"})
    var abs = board.create('segment', [function(){return z}, [0,0]], {strokeColor:"orange"} )
    board.create('text',[()=>-0.1*Math.sign(z.X()),()=>z.Y(),()=>"b"])
    board.create('text',[()=>z.X(),()=>-0.1*Math.sign(z.Y()),()=>"a"])
    var l1 = board.create('line',[[0,0],z],{visible:false})
    var l2 = board.create('line',[[0,0],[10,0]], {visible:false})
    //var ar=  board.create('angle',[l2,l1,1,1])
    var ar= board.create('angle',[function(){return z.Y()>0?[10,0]:[z.X(),z.Y()]},[0,0],function(){return z.Y()>0?[z.X(),z.Y()]:[10,0]}],{name:'',text:'ω',fillColor:"green"})
    board.update()
    }
    pintac()
</script>

Además, el [módulo]{style="color:orange"} de $z$ es la longitud del segmento de extremos $0$ y $(a,b)$.

**Argumento principal de un número complejo.** Dado un número complejo no nulo $z=a+bi$, el *argumento principal* de $z$ es el número real 

$$ 
\arg(a+b\,i)=\left\{
\begin{array}{ll}
\operatorname{arctan}\left(\frac{b}{a}\right)-\pi & \text{si } a < 0, b < 0, \\ 
 -\frac{\pi}{2} & \text{si }a=0, b < 0, \\ 
\operatorname{arctan}\left(\frac{b}{a}\right) & \text{si }a > 0, \\ 
\frac{\pi}{2} & \text{si }a=0, b > 0, \\ 
\operatorname{arctan}\left(\frac{b}{a}\right)+\pi &
\text{si }a < 0, b\geq 0. 
\end{array} \right. 
$$

Gráficamente, el argumento principal representa el ángulo que forma el segmento de extremos $0$ y $(a,b)$ con la parte positiva del eje real.

Sea $z\in \mathbb{C}$, $z\neq 0$. El argumento principal de $z$, $\arg(z)$, es el único número real en el intervalo $]-\pi,\pi]$ que verifica la igualdad

$$z=\|z\|\left(\cos(\arg(z))+i\,\operatorname{sen}(\arg(z))\right).
$$


**Conjunto de argumentos de un número complejo.** Sea $z\in \mathbb{C}$, $z\neq 0$. Se dice que un número real $\omega$ es *un argumento de* $z$ si verifica que

$$z=\|z\|(\cos\omega+i\,\operatorname{sen}\omega).
$$
 A
esta expresión la llamaremos *forma trigonométrica* del número complejo
$z$.


:::: {#exr-3}

Describe geométricamente los conjuntos de números complejos definidos de la siguiente manera:


1.  $\{z\in\mathbb{C}\colon
    \operatorname{Re}(z) > 0\}$. <button id="e3-1" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>

    :::: {#solucion-e3-1 .callout .collapse}
    ::: {#ebox3-1 .jxgbox style="width:400px; height:400px;display:inline-block;text-align: center;"}
    :::
    <script type="text/javascript">
      JXG.Options.axis.ticks.drawLabels = true;
      function pintae31(){
        var board = JXG.JSXGraph.initBoard('ebox3-1', {boundingbox: [-2, 2, 2, -2], axis:true, showCopyright:false, showNavigation:false}),
        l1 = board.create("line",[[1,10],[1,0]], {fixed:true,strokeColor:"orange"});
        ineq = board.create("inequality",[l1]);

      }
      pintae31();
    </script>
    ::::

2.  $\{z\in\mathbb{C}\colon -1\leq \operatorname{Re}(z)\leq 2\,,\; \|z\|=1\}$. <button id="e3-2" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>

    :::: {#solucion-e3-2 .callout .collapse}
    ::: {#ebox3-2 .jxgbox style="width:400px; height:400px;display:inline-block;text-align: center;"}
    :::
    <script type="text/javascript">
    JXG.Options.axis.ticks.drawLabels = true;
    function pintae32(){
    var board = JXG.JSXGraph.initBoard('ebox3-2', {boundingbox: [-2, 2, 2, -2], axis:true, showCopyright:false, showNavigation:false}),
    l1 = board.create("circle",[[0,0],[1,0]], {fixed:true,strokeColor:"orange"});
    }
    pintae32();
    </script>
    
    ::::

3.  $\{z\in\mathbb{C}\colon 1 < \|z\| < 2\}$. <button id="e3-3" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>

    :::: {#solucion-e3-3 .callout .collapse}
    ::: {#ebox3-3 .jxgbox style="width:400px; height:400px;display:inline-block;text-align: center;"}
    :::
    <script type="text/javascript">
    function pintae33(){
    var board = JXG.JSXGraph.initBoard('ebox3-3', {boundingbox: [-3, 3, 3, -3], showCopyright:false, showNavigation:false}),
    c2=board.create("circle",[[0,0],[2,0]], {fixed:true,strokeColor:"orange",fillColor:"orange",fillOpacity:0.1,dash:2});
    c1=board.create("circle",[[0,0],[1,0]], {fixed:true,strokeColor:"orange", fillColor:"white",dash:2});
    board.create('line',[[0,0],[0,1]],{strokeColor:"black",strokeWidth:1});
    var OX=board.create('line',[[0,0],[1,0]],{strokeColor:"black",strokeWidth:1});
    board.create('ticks', [OX], {
        // drawZero: true,
        anchor: 'left',
        drawLabels: true,
        minorTicks: 0,
        label: {
            anchorX: 'middle',
            anchorY: 'top',
            offset: [0, -5]
        }
    });
    //board.create('text',[1,-0.1,1]);
    //board.create('text',[2,-0.1,2]);
    }
    pintae33();
    </script>
    ::::

4.  $\{z\in\mathbb{C}\colon \|z\|\geq 1\}.$

::::

## Forma polar de un número complejo


Se llama* forma polar* del número complejo $z$ a la expresión dada por $z=\left\| z\right\| _{\omega}$ donde $\left\| z\right\| $ es el módulo de $z$ y $\omega$ es un argumento de $z$.

Por ejemplo, $1+i=\left( \sqrt{2}\right)_{\frac\pi 4}$.

**Operaciones con números complejos en forma polar.** Sean $z_1,z_2$ dos números complejos con $z_1=\left\| z_1\right\| _{w_1}$, $z_2=\left\| z_2\right\|_{w_2}.$ Se verifican las siguientes propiedades:

1.  $z_1\cdot z_2=\left( \left\| z_1\right\| \cdot \left\| z_2\right\| \right) _{w_1+w_2}$,

2.  $\frac1{z_1}=\left( \frac1{\left\| z_1\right\| }\right) _{-w_1}$,

3.  $\frac{z_1}{z_2}=\left( \frac{\left\| z_1\right\| }{\left\| z_2\right\| }\right) _{w_1-w_2}$,

4.  $\overline{z_1}=\left( \left\| z_1\right\| \right) _{-w_1}$.

Por reiteración de la fórmula del producto de números complejos en forma polar se tiene la siguiente fórmula.

**Fórmula de de Moivre.** Sea $z\in\mathbb{C}$, $z\neq 0$, y sea $w\in\mathbb{R}$ un argumento de $z$. Entonces 

$$z^n=\left( \left\|
z\right\| _w\right) ^n=\left( \left\| z\right\| ^n\right)
_{nw},\textrm{ para todo } n\in\mathbb{N}.
$$


Si $z\in \mathbb{C}$ verifica que $\|z\|=1$ y $w$ es un argumento de $z$, es decir, $z=1_w=\cos w+i\cdot \operatorname{sen} w$, entonces se tiene la siguiente expresión para las potencias de $z$:

$$(\cos w+i\cdot \operatorname{sen} w)^n=\cos(nw)+i\cdot
\operatorname{sen}(nw),\textrm{ para todo } n\in
\mathbb{N}.
$$


::::: {#exr-4}
1. Sean los siguientes números complejos: $z_1=\sqrt{3}-i,$
$z_2=-\sqrt{3}+i,$ $z_3=-4i,$
$z_4=1.$

    1.  Represéntalos gráficamente en el plano complejo.

    2.  Halla sus respectivos módulos y argumentos.

    3.  Escríbelos en forma polar y trigonométrica.

    4.  Representa gráficamente al número complejo opuesto, al conjugado y al opuesto del conjugado de cada uno de los cuatro números complejos dados. <button id="e4-1" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>

        :::: {#solucion-e4-1 .callout .collapse}
        Vamos a dar la solución para $z_1$. El argumento de $z_1$ es
        $-\dfrac{\pi}{6}$ y su módulo es $2$.

        Por tanto $z_1=(2)_{-\frac{\pi}6}=2\left(\cos\left(-\frac{pi}6\right)+i \operatorname{sen}\left(-\frac{\pi}6\right)\right)$.

        ::: {#ebox4-1 .jxgbox style="width:400px; height:400px;display:inline-block;text-align: center;"}
        :::
        <script type="text/javascript">
        JXG.Options.axis.ticks.drawLabels = true;
        JXG.Options.text.useMathJax = true;
        function pintae41(){
          var board = JXG.JSXGraph.initBoard('ebox4-1', {boundingbox: [-3, 3, 3, -3], showCopyright:false, showNavigation:false, axis:true});
          board.create('point',[Math.sqrt(3),-1],{name:'\\(z_1\\)',fixed:true})
          board.create('point',[-Math.sqrt(3),1],{name:'\\(-z_1\\)',fixed:true})
          board.create('point',[Math.sqrt(3),1],{name:'\\(\\overline{z_1}\\)',fixed:true})
          board.create('point',[-Math.sqrt(3),-1],{name:'\\(-\\overline{z_1}\\)',fixed:true})
        }
        pintae41();
        </script>
        ::::

1.  Sean los siguientes números complejos: $z_1=(2)_{120{{}^o}}$ $z_2=(3)_{45{{}^o}}$.

    1.  Halla la forma binómica de cada uno de ellos.

    2.  Calcula $z_1\cdot z_2$ y $\dfrac{z_1}{z_2}$ utilizando la forma polar. <button id="e4-2" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>

        :::: {#solucion-e4-2 .callout .collapse}
        Tenemos que $z_1=2\left(\cos\left( \frac{2\pi}3 \right) + i
        \operatorname{sen}\left(\frac{2\pi}3 \right) \right)=
        -1+i\sqrt{3}$ y $z_2=3\left(\cos\left( \frac{\pi}2 \right) +
        i \operatorname{sen}\left(\frac{\pi}2 \right) \right)= 3i $.

        El producto es $z_1z_1=(2\times 6)_{120^o+45^o}=(12)_{165^o}$,
        y la división es
        $\dfrac{z_1}{z_2}=\left(\dfrac{2}6\right)_{120^o-45^o}=\left(\dfrac{1}3\right)_{75^o}$.
        ::::

1.  Escribe el número complejo $z=-1+\sqrt{3}i$ en forma polar y calcula $z^6$ en dicha forma. Pasa el resultado a la forma binómica. <button id="e4-3" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>

    ::: {#solucion-e4-3 .callout .collapse}
    Ya hemos visto antes que $z=(2)_{120^o}=(2)_{\frac{2\pi}3}$. Así $z^6=(2^6)_{\frac{12\pi}3}=(64)_{4\pi}=(64)_{0}=64$.
    :::
:::::

## Raíces de un número complejo

Dados $z\in\mathbb{C}$ y $n\in\mathbb{N}$, se dice que un número complejo $v$ es una raíz $n$-ésima de $z$ si $v^n=z$. En particular, si $n=2$ se dice que $v$ es una *raíz cuadrada* de $z$ y si $n=3$ se dice que $v$ es una *raíz cúbica* de $z$.

Si $z$ es el complejo no nulo que tiene por forma polar $\|z\|_{\omega}$, entonces existen $n$ raíces $n$-ésimas de $v$, las cuales están dadas por la siguiente expresión:

$$
\left(\sqrt[n]{\|z\|}\right)_{\frac{\omega +2k\pi}{n}}, k\in\{0,1,\ldots,n-1\}.
$$


Como $-1=1_{\pi}$, entonces las raíces cuadradas de $-1$ son


$$
\begin{aligned} 1_{\frac{\pi+2\cdot
0\,\pi}{2}}&=1_{\frac{\pi}{2}}=\cos\left(\frac{\pi}{2}\right)+i\,\operatorname{sen}\left(\frac{\pi}{2}\right)=i\,,\\
1_{\frac{\pi+2\cdot
1\,\pi}{2}}&=1_{\frac{3\pi}{2}}=\cos\left(\frac{3\pi}{2}\right)+i\,\operatorname{sen}\left(\frac{3\pi}{2}\right)=-i.\end{aligned}
$$


**Representación gráfica de las raíces de un número complejo.** Sea $z\in\mathbb{C}$, $z\neq 0$, $\omega\in\mathbb{R}$ un argumento de $z$ y $n\in\mathbb{N}$, $n\geq 3$. Gráficamente las raíces $n$-ésimas de $z$ están representadas como los vértices de un polígono regular de $n$ lados. Por lo tanto, para representar las $n$ raíces se toma la circunferencia de centro $0$ y de radio $\sqrt[n]{\|z\|}$, se considera primero el ángulo $\frac\omega n$ (para $k=0$) y luego sumándole el ángulo $\frac{2\pi}n$ se van obteniendo las restantes $n-1$ raíces.


:::: {#exr-5}

Calcula:


1.  $\sqrt{i}$. <button id="e5-1" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>

    ::: {#solucion-e5-1 .callout .collapse}
    $\sqrt{i}=\left\{\dfrac{\sqrt{2}}{2}+i
    \dfrac{\sqrt{2}}{2}, -\dfrac{\sqrt{2}}{2}-i
    \dfrac{\sqrt{2}}{2}\right\}$.
    :::

2.  $\sqrt[3]{1}$. <button id="e5-2" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>
    
    ::: {#solucion-e5-2 .callout .collapse}
    $\sqrt[3]{1}=\left\{-\dfrac{1}{2}+i
    \dfrac{\sqrt{3}}{2}, -\dfrac{1}{2}-i \dfrac{\sqrt{3}}{2},1
    \right\}$. 
    :::

3.  $\sqrt[3]{-1+i}$. <button id="e5-3" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>
    
    ::: {#solucion-e5-3 .callout .collapse}
    $\sqrt[3]{-1+i}=\left\{\sqrt[6]{2}\left(\cos\left(\frac{\pi}4
    \right)+i \operatorname{sen}\left(\frac{\pi}4\right) \right),
    \sqrt[6]{2}\left(\cos\left(\frac{11 \pi}{12} \right)+i
    \operatorname{sen}\left(\frac{11 \pi}{12}\right)\right),
    \sqrt[6]{2}\left(\cos\left(\frac{5\pi}{12} \right)+
    i\operatorname{sen}\left(\frac{5\pi}{12}\right) \right)
    \right\}$. 
    :::
::::


------------------------------------------------------------------------

Esta página está basada en los apuntes de María Burgos, Moisés Villegas y Jesús Alcantud. Las representaciones gráficas se han realizado con [JSXGraph](http://jsxgraph.uni-bayreuth.de). Las animaciones en JSXGraph y el maquetado de la página han sido realizados por Pedro A. García Sánchez.
