# programa pararealizar la ecuacion cuadratica
import math

def quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return "La ecuación no tiene solución real."
    elif discriminant == 0:
        x = -b / (2*a)
        return f"La solución única es x={x}."
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Las soluciones son x1=x1 y x2=x2."

# output
print(quadratic_equation(1, -3, 2))  # Debería imprimir "Las soluciones son x1=2.0 y x2=1.0."