from marshmallow import Schema, fields, validates_schema, ValidationError

VALID_CMD = ('filter', 'map', 'unique', 'sort', 'limit')

class Request(Schema):
    cmd1 = fields.Str(required=True)
    value1 = fields.Str(required=True)

    @validates_schema
    def validate_cmd_params(self, values):
        if values['cmd1'] not in VALID_CMD:
            raise ValidationError('cmd 1 contains invalid value')
