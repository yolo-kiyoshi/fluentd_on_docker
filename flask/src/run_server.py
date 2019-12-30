import os
import flask


app = flask.Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/", methods=["GET"])
def api():

    print(f'print cnt :{cnt}')

    return 'returnaaaa'

if __name__ == "__main__":
    print(" * Flask starting server...")
    app.run(host='0.0.0.0',port=80,debug=True)
