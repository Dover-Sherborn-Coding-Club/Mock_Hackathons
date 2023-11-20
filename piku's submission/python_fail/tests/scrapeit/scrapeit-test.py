import micropip
import asyncio
from google_serp_api import ScrapeitCloudClient

def main(event):
    api_key = '97d9a2c1-7d53-48a3-a3f9-f9193dd7dfa8'
    client = ScrapeitCloudClient(api_key=api_key)

    keywords = input("what do you want to search for?\n    ")
    searchNum = input("num of results?\n    ")

    params = {
        "q": keywords,
        "num": searchNum,
        "domain": "google.com"
    }

    response = client.scrape(params=params)
    responseJson = response.json()

    i = 0
    while i < responseJson['organicResults'].index(responseJson['organicResults'][-1]):
        if 'wikipedia' in responseJson['organicResults'][i]['link']:
            print("    \"" + responseJson['organicResults'][i]['title'] + "\"\n" + "    ")
            print("    " + responseJson['organicResults'][i]['link'] + "\"\n" + "    ")
        i += 1
