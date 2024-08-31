from data_seeder.mongo_db_seeder import load_confluence_data
from graph.graph import app
from flask import Flask,jsonify,request

from dotenv import load_dotenv

load_dotenv()

flask_app = Flask(__name__)


@flask_app.route('/search', methods=['POST'])
def search():
    reqquestMpdy = request.get_json()
    result = app.invoke({'question': reqquestMpdy['question']})
    return jsonify(result)


@flask_app.route('/load_data', methods=['GET'])
def load_data():
    load_confluence_data()
    return jsonify({"message": "Data loaded"})

if __name__ == '__main__':
    print('Hello World!')
    flask_app.run(port=5000)