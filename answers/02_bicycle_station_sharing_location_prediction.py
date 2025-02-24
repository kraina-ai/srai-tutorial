# Fill changes in the appropriate cells
train_city = "Amsterdam"
validation_city = "Utrecht"
test_city = "Rotterdam"

###

bicycle_stations = OSMOnlineLoader().load(
    area=regions, tags={"amenity": "charging_station"}
)

###

H3_RESOLUTION = 10
H3_PREDICTION_RANGE = 5
H3_NEIGHBOURS = 5

###
