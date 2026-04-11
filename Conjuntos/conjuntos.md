---
title: Conjuntos
title-block-banner: true
lang: es
format: 
  html: 
    include-in-header: includes-header.html
    toc: true
    page-layout: full
    format-links: true
---

## Conjuntos

La idea de conjunto es una de las más significativas en Matemáticas. La mayor parte de los conceptos matemáticos están construidos a partir de conjuntos.

Podríamos decir de forma informal que un *conjunto* es simplemente una colección de objetos a los que llamaremos elementos del conjunto. Esta definición nos bastará para los contenidos de este curso, pero desde el punto de vista matemático es imprecisa y da lugar rápidamente a paradojas. Desde comienzos del siglo XX esta definición dejó de utilizarse por los problemas que acarrea. Por desgracia, dar una definición precisa está bastante lejos de los objetivos de este guión.

- Cuando $x$ sea un elemento de un conjunto $A$, escribiremos $x\in A$, que se lee "$x$ *pertenece* a $A$".

- Diremos que un conjunto $A$ es *subconjunto* del conjunto $B$, y lo denotaremos por $A\subseteq B$, si todo elemento de $A$ pertenece a $B$.

- Un conjunto $A$ es igual que otro conjunto $B$ si tienen los mismos elementos, a saber, si $A\subseteq B$ y $B\subseteq A$. Cuando esto ocurre, escribiremos $A=B$.

- Admitiremos la existencia de un conjunto sin elementos, al que denotamos por $\emptyset$ y llamaremos *conjunto vacío*. El conjunto vacío es subconjunto de cualquier conjunto.

## Operaciones con conjuntos

Sean $A$ y $B$ conjuntos.

1.  La *intersección* de $A$ y $B$ es el conjunto formado por los elementos comunes de $A$ y de $B$, y lo denotamos así $$A \cap B=\{ x : x\in A,\ x\in B\}.$$ Por ejemplo, $\{1,2,3\}\cap\{0,3,4\}=\{3\}$.

<center>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1"
  viewBox="0 -150 450 300"
  width="450" height="300" display="block">
 <desc>
    Intersección conjuntos
 </desc>
 <circle
    style="fill:lightgreen;stroke:none"
    r="140"
    cy="0"
    cx="150" />
 <circle
    style="fill:lightblue;stroke:none;fill-opacity:.4"
    r="120"
    cy="0"
    cx="300" />
 <text
    style="font-size:30;font-weight:normal;font-family:serif"
    y="30"
    x="80">A</text>
 <text style="font-size:30;font-weight:normal;font-family:serif" y="10" x="210">A&#x2229;B</text>
 <text
    style="font-size:30;font-weight:normal;font-family:serif"
    y="-10"
    x="350">B</text>
</svg>
</center>

2.  La *unión* de $A$ y $B$ es el conjunto formado al tomar todos los elementos de $A$ y los de $B$. $$A\cup B=\{x : x\in A \text{ o } x\in B\}.$$ Por ejemplo, $\{1,2,3\}\cup\{2,3,4\}=\{1,2,3,4\}$ (los elementos que aparecen en ambos conjuntos no tienen que escribirse dos veces; en los conjuntos no hay elementos repetidos).

<center>
  <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1"
  viewBox="0 -150 450 300"
  width="450" height="300">
 <desc>
    Set intersection
 </desc>
 <line x1="150" y1="0" x2="210" y2="115" stroke="black" stroke-width="2"/>
 <circle
    style="fill:lightblue;stroke:black;stroke-width:3"
    r="140"
    cy="0"
    cx="150" />
 <circle
    style="fill:lightblue;stroke:black;stroke-width:3"
    r="120"
    cy="0"
    cx="300" />
 <circle
    style="fill:lightblue;"
    r="137"
    cy="0"
    cx="150" />
 <circle
    style="fill:none;stroke:black;stroke-width:1;stroke-dasharray:8,8"
    r="140" cy="0" cx="150" />
 <circle
    style="fill:none;stroke:black;stroke-width:1;stroke-dasharray:8,8"
    r="120"
    cy="0"
    cx="300" />
 <text
    style="font-size:30;font-weight:normal;font-family:serif"
    y="10"
    x="150">A&#x222A;B</text>
 <text style="font-size:30;font-weight:normal;font-family:serif" y="-100" x="35">A</text>
 <text
    style="font-size:30;font-weight:normal;font-family:serif"
    y="-110"
    x="350">B</text>
