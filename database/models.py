from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    reference_id = Column(String, unique=True)

    name = Column(String)

    role = Column(String)

    city = Column(String)

    age = Column(Integer)

    income = Column(Integer)

    family_size = Column(Integer)

    status = Column(String)

    privacy_settings = Column(JSON)


class Verification(Base):

    __tablename__ = "verifications"

    id = Column(Integer, primary_key=True)

    donee_id = Column(Integer)

    surveyor_id = Column(Integer)

    report = Column(String)

    status = Column(String)


class Donation(Base):

    __tablename__ = "donations"

    id = Column(Integer, primary_key=True)

    donor_id = Column(Integer)

    donee_id = Column(Integer)

    amount = Column(Integer)

    status = Column(String)

from sqlalchemy import Column, String
from database.db import Base


class Registration(Base):

    __tablename__ = "registrations"

    reference_id = Column(String, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String)
    address = Column(String)
    support_type = Column(String)
    status = Column(String)