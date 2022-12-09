from flask import Blueprint, Response, request, jsonify
from marshmallow import ValidationError


from models import Request
from work_by_file import WorkByFile

main_bp = Blueprint('main', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query() -> Response:
    data = request.json
    try:
        Request().load(data=data)
    except ValidationError as error:
        return jsonify(error.messages), 400

    query_builder = WorkByFile()

    return jsonify(query_builder.query(data['cmd1'], data['value1']))


