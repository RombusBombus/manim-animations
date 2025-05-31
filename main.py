from manim import *


class ThreeDCameraRotation(ThreeDScene):
    def construct(self):

        square = Square(
            side_length=2.2,
            stroke_width=0,
            fill_color="#00FF22",
            fill_opacity=1,
        )

        text = Text("Buba")
        
        self.add(square, text)

        group = VGroup(square, text)

        self.play(Create(group))

        self.play(
            group.animate.shift(
                UP * 2.5,
            ),
            rate_func=rate_functions.ease_in_bounce,
            run_time=0.5
        )

        self.wait(1)
        
