from scipy.special import exp10, sindg, cosdg

# Input for exponent value
exponent_value = float(input("Enter the exponent value: "))
print(f"10 raised to the power of {int(exponent_value)} : {exp10(exponent_value)}")

# Input for the angle in degrees
angle = float(input("Enter the angle in degrees: "))
print(f"Sine of {angle} degrees: {sindg(angle)}")
print(f"Cosine of {angle} degrees: {cosdg(angle)}")
