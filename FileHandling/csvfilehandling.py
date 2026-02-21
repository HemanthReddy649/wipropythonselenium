import csv
with open("/DataFormats/data.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

        #writing to the csv file

with open("/DataFormats/writecsv.csv", 'w') as file:
    writer=csv.writer(file)
    writer.writerrow(["id","name","marks"])
    writer.writerrow([1, "rahul", 85])
    writer.writerrow([2, "anitha", 90])
