from manim import *
import argparse

config.background_color = color_gradient(
    [BLUE_E, BLUE_D, BLUE_C, BLUE_B, BLUE_A],
    length_of_output=4
)


class TitleCard(Scene):
    def __init__(self, title="Title Card", chapter_number="Chapter 1", **kwargs):
        super().__init__(**kwargs)
        self.title = title
        self.chapter_number = chapter_number

    def construct(self):

        title = Text(self.title, font_size=96)
        self.add(title)

        horizontal_buffer_units = 0.5

        line_top = Line(
            title.get_critical_point(LEFT) + horizontal_buffer_units * LEFT,
            title.get_critical_point(RIGHT) + horizontal_buffer_units * RIGHT,
        )
        line_top.next_to(title, 2.5 * UP)

        line_bottom = Line(
            title.get_critical_point(LEFT) + horizontal_buffer_units * LEFT,
            title.get_critical_point(RIGHT) + horizontal_buffer_units * RIGHT,
        )
        line_bottom.next_to(title, 2.5 * DOWN)

        number = Tex(self.chapter_number, font_size=72)
        number.move_to(line_top.get_center())
        number.set_z_index(1)

        cover = Rectangle(
            fill_color=BLACK,
            fill_opacity=1,
            width=number.get_width() + 0.7,
            height=0.2,
            stroke_width=0,
        )

        cover.move_to(line_top.get_center())

        self.add(line_top, line_bottom, number, cover)

        self.play(
            Write(title, run_time=2),
            Write(number, run_time=1.5),
            GrowFromCenter(line_top, run_time=1.5),
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