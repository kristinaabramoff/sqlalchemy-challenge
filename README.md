# Climate Analysis and Flask API Project

## Project Overview
This project performs a comprehensive climate analysis on weather data from Hawaii, stored in a **SQLite** database. A **Flask API** is built to dynamically serve the analyzed data through multiple endpoints. The analysis covers precipitation, temperature, and station data, providing insights into climate trends in the region.

This project demonstrates proficiency in:
- **SQLAlchemy** for database management
- **Pandas** for data manipulation and analysis
- **Matplotlib** for visualizing climate data
- **Flask** for developing a RESTful API to serve the data

---

## Key Features

### 1. Database Management with SQLAlchemy
- **Automated Reflection**: Used SQLAlchemy’s `automap_base()` to automatically reflect tables from the SQLite database.
- **Efficient Querying**: Leveraged SQLAlchemy ORM queries to efficiently extract and manipulate the data.

  ![create_engine](https://github.com/user-attachments/assets/cfed6caf-5555-40d2-9622-31ee603c8447)


### 2. Climate Data Analysis
- **Precipitation Analysis**: Queried the most recent 12 months of precipitation data and visualized it using Matplotlib.
- **Station Analysis**: Identified the most active weather station and analyzed temperature trends for the past year.
- **Temperature Statistics**: Calculated minimum, maximum, and average temperatures using SQLAlchemy ORM.

### 3. Flask API Development
The API provides multiple endpoints that allow users to access the climate data:
- `/api/v1.0/precipitation`: Returns the last 12 months of precipitation data in JSON format.
- `/api/v1.0/stations`: Returns a list of all weather stations.
- `/api/v1.0/tobs`: Returns temperature observations for the most active station from the last year.
- `/api/v1.0/<start>`: Returns min, max, and average temperatures from a given start date.
- `/api/v1.0/<start>/<end>`: Returns min, max, and average temperatures for a given date range.

---

## Technical Breakdown

### 1. Precipitation Analysis
- Queried the most recent date and retrieved precipitation data for the previous 12 months.
- Stored results in a **Pandas DataFrame** and sorted by date.
- **Visualization**: Created a time-series plot of the precipitation data using **Matplotlib**.

### 2. Station and Temperature Analysis
- Queried the total number of stations and identified the most active station.
- For the most active station, retrieved and plotted the last 12 months of temperature observations (TOBS) as a histogram.

- ![active_station](https://github.com/user-attachments/assets/e2a52cbc-25e7-4007-921d-f6c32984b189)

- 
![active_station](https://github.com/user-attachments/assets/ca6206a7-a001-4aef-840b-d11e2018f7dc)

### 3. API Endpoints
- Designed dynamic Flask routes to deliver specific climate data. 
- Integrated **Flask** with SQLAlchemy to serve data directly from the database.

---

## How to Use

### 1. Clone the Repository
Ensure the following has been installed in your environment 
- Python
- SQLAlchemy
- Pandas
- Matplotlib
- Flask: To create a RESTful API

run: python app.py 
then open http://127.0.0.1:5000 on your browser

