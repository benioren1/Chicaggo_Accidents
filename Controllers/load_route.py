from flask import Blueprint
from  services.load_data import load_data
bp_data = Blueprint('load',__name__)

@bp_data.route('/load_data', methods=['POST'])
def load_data_bp():
    load_data()
    return 'Data loaded successfully!', 200
