# README
## Climate Analysis and API Project
### Project Overview
This project involves performing climate analysis on a SQLite database containing weather data from Hawaii and creating a Flask API to serve the data. The analysis includes precipitation and station data, and the API provides endpoints to query this data dynamically.

## Key Tasks Completed
### Database Connection

Connected to SQLite Database: Used SQLAlchemy to connect to the database and reflect tables into classes.

Session Management: Created and closed SQLAlchemy sessions to interact with the database.

Precipitation Analysis

Queried Recent Data: Retrieved the most recent date in the dataset.

Collected Precipitation Data: Queried date and precipitation for the last year of data and saved results to a Pandas DataFrame.

Data Visualization: Plotted the precipitation data and printed summary statistics.

### Station Analysis
Station Count: Determined the number of stations in the dataset. 

Active Stations: Listed stations and their observation counts to identify the most active station.

Temperature Statistics: Queried min, max, and average temperatures for the most active station.

Temperature Observations: Retrieved temperature observations for the previous year and plotted a histogram.

##Flask API
Setup and Routes: Established a Flask API with routes for precipitation, stations, and temperature observations.

Precipitation Endpoint: Returned JSON data with date as the key and precipitation as the value for the last year.

Stations Endpoint: Provided JSON data for all stations in the database.

TOBS Endpoint: Returned JSON data for temperature observations of the most active station for the last year.

Dynamic Temperature Endpoints: Created routes to return min, max, and average temperatures for given start and end date ranges.


This project demonstrates the integration of data analysis with web API development, providing a robust framework for accessing and visualizing climate data.
