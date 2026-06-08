from manim import *


class CombinacionesRepeticion(Scene):
    def construct(self):
        # 1. TÍTULO E INTRODUCCIÓN
        titulo = Tex("Combinaciones con Repetición", font_size=40, color=BLUE)
        subtitulo = Tex("Barras y Estrellas (Stars and Bars)", font_size=32, color=GRAY)
        intro = VGroup(titulo, subtitulo).arrange(DOWN, buff=0.2).to_edge(UP)

        self.play(FadeIn(intro))
        self.wait(1)

        txt_ejemplo = MathTex(
            r"\text{Ejemplo: Formar conjuntos de } k=6 \text{ objetos usando } n=3 \text{ clases distintos}",
            font_size=30, color=YELLOW)
        txt_ejemplo.next_to(intro, DOWN, buff=0.2)
        self.play(Write(txt_ejemplo))
        self.wait(1.5)

        # Función auxiliar para generar estrellas homogéneas
        def crear_estrella():
            return Star(n=5, outer_radius=0.2, inner_radius=0.08, color=YELLOW, fill_opacity=1, stroke_width=1)

        # 2. DEFINICIÓN DE LAS CAJAS
        cajas = VGroup(*[
            Rectangle(width=2.0, height=1.6, color=BLUE, stroke_width=3)
            for _ in range(3)
        ]).arrange(RIGHT, buff=0.8).move_to(ORIGIN)

        etiquetas_cajas = VGroup(*[
            Tex(f"Clase {i + 1}", font_size=26, color=BLUE_A).next_to(cajas[i], UP, buff=0.1)
            for i in range(3)
        ])

        self.play(Create(cajas), Write(etiquetas_cajas))
        self.wait(1)

        # --- ASIGNACIÓN 1: [4, 2, 0] ---
        txt_explicativo = Tex("Veamos distintas asignaciones posibles...", font_size=28, color=GREEN).to_edge(DOWN,
                                                                                                              buff=0.6)
        self.play(Write(txt_explicativo))

        c0, c1, c2 = cajas[0].get_center(), cajas[1].get_center(), cajas[2].get_center()

        estrellas_config1 = VGroup(
            crear_estrella().move_to(c0 + np.array([-0.4, 0.3, 0])),
            crear_estrella().move_to(c0 + np.array([0.4, 0.3, 0])),
            crear_estrella().move_to(c0 + np.array([-0.4, -0.3, 0])),
            crear_estrella().move_to(c0 + np.array([0.4, -0.3, 0])),
            crear_estrella().move_to(c1 + np.array([-0.3, 0, 0])),
            crear_estrella().move_to(c1 + np.array([0.3, 0, 0]))
        )
        txt_info1 = MathTex(r"\text{Asignación 1: } 4 \text{ de Clase 1, } 2 \text{ de Clase 2, } 0 \text{ de Clase 3}",
                            font_size=28).to_edge(DOWN, buff=1.2)

        self.play(FadeIn(estrellas_config1), Transform(txt_explicativo, txt_info1))
        self.wait(2.5)

        # --- ASIGNACIÓN 2: [0, 0, 6] ---
        estrellas_config2 = VGroup(
            crear_estrella().move_to(c2 + np.array([-0.4, 0.3, 0])),
            crear_estrella().move_to(c2 + np.array([0, 0.3, 0])),
            crear_estrella().move_to(c2 + np.array([0.4, 0.3, 0])),
            crear_estrella().move_to(c2 + np.array([-0.4, -0.3, 0])),
            crear_estrella().move_to(c2 + np.array([0, -0.3, 0])),
            crear_estrella().move_to(c2 + np.array([0.4, -0.3, 0]))
        )
        txt_info2 = MathTex(
            r"\text{Asignación 2: } 0 \text{ de Clase 1, } 0 \text{ de Clase 2, } 6 \text{ de Clase 3 (Todas iguales)}",
            font_size=28).to_edge(DOWN, buff=1.2)

        self.play(Transform(estrellas_config1, estrellas_config2), Transform(txt_explicativo, txt_info2))
        self.wait(2.5)

        # --- ASIGNACIÓN 3: [2, 2, 2] (De aquí haremos la transición lineal) ---
        estrellas_config3 = VGroup(
            crear_estrella().move_to(c0 + np.array([-0.3, 0, 0])), crear_estrella().move_to(c0 + np.array([0.3, 0, 0])),
            crear_estrella().move_to(c1 + np.array([-0.3, 0, 0])), crear_estrella().move_to(c1 + np.array([0.3, 0, 0])),
            crear_estrella().move_to(c2 + np.array([-0.3, 0, 0])), crear_estrella().move_to(c2 + np.array([0.3, 0, 0]))
        )
        txt_info3 = MathTex(r"\text{Asignación 3: } 2 \text{ de Clase 1, } 2 \text{ de Clase 2, } 2 \text{ de Clase 3}",
                            font_size=28).to_edge(DOWN, buff=1.2)

        self.play(Transform(estrellas_config1, estrellas_config3), Transform(txt_explicativo, txt_info3))
        self.wait(2.5)

        # 3. TRANSICIÓN A REPRESENTACIÓN LINEAL
        # Creamos las dos barras físicas intermedias
        barra1 = Line(UP * 0.5, DOWN * 0.5, color=WHITE, stroke_width=4).move_to((c0 + c1) / 2)
        barra2 = Line(UP * 0.5, DOWN * 0.5, color=WHITE, stroke_width=4).move_to((c1 + c2) / 2)
        barras = VGroup(barra1, barra2)

        txt_lineal_info = Tex("Transformamos las paredes divisorias en barras lineales", font_size=28,
                              color=YELLOW).to_edge(DOWN, buff=1.2)

        # Desvanecemos contenedores externos y dejamos las estrellas del estado 3 + barras
        self.play(
            FadeOut(cajas), FadeOut(etiquetas_cajas),
            Create(barras), Transform(txt_explicativo, txt_lineal_info)
        )
        self.wait(1)

        # Estructuramos la cadena lineal exacta para la configuración [2, 2, 2] -> (E, E, B, E, E, B, E, E)
        cadena_lineal = VGroup(
            estrellas_config1[0], estrellas_config1[1],
            barra1,
            estrellas_config1[2], estrellas_config1[3],
            barra2,
            estrellas_config1[4], estrellas_config1[5]
        )

        self.play(cadena_lineal.animate.arrange(RIGHT, buff=0.4).move_to(ORIGIN))
        self.wait(2)

        # 4. COLOCACIÓN EN CASILLAS (SLOTS)
        self.play(FadeOut(txt_explicativo), FadeOut(txt_ejemplo))

        # Creamos 8 casillas cuadradas tenues
        slots = VGroup(*[
            Square(side_length=0.8, color=GRAY_B, stroke_opacity=0.5)
            for _ in range(8)
        ]).arrange(RIGHT, buff=0.2).move_to(ORIGIN)

        # Numeración superior de las casillas
        numeros_slots = VGroup(*[
            Integer(i + 1, font_size=20, color=GRAY).next_to(slots[i], UP, buff=0.1)
            for i in range(8)
        ])

        txt_slots = MathTex(
            r"\text{Cadenas de longitud fija: } k + (n-1) = 6 \text{ estrellas} + 2 \text{ barras} = 8 \text{ posiciones}",
            font_size=28
        ).to_edge(UP, buff=2.2)

        self.play(Create(slots), Write(numeros_slots), Write(txt_slots))

        # Acomodamos los elementos de la asignación actual dentro de las casillas
        indices_config3 = [0, 1, 2, 3, 4, 5, 6, 7]  # 0,1=E; 2=B; 3,4=E; 5=B; 6,7=E
        self.play(
            estrellas_config1[0].animate.move_to(slots[0].get_center()),
            estrellas_config1[1].animate.move_to(slots[1].get_center()),
            barra1.animate.move_to(slots[2].get_center()),
            estrellas_config1[2].animate.move_to(slots[3].get_center()),
            estrellas_config1[3].animate.move_to(slots[4].get_center()),
            barra2.animate.move_to(slots[5].get_center()),
            estrellas_config1[4].animate.move_to(slots[6].get_center()),
            estrellas_config1[5].animate.move_to(slots[7].get_center()),
            run_time=1.5
        )
        self.wait(1.5)

        # Señalar las posiciones elegidas para estrellas en ROJO
        txt_elegir = Tex("Basta con elegir cuáles posiciones serán para las estrellas.", font_size=28,
                         color=RED_B).to_edge(DOWN, buff=1.2)
        casillas_rojas1 = VGroup(*[slots[i] for i in [0, 1, 3, 4, 6, 7]])

        self.play(casillas_rojas1.animate.set_color(RED), Write(txt_elegir))
        self.wait(2.5)

        # 5. SEGUNDA ELECCIÓN (DEMOSTRACIÓN DE DINÁMICA)
        txt_otra_eleccion = Tex("Si elegimos otra combinación de posiciones (ej. 1, 2, 4, 5, 6, 8)...", font_size=28,
                                color=ORANGE).to_edge(DOWN, buff=1.2)

        # Revertimos color anterior de casillas
        self.play(casillas_rojas1.animate.set_color(GRAY_B), Transform(txt_elegir, txt_otra_eleccion))

        # Coloreamos las nuevas posiciones elegidas para estrellas: 0, 1, 3, 4, 5, 7
        casillas_rojas2 = VGroup(*[slots[i] for i in [0, 1, 3, 4, 5, 7]])
        self.play(casillas_rojas2.animate.set_color(ORANGE))
        self.wait(1)

        # Movemos físicamente los elementos a sus nuevas posiciones correspondientes:
        # Estrellas van a 0, 1, 3, 4, 5, 7. Barras se ven forzadas a ir a 2 y 6.
        # Esto genera la combinación: E, E, B, E, E, E, B, E -> [2, 3, 1]
        self.play(
            estrellas_config1[0].animate.move_to(slots[0].get_center()),
            estrellas_config1[1].animate.move_to(slots[1].get_center()),
            barra1.animate.move_to(slots[2].get_center()),
            estrellas_config1[2].animate.move_to(slots[3].get_center()),
            estrellas_config1[3].animate.move_to(slots[4].get_center()),
            estrellas_config1[4].animate.move_to(slots[5].get_center()),
            barra2.animate.move_to(slots[6].get_center()),
            estrellas_config1[5].animate.move_to(slots[7].get_center()),
            run_time=2
        )

        txt_nueva_config = MathTex(r"\text{¡Automáticamente se genera otra asignación válida! } (2, 3, 1)",
                                   font_size=28, color=YELLOW).to_edge(DOWN, buff=0.5)
        self.play(Write(txt_nueva_config))
        self.wait(3)

        # 6. CONCLUSIÓN FORMAL AMPLIADA
        self.play(
            FadeOut(slots), FadeOut(numeros_slots), FadeOut(estrellas_config1), FadeOut(barras),
            FadeOut(txt_slots), FadeOut(txt_elegir), FadeOut(txt_nueva_config), FadeOut(intro)
        )

        txt_conclusion_pedagogica = Tex(
            "Por tanto, el problema consiste en elegir $k=6$ posiciones de un total de $8$ disponibles.\\\\"
            "Como las posiciones elegidas reciben estrellas indistinguibles y no importa el orden,\\\\"
            "estamos ante un caso puro de \\textbf{Combinaciones Sin Repetición} de tamaño 6 sobre 8 objetos.",
            font_size=28, color=WHITE
        ).move_to(UP * 1.2)

        self.play(Write(txt_conclusion_pedagogica), run_time=4)
        self.wait(2)

        formula_ejemplo = MathTex(
            r"CR_{3}^{6} = C_{3 + 6 - 1}^{6} = C_{8}^{6} = \binom{8}{6} = 28",
            font_size=38, color=YELLOW
        ).next_to(txt_conclusion_pedagogica, DOWN, buff=0.6)

        formula_general = MathTex(
            r"{CR}_{n}^k = C_{n + k - 1}^k = \binom{n + k - 1}{k}",
            font_size=44, color=BLUE
        ).next_to(formula_ejemplo, DOWN, buff=0.5)

        recuadro = SurroundingRectangle(formula_general, color=YELLOW, buff=0.3)

        self.play(Write(formula_ejemplo))
        self.wait(1.5)
        self.play(Write(formula_general))
        self.play(Create(recuadro))
        self.wait(4)