from item_api.formatter import itemFormatter

from flask import Flask, jsonify

formatter = itemFormatter()
app = Flask(__name__)

@app.get('/item/<item_id>')
def get_item(item_id):
    return jsonify(formatter.get_item(item_id))

@app.get('/items')
def get_items():
    return jsonify(formatter.get_json())

app.run(port=3000)