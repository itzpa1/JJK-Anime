from bs4 import BeautifulSoup
import requests
import webbrowser
import re



# season = input("Enter season: ")
season = "2"
episode = input("Enter episode: ")
# episode = "10"

base_url = f"https://animeflix.website/Jujutsu-kaisen-season-{season}-Episode-{episode}/"
print(base_url)

response = requests.get(base_url)

def Video():
        response = requests.get(base_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        drive_links = []
        for ele in soup.find_all('a',href=re.compile("^https://drive")):
            drive_links.append(ele.get('href'))
        drive_link = drive_links[0]
        print(drive_link)
        file_id = drive_link.split('=')[-2].split('&usp')[-2]
        def create_drive_link():
            # prefix = 'https://drive.google.com/uc?/export=download&id='
            video_url = "https://drive.usercontent.google.com/u/0/uc?id="+file_id+"&export=download"
            print(video_url)
            return video_url
        drive_response = requests.get(create_drive_link())
        drive_soup = BeautifulSoup(drive_response.text, 'html.parser')
        body_text = drive_soup.find_all('body')
        if "sorry" in body_text:
            drive_link = drive_links[1]
            create_drive_link()
        webbrowser.open(create_drive_link())

if response.status_code == 200:
    Video()
    
else :
    base_url = f"https://animeflix.website/Jujutsu-Kaisen-season-{season}-in-Hindi-episode-{episode}/"
    # response = requests.get(base_url)
    Video()

