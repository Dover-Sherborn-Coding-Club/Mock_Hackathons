# API library
# To get this to work, what I did was:
# first use pip install serpapi or install it through ide whatever
# then use pip3 install urllib3==1.26.6
# then use pip install google-search-results or again, through ide if preferred
import requests
import json
# Search parameters where "q" is the search key-phrase,
# "num" is the desired amount of search results,
# "api_key" is, well, the api key
resultNum = input("How many results? default is 100\n    ")
if resultNum == "":
    resultNum = "100"
params = {
    'q': input("Search topic?\n    "),
    'num': resultNum,
    'api_key': '7F3C0B8A20E34F588F539E056F861C08'
}
# Creating search variable
api_result = requests.get('https://api.serpwow.com/search', params)
results = api_result.json()
# Assigns dict of json result to results
# Creates variable for organic results section of results dictionary
organicResults = results["organic_results"]
# Wikipedia element search
print("Wikipedia results on google:")
for i in range(organicResults.index(organicResults[-1]) + 1):
    if "wikipedia" in organicResults[i]["link"]:
        print("    \"" + organicResults[i]["title"] + "\"")
        print("    \"" + organicResults[i]["link"] + "\"")
# if "wikipedia" not in organicResults:
#   print ("no wikipedia results in page 1 of search womp womp :c")
