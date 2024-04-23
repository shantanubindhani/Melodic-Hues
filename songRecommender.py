import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


client_id = ""
client_secret = ""
if client_id == "":
    with open("clientid.key", "r") as file:
        client_id = file.readline()
if client_secret == "":
    with open("clientsecret.key", "r") as file:
        client_secret = file.readline()


auth_manager = SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret
)
sp = spotipy.Spotify(auth_manager=auth_manager)


def find_songs_by_mood(mood, lang="english"):
    synonyms = {
        "happy": ["joyful", "cheerful", "upbeat", "positive", "bright"],
        "sad": ["melancholic", "depressed", "gloomy", "sorrowful", "blue"],
        "angry": ["furious", "irritated", "aggressive", "rage", "frustrated"],
        "fear": ["anxious", "scared", "terrified", "nervous", "apprehensive"],
        "surprise": ["astonished", "amazed", "shocked", "startled", "unexpected"],
    }

    search_terms = [mood] + synonyms.get(mood, [])

    random.shuffle(search_terms)
    search_query = " ".join(search_terms[:3])
    search_string = f"{search_query} {lang} playlist"

    playlist_results = sp.search(q=search_string, type="playlist", limit=5)

    playlist_uris = []
    for playlist in playlist_results["playlists"]["items"]:
        playlist_uris.append(playlist["uri"])

    tracks = []
    for playlist_uri in playlist_uris:
        playlist_tracks = sp.playlist_tracks(playlist_uri)
        for item in playlist_tracks["items"]:
            track = item["track"]

            try:
                track_info = {
                    "name": track["name"],
                    "artists": ", ".join(
                        [artist["name"] for artist in track["artists"]]
                    ),
                    "preview_url": track["preview_url"],
                    "spotify_url": track["external_urls"]["spotify"],
                }
                tracks.append(track_info)
            except:
                pass

    random.shuffle(tracks)
    return tracks[:10]


def main():
    mood = input("Enter the mood you want to find songs for: ")
    songs = find_songs_by_mood(mood)

    print(f"Here are some songs for '{mood}':")
    for i, song in enumerate(songs, 1):
        print(f"{i}. {song['name']} by {song['artists']}")
        print(f"   Preview URL: {song['preview_url']}")
        print(f"   Spotify URL: {song['spotify_url']}")
        print()


if __name__ == "__main__":
    main()
