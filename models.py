from pydantic import BaseModel

# Define a Book class inheriting from BaseModel
class Book(BaseModel):
    # Fields representing book attributes with their respective data types
    title: str  # Title of the book (string)
    author: str  # Author of the book (string)
    isbn: str  # ISBN (International Standard Book Number) of the book (string)
    publication_year: int  # Year of publication (integer)
