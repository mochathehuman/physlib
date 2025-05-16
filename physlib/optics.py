import math

class Optics:
    @staticmethod
    def snells_law(n1, n2, theta1_deg):
        theta1_rad = math.radians(theta1_deg)
        sin_theta2 = n1 * math.sin(theta1_rad) / n2
        return math.degrees(math.asin(sin_theta2))

    @staticmethod
    def mirror_equation(f, d_o):
        return 1 / ((1 / f) - (1 / d_o))

    @staticmethod
    def lens_magnification(h_i, h_o):
        return h_i / h_o