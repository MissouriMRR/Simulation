import sys
import json

def feet_to_unreal(qt):
    return meters_to_unreal(feet_to_meters(qt))

def coordinates_to_unreal(qt):
    return meters_to_unreal(coordintes_to_meters(qt))

def feet_to_meters(qt):
    return qt * 0.3048

def meters_to_unreal(qt):
    return qt * 100

def coordintes_to_meters(qt):
    return qt * 111139


def make_coordinates_relative(interop):
    center_lat = interop['mapCenterPos']['latitude']
    center_long = interop['mapCenterPos']['longitude']

    interop['lostCommsPos']['latitude'] = interop['lostCommsPos']['latitude'] - center_lat
    interop['lostCommsPos']['longitude'] = interop['lostCommsPos']['longitude'] - center_long

    for i in range(len(interop['flyZones']['boundaryPoints'])):
        interop['flyZones']['boundaryPoints'][i]['latitude'] = interop['flyZones']['boundaryPoints'][i]['latitude'] - center_lat
        interop['flyZones']['boundaryPoints'][i]['longitude'] = interop['flyZones']['boundaryPoints'][i]['longitude'] - center_long

    for i in range(len(interop['waypoints']))

def translate_coordinates_to_unreal(interop):
    interop['lostCommsPos']['longitude'] = coordinates_to_unreal(interop['lostCommsPos']['longitude'])
    interop['lostCommsPos']['latitude'] = coordinates_to_unreal(interop['lostCommsPos']['latitude'])


if __name__ == "__main__":
    interop_file = open(sys.argv[1], "r")
    interop_string = interop_file.read()

    interop = json.loads(interop_string)

    print(interop['lostCommsPos'])

    make_coordinates_relative(interop)
    
    print(interop['lostCommsPos'])

    translate_coordinates_to_unreal(interop)

    print(interop['lostCommsPos'])
    

    