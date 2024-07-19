from numpy import sqrt as np_sqrt, log as np_log, e as np_e


class meas:
    """Measurements class for handling measurements"""

    def __init__(
        self,
        measurement: float,
        error_value: float = 0,
        error_range: float = 0,
        override_error: float = None,
    ) -> None:
        """Create new measurement

        Args:
            measurement (float): value measured
            error_value (float, optional): error from instrument to multiply by value recorded. Defaults to 0.
            error_range (float, optional): error from instrument according to the recording range. Defaults to 0.
        """
        self.value = measurement
        if not override_error:
            self.err = error_value * measurement + error_range
        else:
            self.err = override_error

    def tostring(self):
        return f"{self.value} +- {self.err}"

    def get_error_txt(self) -> str:
        return f"{self.err}"

    def __pow__(self, power: float):
        new_val = self.value**power
        new_err = new_val * power * (self.err / self.value)
        return meas(new_val, override_error=new_err)

    def ln(self):
        new_val = np_log(self.value)
        new_err = self.err / self.value
        return meas(new_val, override_error=new_err)

    def exp(self):
        new_val = np_e**self.value
        new_err = new_val * self.err
        return meas(new_val, override_error=new_err)

    def __add__(self, other_meas):
        new_val = self.value + other_meas.value
        new_err = np_sqrt(self.err**2 + other_meas.err**2)
        return meas(new_val, override_error=new_err)

    def __sub__(self, other_meas):
        new_val = self.value - other_meas.value
        new_err = np_sqrt(self.err**2 + other_meas.err**2)
        return meas(new_val, override_error=new_err)

    def __mul__(self, other_meas):
        match other_meas:
            case float() | int():
                new_err = self.err * other_meas
                new_val = self.value * other_meas
            case meas():
                new_val = self.value * other_meas.value
                new_err = new_val * np_sqrt(
                    (self.err / self.value) ** 2
                    + (other_meas.err / other_meas.value) ** 2
                )
        return meas(new_val, override_error=new_err)

    __rmul__ = __mul__

    def __truediv__(self, other_meas):
        match other_meas:
            case float() | int():
                new_err = self.err / other_meas
                new_val = self.value / other_meas
            case meas():
                new_val = self.value / other_meas.value
                new_err = new_val * np_sqrt(
                    (self.err / self.value) ** 2
                    + (other_meas.err / other_meas.value) ** 2
                )
        return meas(new_val, override_error=new_err)