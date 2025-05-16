class Dynamics:
    @staticmethod
    def force(m, a):
        return m * a

    @staticmethod
    def weight(m, g=9.81):
        return m * g