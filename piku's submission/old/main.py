# API library
# To get this to work, what I did was:
# first use pip install serpapi or install it through ide whatever
# then use pip3 install urllib3==1.26.6
# then use pip install google-search-results or again, through ide if preferred

#           from pyscript import document
from serpapi import GoogleSearch
from pyscript import document
# Search parameters where "q" is the search key-phrase,
# "num" is the desired amount of search results,
# "api_key" is, well, the api key

# resultNum = input("How many results? default is 100\n    ")
# if resultNum == "":
#     resultNum = "100"
def main(event):
    params = {
        "q": "memes",
        "num": "100",
        "api_key": "624f19b460aa70e54a309edca59430ace68c658cb4f60fd49981a3d25e2191e0"
    }
    output_div = document.querySelector("#output")
    # Creating search variable
    search = GoogleSearch(params)
    # Assigns dict of json result to results
    results = search.get_dict()
    # Creates variable for organic results section of results dictionary
    organicResults = results["organic_results"]
    # Wikipedia element search
    #print("Wikipedia results on google:")
    for i in range(organicResults.index(organicResults[-1]) + 1):
        if "wikipedia" in organicResults[i]["link"]:
            z = "    \"" + organicResults[i]["title"] + "\"\n" + "    \"" + organicResults[i]["link"] + "\"\n"
            output_div.innerText = str(z)
        i += 1
    # if "wikipedia" not in organicResults:
    #   print ("no wikipedia results in page 1 of search womp womp :c")
