class Gravitation:
    G = 6.67430e-11

    @staticmethod
    def gravitational_force(m1, m2, r):
        return Gravitation.G * (m1 * m2) / (r ** 2)