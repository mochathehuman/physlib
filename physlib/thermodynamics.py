class Thermodynamics:
    @staticmethod
    def ideal_gas_pressure(n, T, V, R=8.314):
        return (n * R * T) / V

    @staticmethod
    def heat(q, m, c, delta_T):
        return m * c * delta_T

    @staticmethod
    def efficiency(work_out, heat_in):
        return (work_out / heat_in) * 100