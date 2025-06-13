from manim import *
import numpy as np
from scipy.special import sph_harm

class SphericalHarmonicScene(ThreeDScene):
    def construct(self):
        l, m = 3, 2  # harmonic indices

        # Parametric surface: spherical coords
        def param(u, v):
            theta = u * TAU  # azimuth φ
            phi = v * PI     # polar θ

            Y = sph_harm(m, l, theta, phi)  # SciPy convention: sph_harm(m, l, θ, φ) :contentReference[oaicite:2]{index=2}
            r = np.abs(Y)

            # Convert to Cartesian
            x = r * np.sin(phi) * np.cos(theta)
            y = r * np.sin(phi) * np.sin(theta)
            z = r * np.cos(phi)

            # Map phase to hue [0,1)
            hue = (np.angle(Y) + PI) / (2 * PI)
            color = color_gradient([BLUE, RED, YELLOW, GREEN], hue)
            return np.array([x, y, z]), color

        surface = Surface(
            lambda u, v: param(u, v)[0],
            u_range=[0, 1],
            v_range=[0, 1],
            resolution=(50, 50),
            fill_opacity=1.0,
            checkerboard_colors=None,
            # show_wireframe=False,
        )

        # Apply custom shading via shading function
        palette = [BLUE, RED, YELLOW, GREEN]

        def surface_shader(point):
            x, y, z = point
            r = np.linalg.norm(point)
            phi = np.arccos(z / r)
            theta = np.arctan2(y, x) % TAU
            Y = sph_harm(m, l, theta, phi)

            hue = (np.angle(Y) + PI) / (2 * PI)
            # Convert hue to integer index before coloring
            idx = int(hue * (len(palette) - 1))
            return palette[idx]

        surface.set_style(fill_color=WHITE, fill_opacity=1).set_shader(surface_shader)

        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)
        self.add(surface)

        # Animate camera orbit
        self.begin_ambient_camera_rotation(rate=0.1)  # slow rotation
        self.wait(10)
