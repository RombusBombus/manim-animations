from manim import *
import argparse
from Components import GradientBackground


config.quality = "fourk_quality"


class TitleCard(Scene):
    def __init__(self, title="Title Card", chapter_number="Chapter 1", **kwargs):
        super().__init__(**kwargs)
        self.title = title
        self.chapter_number = chapter_number

    def construct(self):

        # Add gradient background
        background = GradientBackground(n_colors=10)
        self.add(background)

        # Add the title
        title = Text(self.title, font_size=96)
        self.add(title)

        horizontal_buffer_units = 0.5

        # bottom line
        line_bottom = Line(
            title.get_critical_point(LEFT) + horizontal_buffer_units * LEFT,
            title.get_critical_point(RIGHT) + horizontal_buffer_units * RIGHT,
        )
        line_bottom.next_to(title, 2.5 * DOWN)

        # chapter number
        number = Tex(self.chapter_number, font_size=72)
        number.next_to(title, 2.5 * UP)

        top_line_left = Line(
            [line_bottom.get_critical_point(LEFT)[0], number.get_y(), 0],
            [number.get_critical_point(LEFT)[0] - 0.2, number.get_y(), 0],
        )
        top_line_right = Line(
            [line_bottom.get_critical_point(RIGHT)[0], number.get_y(), 0],
            [number.get_critical_point(RIGHT)[0] + 0.2, number.get_y(), 0],
        )

        self.add(line_bottom, number, top_line_left, top_line_right)

        self.play(
            Write(title, run_time=2),
            Write(number, run_time=1.5),
            GrowFromCenter(top_line_left, run_time=1.5),
            GrowFromCenter(top_line_right, run_time=1.5),
            GrowFromCenter(line_bottom, run_time=1.5),
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--title",
        type=str,
        default="Title Card",
        help="The title to display on the title card.",
    )
    parser.add_argument(
        "--chapter_number",
        type=str,
        default="Chapter 1",
        help="The chapter number to display on the title card.",
    )

    args = parser.parse_args()
    title = args.title
    chapter_number = args.chapter_number

    scene = TitleCard(title=title, chapter_number=chapter_number)
    scene.render(preview=True)