import numpy as np
from utils import input_matrix

def run():
    print("\nОперації над матрицями:")

    # Введення першої матриці
    print("Введіть першу матрицю (A):")
    A = input_matrix()
    if A is None:
        print("Помилка введення матриці.")
        return
    A = np.array(A)

    # Введення другої матриці
    print("Введіть другу матрицю (B):")
    B = input_matrix()
    if B is None:
        print("Помилка введення матриці.")
        return
    B = np.array(B)

    # Операції
    print("\nРезультати:")
    try:
        print("A + B:")
        print(A + B)
        print("\nA - B:")
        print(A - B)
        print("\nA * B (множення):")
        print(np.dot(A, B))
        print("\nТранспонування A:")
        print(A.T)
    except ValueError as e:
        print(f"Помилка при операціях: {e}")
