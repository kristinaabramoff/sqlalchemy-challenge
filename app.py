# Import the dependencies.
import numpy as np
import pandas as pd  # Added import for pandas
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
from datetime import datetime

#################################################
# Database Setup
#################################################

# Create engine using the `hawaii.sqlite` database file
engine = create_engine('sqlite:///resources/hawaii.sqlite')
# Declare a Base using `automap_base()`
Base = automap_base()
# Use the Base class to reflect the database tables
Base.prepare(autoload_with=engine)

# Assign the measurement class to a variable called `Measurement`
# and the station class to a variable called `Station`
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"Welcome to the Hawaii Climate API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start/<start><br/>"
        f"/api/v1.0/start/<start>/end/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Find the most recent date in the data set
    latest_date = session.query(func.max(Measurement.date)).first()[0]
    # Calculate the date one year ago from the last data point in the database
    year_ago_date = (pd.to_datetime(latest_date) - pd.DateOffset(years=1)).strftime('%Y-%m-%d')

    # Query precipitation data for the last year
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= year_ago_date).all()
    
    session.close()

    # Convert the query results to a dictionary using date as the key and prcp as the value
    precipitation_dict = {date: prcp for date, prcp in results}

    return jsonify(precipitation_dict)

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all stations
    results = session.query(Station.station).all()
    
    session.close()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(results))

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query the dates and temperature observations of the most-active station for the previous year of data
    most_active_station = session.query(Measurement.station).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).first()[0]
    last_date = session.query(func.max(Measurement.date)).filter(Measurement.station == most_active_station).first()[0]
    year_ago_date = (pd.to_datetime(last_date) - pd.DateOffset(years=1)).strftime('%Y-%m-%d')

    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == most_active_station).filter(Measurement.date >= year_ago_date).all()
    
    session.close()

    # Convert list of tuples into normal list
    tobs_data = []
    for date, tobs in results:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        tobs_data.append(tobs_dict)

    return jsonify(tobs_data)

@app.route("/api/v1.0/start/<start>/<end>", defaults={'end': None})

@app.route("/api/v1.0/start/<start>")
def temperature_stats_start(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Define the query for the temperature statistics
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    # Calculate TMIN, TAVG, TMAX for dates greater than or equal to the start date
    results = session.query(*sel).filter(Measurement.date >= start).all()

    session.close()

    # Convert the query results to a dictionary
    temp_stats = {
        "TMIN": results[0][0],
        "TAVG": results[0][1],
        "TMAX": results[0][2]
    }

    return jsonify(temp_stats)



@app.route("/api/v1.0/start/<start>/end/<end>")
def temperature_stats(start, end):
    # Convert start and end dates to datetime objects
    start_date = datetime.strptime(start, '%Y-%m-%d')
    end_date = datetime.strptime(end, '%Y-%m-%d')

    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Define the query for the temperature statistics
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    # Calculate TMIN, TAVG, TMAX for dates between the start and end date
    results = session.query(*sel).filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

    session.close()

    # Convert the query results to a dictionary
    temp_stats = {
        "TMIN": results[0][0],
        "TAVG": results[0][1],
        "TMAX": results[0][2]
    }

    return jsonify(temp_stats)

# Start the Flask app
if __name__ == "__main__":
    app.run(debug=True)
