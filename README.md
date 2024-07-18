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

# Credits

Made by Daniel Breger, 2024.
