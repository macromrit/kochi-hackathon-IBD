import requests
import json



def get_links(response, snips, sub):
    for i in response[sub]:
        snips[i['snippet']] = i['link']
    return snips


def main(prompt:str):
    url = "https://google.serper.``dev``/search"

    payload = json.dumps({
    "q": prompt
    })
    headers = {
    'X-API-KEY': '0b08d3b988da00cca1c07127d6ce314a4b016e4e',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    response = json.loads(response.text)


    snips_with_links = get_links(response = response, snips = dict(), sub = 'organic')
    snips_with_links = get_links(response = response, snips = snips_with_links, sub = 'peopleAlsoAsk')

    return snips_with_links
