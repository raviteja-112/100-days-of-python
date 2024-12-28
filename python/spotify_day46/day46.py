import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="1b07cac3dc1c4a56a58899bfe7f7ab79",
        client_secret="9ac20c531add4da4a95dc2ec6842db4b",
        show_dialog=True,
        cache_path="token.txt",
        username="Testing", 
    )
)

URL = "https://www.billboard.com/charts/india-songs-hotw/"
# date = input("which year do you want to travel to ? Type the date in this format YYYY-MM-DD:")
date = "2024-05-10"
final_url = URL+date
response = requests.get(url=final_url)
web = response.text

soup = BeautifulSoup(web,"html.parser")

# songs = [song.getText().strip() for song in soup.find_all(name="h3") ] // this will give all h3
# print(songs)

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

# print(song_names)

user_id = sp.current_user()["id"]
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

