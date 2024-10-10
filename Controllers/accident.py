from flask import Blueprint, jsonify
from repository.accident_repo import sum_accidents_by_beat

bp_accident = Blueprint('accident',__name__)

@bp_accident.route('/by_beat/<string:beat>',methods=['GET'])
def accidents_by_beat(beat):
    result = sum_accidents_by_beat(beat)
    return jsonify({
        'beat': beat,
        'accidents': result
    })
