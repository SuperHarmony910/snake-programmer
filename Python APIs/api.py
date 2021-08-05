import json
import requests
app_id  = "2740c991"
app_key  = "c5081adba87cbb9796a7579330aa3a41"
endpoint = "entries"
language_code = "en-gb"
word_id = "silly"
url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word_id.lower() + "?fields=definitions&strictMatch=false"
r = requests.get(url, headers = {"app_id": app_id, "app_key": app_key})
print("text \n" + r.text)
print("DEFINITION!!!!" + r.results[0].lexicalEntries[0].entries[0].senses[0].definitions)