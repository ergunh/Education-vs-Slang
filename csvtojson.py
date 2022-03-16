import csv
import json

csvfile = open('master.csv', 'r')
jsonfile = open('master_json.json', 'w')



fieldnames = ('Position', 'Track Name', 'Artist', 'URL')
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile, indent=4)
    jsonfile.write(',\n')



#with open('scraped2JSON.json', 'r') as file:
    #print(file)



# use Hex Fiend remove sha256 view mode first.
# must add object name with brackets i.e "immigration"
# delete the last comma of the last array, or it won't parse. hacky i know, but it works.
# figure out how to code this ^^^^^^


#need to update formatting for the next step to work.
