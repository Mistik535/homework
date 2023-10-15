# Написать произвольную простую (без вложенностей) схему Pydatic
# 1. Написать класс метод from_csv принимающий объект file (csv), и возвращающий список
# экземпляров схемы заполненных на основании этого файла
# 2. Написать метод объекта to_csv принимающий объект файла (сsv) и дозаписывающий\записывающий информацию
# из схемы в этот сsv файл
from pydantic import BaseModel
import csv


class Model(BaseModel):
    name: str
    surname: str
    age: int

    @classmethod
    def from_csv(cls, file):
        lst = []
        with open(file, "r", encoding="utf-8") as csv_file:
            read_csv = csv.DictReader(csv_file, delimiter=" ", quotechar=",")
            for row in read_csv:
                print(row)
                name = row["name"]
                surname = row["surname"]
                age = int(row["age"])
                exzemplar = cls(name=name, surname=surname, age=age)
                lst.append(exzemplar)
        return lst

    def to_csv(self, file):
        with open(file, "a", encoding="utf-8") as csv_file:
            fields = ["name", "surname", "age"]
            writer = csv.DictWriter(csv_file, fieldnames=fields, delimiter=" ")
            writer.writerow({"name": self.name, "surname": self.surname, "age": self.age})


if __name__ == "__main__":
    data = Model.from_csv("file_test.csv")
    for item in data:
        print(f"name: {item.name}, surname: {item.surname}, age:{item.age}")
    new_exzemplyar = Model(name="vovan", surname="dmitrenko", age=40)
    new_exzemplyar.to_csv("file_test.csv")
