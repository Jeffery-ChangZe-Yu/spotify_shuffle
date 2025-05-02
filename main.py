import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
import random
import os
from dotenv import load_dotenv
import sys


def main(songs=5):
    sp = openSession()

    playRandomSongsMultipleTimes(sp, songs)


def openSession():

    load_dotenv()
    
    scope = "user-modify-playback-state user-library-read"
    
    token = util.prompt_for_user_token(os.getenv("SPOTIPY_USER_ID"),
                                       scope,
                                       client_id=os.getenv("SPOTIPY_CLIENT_ID"),
                                        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
                                        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"))

    if token:
        sp = spotipy.Spotify(auth=token)
    # sp = spotipy.Spotify(
    #     auth_manager=SpotifyOAuth(
    #         client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    #         client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    #         redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    #         scope=scope,
    #     )
    # )
        return sp


def playRandomSongFromUserSavedTracks(sp):
    results = sp.current_user_saved_tracks(
        offset=random.randint(0, 1000)
    )  # get current user tracks

    chosenSong = results["items"][random.randint(0, len(results["items"])-1)][
        "track"
    ]  # choose a random track, get URI

    chosenSongUri = chosenSong["uri"]
    chosenSongId = chosenSong["id"]

    sp.add_to_queue(chosenSongUri)
    return chosenSongId, chosenSongUri

    # sp.start_playback(uris=[chosenSong]) #play random track


def playRandomSongsMultipleTimes(sp, numSongsToAdd=10):
    songsAdded = {}

    while len(songsAdded) < numSongsToAdd:
        chosenSongId, chosenSongUri = playRandomSongFromUserSavedTracks(sp)
        songsAdded[chosenSongId] = chosenSongUri


if __name__ == "__main__":
    songsStr = sys.argv[1]
    if songsStr != None:
        songsInt = int(songsStr)
        main(songsInt)
