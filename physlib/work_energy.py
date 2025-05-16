import math

class WorkEnergy:
    @staticmethod
    def work_done(force, displacement, angle_deg=0):
        angle_rad = math.radians(angle_deg)
        return force * displacement * math.cos(angle_rad)

    @staticmethod
    def kinetic_energy(m, v):
        return 0.5 * m * v ** 2

    @staticmethod
    def potential_energy(m, h, g=9.81):
        return m * g * h