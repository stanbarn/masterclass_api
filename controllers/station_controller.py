from flask import jsonify
from models.station import Station

class StationController:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    @staticmethod
    def get_station(name):

        if not name or name.isspace():
            return jsonify({
                "message":"name is required"
            }),400

        if type(name) != str:
            return jsonify({
                "message": "name should be a string"
            }),400

        station_model = Station("","")
        my_station = station_model.get_station(name)
        if my_station is None:
            return jsonify({
                "message":"station was not found"
            }),200
        
        return jsonify({
            "message":"successful",
            "station":my_station
        }), 200
    
    def create_station(self, fm_band):
        if not self.name or self.name.isspace():
            return jsonify({
                "message":"name is required"
            }),400

        if type(self.name) != str:
            return jsonify({
                "message": "name should be a string"
            }),400
        if not self.address or self.address.isspace():
            return jsonify({
                "message":"address is required"
            }),400

        if type(self.address) != str:
            return jsonify({
                "message": "address should be a string"
            }),400
        
        station_model = Station(self.name,self.address)
        station = station_model.create_station(fm_band)


        return jsonify({
            "message":"station created successfully",
            "station" :station
        }), 201
    
    @staticmethod
    def get_stations():
        model  = Station("","")

        stations = model.get_stations()

        if len(stations) == 0:
            return jsonify({
                "message":"sorry! no statiosn were found"
            })

        return jsonify({
            "message":"successful",
            "stations":stations
        })

    @app.route('/api/v1/songs/<name>/plays')
    def get_plays_for_song(name)
