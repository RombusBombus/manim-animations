import manim
import numpy as np

def GradientBackground(colors):
    arr = np.random.randint(0, 256, size=(3, 10, 10), dtype=np.uint8)
    print(arr)
    background = manim.ImageMobject(arr)
    background.height = manim.config.frame_height
    background.width = manim.config.frame_width

    return background