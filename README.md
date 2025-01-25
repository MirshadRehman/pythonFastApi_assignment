Project setup instrutions -
Download and install MongoDB, create a database "bookmanagementsystem"
Install fastapi, uvicorn, motor & pydantic inside the folder.
Run mongoDB and "use bookmanagementsystem"


Api Documentation -

base url : http://127.0.0.1:8000
1. List all books- <br/>
     GET /api/books
   Description: Fetches a paginated list of books from the database.
   Response: 200 OK-
   [
  {
    "id": "63d0fdfd1234567890abcdef",
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "isbn": "9783161484100",
    "price": 10.99,
    "quantity": 5,
    "published_date": "1925-04-10T00:00:00",
    "genre": "Classic",
    "description": "A novel about the American dream.",
    "created_at": "2025-01-01T12:00:00",
    "updated_at": "2025-01-10T15:00:00"
  }
   ]

2. Get book details by "id" -
     GET /api/books/{id}
   Description: Fetch details of a specific book by its unique ID.
                 id: The ID of the book
   Response:
   200 OK-
   {
  "id": "63d0fdfd1234567890abcdef",
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "isbn": "9783161484100",
  "price": 10.99,
  "quantity": 5,
  "published_date": "1925-04-10T00:00:00",
  "genre": "Classic",
  "description": "A novel about the American dream.",
  "created_at": "2025-01-01T12:00:00",
  "updated_at": "2025-01-10T15:00:00"
  }
  404 Not Found-
  {
  "detail": "Book not found"
  } 

3. Add New Book-
     POST /api/books
   Description: Adds a new book to the inventory.
   Request Body:
     {
      "title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "isbn": "9783161484100",
      "price": 10.99,
      "quantity": 5,
      "published_date": "1925-04-10T00:00:00",
      "genre": "Classic",
      "description": "A novel about the American dream."
    }
  Response:
    201 Created-
     {
  "id": "63d0fdfd1234567890abcdef",
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "isbn": "9783161484100",
  "price": 10.99,
  "quantity": 5,
  "published_date": "1925-04-10T00:00:00",
  "genre": "Classic",
  "description": "A novel about the American dream.",
  "created_at": "2025-01-01T12:00:00",
  "updated_at": "2025-01-01T12:00:00"
    }

4. Update Book details by "id"-
     PUT /api/books/{id}
   Description: Updates the details of a specific book.
   Request Body:
     You can update any field(s). For example:
     {
      "price": 12.99,
      "quantity": 10
     }
   Response:
     200 OK -
     {
      "id": "63d0fdfd1234567890abcdef",
      "title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "isbn": "9783161484100",
      "price": 12.99,
      "quantity": 10,
      "published_date": "1925-04-10T00:00:00",
      "genre": "Classic",
      "description": "A novel about the American dream.",
      "created_at": "2025-01-01T12:00:00",
      "updated_at": "2025-01-20T14:00:00"
    }
    400 Bad Request-
     {
      "detail": "No fields to update"
     }
    404 Not Found-
     {
      "detail": "Book not found"
     }

5. Remove Book by "id" -
     DELETE /api/books/{id}
   Description: Deletes a specific book by its unique ID.
   Response:
     200 OK-
       {
        "message": "Book deleted"
       }
     404 Not Found-
       {
        "message": "Book deleted"
       }

6. Search books by title, author, or genre-
   
