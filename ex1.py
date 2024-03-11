# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
from datetime import datetime

def load_people(file_name):
    with open(file_name, "r") as f:
        return json.load(f)

def save_people(file_name, people_list):
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(people_list, f, ensure_ascii=False, indent=4)

def get_person():
    """
    Запросить данные о человеке.
    """
    person = {}
    person["surname"] = input("Введите фамилию: ")
    person["name"] = input("Введите имя: ")
    person["zodiac"] = input("Введите знак зодиака: ")
    person["birthday"] = input("Дата рождения (число.месяц.год):").split(".")
    return person


def display_people(people):
    """
    Отобразить список людей.
    """
    if people:
        line = "+-{}-+-{}-+-{}-+-{}-+-{}-+".format(
            "-" * 4, "-" * 30, "-" * 30, "-" * 20, "-" * 20
        )
        print(line)
        print(
            "| {:^4} | {:^30} | {:^30} | {:^20} | {:^20} |".format(
                "№", "Фамилия", "Имя", "Знак зодиака", "Дата рождения"
            )
        )
        print(line)

        for idx, person in enumerate(people, 1):
            print(
                "| {:>4} | {:<30} | {:<30} | {:<20} | {:>20} |".format(
                    idx,
                    person.get("surname", ""),
                    person.get("name", ""),
                    person.get("zodiac", ""),
                    ".".join(person.get("birthday", "")),
                )
            )
        print(line)
    else:
        print("Список пуст")


def select_people(surname, people):
    """
    Выбрать людей с заданной фамилией.
    """
    result = []
    for i in people:
        if i.get("surname", "") == surname:
            result.append(i)
    return result


def get_instructions():
    print("add - добавление нового человека;")
    print("info - данные о человеке по его фамилии;")
    print("exti - завершение программы;")
    print("list - вывод информации о всех людях;")
    print("load - загрузить данные из файла;")
    print("save - сохранить данные в файл;")


def main():
    """
    Главная функция программы.
    """
    people = []

    while True:
        command = input("Введите команду (add, info, list, load, save, exit, help): ").strip().lower().split(maxsplit=1)

        match command[0]:
            case "exit":
                break
            
            case "load":
                file_name = command[1]
                people = load_people(file_name)

            case "save":
                file_name = command[1]
                save_people(file_name, people)

            case "add":
                person = get_person()
                people.append(person)
                people.sort(
                    key=lambda x: datetime.strptime(".".join(x["birthday"]), "%d.%m.%Y")
                )

            case "info":
                surname = input("Введите фамилию: ")
                selected = select_people(surname, people)
                display_people(selected)

            case "list":
                display_people(people)

            case "help":
                get_instructions()

            case _:
                print(f"Неизвестная команда {command[0]}", file=sys.stderr)

if __name__ == "__main__":
    main()