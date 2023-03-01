from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    emit('my_response', {'data': 'Connected'})

@socketio.on('start_progress')
def start_progress():
    for i in range(101):
        emit('update_progress', {'data': i})
        time.sleep(0.1)

if __name__ == '__main__':
    socketio.run(app, debug=True)
