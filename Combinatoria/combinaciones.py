from manim import *


class DeduccionCombinaciones(Scene):
    def construct(self):
        # 1. TÍTULO E INTRODUCCIÓN
        titulo = Tex("Deducción de la Fórmula de Combinaciones", font_size=40, color=BLUE)
        subtitulo = MathTex(r"\text{Ejemplo: Elegir } k=2 \text{ elementos de un conjunto de } n=5", font_size=32,
                            color=GRAY)
        intro = VGroup(titulo, subtitulo).arrange(DOWN, buff=0.2).to_edge(UP)

        self.play(FadeIn(intro))
        self.wait(1.5)

        # 2. CREACIÓN DE LAS 5 FIGURAS GEOMÉTRICAS
        circulo = Circle(color=RED, fill_opacity=0.6).scale(0.6)
        cuadrado = Square(color=BLUE, fill_opacity=0.6).scale(0.6)
        triangulo = Triangle(color=GREEN, fill_opacity=0.6).scale(0.6)
        pentagono = RegularPolygon(n=5, color=ORANGE, fill_opacity=0.6).scale(0.6)
        hexagono = RegularPolygon(n=6, color=PURPLE, fill_opacity=0.6).scale(0.6)

        figuras = VGroup(circulo, cuadrado, triangulo, pentagono, hexagono)
        figuras.arrange(RIGHT, buff=0.6).move_to(ORIGIN)

        self.play(DrawBorderThenFill(figuras), run_time=2)
        self.wait(1)

        # GUARDAR POSICIONES ORIGINALES
        pos0 = figuras[0].get_center().copy()
        pos1 = figuras[1].get_center().copy()
        pos2 = figuras[2].get_center().copy()
        pos3 = figuras[3].get_center().copy()
        pos4 = figuras[4].get_center().copy()

        # Texto de permutaciones totales
        txt_perm_totales = MathTex(r"\text{Ordenaciones totales de los objetos} = 5! = 120", font_size=34)
        txt_perm_totales.next_to(figuras, UP, buff=0.5)
        self.play(Write(txt_perm_totales))
        self.wait(1)

        # CAMBIO 1: MOSTRAR ALGUNAS PERMUTACIONES DE EJEMPLO (MEZCLAS RÁPIDAS)
        self.play(
            figuras[0].animate.move_to(pos2),
            figuras[1].animate.move_to(pos4),
            figuras[2].animate.move_to(pos0),
            figuras[3].animate.move_to(pos1),
            figuras[4].animate.move_to(pos3),
            run_time=0.6
        )
        self.wait(0.2)
        self.play(
            figuras[0].animate.move_to(pos3),
            figuras[1].animate.move_to(pos1),
            figuras[2].animate.move_to(pos4),
            figuras[3].animate.move_to(pos0),
            figuras[4].animate.move_to(pos2),
            run_time=0.6
        )
        self.wait(0.2)
        # Regresamos al orden original para estructurar la explicación
        self.play(
            figuras[0].animate.move_to(pos0),
            figuras[1].animate.move_to(pos1),
            figuras[2].animate.move_to(pos2),
            figuras[3].animate.move_to(pos3),
            figuras[4].animate.move_to(pos4),
            run_time=0.6
        )
        self.wait(1.5)

        # 3. DIVISIÓN EN SELECCIONADOS Y NO SELECCIONADOS
        linea_div = DashedLine(UP * 1.5, DOWN * 1.5, color=YELLOW).move_to(
            (pos1 + pos2) / 2
        )

        llave_k = Brace(figuras[:2], DOWN, color=RED_B)
        txt_k = MathTex(r"\text{Seleccionados } (k=2)", font_size=28).next_to(llave_k, DOWN, buff=0.2).set_color(RED_B)

        llave_nk = Brace(figuras[2:], DOWN, color=GREEN_B)
        txt_nk = MathTex(r"\text{No seleccionados } (n-k=3)", font_size=28).next_to(llave_nk, DOWN, buff=0.2).set_color(
            GREEN_B)

        self.play(
            Create(linea_div),
            Create(llave_k), Write(txt_k),
            Create(llave_nk), Write(txt_nk)
        )
        self.wait(1.5)

        # 4. DEMOSTRACIÓN DEL SOBRECONTEO (PERMUTACIONES INTERNAS)
        txt_explicacion = Tex(
            "Moverlos internamente no cambia qué objetos fueron elegidos.",
            font_size=30, color=YELLOW
        ).to_edge(DOWN, buff=0.4)

        self.play(Write(txt_explicacion))
        self.wait(1)

        # Intercambio en el grupo K (2! formas)
        self.play(
            figuras[0].animate.move_to(pos1),
            figuras[1].animate.move_to(pos0),
            run_time=1.2
        )

        txt_rep_k = MathTex(r"k! = 2! = 2 \text{ formas de ordenar los elegidos}", font_size=30).next_to(txt_k, DOWN,
                                                                                                         buff=0.4).set_color(
            RED_B)
        self.play(Write(txt_rep_k))
        self.wait(2)

        # CAMBIO 3: DESAPARECER EL TEXTO DE LOS ELEGIDOS PARA EVITAR SOLAPAMIENTOS
        self.play(FadeOut(txt_rep_k))

        # CAMBIO 2: MOSTRAR LAS 6 PERMUTACIONES (3!) DE LOS NO ELEGIDOS
        # Definimos las posiciones secuenciales para recorrer los 6 órdenes posibles de las 3 figuras de la derecha
        perm_orders = [
            (pos2, pos4, pos3),  # Orden 2
            (pos3, pos2, pos4),  # Orden 3
            (pos3, pos4, pos2),  # Orden 4
            (pos4, pos2, pos3),  # Orden 5
            (pos4, pos3, pos2),  # Orden 6
            (pos2, pos3, pos4)  # Regreso al estado base
        ]

        for p2, p3, p4 in perm_orders:
            self.play(
                figuras[2].animate.move_to(p2),
                figuras[3].animate.move_to(p3),
                figuras[4].animate.move_to(p4),
                run_time=0.5
            )

        txt_rep_nk = MathTex(r"(n-k)! = 3! = 6 \text{ formas de ordenar los no elegidos}", font_size=30).next_to(txt_nk,
                                                                                                                 DOWN,
                                                                                                                 buff=0.4).set_color(
            GREEN_B)
        self.play(Write(txt_rep_nk))
        self.wait(2)

        # 5. PRINCIPIO MULTIPLICATIVO Y CONCLUSIÓN FORMAL
        self.play(FadeOut(txt_explicacion), FadeOut(txt_perm_totales))

        txt_multiplicacion = MathTex(
            r"\text{Cada combinación se repite exactamente: } 2! \times 3! = 12 \text{ veces}",
            font_size=34, color=YELLOW
        ).to_edge(DOWN, buff=1.2)

        self.play(Write(txt_multiplicacion))
        self.wait(3)

        # Limpieza de pantalla (txt_rep_k ya no está, así que no lo incluimos)
        self.play(
            FadeOut(figuras), FadeOut(linea_div),
            FadeOut(llave_k), FadeOut(txt_k),
            FadeOut(llave_nk), FadeOut(txt_nk),
            FadeOut(txt_rep_nk),
            FadeOut(txt_multiplicacion),
            FadeOut(intro)
        )

        # Ajuste matemático final
        formula_ejemplo = MathTex(
            r"\text{Combinaciones } (n=5, k=2) = \frac{5!}{2! \times 3!} = \frac{120}{2 \times 6} = 10",
            font_size=38
        ).move_to(UP * 1)

        formula_general = MathTex(
            r"C_n^k = \binom{n}{k} = \frac{n!}{k!(n-k)!}",
            font_size=48, color=BLUE
        ).move_to(DOWN * 1)

        recuadro = SurroundingRectangle(formula_general, color=YELLOW, buff=0.4)

        self.play(Write(formula_ejemplo))
        self.wait(2)
        self.play(Write(formula_general))
        self.play(Create(recuadro))
        self.wait(4)