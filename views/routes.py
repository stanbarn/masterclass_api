from flask import Flask, jsonify, request
from controllers.station_controller import StationController

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def index():
    return "This is the MusicX Api"

@app.route("/api/v1/stations/<name>", methods = ["GET"])
def get_station(name):
    station_controller =StationController("","")

    station = station_controller.get_station(name)
    return station

@app.route('/api/v1/stations', methods = ["POST"])
def create_station():
    data = request.get_json()

    name = data.get('name')
    address = data.get('address')
    fm_band = data.get('fm_band')

    station_controller =StationController(name, address)

    station = station_controller.create_station(fm_band)

    return station

@app.route('/api/v1/stations', methods = ["GET"])
def get_stations():
    station_controller =StationController("","")
    stations = station_controller.get_stations()
    return stations