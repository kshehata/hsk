import sys
import csv

filename = "hsk_all.csv"
if len(sys.argv) > 1:
    filename = sys.argv[1]

words = []
with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    columns = next(csv_reader)
    # This magic converts the row into dictionary
    words = [ dict(zip(columns, r)) for r in csv_reader ]

for level in range(6):
    level = level + 1

    with open(f"hsk_simplified_{level}.csv", "w+") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(["hanzi", "pinyin", "english"])
        for w in words:
            if len(w["level"]) > 0 and int(w["level"]) == level:
                csv_writer.writerow([w["simplified"], w["pinyin"], w["english"]])

    with open(f"hsk_traditional_{level}.csv", "w+") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(["hanzi", "pinyin", "english"])
        for w in words:
            if len(w["level"]) > 0 and int(w["level"]) == level:
                csv_writer.writerow([w["traditional"], w["pinyin"], w["english"]])
