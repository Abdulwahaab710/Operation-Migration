from birdWatchers import app
import tensorflow as tf
import os
from flask import request, jsonify
import base64
# from birdWatchers.Inception.inception import download
from birdWatchers.inception import Inception


@app.route('/')
def main():
    return '<h1>hello world!</h1>'


@app.route('/search', methods=['POST'])
def search():
    print(request.json)
    print(tf.__version__)
    jsonRequest = request.json
    base64ToImg(jsonRequest['image'])
    image_path = os.path.join('temp.jpg')
    # Load the Inception model so it is ready for classifying images.
    model = Inception()
    pred = model.classify(image_path=image_path)
    # Print the scores and names for the top-10 predictions.
    l = model.print_scores(pred=pred, k=10)
    print(l)
    # Close the TensorFlow session.
    model.close()
    response = {"top3":l[0:3]}
    return jsonify( response )


def base64ToImg(img_data):
    img_data = str.encode(img_data)
    with open('temp.jpg', 'wb') as img:
        img.write(base64.decodestring(img_data))
    # img_data = str.encode(img_data)
    # img = open('temp.jpg', 'wb')
    # img.write(img_data.decode('base64'))
    # img.close()
