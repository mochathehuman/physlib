import math

class RotationalMotion:
    @staticmethod
    def angular_velocity(theta, t):
        return theta / t

    @staticmethod
    def torque(r, F, angle_deg):
        angle_rad = math.radians(angle_deg)
        return r * F * math.sin(angle_rad)

    @staticmethod
    def moment_of_inertia(m, r):
        return m * r ** 2