</svg>
</center>

3.  La *diferencia* de $A$ y $B$ es el conjunto que tiene por elementos los elementos de $A$ que no están en $B$. $$A\setminus B=\{x\in A : x\not\in B\}$$(siempre que tachemos un símbolo, estamos indicando que no se cumple la condición sin tachar; así $x\not \in B$ significa que $x$ no pertenece a $B$, $A\not=B$ significa que $A$ es distinto de $B$, etcétera). Por ejemplo, $\{1,2,3\}\setminus\{2,4,5\}=\{1,3\}$.

    En algunos textos a la diferencia de $A$ y $B$ se le denota usando $A-B$.

<center>
  <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1"
  viewBox="0 -150 450 300"
  width="450" height="300">
 <desc>
    Set intersection
 </desc>
 <line x1="150" y1="0" x2="210" y2="115" stroke="black" stroke-width="2"/>
 <circle
    style="fill:lightgreen;stroke:black;stroke-width:1"
    r="140"
    cy="0"
    cx="150" />
 <circle
    style="fill:lightblue;stroke:black;stroke-width:1"
    r="120"
    cy="0"
    cx="300" />
 <circle
    style="fill:none;stroke:black;stroke-width:1;stroke-dasharray:8,8"
    r="140" cy="0" cx="150" />
 <text
    style="font-size:30;font-weight:normal;font-family:serif"
    y="10"
    x="80">A\B</text>
 <text style="font-size:30;font-weight:normal;font-family:serif" y="-100" x="35">A</text>
 <text
    style="font-size:30;font-weight:normal;font-family:serif"
    y="-110"
    x="350">B</text>
</svg>
</center>

4.  Si $A\subseteq X$, el *complementario* de $A$ en $X$ es $X \setminus A$. Si $X$ se sobreentiende en el contexto, entonces a $X\setminus A$ se denota por $\overline{A}$ o $A^c$. Claramente, $\overline{\overline{A}}=A$.

    Por ejemplo, el complemento de $\{1,2\}$ en $\{1,2,3,4\}$ es $\{3,4\}$.

    #### Leyes de DeMorgan

    Dados $A$ y $B$ subconjuntos de $X$, se tiene que
    $$\overline{A\cap B}=\overline{A}\cup \overline{B},$$ $$\overline{A\cup B}=\overline{A}\cap \overline{B}.$$

5.  $\mathcal P(A)=\{ X : X\subseteq A\}$ es el *conjunto de partes* de $A$ o conjunto *potencia* de $A$, que es a su vez un conjunto. Por ejemplo, $\mathcal{P}(\{1,2\})=\{\emptyset,\{1\},\{2\},\{1,2\}\}$.

6.  El producto cartesiano de $A$ y $B$ es el conjunto de parejas cuya primera componente está en $A$ y la segunda en $B$. Esto se escribe de la siguiente forma. $$A\times B=\{ (a,b) : a\in A \text{ y } b\in B\}.$$
	<center><div id="box" class="jxgbox" style="width:400px; height:400px;"></div></center>
    <script type="text/javascript">
      //JXG.Options.text.useMathJax = true;
      function pintac(){
        JXG.Options.axis.ticks.drawLabels = false;
        var board = JXG.JSXGraph.initBoard('box', {boundingbox: [-.5,3,3,-.5], axis:true, showCopyright:false, showNavigation:false, grid:false});
        var sx = board.create('segment',[[1,0],[2.5,0]], {visible:false})
        var sy = board.create('segment',[[0,1],[0,2.5]], {visible:false})
        var px = board.create('glider',[1.5,0,sx],{visible:true, withLabel:false, face:'o'});
        var py = board.create('glider',[0,2,sy],{visible:true, withLabel:false, face:'o'});
        var a=board.create('segment',[[0.5,0],px], {withLabel:true, name:'A'})
        var b=board.create('segment',[[0,.5],py],  {withLabel:true, name:'B'})
        var c=board.create('polygon',[[0.5,0.5],[function(){return px.X()},0.5],[function(){return px.X()},function(){return py.Y()}], [0.5,function(){return py.Y()}]],
        {vertices: {visible:false}})
        board.update()
      }
      pintac()
    </script>
    Si en vez de dos conjuntos tenemos $A_1,\ldots, A_n$, $$A_1\times \cdots \times A_n=\{ (a_1,\ldots, a_n) : a_1\in A_1,\ldots, a_n\in A_n\},$$ y a los elementos de $A_1\times \cdots \times A_n$ les llamaremos *$n$-uplas*.

    Al conjunto $A\times \stackrel{n}{\cdots} \times A$ lo denotaremos por $A^n$, para $n$ un entero positivo.

