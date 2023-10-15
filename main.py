
def main() -> None:
    main_menu()
    choice = 0
    while True:
        try:
            choice = int(input("Ввод: "))
            break
        except (TypeError, ValueError):
            print("Неверный ввод, повторите попытку:", end=" ")
            continue
    if choice == 0:
        return


def main_menu() -> None:
    print("Главное меню:\n"
          "1. Копирование содержимого файлов\n"
          "2. Считывание файла и замена вывода\n"
          "3. Учебные предметы\n"
          "0. Выход\n")