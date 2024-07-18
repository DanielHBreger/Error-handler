class measurements:
    """Measurements class for handling measurements"""

    def __init__(
        self, measurement: float, error_value: float = 0, error_range: float = 0
    ) -> None:
        """Create new measurement

        Args:
            measurement (float): value measured
            error_value (float, optional): error from instrument to multiply by value recorded. Defaults to 0.
            error_range (float, optional): error from instrument according to the recording range. Defaults to 0.
        """
        self.value = measurement
        self.error = error(error_value, error_range)

    def get_error_txt(self) -> str:
        return f"{self.error.tostring()}"
    
    def value(self):
        return self.value

    class error:
        """Error class for handling measurement errors and their propagation"""

        def __init__(self, measurement, error_value: float = 0, error_range: float = 0) -> None:
            self.error_value = error_value
            self.error_range = error_range
            self.measurement = measurement

        def mult_const(self, const: float):
            return const * self.value

        def pow(self, other_measurement, power: float):
            return self.measurement.value() * (power * (other_measurement.error()/other_measurement.value()))

        @classmethod
        def from_errors(cls, errors: list):
            pass

        def tostring(self) -> str:
            return f"{self.error_value}x+-{self.error_range}"

        def value(self, measurement: float = 0) -> float:
            return self.error_value * measurement + self.error_range
