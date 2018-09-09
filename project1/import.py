import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    print("dropping the old table")
    db.execute("DROP TABLE books RESTRICT")

    print("re-creating the new table 'books'")
    db.execute("CREATE TABLE books (book_id SERIAL PRIMARY KEY, isbn VARCHAR, title VARCHAR, author VARCHAR, year VARCHAR)")

    print(f"Opening books.....")
    f = open("books2.csv")
    print(f"Reading books.....")
    reader = csv.reader(f)
        # next(reader, None)
    print(f"Looping through books.....")
    line = 0
    for ISBN, title, author, year in reader:
        line+=1
        print(line, ISBN, title, author, year)
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)", {"isbn": ISBN, "title": title, "author": author, "year": year})        
    print(f"Committing books.....")
    db.commit()
    print(f"Added all the books into the database.")

if __name__ == "__main__":
    main()

