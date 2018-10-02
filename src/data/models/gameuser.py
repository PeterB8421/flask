from flask_login import UserMixin
from sqlalchemy.schema import Column
from sqlalchemy.types import Boolean, Integer, String, Date

from ..database import db
from ..mixins import CRUDModel
from ..util import generate_random_token
from ...settings import app_config
from ...extensions import bcrypt

class GameUser(CRUDModel):
    __tablename__ = 'gameusers'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True,autoincrement=True)
    email = Column(String(64), nullable=False, unique=True, index=True, doc="The user's email address.")
    username = Column(String(64), nullable=False, unique=True, index=True, doc="The user's username.")
    datumposlednihopristupu = Column(Date,nullable=False,doc="Date")

    # Use custom constructor
    # pylint: disable=W0231
    def __init__(self, **kwargs):
        self.activate_token = generate_random_token()
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

    @staticmethod
    def find_by_email(email):
        return db.session.query(GameUser).filter_by(email=email).scalar()

    @staticmethod
    def find_by_username(username):
        return db.session.query(GameUser).filter_by(username=username).scalar()

    # pylint: disable=R0201
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password, app_config.BCRYPT_LOG_ROUNDS)

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def is_verified(self):
        " Returns whether a user has verified their email "
        return self.verified is True
