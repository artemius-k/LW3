
def second_exercise_main() -> None:
    print("\nЗадание 2:")
    initial_list_of_strings = read_from_file()
    russian_list_of_strings = translate_list(initial_list_of_strings)
    write_to_file(russian_list_of_strings)
    print("Выполнено успешно.")


def read_from_file() -> list:
    with open("second_exercise/text_file.txt", "r") as file_to_read:
        return file_to_read.readlines()


def translate_list(list_to_translate: list) -> list:
    translated = [0, 0, 0, 0]
    counter = 0
    for element in list_to_translate:
        parsed_element = element.split()
        if counter == 0:
            parsed_element[0] = "Один"
        elif counter == 1:
            parsed_element[0] = "Два"
        elif counter == 2:
            parsed_element[0] = "Три"
        elif counter == 3:
            parsed_element[0] = "Четыре"
        translated[counter] = str(" ".join(parsed_element))+"\n"
        counter = counter + 1
    return translated


def write_to_file(list_to_write: list) -> None:
    with open("second_exercise/translated.txt", "w") as file_to_write:
        file_to_write.writelines(list_to_write)
