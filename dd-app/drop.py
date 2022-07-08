from flask import (Blueprint, request, jsonify)

from . import db
import uuid

bp = Blueprint('drop', __name__, url_prefix='/drop')


@bp.route('/dropme', methods=["POST"])
def add_drop():
    json = request.get_json()
    print(json['data'])
    path = uuid.uuid4().hex
    db.get_db().execute("insert into drop_table(path, data) values (?,?)", (path, json['data'],))
    db.get_db().commit()

    return jsonify(success=True, path=path)


@bp.route('/retrieve/<path_id>', methods=["GET"])
def retrieve(path_id):
    print(path_id)
    cursor = db.get_db().cursor()
    cursor.execute("select data from drop_table where path = ?", (path_id,))
    record = cursor.fetchone()
    print(record[0])
    print(jsonify(success=True, data=record[0]).get_json())
    return jsonify(success=True, data=record[0])
