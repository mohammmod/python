from preparator import Preparator
from painter import Painter

height = Preparator().get_height_in_range(0, 24)
Painter().draw_the_pyramid(height)

