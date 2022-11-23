from flask import Flask, request, redirect
import json
from flask.ext.cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'application/json'


# Setup flask server
app = Flask(__name__)

# Setup url route which will calculate
# total sum of array.


@app.route('/main', methods=['POST'])
def sum_of_array():
    data = request.get_json()
    print(data)

    # Data variable contains the
    # data from the node server
    #ls = data['array']
    # result = sum(ls)  # calculate the sum

    # Return data in json format
    return json.dumps({"result": "yes"})


if __name__ == "__main__":
    app.run(port=5000)
