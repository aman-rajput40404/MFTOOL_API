"""
This API takes AMFI code of mutual funds and returns mutual funds scheme date. Data taken from amfiindia

route for specific scheme details:
/fund_details/?user= <scheme code>
eg:
http://127.0.0.1:5000/fund_details/?user=144756

all data is in json
"""

from flask import Flask, request, url_for
import mftool as Mf
import json

mf = Mf.Mftool()
app = Flask(__name__)

@app.route('/', methods=['GET'])
def all_codes():
    all_scheme_codes = mf.get_scheme_codes()
    # converting dict to json
    data = json.dumps(all_scheme_codes, indent=4)
    return data

@app.route('/fund_details/', methods=['GET'])
def funds_details():
    #getting the code
    user_query = str(request.args.get('user'))

    scheme = mf.get_scheme_quote(user_query)
    # converting dict to json
    data = json.dumps(scheme, indent=4)
    return data


if __name__ == '__main__':

    PORT = 5000
    app.run(port=PORT)
