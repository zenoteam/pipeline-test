from flask import Flask, jsonify, request, Response
import http.client
from db import db_config, db
from models import Post

app = Flask(__name__)

app.config.update(db_config)

db.init_app(app)
app.db = db


@app.route('/', methods=['GET', 'POST'])
def getall_create():
    if request.method == "GET":
        posts = Post.query.order_by('id').all()
        response = []
        for post in posts:
            post = post.__dict__
            del post["_sa_instance_state"]
            response.append(post)
        print(response)
        return jsonify({'posts': response})

    if request.method == 'POST':
        request_body = request.json
        body = request_body['body']
        description = request_body['description']
        title = request_body['title']

        post = Post(title=title, body=body, description=description)

        db.session.add(post)
        db.session.commit()

        post = {"body": body, "title": title, 'description': description}

    return jsonify({'result': post})


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
    app.run(host='0.0.0.0')
