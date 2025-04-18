import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
import random
import os
from dotenv import load_dotenv




def main():
    sp = openSession()

    playRandomSongsMultipleTimes(sp, 5)

    """
    print(len(results['items']))
    print(results['items'][0]['track']['uri'])

    for idx, item in enumerate(results['items']):
        track = item['track']
        chosenSong = track['uri']
        print(idx, track['artists'][0]['name'], " - ", track['name'], track['uri'])
    
    print("trying to make one API call")
    """

def openSession():

    load_dotenv()

    scope = "user-modify-playback-state user-library-read"
    # scope = "user-library-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv('SPOTIPY_CLIENT_ID'),
        client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
        redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
        scope=scope))
    
    return sp

def playRandomSongFromUserSavedTracks(sp):
    results = sp.current_user_saved_tracks(offset=random.randint(0,1000)) #get current user tracks

    chosenSong = results['items'][random.randint(0, len(results['items']))]['track'] #choose a random track, get URI

    chosenSongUri = chosenSong['uri']
    chosenSongId = chosenSong['id'];

    sp.add_to_queue(chosenSongUri)
    return chosenSongId, chosenSongUri

    # sp.start_playback(uris=[chosenSong]) #play random track

def playRandomSongsMultipleTimes(sp, numSongsToAdd=10):
    songsAdded = {}

    while (len(songsAdded) < numSongsToAdd):
        chosenSongId, chosenSongUri = playRandomSongFromUserSavedTracks(sp)
        songsAdded[chosenSongId] = chosenSongUri


    

    
    
    

if __name__ == "__main__":
    main()