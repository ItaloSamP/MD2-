def gcd(a, b):
    """Calcula o MDC de dois números muito grandes e mostra os restos intermediários."""
    print(f"Calculando MDC({a}, {b})")
    steps = 0
    while b != 0:
        resto = a % b
        steps += 1
        print(f"Passo {steps}: {a} = {a//b} * {b} + {resto}")
        a, b = b, resto
    print(f"\nO MDC é: {a}")
    print(f"Total de passos: {steps}")
    return a

# Números de exemplo muito grandes (mais de 20 dígitos)
num1 = 9742867231360457281220952
num2 = 2825240788613971993199718

# Calcular o MDC
gcd(num1, num2)
