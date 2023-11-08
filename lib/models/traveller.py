# lib/sqlalchemy_sandbox.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    trips = relationship("Participant", back_populates= "users")

    def add_trip(self, trip):
        self.trips.append(trip)

    def remove_trip(self, trip):
        self.trips.remove(trip)

    def display_trips(self):
        all_trips = []

    
    def add_user(session, name, age):
        user = User(name = name, age=age)
        session.add(user)
        session.commit()
    
    def delete_user(session, user_id):
        user = session.query(User).get(user_id)
        if user:
            session.delete(user)
            session.commit()

    

class Participant(Base):
    __tablename__ = 'Participants'
    id = Column(Integer, primary_key = True)
    trip_id = Column(Integer, ForeignKey("trips.id"))
    user_id = Column(Integer, ForeignKey('users.id')  )

    # def participant_remove_instance(self, model, model_id):
    #     self.model.remove(model_id)
    
    # def participant_add_instance(self,model, model_id):
    #     self.model.remove(model.id)



class Trip(Base):
    __tablename__ = "trips"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    participants = relationship("Participant", backref='trips')

    def add_participant(self, participant):
        self.participants.append(participant)

    def remove_participant(self, participant):
        self.participants.remove(participant)
    
    def delete_Trip(session, trip_id):
        trip = session.query(Trip).get(trip_id)
        if trip:
            session.delete(trip)
            session.commit()


    

class Stop(Base):
    __tablename__ = "stops"
    id = Column(Integer(), primary_key=True)
    trip_id = Column(Integer, ForeignKey('trips.id'))
    attraction_id = Column(Integer, ForeignKey= ("attractions.id"))



class Attractions(Base):
    __tablename__ = "attractions"
    id = Column(Integer, primary_key=True)
    country = Column(String)
    city = Column(String)
    attraction_name = Column(String)
    age_limit = Column(Integer)
    stops = relationship("Stop", backref = "stops")




