from flask import Flask

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def main():
	return 'hello'

app.run('0.0.0.0',debug=True, port=1000)

test_long_var_name = 3