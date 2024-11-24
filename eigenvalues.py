import numpy as np
from utils import input_matrix

def run():
    print("\nВласні значення і вектори:")

    # Введення матриці
    print("Введіть квадратну матрицю:")
    A = input_matrix()
    if A is None or len(A) != len(A[0]):
        print("Помилка: матриця повинна бути квадратною.")
        return
    A = np.array(A)

    # Обчислення власних значень і векторів
    eigenvalues, eigenvectors = np.linalg.eig(A)

    print("\nМатриця A:")
    print(A)
    print("\nВласні значення:")
    print(eigenvalues)
    print("\nВласні вектори:")
    print(eigenvectors)
