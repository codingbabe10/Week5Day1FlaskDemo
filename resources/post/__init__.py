from flask_smorest import Blueprint
bp = Blueprint('posts',__name__, description='Ops on Posts')

from . import routes