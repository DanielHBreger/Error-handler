# Error handler
This library is provided to handle measurements and errors for technion labs python code.

#Usage

add measurements.py file to the folder containing your python code and import:

```python
from measurements.py import meas
```

To create a new measurement with a value and two error values (first based on % of reading and second based on % of range):
```python
measurement = meas(value, error_by_value, error_by_range)
```

To create a new measurement with a value and a flat error:
```python
measurement = meas(value, override_error=error_value)
```

# Using measurements

Measurements support various mathematical operations:
- Addition
- subtraction
- multiplication
- division
- exponentiation
- natural log
- powers

Just use the objects as regular numbers and the errors will be handled on their own via the formulas relevant for each.

# Examples

```python
meas1 = meas(3.4,0.01,0.5) # 3.4 measured, 1% error of measured value, 0.5 error calculated for range
meas2 = meas(8,0.02,1) # 8 measured, 2% error of measured value, 1 error calculated for range

sum = meas1 + meas2 # 11.4 +- 1.3
diff = meas1 - meas2 # -4.6 +- 1.3
mult = meas1 * meas2 # 27.2 +- 0.2
divis = meas1 / meas2 # 0.425 +- 0.2
meas_exp = meas1.exp() # 29.96 +- 16.00
meas_ln = meas1.ln() # 1.223 +- 0.157
meas_pow = meas1 ** 2 # 11.56 +- 3.63
```

# TODO

1. Automatically handle significant digits

# Credits

Made by Daniel Breger, 2024.
