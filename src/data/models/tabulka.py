from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, DateTime, Float

from ..database import db
from ..mixins import CRUDModel

class Tabulka(CRUDModel):
    __tablename__ = 'tabulka'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True )
    SPZ = Column(String(7), nullable=False, index=False)
    Rychlost = Column(Float, nullable=False, index=True)
    datum_insertu= Column(DateTime)



    # Use custom constructor
    # pylint: disable=W0231
    def __init__(self, **kwargs):
        self.datum_insertu = datetime.utcnow()
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

