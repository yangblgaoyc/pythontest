from flask import Blueprint
bp = Blueprint('hello', __name__)

from . import hello
from . import default

from . import index
from . import login
from . import user
from . import post