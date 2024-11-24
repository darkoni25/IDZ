import solve_linear_system
import matrix_operations
import eigenvalues

def main():
    while True:
        print("\nЛінійна алгебра: виберіть задачу")
        print("1. Розв'язання системи лінійних рівнянь")
        print("2. Операції над матрицями")
        print("3. Власні значення і вектори")
        print("0. Вихід")

        choice = input("Ваш вибір: ").strip()

        if choice == "1":
            solve_linear_system.run()
        elif choice == "2":
            matrix_operations.run()
        elif choice == "3":
            eigenvalues.run()
        elif choice == "0":
            print("Програма завершена.")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
