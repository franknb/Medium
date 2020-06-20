#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 11:03:37 2020

@author: frank
"""
import base64
import io
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from PIL import Image
import tensorflow as tf
import numpy as np
import flask

model = tf.keras.applications.MobileNet()
labels_path = tf.keras.utils.get_file(
    'ImageNetLabels.txt',
    'https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt')
imagenet_labels = np.array(open(labels_path).read().splitlines())[1:]

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)

app.layout = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '50%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        # multiple=True
    ),
    html.Div(id='output-data-upload'),
])

@app.callback(Output('output-data-upload', 'children'),
              [Input('upload-data', 'contents')])
def update_output(content):
    if content is not None:
        content_type, content_string = content.split(',')
        data = base64.b64decode(content_string)
        im = Image.open(io.BytesIO(data))
        im = im.resize((224,224))
        x = tf.keras.preprocessing.image.img_to_array(im)
        x = tf.keras.applications.mobilenet.preprocess_input(x[tf.newaxis,...])
        p = model(x)
        decoded = sorted(list(zip(imagenet_labels,p.numpy()[0])), key = lambda x: x[1])[-1]
        return html.Div([
        # HTML images accept base64 encoded strings in the same format
        # that is supplied by the upload
        html.Div('Original Image'),
        html.Img(src=content, style={'height':'50%', 'width':'50%'}),
        html.Hr(),
        html.Div('Processed Image'),
        html.Img(src=im, style={'height':'50%', 'width':'50%'}),
        html.Hr(),
        html.Div('Our best guess: {}, with {:.3f} confidence.'.format(decoded[0], decoded[1]))
    ])
    
if __name__ == '__main__':
    app.run_server(debug=True)
    