from flask import Flask
from flask import jsonify, request
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
@app.route('/query-example')
def query_example():
    name = request.args.get('name') 
    password = request.args.get('pass')  
return '''<h1>name : {}</h1>
              <h1>password: {}</h1>

@app.route('/json_example', methods=['POST'])
def json_example():
    req_data = request.get_json()
    if 'language' in req_data:
        language = req_data['language']
    name = req_data['name']
    password = req_data['password']
    return '''</h1>
        name {}
        passord {}
        </h1>'''.format(name, password)
app.run(port=1234, debug=True)

