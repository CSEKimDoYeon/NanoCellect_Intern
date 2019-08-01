
from flask import Flask, render_template,request
import plotly
import plotly.graph_objs as go

import numpy as np
import json
import db

app = Flask(__name__)


@app.route('/')


def index():
    feature = 'Bar'
    bar = create_plot(feature) # 초기는 Bar형으로 띄운다.
    return render_template('index.html', plot=bar)

def create_plot(feature):
    data = db.df_base
    engine_base = db.engine

    data = db.extract_Underfifty(engine_base)
    print(data)

    if feature == 'Bar':
        df = data  # creating a sample dataframe
        print(df)
        data = [
            go.Bar(
                x=df['company'],  # assign x as the dataframe column 'x'
                y=df['count']
            )
        ]
    else:
        N = 1000
        random_x = np.random.randn(N)
        random_y = np.random.randn(N)

        # Create a trace
        data = [go.Scatter(
            x = random_x,
            y = random_y,
            mode = 'markers'
        )]


    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

@app.route('/bar', methods=['GET', 'POST'])
def change_features():

    feature = request.args['selected']
    graphJSON= create_plot(feature)




    return graphJSON

if __name__ == '__main__':
    app.run()