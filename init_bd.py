import csv
import os.path

db = []
Phone_book = "Phone_book.csv"


# def init_data_base(file_name='Phone_book.csv'):
#     global db
#     global db_file_name
#     db_file_name = Phone_book
#     if os.path.exists(Phone_book):
#         with open(Phone_book, 'r', encoding="utf-8") as csv_file:
#             reader = csv.reader(csv_file)
#             for i in reader:
#                 db.append(i)
#
#     else:
#         open(db_file_name, 'w', newline='').close()


def import_csv():
   with open("Phone_book.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter = ",")
    for row in file_reader:
            print(f'{row}')


