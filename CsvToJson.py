import csv

def write_json(lang, input_filename,output_filename):
    with open(input_filename, "r", encoding='utf8') as file:
        reader = csv.DictReader(file, fieldnames=["datakey", "en", "fr", "es", "nl", "de", "eo", "it", "pl", "pt"])
        with open(output_filename, "w", encoding='utf8') as outputfile:
            outputfile.write('{\n    "null": "null"')
            for line in reader:
                datakey = line["datakey"]
                if lang == 'en':
                    content = line["en"]
                if lang == 'fr':
                    content = line["fr"]
                if lang == 'es':
                    content = line["es"]
                if lang == 'nl':
                    content = line["nl"]
                if lang == 'de':
                    content = line["de"]
                if lang == 'eo':
                    content = line["eo"]
                if lang == 'it':
                    content = line["it"]
                if lang == 'pl':
                    content = line["pl"]
                if lang == 'pt':
                    content = line["pt"]
                result = f',\n    "{datakey}": "{content}"'
                outputfile.write(result)
            outputfile.write("\n}")
#file :)

write_json("en", "LangExport.csv", "Languages/en.json")
write_json("fr", "LangExport.csv", "Languages/fr.json")
write_json("es", "LangExport.csv", "Languages/es.json")
write_json("nl", "LangExport.csv", "Languages/nl.json")
#write_json("de", "LangExport.csv", "Languages/de.json")
#write_json("eo", "LangExport.csv", "Languages/eo.json")
#write_json("it", "LangExport.csv", "Languages/it.json")
#write_json("pl", "LangExport.csv", "Languages/pl.json")
#write_json("pt", "LangExport.csv", "Languages/pt.json")
