
def third_exercise_menu() -> None:
    print("\nЗадание 3:")
    studies = read_from_file("third_exercise/studies.txt")
    convert_to_dictionary_and_print(studies)
    print("Выполнено успешно.")


def read_from_file(filename: str) -> list:
    with open(filename, "r") as file_to_read:
        return file_to_read.readlines()


def convert_to_dictionary_and_print(studies: list) -> None:
    dictionary = dict()
    complete_hours = int()
    for string in studies:
        parsed_string = string.split()
        for i in range(len(parsed_string)):
            try:
                complete_hours += int(parsed_string[i])
            except (TypeError, ValueError):
                continue
        dictionary.update({parsed_string[0]:complete_hours})
        complete_hours = 0
    print(f"Конечный словарь: {dictionary}")
