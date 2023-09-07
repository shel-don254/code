import random
import string
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review

def generate_random_name():
    first_name = ''.join(random.choices(string.ascii_uppercase, k=5))
    last_name = ''.join(random.choices(string.ascii_uppercase, k=5))
    return f"{first_name} {last_name}"

def seed_database():
    engine = create_engine('sqlite:///restaurants.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # session.query(Restaurant).delete()
    # session.query(Customer).delete()
    # session.query(Reviews).delete()
    # session.commit()

    print("Seeding...")

    restaurants = []
    for i in range(3):
        restaurant = Restaurant(
            name=generate_random_name(),
            price=random.randint(1, 5)
        )
        session.add(restaurant)
        restaurants.append(restaurant)

    customers = []
    for i in range(50):
        customer = Customer(
            first_name=generate_random_name(),
            last_name=generate_random_name()
        )
        session.add(customer)
        customers.append(customer)

    for restaurant in restaurants:
        for _ in range(random.randint(1, 5)):
            customer = random.choice(customers)

            review = Review(
                ratings=random.randint(1, 5),
                customer_id=customer.id,
                restaurant_id=restaurant.id
            )
            session.add(review)

    session.commit()
    session.close()
    print("Seed completed.")

if __name__ == '__main__':
    seed_database()
