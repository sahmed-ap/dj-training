import csv

with open("test_file.csv", "w", newline="", encoding='utf-8') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows([[1, 2, 3, 4, 5, 6]])
    writer.writerows([[7, 8, 9, 10, 11, 12]])
    writer.writerows([[13, 14, 15, 16, 17, 18]])

with open("test_file.csv", "r", newline="", encoding='utf-8') as csvFile:
    reader = csv.reader(csvFile)
    data = list(reader)
    print("Data written in file")
    for row in data:
        print(row)
