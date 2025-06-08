from manim import *
from Components import GradientBackground

class Test(Scene):
    def construct(self):
        
        background = GradientBackground([BLUE, GREEN])
        self.add(background)

        self.wait(10)