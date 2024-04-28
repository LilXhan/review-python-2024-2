from io import open
import csv
import os

# write

with open("archivo/text.csv", "w") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["tweet_id", "user_id", "text"])
    writer.writerow([15, 1, "tweet"])
    writer.writerow([25, 2, "other tweet"])


# read

with open("archivo/text.csv") as archivo:
    reader = csv.reader(archivo)
    print(list(reader))
    archivo.seek(0)
    for line in reader:
        print(line)

# modified

with open("archivo/text.csv") as r, open("archivo/archivo_temp.csv", "w") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)

    for line in reader:
        if line[0] == "15":
            writer.writerow([1000, 1, "modified"])
        else:
            writer.writerow(line)

    os.remove("archivo/text.csv")
    os.rename("archivo/archivo_temp.csv", "archivo/text.csv")