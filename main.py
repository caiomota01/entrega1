from mean_var_std import calculate

try:
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # Lista de exemplo
    result = calculate(numbers)
    print("Cálculo realizado com sucesso!")
    print(result)
except ValueError as e:
    print(f"Erro: {e}")
