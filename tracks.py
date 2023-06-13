import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from credentials import *

def get_playlist_tracks(playlist_link):
    # Spotify API credentials
    client_id = id()
    client_secret = secret()

    # Create a Spotify client
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Extract the playlist ID from the link
    playlist_id = playlist_link.split('/')[-1]

    # Get the playlist's tracks
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']

    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])

    return tracks

def format_track_info(track):
    song_title = track['track']['name']
    artist = track['track']['artists'][0]['name']
    return f"{song_title} - {artist}"

def format_list_info(track):
    song_title = track['track']['name']
    artist = track['track']['artists'][0]['name']
    album_art = track['track']['album']['images'][0]['url']
    song_url = track['track']['external_urls']['spotify']
    artist_url = track['track']['album']['artists'][0]['external_urls']['spotify']

    open('song.json', 'w').write(json.dumps(track))

    return [song_title, artist, album_art, song_url, artist_url]

def save_tracks_to_file(tracks, output_file):
    with open(output_file, 'w') as file:
        for track in tracks:
            file.write(format_track_info(track) + '\n')

def get_playlist_info(playlist_link):
    client_id = id()
    client_secret = secret()

    # Create a Spotify client
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Extract the playlist ID from the link
    playlist_id = playlist_link.split('/')[-1]

    # Get the playlist info
    playlist = sp.playlist(playlist_id)

    # Extract the title and artwork URL
    title = playlist['name']
    artwork_url = playlist['images'][0]['url']

    return title, artwork_url
