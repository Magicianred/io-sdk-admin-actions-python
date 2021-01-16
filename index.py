import sys
from flask import Flask
from flask import request
from flask_cors import CORS

# from actions.iosdk.send import main as send
from actions.util.get_custom_connectors import main as get_custom_connectors
from actions.util.select_connectors import main as select_connectors
from actions.util.messages import main as messages
from actions.util.sample import main as sample
from actions.util.send import main as send
from actions.util.store import main as store
from actions.util.upload import main as upload
from actions.util.cache import main as cache

app = Flask(__name__)
CORS(app)

@app.route('/api/v1/web/guest/util/get_custom_connectors')
def get_custom_connectors_route():
    args = request.args
    return get_custom_connectors(args)

@app.route('/api/v1/web/guest/util/select_connectors')
def select_connectors_route():
    args = request.args
    return select_connectors(args)


@app.route('/api/v1/web/guest/util/store')
def store_route():
    args = request.args
    return store(args)

@app.route('/api/v1/web/guest/util/upload')
def upload_route():
    args = request.args
    return upload(args)

@app.route('/api/v1/web/guest/util/send', methods=['POST'])
def send_route():
    args = request.args
    return send(args)

@app.route('/api/v1/web/guest/util/messages')
def messages_route():
    args = request.args
    return messages(args)

@app.route('/api/v1/web/guest/util/sample')
def sample_route():
    args = request.args
    return sample(args)

@app.route('/api/v1/web/guest/util/cache')
def cache_route():
    args = request.args
    return cache(args)

if __name__ == '__main__':
    app.run(port=3280)