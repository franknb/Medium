import requests
import base64
import io
from PIL import Image
from sklearn import datasets

# Load Iris dataset 
data = datasets.load_iris()
X = data.data
y = data.target
tn = data.target_names

Setosa = requests.get("https://raw.githubusercontent.com/Frank-Xu-Huaze/Medium/master/Dash_GCP/Setosa.png").content
Versicolor = requests.get("https://raw.githubusercontent.com/Frank-Xu-Huaze/Medium/master/Dash_GCP/Versicolor.png").content
Virginica = requests.get("https://raw.githubusercontent.com/Frank-Xu-Huaze/Medium/master/Dash_GCP/Virginica.png").content
pic = [Setosa, Versicolor, Virginica]

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=124)
lm = LogisticRegression(max_iter=150)
lm.fit(X_train, y_train)
print('Model score on test set: {}'.format(lm.score(X_test, y_test)))

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1(children="Guess the Iris Species App"),
    html.Div(children="Powered by Frank Xu"),
    html.Hr(),
    dcc.Input(id="input_sepal_length",
              type="number", 
              placeholder="input sepal length"),
    dcc.Input(id="input_sepal_width",
              type="number", 
              placeholder="input sepal width"),
    dcc.Input(id="input_petal_length",
              type="number", 
              placeholder="input petal length"),
    dcc.Input(id="input_petal_width",
              type="number", 
              placeholder="input petal width"),
    html.Button('Go', id='show', style={'width':'5vw', 'display': 'inline-block'}),
    html.Hr(),
    html.Div(id='out')]
)

@app.callback(
    Output("out", "children"),
    [Input("show", "n_clicks")],
    state=[State("input_sepal_length", "value"),
           State("input_sepal_width", "value"),
           State("input_petal_length", "value"),
           State("input_petal_width", "value")])
def predict(n_clicks, sl, sw, pl, pw):
    if n_clicks is None:
        return html.Div('Please input the values to see prediction.')
    pred = lm.predict([[sl,sw,pl,pw]])[0]
    im = Image.open(io.BytesIO(pic[pred]))
    return html.Div([
        html.Div('Best guess according to your input: {}'.format(tn[pred])), 
        html.Hr(),
        html.Img(src=im, style={'height':'20%', 'width':'20%'})
    ])

if __name__ == '__main__':
    app.run_server(debug=True)