from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit, join_room

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('start.html')

@app.route('/chat')
def guess():
    return render_template('chat.html')

if __name__ == '__main__':
    app.run()
