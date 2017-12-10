#!flask/bin/python
from flask import Flask, jsonify,request
app = Flask(__name__)

Branches =({'name' : 'Electronics'},{'name' : 'Computer Science'},{'name' : 'Electrical'})

# we get all the list as in jsonify format
@app.route('/Branch', methods=['GET'])
def viewallthelist():
    return jsonify({'Branches' : Branches})
# here it search and we can loook for that
@app.route('/Branch/<string:name>', methods=['GET'])
def  requiredone(name):
	
allbranches = [allbranches for allbranches in Branches if allbranches['name'] ==name]
return jsonify({'allbranches' : allbranches[0] })

if __name__ == '__main__':
    app.run(debug=True)
