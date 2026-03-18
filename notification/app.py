from flask import Flask

app = Flask(__name__)

@app.route('/notify')
def notify():
    return {"message": "Notification sent successfully!"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)