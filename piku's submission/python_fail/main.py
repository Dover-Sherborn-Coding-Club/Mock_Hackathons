# 1. Install this package


# 2. Patch requests
import pyodide_http
pyodide_http.patch_all()  # Patch all libraries

# 3. Use requests
import requests
response = requests.get('https://raw.githubusercontent.com/statsbomb/open-data/master/data/lineups/15946.json')# Prompt user to input number of results desired and assert default if left blank
q = input("Search topic?\n    ")
num = input("How many results? default is 100\n    ")
if num == "":
    num = "100"

# Search parameters where "q" is the search key-phrase,
# "num" is the desired amount of search results,
# "api_key" is, well, the api key
params = {
    'q': q,
    'num': num,
    'api_key': '7F3C0B8A20E34F588F539E056F861C08'
}
# Creating search variable
apiResult = requests.get('https://api.serpwow.com/search', params)
results = apiResult.json()
# Assigns dict of json result to results
# Creates variable for organic results section of results dictionary
organicResults = results["organic_results"]
# Wikipedia element search
print("Wikipedia results on google:")
for i in range(organicResults.index(organicResults[-1]) + 1):
    if "wikipedia" in organicResults[i]["link"]:
        print("    \"" + organicResults[i]["title"] + "\"")
        print("    \"" + organicResults[i]["link"] + "\"")
