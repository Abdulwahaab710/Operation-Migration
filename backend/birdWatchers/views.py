from birdWatchers import app, db
import tensorflow as tf
import os
from flask import request, jsonify, abort
import base64
from birdWatchers.inception import Inception
from birdWatchers.models import Bird, SpottedBird


@app.route('/')
def main():
    return '<h1>hello world!</h1>'


@app.route('/search', methods=['POST', 'GET'])
def search():
    print(request.method)
    print(tf.__version__)
    if request.method == 'POST':
        jsonRequest = request.json
        base64ToImg(jsonRequest['image'])
        image_path = os.path.join('temp.jpg')
        # Load the Inception model so it is ready for classifying images.
        model = Inception()
        pred = model.classify(image_path=image_path)
        # Print the scores and names for the top-10 predictions.
        l = model.print_scores(pred=pred, k=10)
        # Close the TensorFlow session.
        model.close()
        bird = db.session.query(Bird).filter(Bird.bird_name == l[0][1]).first()
        print(l[0][1])
        print(bird)
        if bird is None:
            bird = Bird(bird_name=l[0][1])
            db.session.add(bird)
            db.session.commit()
        spotted = SpottedBird(
            # gps_lat, gps_long, timestamp, bird_id
            jsonRequest['gps']['lat'],
            jsonRequest['gps']['long'],
            jsonRequest['timestamp'],
            bird.id
        )
        db.session.add(spotted)
        db.session.commit()
        response = {"top3": l[0:3], "top1": l[0]}
        return jsonify(response)
    return abort(404)


@app.route('/getbird', methods=['GET'])
def fetchGPSbird():
    if request.args.get('bird-name'):
        birdName = request.args.get('bird-name')
        query = db.session.query(Bird).filter(
            Bird.bird_name == birdName
        )
        responseList = []
        for spottedBird in query.one().spotted_bird.all():
            responseList.append(
                {
                    "lat": spottedBird.gps_long,
                    "long": spottedBird.gps_lat,
                    "timestamp": spottedBird.timestamp
                }
            )
        response = {"data": responseList}
        return jsonify(response)
    return abort(404)


def base64ToImg(img_data):
    img_data = str.encode(img_data)
    with open('temp.jpg', 'wb') as img:
        img.write(base64.decodestring(img_data))
