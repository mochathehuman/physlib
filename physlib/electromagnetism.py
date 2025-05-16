class Electromagnetism:
    @staticmethod
    def ohms_law(V=None, I=None, R=None):
        if V is None:
            return I * R
        elif I is None:
            return V / R
        elif R is None:
            return V / I

    @staticmethod
    def electric_power(V, I):
        return V * I

    @staticmethod
    def coulomb_force(q1, q2, r, k=8.9875517923e9):
        return k * q1 * q2 / r ** 2