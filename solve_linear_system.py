import numpy as np
from utils import input_matrix, input_vector

def run():
    print("\nРозв'язання системи лінійних рівнянь:")

    # Введення матриці коефіцієнтів
    print("Введіть матрицю коефіцієнтів системи:")
    A = input_matrix()
    if A is None:
        print("Помилка введення матриці.")
        return

    # Введення вектора правих частин
    print("Введіть вектор правих частин:")
    B = input_vector(len(A))
    if B is None:
        print("Помилка введення вектора.")
        return

    try:
        # Розв'язок системи
        x = np.linalg.solve(A, B)
        print("Розв'язок:")
        print(x)
    except np.linalg.LinAlgError as e:
        print(f"Помилка при розв'язанні: {e}")
