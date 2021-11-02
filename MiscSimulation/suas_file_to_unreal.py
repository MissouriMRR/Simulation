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

    for j in range(len(interop['flyZones'])):
        for i in range(len(interop['flyZones'][j]['boundaryPoints'])):
            interop['flyZones'][j]['boundaryPoints'][i]['latitude'] = interop['flyZones'][j]['boundaryPoints'][i]['latitude'] - center_lat
            interop['flyZones'][j]['boundaryPoints'][i]['longitude'] = interop['flyZones'][j]['boundaryPoints'][i]['longitude'] - center_long

    for i in range(len(interop['waypoints'])):
        interop['waypoints'][i]['latitude'] = interop['waypoints'][i]['latitude'] - center_lat
        interop['waypoints'][i]['longitude'] = interop['waypoints'][i]['longitude'] - center_long

    for i in range(len(interop['searchGridPoints'])):
        interop['searchGridPoints'][i]['latitude'] = interop['searchGridPoints'][i]['latitude'] - center_lat
        interop['searchGridPoints'][i]['longitude'] = interop['searchGridPoints'][i]['longitude'] - center_long

    interop['offAxisOdlcPos']['latitude'] = interop['offAxisOdlcPos']['latitude'] - center_lat
    interop['offAxisOdlcPos']['longitude'] = interop['offAxisOdlcPos']['longitude'] - center_long

    interop['emergentLastKnownPos']['latitude'] = interop['emergentLastKnownPos']['latitude'] - center_lat
    interop['emergentLastKnownPos']['longitude'] = interop['emergentLastKnownPos']['longitude'] - center_long

    for i in range(len(interop['airDropBoundaryPoints'])):
        interop['airDropBoundaryPoints'][i]['latitude'] = interop['airDropBoundaryPoints'][i]['latitude'] - center_lat
        interop['airDropBoundaryPoints'][i]['longitude'] = interop['airDropBoundaryPoints'][i]['longitude'] - center_long

    interop['airDropPos']['latitude'] = interop['airDropPos']['latitude'] - center_lat
    interop['airDropPos']['longitude'] = interop['airDropPos']['longitude'] - center_long

    interop['ugvDrivePos']['latitude'] = interop['ugvDrivePos']['latitude'] - center_lat
    interop['ugvDrivePos']['longitude'] = interop['ugvDrivePos']['longitude'] - center_long

    for i in range(len(interop['stationaryObstacles'])):
        interop['stationaryObstacles'][i]['latitude'] = interop['stationaryObstacles'][i]['latitude'] - center_lat
        interop['stationaryObstacles'][i]['longitude'] = interop['stationaryObstacles'][i]['longitude'] - center_long


def translate_coordinates_to_unreal(interop):
    interop['lostCommsPos']['longitude'] = coordinates_to_unreal(interop['lostCommsPos']['longitude'])
    interop['lostCommsPos']['latitude'] = coordinates_to_unreal(interop['lostCommsPos']['latitude'])

    for j in range(len(interop['flyZones'])):
        for i in range(len(interop['flyZones'][j]['boundaryPoints'])):
            interop['flyZones'][j]['boundaryPoints'][i]['latitude'] = coordinates_to_unreal(interop['flyZones'][j]['boundaryPoints'][i]['latitude'])
            interop['flyZones'][j]['boundaryPoints'][i]['longitude'] = coordinates_to_unreal(interop['flyZones'][j]['boundaryPoints'][i]['longitude'])

    for i in range(len(interop['waypoints'])):
        interop['waypoints'][i]['latitude'] = coordinates_to_unreal(interop['waypoints'][i]['latitude'])
        interop['waypoints'][i]['longitude'] = coordinates_to_unreal(interop['waypoints'][i]['longitude'])

    for i in range(len(interop['searchGridPoints'])):
        interop['searchGridPoints'][i]['latitude'] = coordinates_to_unreal(interop['searchGridPoints'][i]['latitude'])
        interop['searchGridPoints'][i]['longitude'] = coordinates_to_unreal(interop['searchGridPoints'][i]['longitude'])

    interop['offAxisOdlcPos']['latitude'] = coordinates_to_unreal(interop['offAxisOdlcPos']['latitude'])
    interop['offAxisOdlcPos']['longitude'] = coordinates_to_unreal(interop['offAxisOdlcPos']['longitude'])

    interop['emergentLastKnownPos']['latitude'] = coordinates_to_unreal(interop['emergentLastKnownPos']['latitude'])
    interop['emergentLastKnownPos']['longitude'] = coordinates_to_unreal(interop['emergentLastKnownPos']['longitude'])

    for i in range(len(interop['airDropBoundaryPoints'])):
        interop['airDropBoundaryPoints'][i]['latitude'] = coordinates_to_unreal(interop['airDropBoundaryPoints'][i]['latitude'])
        interop['airDropBoundaryPoints'][i]['longitude'] = coordinates_to_unreal(interop['airDropBoundaryPoints'][i]['longitude'])

    interop['airDropPos']['latitude'] = coordinates_to_unreal(interop['airDropPos']['latitude'])
    interop['airDropPos']['longitude'] = coordinates_to_unreal(interop['airDropPos']['longitude'])

    interop['ugvDrivePos']['latitude'] = coordinates_to_unreal(interop['ugvDrivePos']['latitude'])
    interop['ugvDrivePos']['longitude'] = coordinates_to_unreal(interop['ugvDrivePos']['longitude'])

    for i in range(len(interop['stationaryObstacles'])):
        interop['stationaryObstacles'][i]['latitude'] = coordinates_to_unreal(interop['stationaryObstacles'][i]['latitude'])
        interop['stationaryObstacles'][i]['longitude'] = coordinates_to_unreal(interop['stationaryObstacles'][i]['longitude'])

    interop['mapCenterPos']['latitude'] = 0
    interop['mapCenterPos']['longitude'] = 0


def translate_distances_to_unreal(interop):
    for j in range(len(interop['flyZones'])):
        interop['flyZones'][j]['altitudeMin'] = feet_to_unreal(interop['flyZones'][j]['altitudeMin'])
        interop['flyZones'][j]['altitudeMax'] = feet_to_unreal(interop['flyZones'][j]['altitudeMax'])

    for i in range(len(interop['waypoints'])):
        interop['waypoints'][i]['altitude'] = feet_to_unreal(interop['waypoints'][i]['altitude'])

    for i in range(len(interop['stationaryObstacles'])):
        interop['stationaryObstacles'][i]['radius'] = feet_to_unreal(interop['stationaryObstacles'][i]['radius'])
        interop['stationaryObstacles'][i]['height'] = feet_to_unreal(interop['stationaryObstacles'][i]['height'])

    interop['mapHeight'] = feet_to_unreal(interop['mapHeight'])
 

if __name__ == "__main__":
    interop_file = open(sys.argv[1], "r")
    interop_string = interop_file.read()

    interop = json.loads(interop_string)

    make_coordinates_relative(interop)

    translate_coordinates_to_unreal(interop)
    translate_distances_to_unreal(interop)

    output_file = open(sys.argv[2], "w")
    
    json.dump(interop, output_file, indent=2)