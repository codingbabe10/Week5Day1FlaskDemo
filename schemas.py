from marshmallow import Schema, fields

class user (schema):
    id=fields.str(dump_only = True)
    email = fields.Str(required = True)
    username = fields.Str(required = True)
    password = fields.str(required =True, load_only = True)
    first_name = fields.Str()
    last_name = fields.Str()

class post(schema):
    id = fields.str(dump_only=True)
    body = fields.Str(required = True)
    timestamp = fields.datetime(dump_only=True)
    