from flask import Flask,request
app = Flask(__name__)
# app = Flask


@app.route("/<flask_api>/send", methods=['POST'])
def send_details(flask_api):
    data = request.get_json()
    print(data)
    return data
@app.route("/<flask_api>/get", methods=['GET','POST'])
def get_details(flask_api):
    json=request.get_json()
    print(json.get("Age"))
    print(json.get('str_tp'))
    print(type(json.get('integer')))
    print(type(json.get('str_tp')))
    print(type(json.get('bool_tp')))
    print(int(json.get('bool_tp')))
    print("----------Bool-----",bool(json.get('str_tp')))
    return "Pass",json


if __name__=='__main__':
    app.run(port=5000,host='0.0.0.0')