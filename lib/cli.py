# lib/cli.py
import inquirer
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, delete
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

DATABASE_URL ='sqlite:///sisterhoodofthetravelingplans.db'
engine= create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()



Base = declarative_base()

from helpers import (
    exit_program,
    helper_1
)


class Trip(Base):
    __tablename__ = "trips"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    attractions = relationship("Attraction", back_populates='trip')

class Attraction(Base):
    __tablename__ = "attractions"
    id = Column(Integer, primary_key=True)
    country = Column(String)
    city = Column(String)
    attraction_name = Column(String)
    age_limit = Column(Integer)
    trip_id = Column(Integer, ForeignKey("trips.id"))
    trip = relationship("Trip", back_populates="attractions")

    def __repr__(self):
        return f'{self.attraction_name} in {self.city}, {self.country}'

Base.metadata.create_all(engine)

global tripID

def create_trip():
    global tripID
    answers = inquirer.prompt([inquirer.Text(name='title', message="What would you like to call your trip?")])

    trip = session.query(Trip).filter(Trip.title == answers['title']).first()
    if not trip:
        trip = Trip(title = answers['title'])
        session.add(trip)
        session.commit()
        tripID = trip.id
        return trip
    print('That trip already exists! Please try again! :)')
    create_trip()
    # tripID = trip.id
    # return trip

def create_your_own_itinerary():
    global tripID
    country_ans = inquirer.prompt([inquirer.Text(name='country', message="Which country would you like to go to?")])
    city_ans = inquirer.prompt([inquirer.Text(name='city', message="Great choice! Which city would you like to go to?")])
    attr_name_ans = inquirer.prompt([inquirer.Text(name='attraction_name', message="That's amazing! Which attraction would you like to go to?")])
    age_limit_ans = inquirer.prompt([inquirer.Text(name='age_limit', message="So fun! What is the age limit for this?")])
    new_attr = Attraction(country = country_ans["country"], city = city_ans["city"], attraction_name = attr_name_ans["attraction_name"], age_limit = age_limit_ans["age_limit"], trip_id =tripID)
    session.add(new_attr)
    session.commit()
    print("Great addition!")
    questions = [
        inquirer.List(
            "options",
            message= "Further options:",
            choices=[
                "Add another stop!",
                "See existing itineraries",
                "Create another trip!",
                "Main menu",
                "Exit program"
            ])
            ]
    action = inquirer.prompt(questions)
    if action["options"] == "Add another stop!":
        create_your_own_itinerary()
    if action["options"] == "See existing itineraries":
        choose_a_trip()
    elif action["options"] == "Create another trip!":
        create_trip()
    elif action["options"] == "Main menu":
        main()
    elif action["options"] == "Exit program":
        exit_program()
    return new_attr

  
def add_attraction():
    global tripID


def choose_a_trip():
    questions = [
        inquirer.List(
            "trips", 
            message="What trip would you like to access?", 
            choices=[trip.title for trip in session.query(Trip).all()])
    ]
    answers = inquirer.prompt(questions)
    print(answers['trips'])
    chosen_trip = session.query(Trip).filter(Trip.title == answers["trips"]).first()
    print(chosen_trip.attractions)
    options = [
        inquirer.List(
        "attractions", 
        message = "What would you like to do with this trip?", 
        choices =[
            "Update", 
            "Delete this itinerary",
            "Copy this itinerary!", 
            "Choose A Different Existing Trip",
            "Create Another Itinerary!",
            "Main Menu",
            "Exit the program"
            ])
    ]
    action = inquirer.prompt(options)
    if action["attractions"] == "Update":
        options = [
        inquirer.List(
            "stops", 
            message="Which stop would you like to access?", 
            choices=chosen_trip.attractions)
        ]
        stop_options = inquirer.prompt(options)
        print(stop_options['stops'])
        # stop_to_edit = session.query(Attraction).filter_by(chosen_trip.id).first()
        # print(stop_to_edit)
        update_options = [
            inquirer.List(
                "attribute", 
                message="Which would you like to update?", 
                choices=[
                    "attraction_name",
                    "city",
                    "country"
                    ])
        ]
        chosen_update_options = inquirer.prompt(update_options)
        if chosen_update_options["attribute"] == "attraction_name":
            print(stop_options.result())
            # new_attraction = input("Enter a new name: ")
            # print(stop_to_edit)
            # stop_to_edit.attraction_name = new_attraction
            # session.add(stop_to_edit.attraction_name)
            # session.commit()

    elif action["attractions"] == "Delete this itinerary":
        if chosen_trip is not None:
            try:
                session.delete(chosen_trip)
                session.commit()
                print("Trip deleted successfully.")
            except Exception as e:
                print(f"An error occurred: {e}")
                session.rollback()
            else:
                print(" ")
    elif action["attractions"] == "Copy this itinerary!":
        print("copy function here")
    elif action["attractions"] == "Choose A Different Existing Trip":
        choose_a_trip()
    elif action["attractions"] == "Create Another Itinerary!":
        create_your_own_itinerary()
    elif action["attractions"] == "Main Menu":
        main()
    elif action["attractions"] == "Exit the program":
        exit_program()
    
    





countries = []
def list_countries():
    attractions = session.query(Attraction).all()
    for attraction in attractions:
        print(f"{index}. {attraction.country}")
        countries.append(attraction.country)
    for country in countries:
        print(country)


global name

def main():
    while True:
        global name
        name = input('Thanks for choosing us for your travel needs! What is your name: ')
        # menu()
        print(f"Congratulations {name} on your PTO approval! Please choose from the following options!")
        # inquire
        
        print("1. Create a trip")
        print("2. View Existing trips")
        print("0. Exit the program")
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_trip()
            post_trip_menu()
        elif choice == "2":
            choose_a_trip()
        else:
            print("Invalid choice")


def post_trip_menu():
    print("Thanks for creating a trip!")
    print("Please select an option from the below menu")
    print("1. Create your own itinerary!")
    print("2. Recommended itineraries")
    print("3. Access existing trips")
    print("0. Exit program")
    choice = input("> ")
    if choice == "0":
            exit_program()
    elif choice == "1":
        create_your_own_itinerary()
    elif choice == "2":
        print(" pre-existing itineraries coming soon!")
    elif choice == "3":
        choose_a_trip()
    else:
        print("Please select a valid option!")




 


if __name__ == "__main__":
    main()
