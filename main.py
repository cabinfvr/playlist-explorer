from flask import Flask, render_template, request, redirect
import tracks
import credentials

app = Flask('app')

@app.route('/')
def index():
  return render_template('main.html')

@app.route('/<playlist>')
def explore(playlist):
  playlist_tracks = tracks.get_playlist_tracks(playlist)

  final_tracks = []

  for track in playlist_tracks:
    final_tracks.append(tracks.format_list_info(track))

  japan = tracks.get_playlist_info(playlist)

  return render_template('playlist.html', playlist_songs=final_tracks, playlist_info=japan)

@app.route('/playlist_gen', methods=['POST', 'GET'])
def playlist_generator():
  
  if request.method == 'POST':
    url = request.form['url']
    url = url.split('?')[0]
    url = url.replace('https://open.spotify.com', '')
    url = url.replace('/playlist/','')
    return redirect(f'/{url}')
  else:
    return redirect('/')


app.run(host='0.0.0.0', port=8080)
