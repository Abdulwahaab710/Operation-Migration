from birdWatchers import app
import tensorflow as tf
import os
# from flask import render_template
# from birdWatchers.Inception.inception import download
from birdWatchers.inception import Inception


@app.route('/')
def main():
    return '<h1>hello world!</h1>'


@app.route('/search')
def search():
    print(tf.__version__)

    # Download Inception model if not already done.
    # maybe_download()

    data_dir = "birdWatchers/inception"
    imagePath = 'cropped_panda.jpg'
    image_path = os.path.join(data_dir, imagePath)
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
