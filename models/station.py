stations = []
class Station:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    @staticmethod
    def get_stations():
        return stations
    
    def create_station(self, fm_band):
        station = dict(
            name = self.name,
            address = self.address,
            fm_band = fm_band
        )

        stations.append(station)
        return station
    
    @staticmethod
    def get_station(name):

        for station in stations:
            if station["name"] == name:
                return station
            else:
                return None
        