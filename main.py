#!/usr/bin/env python
import spotipy.util as util
from spotipy import Spotify
from youtube_dl import YoutubeDL
import os

username = os.environ.get('SPOTIFY_USERNAME')
scope = 'user-library-read'
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')

token = util.prompt_for_user_token(username, scope, client_id=client_id, client_secret=client_secret,\
     redirect_uri='http://localhost:5000')

sp = Spotify(auth=token)

saved_tracks = sp.current_user_saved_tracks(limit=20)

songs = list()

while saved_tracks:
    for track in saved_tracks['items']:
        name = track['track']['name']
        artists = list()
        for artist in track['track']['artists']:
            artists.append(artist['name'])
        songs.append(name+' '+' '.join(artists))
        print('done....')
    if saved_tracks['next']:
        saved_tracks = sp.next(saved_tracks)
    else:
        saved_tracks = None
        
f = open('likes.txt', 'w')

for song in songs:
    f.write(song + os.linesep)
