from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit, join_room

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat')
def guess(id):
    return render_template('chat.html', guess=guesses[id])

if __name__ == '__main__':
    app.run()
