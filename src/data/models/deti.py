from flask_login import UserMixin
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, Date

from ..database import db
from ..mixins import CRUDModel
from ..util import generate_random_token
from ...settings import app_config
from ...extensions import bcrypt

class Deti(CRUDModel):
    __tablename__ = 'deti'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True,autoincrement=True)
    jmeno = Column(String(50), nullable=False, index=True, doc="Jmeno")
    prijmeni = Column(String(50), nullable=False, index=True, doc="Prijmeni")
    datum_nar = Column(Date,nullable=False,doc="Datum narozeni")

    # Use custom constructor
    # pylint: disable=W0231
    def __init__(self, **kwargs):
        self.activate_token = generate_random_token()
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

    @staticmethod
    def find_by_email(email):
        return db.session.query(Deti).filter_by(email=email).scalar()

    @staticmethod
    def find_by_username(username):
        return db.session.query(Deti).filter_by(username=username).scalar()

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
