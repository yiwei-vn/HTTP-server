from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)



@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return jsonify({"User": str(username)})
    # return 'User %s' % str(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % str(subpath)   

@app.route('/',methods=['GET', 'POST'])
def hello_world():
    return jsonify({"username":"xyz","password":"xyz"})   

@app.route('/query-example/api')
def query_example():
    ten = request.args.get('name') 
    matkhau = request.args.get('password')  
    return jsonify ({"name":ten,"password":matkhau})

@app.route('/api/json_example', methods=['POST'])
def json_example():
    req_data = request.get_json()
    ten = req_data['name']
    matkhau = req_data['password']
    return jsonify ({"name":ten,"password":matkhau})


app.run(port=5000, debug=True)

