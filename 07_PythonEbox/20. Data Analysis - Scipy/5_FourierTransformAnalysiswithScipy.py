import numpy as np
from scipy.fft import fft, ifft

# Input: Get sequence of values from the user
sequence = input("Enter the sequence (comma-separated values): ")

# Convert the input string into a list of numbers
sequence = [float(num) for num in sequence.split(",")]

# Perform Fourier Transform
fourier_transform = fft(sequence)

# Perform Inverse Fourier Transform
inverse_fourier_transform = ifft(fourier_transform)

# Display results
print(f"\nFourier Transform of the sequence: {fourier_transform}")
print(f"Inverse Fourier Transform of the transformed sequence: {inverse_fourier_transform}")   