from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')

def home():
    return jsonify({
        "message": "welcome to the flask api application",
    "status":"success"
    })

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 5050)