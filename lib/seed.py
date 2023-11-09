
# from sqlalchemy import Column, Integer, String, create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship, sessionmaker

# DATABASE_URL ='sqlite:///sisterhoodofthetravelingplans.db'
# engine= create_engine(DATABASE_URL)
# Session = sessionmaker(bind=engine)
# session = Session()

# Base = declarative_base()


# class PreMadeItineraries(Base):
#     __tablename__ = "premade_itineraries"

#     id = Column(Integer, primary_key = True)
#     country = Column(String)
#     attraction_1_city = Column(String)
#     attraction_1_activity = Column(String)
#     attraction_1_activity2 = Column(String)
#     attraction_2_city = Column(String)
#     attraction_2_activity = Column(String)
#     attraction_2_activity2 = Column(String)

#     def __repr__(self):
#         return f' {self.country} Itinerary: \n Cities and events: \n {self.attraction_1_city}:\n    {self.attraction_1_activity}\n  {self.attraction_1_activity2}\n {self.attraction_2_city}:\n     {self.attraction_2_activity}\n      {self.attraction_2_activity2}'
    
# france = PreMadeItineraries("France", "Paris", "Eiffel Tower", "Louvre Museum", "Nice", "St. Tropez", "Beach Day")
# session.add(france)


# print(france)
# france

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, Session

DATABASE_URL ='sqlite:///sisterhoodofthetravelingplans.db'
engine= create_engine(DATABASE_URL)
# Session = sessionmaker(bind=engine)
# session = Session()

Base = declarative_base()

class PreMadeItineraries(Base):
   __tablename__ = "premade_itineraries"

   id = Column(Integer, primary_key = True)
   country = Column(String)
   attraction_1_city = Column(String)
   attraction_1_activity = Column(String)
   attraction_1_activity2 = Column(String)
   attraction_2_city = Column(String)
   attraction_2_activity = Column(String)
   attraction_2_activity2 = Column(String)

   def __repr__(self):
       return f'\n\n{self.country} Itinerary:\n{self.attraction_1_city}:\n   {self.attraction_1_activity}\n   {self.attraction_1_activity2}\n{self.attraction_2_city}:\n   {self.attraction_2_activity}\n   {self.attraction_2_activity2}'

# PreMadeItineraries.__table__.drop(engine)  
Base.metadata.create_all(engine)

france = PreMadeItineraries(country="France", attraction_1_city="Paris", attraction_1_activity="Eiffel Tower", attraction_1_activity2="Louvre Museum", attraction_2_city="Nice", attraction_2_activity="St. Tropez", attraction_2_activity2="Beach Day")
spain = PreMadeItineraries(country ="Spain", attraction_1_city="Madrid", attraction_1_activity="Prado Museum", attraction_1_activity2="Sagrada Familia", attraction_2_city="Barcelona", attraction_2_activity="Beach", attraction_2_activity2="Football Match")
india = PreMadeItineraries(country ="India", attraction_1_city="Delhi", attraction_1_activity="Red Fort", attraction_1_activity2="Day trip to Agra", attraction_2_city="Pushkar", attraction_2_activity="Savitri Mata Temple", attraction_2_activity2="Pushkar Lake")
ireland = PreMadeItineraries(country ="Ireland", attraction_1_city="Dublin", attraction_1_activity="Trinity College Library", attraction_1_activity2="Temple Bar", attraction_2_city="Inis Moor", attraction_2_activity="Bikeride around island", attraction_2_activity2="Get traditional knitwear")

# with Session(engine) as session:

    # session.add(france)
    # session.add(spain)
    # session.add(india)
    # session.add(ireland)
    # session.commit()
