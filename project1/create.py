import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    db.execute("CREATE TABLE books (book_id SERIAL PRIMARY KEY, isbn VARCHAR NOT NULL, title VARCHAR NOT NULL, author VARCHAR NOT NULL, year VARCHAR NOT NULL)")
    db.execute("CREATE TABLE users (user_id SERIAL PRIMARY KEY, username VARCHAR NOT NULL, password VARCHAR NOT NULL)")
    db.execute("CREATE TABLE reviews (review_id SERIAL PRIMARY KEY, review VARCHAR NOT NULL)")    
    db.commit()
    print(f"Created the table with all fields - BOOM!!")

if __name__ == "__main__":
    main()
