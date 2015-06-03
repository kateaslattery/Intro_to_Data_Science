import json
import requests

def api_get_request(url):

    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain.
    #
    # Once you've done this, return the name of the number 1 top artist in Spain.
    
    url = 'http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=**&format=json'
    
    response = requests.get(url)
    top_artists = json.loads(response.text)
    return top_artists['topartists']['artist'][0]['name']
