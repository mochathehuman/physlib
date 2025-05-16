import math

class Kinematics:
    @staticmethod
    def final_velocity(u, a, t):
        return u + a * t
    
    @staticmethod
    def displacement(u, a, t):
        return u * t + 0.5 * a * t ** 2

    @staticmethod
    def final_velocity2(u, a, s):
        return math.sqrt(u**2 + 2 * a * s)