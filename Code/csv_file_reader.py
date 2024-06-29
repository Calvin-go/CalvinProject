# csv_file_reader.py
import csv

def read_csv(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(', '.join(row))

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    read_csv(filename)
