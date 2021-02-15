from flask import Flask, jsonify, request, url_for, render_template, redirect
import http.client
from db import db_config, db
from models import Post

app = Flask(__name__)

app.config.update(db_config)

db.init_app(app)
app.db = db


@app.route('/', methods=['GET', 'POST'])
def getall():
    if request.method == "GET":
        posts = Post.query.order_by('id').all()
        response = []
        for post in posts:
            post = post.__dict__
            del post["_sa_instance_state"]
            response.append(post)
        print(response)
        return render_template('blog/index.html', posts=response)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        description = request.form['description']
        title = request.form['title']
        body = request.form['body']

        post = Post(title=title, body=body, description=description)

        db.session.add(post)
        db.session.commit()

        return redirect(url_for('getall'))

    return render_template('blog/create.html')


@app.route('/<int:postId>', methods=['GET', 'DELETE'])
def get_delete_post(postId):
    post = Post.query.get(postId)
    if not post:
        return jsonify(http.client.NOT_FOUND), 404

    if request.method == "GET":
        post = post.__dict__
        del post["_sa_instance_state"]
        return jsonify({'posts': post})

    if request.method == 'DELETE':
        db.session.delete(post)
        db.session.commit()

    return jsonify({'result': []}), 204


if __name__ == '__main__':
    app.run(debug=True)
