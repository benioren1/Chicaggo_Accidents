import csv
from database.connect import *


def read_csv(csv_path):
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield row

def init_Chicago_db():
    Accidents.drop()
    Location.drop()
    Injuries.drop()
    Dates.drop()


    for row in read_csv("../data/Traffic_Crashes_-_Crashes - 20k rows.csv"):

        location = {
            'beat_of_occurrence': row['BEAT_OF_OCCURRENCE'],
            'street_no' : row['STREET_NO'],
            'street_direction': row['STREET_DIRECTION'],
            'street_name': row['STREET_NAME'],
            'longitude': row['LONGITUDE'],
            'latitude': row['LATITUDE'],
            'location': row['LOCATION']
        }

        locationId = Location.insert_one(location).inserted_id

        injuries = {
            'INJURIES_TOTAL': row['INJURIES_TOTAL'],
            'MOST_SEVERE_INJURY': row['MOST_SEVERE_INJURY'],
            'INJURIES_FATAL': row['INJURIES_FATAL'],
            'INJURIES_INCAPACITATING': row['INJURIES_INCAPACITATING'],
            'INJURIES_NON_INCAPACITATING': row['INJURIES_NON_INCAPACITATING'],
            'INJURIES_REPORTED_NOT_EVIDENT': row['INJURIES_REPORTED_NOT_EVIDENT'],
            'INJURIES_NO_INDICATION': row['INJURIES_NO_INDICATION'],
            'INJURIES_UNKNOWN': row['INJURIES_UNKNOWN']
        }
        injuriesId = Injuries.insert_one(injuries).inserted_id

        date = {
            'CRASH_DATE_EST_I': row['CRASH_DATE_EST_I'],
            'CRASH_DATE': row['CRASH_DATE'],
            'CRASH_HOUR': row['CRASH_HOUR'],
            'CRASH_DAY_OF_WEEK': row['CRASH_DAY_OF_WEEK'],
            'CRASH_MONTH': row['CRASH_MONTH']
        }

        datesId = Dates.insert_one(date).inserted_id

        Traffic_Conditions = {
            'DEVICE_CONDITION': row['DEVICE_CONDITION'],
            'WEATHER_CONDITION': row['WEATHER_CONDITION'],
            'LIGHTING_CONDITION': row['LIGHTING_CONDITION'],
            'TRAFFICWAY_TYPE': row['TRAFFICWAY_TYPE'],
            'LANE_CNT': row['LANE_CNT'],
            'ALIGNMENT': row['ALIGNMENT'],
            'ROADWAY_SURFACE_COND': row['ROADWAY_SURFACE_COND'],
            'ROAD_DEFECT': row['ROAD_DEFECT']
        }

        accident = {
            'CRASH_RECORD_ID': row['CRASH_RECORD_ID'],
            'POSTED_SPEED_LIMIT': row['POSTED_SPEED_LIMIT'],
            'TRAFFIC_CONTROL_DEVICE': row['TRAFFIC_CONTROL_DEVICE'],
            'FIRST_CRASH_TYPE': row['FIRST_CRASH_TYPE'],
            'REPORT_TYPE': row['REPORT_TYPE'],
            'CRASH_TYPE': row['CRASH_TYPE'],
            'INTERSECTION_RELATED_I': row['INTERSECTION_RELATED_I'],
            'NOT_RIGHT_OF_WAY_I': row['NOT_RIGHT_OF_WAY_I'],
            'HIT_AND_RUN_I': row['HIT_AND_RUN_I'],
            'DAMAGE': row['DAMAGE'],
            'DATE_POLICE_NOTIFIED': row['DATE_POLICE_NOTIFIED'],
            'PRIM_CONTRIBUTORY_CAUSE': row['PRIM_CONTRIBUTORY_CAUSE'],
            'SEC_CONTRIBUTORY_CAUSE': row['SEC_CONTRIBUTORY_CAUSE'],
            'PHOTOS_TAKEN_I': row['PHOTOS_TAKEN_I'],
            'STATEMENTS_TAKEN_I': row['STATEMENTS_TAKEN_I'],
            'DOORING_I': row['DOORING_I'],
            'WORK_ZONE_I': row['WORK_ZONE_I'],
            'WORK_ZONE_TYPE': row['WORK_ZONE_TYPE'],
            'WORKERS_PRESENT_I': row['WORKERS_PRESENT_I'],
            'NUM_UNITS': row['NUM_UNITS'],
            'location_id':locationId,
            'injuries_id': injuriesId,
            'date_id': datesId,
            'traffic_conditions_id': Traffic_Conditions
        }


        Accidents.insert_one(accident)

init_Chicago_db()