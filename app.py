from flask import Flask, request, jsonify

app = Flask(__name__)
latest_command = None

@app.route('/command', methods=['POST'])
def set_command():
    global latest_command
    data = request.get_json()
    latest_command = data.get('command')
    return jsonify({'status': 'ok', 'message': f'Command {latest_command} received'})

@app.route('/get_command', methods=['GET'])
def get_command():
    global latest_command
    cmd = latest_command
    latest_command = None  # reset after fetching
    return jsonify({'command': cmd})

if __name__ == '__main__':
    app.run()
