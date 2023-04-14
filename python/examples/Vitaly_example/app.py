# Importing necessary packages
from flask import Flask, render_template
import pandas as pd
import tradingeconomics as te
import plotly.graph_objs as go
import plotly.express as px
from datetime import datetime

# Initializing the Flask app and logging in to Trading Economics API
app = Flask(__name__)
te.login('1bd87fc8c9d34e6:le03ymqbzyehuk6')

# Defining the initial and end dates for data retrieval
INIT_DATE = '2022-01-01'
END_DATE = '2022-12-31'


# Function to retrieve and preprocess the data for a specific country
def get_country_data(country):
    # Retrieving raw data from Trading Economics API
    data_dict = te.getHistoricalData(country=country, indicator='Balance of Trade',
                                     initDate=INIT_DATE, endDate=END_DATE, output_type='raw')
    # Converting raw data to a pandas DataFrame and preprocessing it
    data = pd.DataFrame(data_dict).drop(['Category', 'Frequency', 'HistoricalDataSymbol'], axis=1)
    data = data.drop(0).iloc[::-1].reset_index(drop=True)
    data.index += 1
    data['DateTime'] = pd.to_datetime(data['DateTime']).dt.date
    data['LastUpdate'] = pd.to_datetime(data['LastUpdate']).dt.date
    return data


# Route for the home page
@app.route('/')
def home():
    # Retrieving and preprocessing data for Mexico and Thailand
    mexico_data = get_country_data('Mexico')
    thailand_data = get_country_data('Thailand')

    # Creating a plotly figure object and adding traces for each country's data
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=mexico_data['DateTime'], y=mexico_data.Value, name='Mexico'))
    fig.add_trace(go.Scatter(x=thailand_data['DateTime'], y=thailand_data.Value, name='Thailand'))
    fig.update_layout(
        title='',
        xaxis_title='Date by months',
        yaxis_title='Millions of US dollars',
    )

    # Converting the plotly figure object to HTML for rendering on the web page
    chart = fig.to_html(full_html=False, default_height=500, default_width=700)

    # Converting the preprocessed data for Mexico and Thailand to HTML tables for rendering on the web page
    table1 = mexico_data.to_html(classes='table')
    table2 = thailand_data.to_html(classes='table')

    # Rendering the index.html template with the plotly figure and data tables
    return render_template('index.html', chart=chart, table1=table1, table2=table2)


# Starting the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5000)
