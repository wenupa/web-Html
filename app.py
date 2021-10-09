from flask import Flask,render_template,jsonify
import json

app = Flask(__name__)

inputfile = 'data/posts.json'
    
with open(inputfile) as data_file:
    data = json.load(data_file)

@app.route('/')
def index():
    return render_template('home.html',posts=data)


@app.route('/api/posts')
def posts():
    return jsonify(data)


@app.route('/p/<page_id>')
def page(page_id):
    pageid = page_id
    realid = int(pageid)
    postContent = data[realid -1]
    return render_template('post.html',posts=postContent)


if __name__ == '__main__':
    app.run(threaded=True, port=8000)