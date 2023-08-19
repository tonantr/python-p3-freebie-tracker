#!/usr/bin/env python3

# Script goes here!

from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Freebie, Company, Dev

if __name__ == '__main__':
    engine = create_engine('sqlite:///freebies.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Freebie).delete()
    session.query(Company).delete()
    session.query(Dev).delete()

    fake = Faker()
    
    companies = []
    for i in range(50):
        company = Company(
            name = fake.unique.name(),
            founding_year = random.randint(2001, 2099)
        )

        session.add(company)
        session.commit()

        companies.append(company)

    
    devs = []
    for i in range(50):
        dev = Dev(
            name = fake.unique.name()
        )

        session.add(dev)
        session.commit()

        devs.append(dev)
    

    freebies = []
    for company, dev in zip(companies, devs):
        for i in range(random.randint(1, 10)):
            freebie = Freebie(
                item_name = fake.unique.name(),
                value = random.randint(1, 20),
                company_id = company.id,
                dev_id = dev.id
            )

            freebies.append(freebie)


    session.add_all(freebies)
    session.commit()
    session.close()


        
