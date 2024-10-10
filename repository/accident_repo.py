from database.connect import Location

def sum_accidents_by_beat(beat):
    result = Location.count_documents({'BEAT_OF_OCCURRENCE':beat})
    return result


def sum_accidents_by_date(beat,type_date,date):
    if type_date == 'day':
        result = Location.count_documents({'BEAT_OF_OCCURRENCE':beat, 'DATE_OF_OCCURRENCE': {'$dayOfYear': date}})