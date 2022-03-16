import json
import csv
with open("DataSentimentAnalyzed.json") as file:
    data = json.load(file)

fname = "prAna_analyzed.csv"

with open(fname, "w") as file:
    csv_file = csv.writer(file)
    csv_file.writerow([])
    for item in data["tweets"]:
        csv_file.writerow([item['responces'],item['product name'], item['metaphorsFound'], item['metaphorFamily'], item['SentimentScore'], item['Sentiment']])
