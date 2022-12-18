import os
from flask import Blueprint, Response, request, jsonify
from werkzeug.exceptions import BadRequest

from work_by_file import WorkByFile

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

main_bp = Blueprint('main', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query() -> Response:
    params = request.json
    file_path = os.path.join(DATA_DIR, params['file']['filename'])

    if not os.path.exists(file_path):
        raise BadRequest('file not exist')

    query_builder = WorkByFile(file_path)

    # итерируемся по принятому json и применяем заданные фильтры
    result = None
    for query in params['queries']:
        result = query_builder.query(
            cmd=query['cmd'],
            value=query['value'],
            data=result,
        )

    return jsonify(result)
