import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    print(f"Opening books.....")
    f = open("books2.csv")
    # with open('books.csv') as csvfile:
        # reader = csv.DictReader(csvfile)
    print(f"Reading books.....")
    reader = csv.reader(f)
        # next(reader, None)
    print(f"Looping through books.....")
    for ISBN, title, author, year in reader:
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)", {"isbn": ISBN, "title": title, "author": author, "year": year})        
    print(f"Committing books.....")
    db.commit()
    print(f"Added all the books into the database.")

if __name__ == "__main__":
    main()

