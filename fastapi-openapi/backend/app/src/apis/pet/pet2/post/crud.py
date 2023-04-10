
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # items = relationship("Item", back_populates="owner")

    def as_dict(self):
        print(self.__table__.columns)
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
