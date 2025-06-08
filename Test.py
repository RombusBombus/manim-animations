from manim import *
from Components import GradientBackground


class Test(Scene):
    def construct(self):

        # add background
        background = GradientBackground(n_colors=10)
        self.add(background)
        self.play(
            FadeIn(background, run_time=2, rate_func=linear),
        )

        self.wait(10)
