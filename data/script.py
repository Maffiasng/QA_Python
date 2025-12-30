import csv
import json

class User():
    def __init__(self):
        self.users = []
        self.books = []
        self.result_data = []


    def pars_json(self,filename):
        with open(filename, 'r') as user:
            reader = json.load(user)
            for usr in reader:
                self.users.append({"name":usr["name"],"gender":usr["gender"],"address":usr["address"],"age":usr["age"]})
            return self.users


    def pars_scv(self,filename):
        with open(filename, 'r', newline='') as book:
            reader = csv.DictReader(book)
            for row in reader:
                self.books.append({"title":row["Title"],"author":row["Author"],"pages":int(row["Pages"]),"gender":row["Genre"]})
            return self.books


    def update_users(self):
        if not self.users or not self.books:
            return f"Вернуть если {self.users} и {self.books} пустые"

        count_books = int(len(self.books) / len(self.users))
        remainder_books = int(len(self.books) % len(self.users))

        books_copy = self.books.copy()
        self.result_data = []

        for usr in self.users:
            user_with_books = usr.copy()
            user_with_books["books"] = []

            for i in range(count_books):
                if books_copy:
                    user_with_books["books"].append(books_copy.pop())
            if remainder_books > 0 and books_copy:
                user_with_books["books"].append(books_copy.pop())
                remainder_books -= 1
            self.result_data.append(user_with_books)

        with open('new_list_users.json', 'w') as new_list_users:
            json.dump(self.result_data, new_list_users, indent=10, ensure_ascii=False)

        return self.result_data


x = User()
c = x.pars_json('Путь до файла ')
d = x.pars_scv('Путь до файла')
print(x.update_users())
