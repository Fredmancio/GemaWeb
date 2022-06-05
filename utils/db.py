from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import *

pending = PendingRollbackError
integrity = IntegrityError

db = SQLAlchemy()