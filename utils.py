def input_matrix():
    """
    Введення матриці користувачем.
    """
    try:
        rows = int(input("Введіть кількість рядків матриці: "))
        cols = int(input("Введіть кількість стовпців матриці: "))
        print("Введіть елементи матриці (кожний рядок вводьте через пробіл):")
        matrix = []
        for i in range(rows):
            row = list(map(float, input(f"Рядок {i + 1}: ").strip().split()))
            if len(row) != cols:
                print("Помилка: кількість елементів у рядку не відповідає кількості стовпців.")
                return None
            matrix.append(row)
        return matrix
    except ValueError:
        print("Помилка: введіть коректні числа.")
        return None

def input_vector(size):
    """
    Введення вектора користувачем.
    """
    try:
        print("Введіть елементи вектора через пробіл:")
        vector = list(map(float, input().strip().split()))
        if len(vector) != size:
            print(f"Помилка: вектор має містити {size} елементів.")
            return None
        return vector
    except ValueError:
        print("Помилка: введіть коректні числа.")
        return None
