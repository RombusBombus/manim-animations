from manim import *

class ThreeDCameraRotation(ThreeDScene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-3, 3],
            x_length=6,
            y_length=6,
            axis_config={"color": BLUE},
        )

        self.add(axes)

        graph = axes.plot(lambda x: np.sin(x), color=YELLOW)

        self.play(Create(graph))

        # Create a tangent line at a specific point
        # move the point and the tangent line to the right
        tangent_line = axes.get_tangent_line(graph, 1, color=RED)
        self.play(Create(tangent_line))
        self.play(tangent_line.animate.shift(RIGHT * 2))