import requests
from flask import Flask

app = Flask(__name__)

@app.route('/transaction')
def transaction():
    try:
        acc = requests.get("http://account:3000/accounts").json()
        notify = requests.get("http://notification:5000/notify").json()

        return {
            "transaction": "SUCCESS",
            "account_response": acc,
            "notification_response": notify
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)