from birdWatchers import app
import tensorflow as tf
import os
from flask import request
import base64
# from birdWatchers.Inception.inception import download
from birdWatchers.inception import Inception


@app.route('/')
def main():
    return '<h1>hello world!</h1>'


@app.route('/search', methods=['POST'])
def test():
    # print(request.json)
    jsonRequest = request.json
    base64ToImg(jsonRequest['image'])
    return 'hello'


def search():
    print(request.json)
    print(tf.__version__)

    # data_dir = "birdWatchers/inception"
    # imagePath = 'cropped_panda.jpg'
    # image_path = os.path.join(data_dir, imagePath)
    image_path = os.path.join('temp.jpg')
    # Load the Inception model so it is ready for classifying images.
    model = Inception()
    pred = model.classify(image_path=image_path)
    # Print the scores and names for the top-10 predictions.
    l = model.print_scores(pred=pred, k=10)

    # Close the TensorFlow session.
    model.close()
    response = '<ul>'
    for i in l:
        response += '<li>'
        response += str(i[1])
        response += '</li>'
    response += '</ul>'
    return response


def base64ToImg(img_data):
    img_data = str.encode(img_data)
    with open('temp.jpg', 'wb') as img:
        img.write(base64.decodestring(img_data))
    # img_data = str.encode(img_data)
    # img = open('temp.jpg', 'wb')
    # img.write(img_data.decode('base64'))
    # img.close()