El *cardinal* de un conjunto es el número de elementos que contiene. Usaremos $\sharp A$ para denotar el cardinal del conjunto $A$.

-   $\sharp \mathcal P(A)=2^{\sharp A}$.

-   $\sharp (A\times B)=\sharp A \cdot \sharp B$.

## Relaciones de equivalencia

Sea $A$ un conjunto. Una *relación binaria* en $A$ es un subconjunto $R$ de $A\times A$. Cuando $(x,y)\in R$ escribimos $x\ R\ y$ y decimos que $x$ está relacionado (mediante $R$) con $y$.

Una relación binaria $R$ sobre un conjunto $A$ es una relación de *equivalencia* si verifica las siguientes propiedades.

1.  Para todo $a\in A$, $a\ R\ a$ ($R$ es *reflexiva*).

2.  Dados $a, b\in A$, si $a\ R\ b$, entonces $b\ R\ a$ ($R$ es *simétrica*).

3.  Para cualesquiera $a,b,c\in A$, si $a\ R\ b$ y $b\ R\ c$, entonces $a\ R\ c$ ($R$ es *transitiva*).

Si $R$ es una relación de equivalencia sobre un conjunto $A$, y $a$ es un elemento de $A$, entonces la *clase* de $a$ es el conjunto de todos los elementos de $A$ que están relacionados con $a$, $$[a]=\{x\in A : x\ R\ a\}.$$ Se define el *conjunto cociente* de $A$ por $R$ como el conjunto de todas las clases de equivalencia de elementos de $A$, y se denota por $A/R$. Así $$\frac{A}R=\{ [a] : a\in A\}.$$

Para una relación de equivalencia $R$ en un conjunto $A$ se tiene que

1.  $a\ R\ b$ si y sólo si $[a]=[b]$,

2.  $a\not{R}\ b$ si y sólo si $[a]\cap[b]=\emptyset$.


