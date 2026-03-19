import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return math.exp(-x/4) * math.atan(x)

def g(x):
    return math.atan(x) - 4/(x**2 + 1)

def g_diff(x):
    return 1/(x**2 + 1) + 8*x/(x**2 + 1)**2

# Newtons metode
x = 1.0
for i in range(20):
    xn = x - g(x)/g_diff(x)
    print(f'x{i+1} = {xn:.6f}')
    if abs(xn - x) < 1e-8:
        break
    x = xn

x_max = x
y_max = f(x_max)
print(f'\nToppunkt: ({x_max:.4f}, {y_max:.4f})')

# Plot
x_vals = np.linspace(-10, 10, 1000)
y_vals = [math.exp(-xi/4) * math.atan(xi) for xi in x_vals]

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, 'b-', linewidth=2, label=r'$f(x) = e^{-x/4} \cdot \tan^{-1}x$')
plt.plot(x_max, y_max, 'ro', markersize=10, label=f'Toppunkt ({x_max:.4f}, {y_max:.4f})')
plt.axhline(y=0, color='k', linewidth=0.5)
plt.axvline(x=0, color='k', linewidth=0.5)
plt.grid(True, alpha=0.3)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()