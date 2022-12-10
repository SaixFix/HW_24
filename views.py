from flask import Blueprint, Response, request, jsonify
from marshmallow import ValidationError

from models import BatchRequestParams
from work_by_file import WorkByFile

main_bp = Blueprint('main', __name__)


@main_bp.route('/perform_query', methods=['POST'])
def perform_query() -> Response:
    # принимаем фильтры по схеме и выдаем ошибку если не совпадает
    try:
        params = BatchRequestParams().load(data=request.json)
    except ValidationError as error:
        return jsonify(error.messages), 400

    query_builder = WorkByFile()

    # итерируемся по принятому jsony и применяем заданные фильтры
    result = None
    for query in params['queries']:
        result = query_builder.query(
            cmd=query['cmd'],
            value=query['value'],
            data=result,
        )

    return jsonify(result)
