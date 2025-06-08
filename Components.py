import manim as m
import numpy as np

def GradientBackground(colors=["#19143E", "#2E0C57"], n_colors=100, direction=m.DL):
    background = m.Rectangle(
        width=m.config.frame_width,
        height=m.config.frame_height,
        fill_color=m.color_gradient(colors, n_colors),
        fill_opacity=1,
        stroke_width=0,
        sheen_direction=direction,
    )
    return background