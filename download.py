from bs4 import BeautifulSoup
import requests
import re
import webbrowser


season = str(2)    #set season
episode = str(14)    #set episode

url = "https://animeflix.website/Jujutsu-kaisen-season-"+season+"-Episode-" + episode + "/"

response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    drive_links = []
    for ele in soup.find_all('a',href=re.compile("^https://drive")):
        drive_links.append(ele.get('href'))
    print(url)
    drive_link = drive_links[1]  #change to 0 if 1 doesn't work
    print(drive_link)

    webbrowser.open(drive_link)
