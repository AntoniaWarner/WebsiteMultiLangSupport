import pandas as pd
import csv

start_file = 'LangExport.xlsx'
#LangExport.csv will be overwritten if it exists

read_file = pd.read_excel(start_file)   #parses xlsx to CSV

read_file.to_csv("LangExport.csv", index=0, header=True)

df = pd.DataFrame(pd.read_csv("LangExport.csv"))


def write_json(lang, input_filename,output_filename):       #parses 
    with open(input_filename, "r", encoding='utf8') as file:
        reader = csv.DictReader(file, fieldnames=["datakey", "en", "nl", "fr", "es"]) #in order of languages in xlsx
        with open(output_filename, "w", encoding='utf8') as outputfile:
            outputfile.write('{\n    "null": "null"')
            for line in reader:
                datakey = line["datakey"]
                if lang == 'en':
                    content = line["en"] #add for each supported language
                if lang == 'fr':
                    content = line["fr"]
                if lang == 'es':
                    content = line["es"]
                if lang == 'nl':
                    content = line["nl"]
                result = f',\n    "{datakey}": "{content}"'
                outputfile.write(result)
            outputfile.write("\n}")

write_json("en", "LangExport.csv", "Languages/en.json") #end file names and paths
write_json("nl", "LangExport.csv", "Languages/nl.json")
write_json("fr", "LangExport.csv", "Languages/fr.json") #extend for each supported language
write_json("es", "LangExport.csv", "Languages/es.json")
