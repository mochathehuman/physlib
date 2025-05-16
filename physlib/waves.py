class Waves:
    @staticmethod
    def wave_speed(frequency, wavelength):
        return frequency * wavelength

    @staticmethod
    def frequency(speed, wavelength):
        return speed / wavelength

    @staticmethod
    def period(frequency):
        return 1 / frequency