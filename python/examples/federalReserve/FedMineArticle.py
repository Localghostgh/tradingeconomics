from flask import Flask, render_template
import pandas as pd
import tradingeconomics as te

app = Flask(__name__)
te.login('1bd87fc8c9d34e6:le03ymqbzyehuk6')

# Route for the homepage
@app.route('/')
def home():
    return 'Welcome to my Federal Reserve data web app!'

# Route to display the list of all US states
@app.route('/fedr-states')
def fedr_states():
    mydata = te.getFedRStates(output_type='df')
    return render_template('fedr-states.html', data=mydata.to_html())

# Route to display the list of all counties per state
@app.route('/fedr-counties/<county>')
def fedr_counties(county):
    mydata = te.getFedRStates(county=county, output_type='df')
    return render_template('fedr-counties.html', data=mydata.to_html())

# Route to display data by symbol
@app.route('/fedr-snaps/<symbol>')
def fedr_snaps(symbol):
    mydata = te.getFedRSnaps(symbol=symbol, output_type='df')
    return render_template('fedr-snaps.html', data=mydata.to_html())

# Route to display data by URL
@app.route('/fedr-snaps-url')
def fedr_snaps_url():
    mydata = te.getFedRSnaps(url='united states''/united-states/white-to-non-white-racial-dissimilarity-index-for-benton-county-ar-fed-data.html', output_type='df')
    return render_template('fedr-snaps.html', data=mydata.to_html())

# Route to display data by country
@app.route('/fedr-snaps-country/<country>')
def fedr_snaps_country(country):
    mydata = te.getFedRSnaps(country=country, output_type='df')
    return render_template('fedr-snaps.html', data=mydata.to_html())

# Route to display data by state
@app.route('/fedr-snaps-state/<state>')
def fedr_snaps_state(state):
    mydata = te.getFedRSnaps(state=state, output_type='df')
    return render_template('fedr-snaps.html', data=mydata.to_html())

# Route to display data by county
@app.route('/fedr-county')
def fedr_county():
    mydata = te.getFedRCounty(output_type='df')
    return render_template('fedr-county.html', data=mydata.to_html())

# Route to display data accessed only through symbol
@app.route('/fedr-historical/<symbol>')
def fedr_historical(symbol):
    mydata = te.getHistorical(symbol, output_type='df')
    return render_template('fedr-historical.html', data=mydata.to_html())

# Route to display data by multiple symbols
@app.route('/fedr-historical-symbols')
def fedr_historical_symbols():
    mydata = te.getFedRHistorical(symbol=['racedisparity005007', '2020ratio002013'], output_type='df')
    return render_template('fedr-historical.html', data=mydata.to_html())

# Route to display data by symbol and a start date
@app.route('/fedr-historical-startdate/<symbol>')
def fedr_historical_startdate(symbol):
    mydata = te.getFedRHistorical(symbol=symbol, initDate='2018-05-01', output_type='df')
    return render_template('fedr-historical.html', data=mydata.to_html())

# Route to display data by symbol and a date range
