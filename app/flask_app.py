from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': 'OpenShift Jenkins Pipeline Python/Nginx Implementation',
        'description': 'Find the implementation at '
    },
    {
        'id': 2,
        'title': 'OpenShift Jenkins Pipeline Django Implementation',
        'description': 'Find the implementation '
    }
]


@app.route('/', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.run()
