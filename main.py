from manim import *

class ThreeDCameraRotation(ThreeDScene):
    def construct(self):
        text1 = MathTex(r"m \ddot{x} = -k x")
        text2 = MathTex(r"i \hbar \frac{\partial}{\partial t} \Psi = \hat{H} \Psi")
        
        # align the texts
        text1.move_to(UP * 1)
        text2.move_to(DOWN * 1)
        
        self.play(
            Write(text1),
            Write(text2),
            run_time=2
        )

        self.wait(1)

        self.play(
            Unwrite(text1),
            Unwrite(text2),
            run_time=5
        )

        # Create 3d axes
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-3, 3, 1],
            axis_config={"color": BLUE}
        )

        self.set_camera_orientation(
            phi=45 * DEGREES,
            theta=55 * DEGREES,
            distance=20,
        )

        self.play(
            Create(axes),
            run_time=1
        )

        self.wait(1)

        def surface_function(x, y):
            return np.array([x, y, np.sin(x) * np.cos(y)])
        
        surface = Surface(
            surface_function,
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(30, 30),
            fill_color=YELLOW,
            fill_opacity=0.7
        )

        self.play(
            Create(surface),
        )

        self.wait(1)
