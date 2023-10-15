
def first_exercise_main() -> None:
    print("\nЗадание 1:")
    write_file()
    copy_one_file_to_another()
    print("Выполнено успешно.")


def write_file() -> None:
    initial_file = open("first_exercise/first.txt", "w")
    print("Введите сохраняемую в файл информацию (ввод прекратится после двойного нажатия на 'Enter'):")
    user_input = "\n".join(iter(input, ""))
    initial_file.writelines(user_input)
    initial_file.close()


def copy_one_file_to_another() -> None:
    with open("first_exercise/first.txt", "r") as copying:
        newfile = open("first_exercise/second.txt", "w")
        string_list = copying.readlines()
        for element in string_list:
            element = element.lower()
            parsed_element = element.split()
            for i in range(len(parsed_element)):
                counter = parsed_element.count(parsed_element[i])
                if counter >= 2:
                    newfile.write(element)
                    break
        newfile.close()
