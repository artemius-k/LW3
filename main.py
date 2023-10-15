import first_exercise.first_exercise as first
import second_exercise.second_exercise as second


def main() -> None:
    while True:
        print_main_menu()
        choice = 0
        while True:
            try:
                choice = int(input("Ввод: "))
                break
            except (TypeError, ValueError):
                print("Неверный ввод, повторите попытку:", end=" ")
                continue
        if choice == 0:
            break
        elif choice == 1:
            first.first_exercise_main()
        elif choice == 2:
            second.second_exercise_main()


def print_main_menu() -> None:
    print("Главное меню:\n"
          "1. Копирование содержимого файлов\n"
          "2. Считывание файла и замена вывода\n"
          "3. Учебные предметы\n"
          "0. Выход\n")


main()
