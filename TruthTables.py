from manim import *


class TruthTable(MovingCameraScene):
    def construct(self):

        cells = [
            [
                MathTex(r"\text{A}", font_size=60),
                MathTex(r"\text{B}", font_size=60),
                MathTex(r"\text{A $\land$ B}", font_size=60),
                MathTex(r"\text{A $\lor$ B}", font_size=60),
                MathTex(r"\text{A $\implies$ B}", font_size=60),
                MathTex(r"\text{A $\iff$ B}", font_size=60),
            ],
            [
                MathTex(r"\text{True}", color=RED),
                MathTex(r"\text{True}"),
                MathTex(r"\text{True}", color=GREEN),
                MathTex(r"\text{True}", color=GREEN),
                MathTex(r"\text{True}", color=GREEN),
                MathTex(r"\text{True}", color=GREEN),
            ],
            [
                MathTex(r"\text{True}"),
                MathTex(r"\text{False}"),
                MathTex(r"\text{False}"),
                MathTex(r"\text{True}", color=GREEN),
                MathTex(r"\text{False}"),
                MathTex(r"\text{False}"),
            ],
            [
                MathTex(r"\text{False}"),
                MathTex(r"\text{True}"),
                MathTex(r"\text{False}"),
                MathTex(r"\text{True}", color=GREEN),
                MathTex(r"\text{True}", color=GREEN),
                MathTex(r"\text{False}"),
            ],
            [
                MathTex(r"\text{False}"),
                MathTex(r"\text{False}"),
                MathTex(r"\text{False}"),
                MathTex(r"\text{False}"),
                MathTex(r"\text{True}", color=GREEN),
                MathTex(r"\text{True}", color=GREEN),
            ],
        ]
        table = MobjectTable(cells)

        for row in cells:
            for cell in row:
                if cell.get_tex_string() == r"\text{True}":
                    cell.set_color(GREEN)
                elif cell.get_tex_string() == r"\text{False}":
                    cell.set_color(RED)
                cell.set_opacity(0)

        table.get_horizontal_lines()[0].set_stroke(width=5)

        table.to_edge(LEFT)

        self.play(Create(table), run_time=2)

        # Reveal the cells in the first column
        for i in range(len(cells)):
            self.play(cells[i][0].animate.set_opacity(1), run_time=0.5)

        # Reveal the cells in the second column
        for i in range(len(cells)):
            self.play(cells[i][1].animate.set_opacity(1), run_time=0.5)
        self.wait(2)

        # Reveal the cells in the third column
        for i in range(len(cells)):
            self.play(cells[i][2].animate.set_opacity(1), run_time=0.5)
        self.wait(2)

        # Move the camera over the fourth column
        self.play(self.camera.frame.animate.move_to(table.get_columns()[3].get_center()), run_time=2)
        self.wait(2)

        # Reveal the cells in the fourth column
        for i in range(len(cells)):
            self.play(cells[i][3].animate.set_opacity(1), run_time=0.5)
        self.wait(2)

        self.play(self.camera.frame.animate.move_to(table.get_columns()[4].get_center()), run_time=2)
        self.wait(2)

        # Reveal the cells in the fifth column
        for i in range(len(cells)):
            self.play(cells[i][4].animate.set_opacity(1), run_time=0.5)
        self.wait(2)

        self.play(self.camera.frame.animate.move_to(table.get_columns()[5].get_center()), run_time=2)
        self.wait(2)

        # Reveal the cells in the sixth column
        for i in range(len(cells)):
            self.play(cells[i][5].animate.set_opacity(1), run_time=0.5)
        self.wait(2)

        self.wait(10)