:::: {#exr-1}

En el conjunto $\mathbb Z=\{0,1,-1,2,-2,\ldots\}$ de los números enteros, definimos la siguiente relación de equivalencia. $$x\ R\ y \text{ si }x-y\text{ es múltiplo de } 5.$$

1.  Demuestra que $R$ es una relación de equivalencia.

2.  Calcula $[2]$.

::: {.callout collapse=true title="Solución"}


Para probar que es una relación de equivalencia comprobamos que se cumplen las tres propiedades que hemos dicho: reflexiva, simétrica y transitiva.

Reflexiva: $x\ R\ x$ ya que

$x-x=0$

es divisible por $5$

Simétrica: si $x\ R\ y$, entonces $x-y$ es divisible por $ 5$ y, por tanto $y-x=-(x-y)$ también lo es

Transitiva: si $x \ R \ y$ y $ y \ R \ z$, entonces $y-x$ y $z-y$ son divisibles por cinco. Por tanto, $z-x=(z-y)+(y-x) $ también es divisible por cinco

La clase de equivalencia de dos está formada por aquellos números $x$ que cumplen que $x-2 $ es divisible por cinco. Despejando $ x$ tiene que ser de la forma siguiente $$[2] = \{x : x-2 \text{ es divisible por } 5 \} = \{ 2+5p : p \in \mathbb{Z}\} = \{ \dots,-3,2,7,\dots \}. $$

:::

::::

:::: {#exr-2   }

En el conjunto ${\mathcal P}(\{1,2,3\})$, definimos la siguiente relación binaria. $$A\sim B\text{ si }\#A=\#B.$$

1.  Demuestra que $\sim$ es una relación de equivalencia.

2.  Calcula $[\{1,2\}]$.

::::

Dado un conjunto $X$, una *partición* de $X$ es una familia de subconjuntos de $X$, $\{A_i\}_{i\in I}$ ($=\{A_i : i\in I\}$), de forma que

1. $A_i\not=\emptyset$ para todo $i\in I$,

2. $A_i\cap A_j=\emptyset$ para cualesquiera $i,j\in I$ con $i\neq j$,

3. $X=\bigcup_{i\in I} A_i$ (la unión de todos los elementos de la familia $\{A_i\}_{i\in I}$).

- Se puede comprobar fácilmente que el hecho de ser $R$ una relación de equivalencia sobre $A$ hace que $A/R$ sea una partición de $A$.

- Es más, si $\{A_1,\ldots,A_n\}$ es una partición de $A$, entonces $$R=(A_1\times A_1)\cup \cdots \cup(A_n\times A_n)$$ es una relación de equivalencia sobre $A$ (nótese que para $a,b\in A$, $a\ R\ b$ si y sólo si existe $i\in\{1,\ldots,n\}$ tal que $a,b\in A_i$) y $$\frac{A}R=\{A_1,\ldots, A_n\}.$$

## Relaciones de orden

Una relación binaria $\le$ sobre un conjunto $A$ es una *relación de orden* si verifica las siguientes propiedades.

1. Para todo $a\in A$, $a\le a$ (reflexiva).

2. Dados $a, b\in A$, si $a\le b$ y $b\le a$, entonces $a=b$ (*antisimétrica*).

3. Para cualesquiera $a,b,c\in A$, si $a\le b$ y $b\le c$, entonces $a\le c$ (transitiva).

Ejemplos de orden son $\le$ en $\mathbb N$, $\mathbb Z$, $\mathbb Q$ y $\mathbb R$.

Si un conjunto $A$ tiene una relación de orden $\le$, al par $(A,\le)$ lo llamaremos *conjunto ordenado*.

:::: {#exr-3}

En el conjunto de los números naturales $\mathbb N=\{0,1,2,\ldots\}$ definimos la relación $a\mid b$ si $b$ es múltiplo de $a$. Demuestra que $\mid$ es una relación de orden.Solución
::::

::: {.callout collapse=true title="Solución"}
Como para cualquier natural $n$, se tiene que $n$ divide a $n$, tenemos que es reflexiva.

Si tenemos tres números naturales tales que $a\mid b$ y $b\mid c$, entonces existen $n,m\in \mathbb{N}$ de forma que $b=n a$ y $c=m b$. Substituyendo $b$ en la segunda igualdad, tenemos $c=m(na)= (mn)a$, y en consecuencia $a\mid c$. Esto prueba que la relación de divisibilidad es transitiva.

Para la antisimetría, supongamos que $a\mid b$ y que $b\mid a$, con $a,b\in \mathbb{N}$. Si $a$ y $b$ son cero, hemos terminado. Entonces existen $m,n\in \mathbb{N}$ de forma que $a=n b$ y $b=ma$. Si cambiamos $b$ por su valor en la primera igualdad, tenemos $ a= n m a$, y de igual manera $b=mnb$. Como, o bien $a$ o $b$ es no nulo, esto lleva a que $mn=1$. Sobre los naturales esto sólo es posible si $n=m=1$. Esto demuestra que $a=1b=b$, y por tanto la relación es antisimétrica.
:::

El conjunto de partes de $\{1,2,3\}$ ordenado por inclusión se puede representar como sigue:

<center><span id="partes" class='content'>Grafo (se necesita conexión a internet) </span></center>
<script>
 document.getElementById("partes").innerHTML =Viz('graph NSGraph{     node [shape=none]; 0 [label="Ø"]; 1 [label="{1}"]; 2 [label="{2}"]; 3 [label="{3}"]; 12 [label="{1,2}"]; 13 [label="{1,3}"]; 23 [label="{2,3}"]; 123 [label="{1,2,3}"]; 1 -- 0; 2 -- 0; 3--0; 12 -- 1; 12 -- 2; 13 -- 1; 13 -- 3; 23 -- 2; 23 -- 3; 123 -- 12; 123 -- 13; 123 -- 23;  }', {engine: "dot"});
</script>

::: {#exr-4}

Sea $X$ un conjunto. Demuestra que $\subseteq$ es una relación de orden en $\mathcal P(X)$.

:::

Un conjunto ordenado $(A,\le)$ es *totalmente ordenado* si para cada $a,b\in A$, se tiene que $a\le b$ o $b\le a$.

En $\mathbb N^n$ definimos la siguiente relación binaria $$(a_1,\ldots,a_n)\le_p (b_1,\ldots,b_n) \text{ si } a_1\le b_1,\ldots, a_n\le b_n.$$ Demuestra que $\le_p$ es una relación de orden (orden producto cartesiano), pero no es un orden total para $n\ge 2$.

::: {#exr-5}
En $\mathbb N^n$ definimos la siguiente relación binaria $(a_1,\ldots,a_n)\preceq_\mathrm{lex} (b_1,\ldots,b_n)$ si la primera coordenada no nula de $(a_1-b_1,\ldots, a_n-b_n)\in \mathbb Z^n$ es positiva (caso de que exista, es decir, puede ser que todas sean nulas). Demuestra que $\preceq_\mathrm{lex}$ es un orden total.
:::

## Aplicaciones entre conjuntos

Sean $A$ y $B$ dos conjuntos. Una *aplicación* $f$ de $A$ en $B$, que denotaremos como $f:A\to B$, es una correspondencia que a cada elemento de $A$ le asocia un único elemento de $B$ (de nuevo esta definición es algo imprecisa, pero suficiente para nuestro curso). Si $a\in A$, al elemento que le asocia $f$ en $B$ lo denotamos por $f(a)$, y se llama la *imagen* de $a$ por $f$. Los conjuntos $A$ y $B$ son el *dominio* y *codominio* de $f$, respectivamente. Llamaremos *conjunto imagen* de $f$ a $${\rm Im}(f)=\{f(a) : a\in A\}.$$

### Tipos especiales de aplicaciones

Si $f:A\to B$ es una aplicación, diremos que $f$ es

1.  *inyectiva* si $f(a)=f(a')$ para $a,a'\in A$, implica $a=a'$;

    ::: {#iny .jxgbox style="width:300px; height:200px;border:0pt solid black;"}
    :::

    <script type="text/javascript">
      //JXG.Options.text.useMathJax = true;
      function pintac(){
        JXG.Options.axis.ticks.drawLabels = false;
        var board = JXG.JSXGraph.initBoard('iny', {boundingbox: [0,3,3,0], axis:false, showCopyright:false, showNavigation:false, grid:false});
        var a1 = board.create('point',[0.5,0.5],{fixed:true, size:1,name:"b"})
        //var a2 = board.create('point',[0.5,1.5],{fixed:true})
        var a3 = board.create('point',[0.5,2.5],{fixed:true,size:1,name:"a"})
        var b1 = board.create('point',[2.5,0.5],{fixed:true,size:1,name:"c'"})
        var b2 = board.create('point',[2.5,1.5],{fixed:true,size:1,name:"b'"})
        var b3 = board.create('point',[2.5,2.5],{fixed:true,size:1,name:"a'"})
        var s1 = board.create('segment',[a1,b1], {lastArrow:true,color:'black'})
        var s2 = board.create('segment',[a3,b3], {lastArrow:true,color:'black'})
        var A=board.create('polygon',[[0.25,0.25],[0.75,0.25],[0.75,2.75], [0.25,2.75]],
        {vertices: {visible:false}, borders:{visible:false}, fixed:true})
        var B=board.create('polygon',[[2.25,0.25],[2.75,0.25],[2.75,2.75], [2.25,2.75]],
        {vertices: {visible:false}, borders:{visible:false}, fixed:true})
        board.update()
      }
      pintac()
    </script>


2.  *sobreyectiva* si ${\rm Im}(f)=B$ (para todo $b\in B$, existe $a\in A$ tal que $f(a)=b$);

    ::: {#sobr .jxgbox style="width:300px; height:200px;border:0pt solid black;"}
    :::

    <script type="text/javascript">
      //JXG.Options.text.useMathJax = true;
      function pintac(){
        JXG.Options.axis.ticks.drawLabels = false;
        var board = JXG.JSXGraph.initBoard('sobr', {boundingbox: [0,3,3,0], axis:false, showCopyright:false, showNavigation:false, grid:false});
        var a1 = board.create('point',[0.5,0.5],{fixed:true, size:1,name:"c"})
        var a2 = board.create('point',[0.5,1.5],{fixed:true,size:1,name:"b"})
        var a3 = board.create('point',[0.5,2.5],{fixed:true,size:1,name:"a"})
        var b1 = board.create('point',[2.5,0.5],{fixed:true,size:1,name:"b'"})
        //var b2 = board.create('point',[2.5,1.5],{fixed:true,size:1,name:"b'"})
        var b3 = board.create('point',[2.5,2.5],{fixed:true,size:1,name:"a'"})
        var s1 = board.create('segment',[a1,b1], {lastArrow:true,color:'black'})
        var s2 = board.create('segment',[a3,b3], {lastArrow:true,color:'black'})
        var s3 = board.create('segment',[a2,b3], {lastArrow:true,color:'black'})
        var A=board.create('polygon',[[0.25,0.25],[0.75,0.25],[0.75,2.75], [0.25,2.75]],
        {vertices: {visible:false}, borders:{visible:false}, fixed:true})
        var B=board.create('polygon',[[2.25,0.25],[2.75,0.25],[2.75,2.75], [2.25,2.75]],
        {vertices: {visible:false}, borders:{visible:false}, fixed:true})
        board.update()
      }
      pintac()
    </script>


3.  *biyectiva* si es inyectiva y sobreyectiva.

    ::: {#biy .jxgbox style="width:300px; height:200px;border:0pt solid black;"}
    :::

  <script type="text/javascript">
    //JXG.Options.text.useMathJax = true;
    function pintac(){
      JXG.Options.axis.ticks.drawLabels = false;
      var board = JXG.JSXGraph.initBoard('biy', {boundingbox: [0,3,3,0], axis:false, showCopyright:false, showNavigation:false, grid:false});
      var a1 = board.create('point',[0.5,0.5],{fixed:true, size:1,name:"c"})
      var a2 = board.create('point',[0.5,1.5],{fixed:true,size:1,name:"b"})
      var a3 = board.create('point',[0.5,2.5],{fixed:true,size:1,name:"a"})
      var b1 = board.create('point',[2.5,0.5],{fixed:true,size:1,name:"b'"})
      var b2 = board.create('point',[2.5,1.5],{fixed:true,size:1,name:"c'"})
      var b3 = board.create('point',[2.5,2.5],{fixed:true,size:1,name:"a'"})
      var s1 = board.create('segment',[a1,b1], {lastArrow:true,color:'black'})
      var s2 = board.create('segment',[a3,b2], {lastArrow:true,color:'black'})
      var s3 = board.create('segment',[a2,b3], {lastArrow:true,color:'black'})
      var A=board.create('polygon',[[0.25,0.25],[0.75,0.25],[0.75,2.75], [0.25,2.75]],
      {vertices: {visible:false}, borders:{visible:false}, fixed:true})
      var B=board.create('polygon',[[2.25,0.25],[2.75,0.25],[2.75,2.75], [2.25,2.75]],
      {vertices: {visible:false}, borders:{visible:false}, fixed:true})
      board.update()
    }
    pintac()
  </script>


::: {#exr-6}

1.  Demuestra que la aplicación $f:\mathbb Q\to \mathbb R$ definida por $f(x)=\frac{1}{2} (2x+1)$ es inyectiva pero no sobreyectiva. <button id="e6-1" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>

    ::: {#solucion-e6-1 .callout .collapse}

    La función $f$ no es sobreyectiva porque $f(q)=q+\frac{1}{2}$ es racional siempre que $q$ sea racional. Veamos que es inyectiva: si $f(x)=f(y),$ entonces $$2x+1= 2y+1 \text{ si y sólo si } x+1= y+1 \text{, lo que equivale a } x=y. $$
    :::

2.  Demuestra que la aplicación $f:\mathbb{Z} \to \mathbb{N}$, $f(x)=\lvert x\rvert$ (valor absoluto) es sobreyectiva pero no inyectiva. <button id="e6-2" class="btn btn-light btn-sm" onclick="show(this.id);">Solución</button>

    ::: {#solucion-e6-2 .callout .collapse}

    Como $f(1)=f(-1)$, la función no es inyectiva. Es sobreyectiva ya que $f(n)=n$, para cualquier natural $n$.
    :::

3.  Demuestra que la aplicación $f:\mathbb Q\to \mathbb Q$, $f(x)=\frac{3x+1}{2}$ es biyectiva.
:::


## Composición de aplicaciones

Sean $f:A\to B$ y $g:B\to C$ dos aplicaciones. La aplicación *composición* de $f$ y $g$ (también conocida como $f$ compuesta con $g$) es la aplicación $g\circ f: A\to C$, definida como $(g\circ f)(a)=g(f(a))$. Para calcular la imagen de un elemento por la composición primero aplicamos $f$ y luego $g$.

Sean $f:\mathbb Z\to \mathbb Z$, $x\mapsto x^2$, y $g:\mathbb Z\to \mathbb Q$, $y\mapsto \frac{1}2(y+1)$. Calcula $g\circ f$.

-   La composición de aplicaciones es asociativa ($f\circ(g\circ h)=(f\circ g)\circ h$) pero no es conmutativa ($f\circ g$ no tiene por qué ser igual a $g\circ f$).

Sea $A$ un conjunto. La aplicación *identidad* en $A$ es la aplicación $1_A: A\to A$ definida como $1_A(a)=a$ para todo $a\in A$.

-   Una aplicación $f:A\to B$ es biyectiva si y sólo si existe una única aplicación $g:B\to A$ tal que $g\circ f=1_A$ y $f\circ g=1_B$. Dicha aplicación diremos que es la *inversa* de $f$ y la denotaremos por $f^{-1}$.

::: {#exr-7}
Demuestra que la aplicación $f:\mathbb Q\to \mathbb Q$, $f(x)=\frac{1}3(2x+1)$ es biyectiva. Calcula $f^{-1}$. Solución
:::

::: {.callout collapse=true title="Solución"}
Para la inyectividad, si $f(x)=f(y)$ para $x,y\in\mathbb{Q}$, entonces $\frac{1}3(2x+1)=\frac{1}3(2y+1)$. Multiplicando por $3$ en ambos lados de la igualdad, tenemos que $2x+1=2y+1$. Restando $1$ en ambas partes de la igualdad y luego dividiendo por $2$, llegamos a que $x=y$, por lo que $f$ es inyectiva.

Para ver que es sobreyectiva, sea $y\in\mathbb{Q}$, y busquemos $x\in \mathbb{Q}$ de forma que $f(x)=y$. Ahora bien, planteando la igualdad $y=\frac{1}3(2x+1)$, y despejando, obtenemos que $x=\frac{3y-1}2$, que es racional. Esto prueba que $f$ es sobreyectiva. Por tanto, $f$ es biyectiva.

De cómo hemos demostrado la sobreyectividad, se sigue que $f^{-1}(y)=\frac{1}2(3y-1)$.
:::


------------------------------------------------------------------------

[Esta página está basada en los apuntes de J.C. Rosales y P. A. García-Sánchez, [Notas de Álgebra Lineal y Estructuras Matemáticas](https://hdl.handle.net/10481/43099) Las representaciones gráficas se han realizado con [JSXGraph](https://jsxgraph.uni-bayreuth.de) y con [viz.js](https://viz-js.com). Las animaciones en JSXGraph y el maquetado de la página han sido realizados por Pedro A. García Sánchez.]{.small}
