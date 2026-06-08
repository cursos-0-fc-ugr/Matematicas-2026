from manim import *


class PrincipioPalomar(Scene):
    def construct(self):
        # 1. Título y textos iniciales
        titulo = Text("El Principio del Palomar", font_size=40).to_edge(UP)
        subtitulo = Text("10 pelotas blancas en 3 cajas", font_size=24, color=GRAY).next_to(titulo, DOWN)
        self.play(Write(titulo), FadeIn(subtitulo))
        self.wait(1)

        # 2. Crear las 3 cajas en pantalla
        # Separadas horizontalmente de forma simétrica
        cajas = VGroup(*[
            Rectangle(width=2.2, height=3, color=BLUE).shift(RIGHT * (i - 1) * 3.5 + DOWN * 0.5)
            for i in range(3)
        ])
        etiquetas_cajas = VGroup(*[
            Text(f"Caja {i + 1}", font_size=20).next_to(cajas[i], DOWN)
            for i in range(3)
        ])

        self.play(Create(cajas), Write(etiquetas_cajas))
        self.wait(0.5)

        # 3. Crear las 10 pelotas blancas ordenadas arriba
        pelotas = VGroup(*[
            Dot(color=WHITE, radius=0.18) for _ in range(10)
        ])
        pelotas.arrange(RIGHT, buff=0.25).move_to(UP * 1.8)
        self.play(FadeIn(pelotas, shift=DOWN))
        self.wait(1)

        # Contador para saber cuántas pelotas tiene cada caja e ir apilándolas
        conteo_cajas = [0, 0, 0]

        # 4. Simulación del reparto equitativo uno a uno
        for i in range(10):
            # Determina a qué caja va mediante el módulo (0, 1, 2, 0, 1...)
            caja_destino = i % 3

            # Calcular la posición exacta dentro de la caja para que queden alineadas
            pos_x = cajas[caja_destino].get_center()[0]
            pos_y = cajas[caja_destino].get_bottom()[1] + 0.4 + (conteo_cajas[caja_destino] * 0.6)

            # Animación de movimiento de la pelota actual
            self.play(
                pelotas[i].animate.move_to([pos_x, pos_y, 0]),
                run_time=0.4
            )
            conteo_cajas[caja_destino] += 1

            # Pausa dramática en la novena pelota para mostrar el equilibrio
            if i == 8:
                texto_alerta = Text("Cada caja tiene exactamente 3 pelotas", font_size=22, color=YELLOW).to_edge(
                    DOWN * 1.5)
                self.play(Write(texto_alerta))
                self.wait(1.5)
                self.play(FadeOut(texto_alerta))

        self.wait(1)

        # 5. Conclusión y demostración del principio
        # Resaltamos la caja 1 que ha recibido la décima pelota
        rect_resaltado = SurroundingRectangle(cajas[0], color=RED, buff=0.15, stroke_width=4)

        formula_mate = MathTex(r"\lceil 10 / 3 \rceil = 4", font_size=36, color=RED).to_edge(DOWN * 2)
        texto_conclusion = Text("¡Por lo tanto, al menos una caja tiene 4 pelotas!", font_size=24, color=RED).next_to(
            formula_mate, DOWN, buff=0.2)

        self.play(Create(rect_resaltado))
        self.play(Write(formula_mate))
        self.play(Write(texto_conclusion))
        self.wait(3)