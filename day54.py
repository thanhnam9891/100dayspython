import csv # Imports the csv library

with open("day54totals.csv") as file:
    #reader = csv.reader(file)
    reader = csv.DictReader(file) # Treats the file as a dictionary 
    total = 0
    for row in reader:
        total += float(row["Cost"])*float(row["Quantity"])
        print (row)
    print(f"Total: {total}")

