from manim import *
from Components import GradientBackground

class Test(Scene):
    def construct(self):

        point = Dot(color=WHITE).move_to(ORIGIN)
        self.add(point)

        path = TracedPath(point.get_center, stroke_color=WHITE, stroke_width=2, dissipating_time=0.1)
        self.add(path)

        self.play(
            point.animate.move_to(UP * 2),
            run_time=2,
            rate_func=linear
        )