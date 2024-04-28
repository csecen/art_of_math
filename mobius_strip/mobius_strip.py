# from manim import *
import numpy as np
import manim

BG_COLOR = "#F7F5E7"
manim.config.background_color = BG_COLOR


def new_get_shaded_rgb(
    rgb: np.ndarray,
    point: np.ndarray,
    unit_normal_vect: np.ndarray,
    light_source: np.ndarray,
) -> np.ndarray:
    to_sun = manim.utils.space_ops.normalize(light_source - point)
    factor = 0.5 * np.dot(unit_normal_vect, to_sun) ** 3
    factor = abs(factor)   # This patch will give the same color for a back or front face.
    result = rgb + factor
    return result


manim.camera.three_d_camera.get_shaded_rgb = new_get_shaded_rgb


def mobius_func(u, v):
    x = (1 + v / 2 * np.cos(u / 2)) * np.cos(u)
    y = (1 + v / 2 * np.cos(u / 2)) * np.sin(u)
    z = v / 2 * np.sin(u / 2)
    return np.array((x, y, z))


class Logo(manim.ThreeDScene):
    def construct(self):

        self.set_camera_orientation(
            phi=50 * manim.DEGREES, theta=330 * manim.DEGREES, run_time=2, zoom=2.2
        )

        mobius = manim.Surface(
            mobius_func,
            u_range=[0, 2 * manim.PI],
            v_range=[-1, 1],
            resolution=(64, 16),
        )
        # mobius.set_color(manim.PURPLE_E)
        mobius.set_color("#542c99")
        self.add(mobius)
