Project setup instrutions -                                                       <br/>
Download and install MongoDB, create a database "bookmanagementsystem"            <br/>
Install fastapi, uvicorn, motor & pydantic inside the folder.                     <br/>
Run mongoDB and "use bookmanagementsystem"                                        <br/>
<br/>

Api Documentation -                                                               <br/>

base url : http://127.0.0.1:8000                                                  <br/>
1. List all books-                                                                <br/>
     GET /api/books                                                               <br/>
   Description: Fetches a paginated list of books from the database.              <br/>
   Response: 200 OK-                                                              <br/>
   example-                                                                       <br/>
   [
  {
    "id": "63d0fdfd1234567890abcdef",<br/>
    "title": "The Great Gatsby",<br/>
    "author": "F. Scott Fitzgerald",<br/>
    "isbn": "9783161484100",<br/>
    "price": 10.99,<br/>
    "quantity": 5,<br/>
    "published_date": "1925-04-10T00:00:00",<br/>
    "genre": "Classic",<br/>
    "description": "A novel about the American dream.",<br/>
    "created_at": "2025-01-01T12:00:00",<br/>
    "updated_at": "2025-01-10T15:00:00"     <br/>
  }
   ]                                                       <br/>
<br/>     
2. Get book details by "id" -                              <br/>
     GET /api/books/{id}                                   <br/>
   Description: Fetch details of a specific book by its unique ID.     <br/>
                 id: The ID of the book          <br/>
   Response:          <br/>
   200 OK-          <br/>
   {
  "id": "63d0fdfd1234567890abcdef",     <br/>
  "title": "The Great Gatsby",     <br/>
  "author": "F. Scott Fitzgerald",     <br/>
  "isbn": "9783161484100",     <br/>
  "price": 10.99,          <br/>
  "quantity": 5,          <br/>
  "published_date": "1925-04-10T00:00:00",     <br/>
  "genre": "Classic",          <br/>
  "description": "A novel about the American dream.",     <br/>
  "created_at": "2025-01-01T12:00:00",     <br/>
  "updated_at": "2025-01-10T15:00:00"     <br/>
  }<br/>
  404 Not Found-          <br/>
  {
  "detail": "Book not found"
  }                                                    <br/>
 <br/>
3. Add New Book-                                        <br/>
     POST /api/books               <br/>
   Description: Adds a new book to the inventory.     <br/>
   Request Body:<br/>
     {
      "title": "The Great Gatsby",          <br/>
      "author": "F. Scott Fitzgerald",     <br/>
      "isbn": "9783161484100",     <br/>
      "price": 10.99,          <br/>
      "quantity": 5,          <br/>
      "published_date": "1925-04-10T00:00:00",          <br/>
      "genre": "Classic",          <br/>
      "description": "A novel about the American dream."     <br/>
    }     <br/>
  Response:          <br/>
    201 Created-          <br/>
     {     
  "id": "63d0fdfd1234567890abcdef",     <br/>
  "title": "The Great Gatsby",     <br/>
  "author": "F. Scott Fitzgerald",     <br/>
  "isbn": "9783161484100",          <br/>
  "price": 10.99,          <br/>
  "quantity": 5,          <br/>
  "published_date": "1925-04-10T00:00:00",          <br/>
  "genre": "Classic",     <br/>
  "description": "A novel about the American dream.",     <br/>
  "created_at": "2025-01-01T12:00:00",          <br/>
  "updated_at": "2025-01-01T12:00:00"          <br/>
    }
<br/>
4. Update Book details by "id"-          <br/>
     PUT /api/books/{id}               <br/>
   Description: Updates the details of a specific book.          <br/>
   Request Body:          <br/>
     You can update any field(s). For example:<br/>
     {     
      "price": 12.99,     <br/>
      "quantity": 10     <br/>
     }<br/>
   Response:<br/>
     200 OK -<br/>
     {
      "id": "63d0fdfd1234567890abcdef",     <br/>
      "title": "The Great Gatsby",     <br/>
      "author": "F. Scott Fitzgerald",     <br/>
      "isbn": "9783161484100",     <br/>
      "price": 12.99,     <br/>
      "quantity": 10,     <br/>
      "published_date": "1925-04-10T00:00:00",     <br/>
      "genre": "Classic",     <br/>
      "description": "A novel about the American dream.",     <br/>
      "created_at": "2025-01-01T12:00:00",     <br/>
      "updated_at": "2025-01-20T14:00:00"     <br/>
    }<br/>
    400 Bad Request-          <br/>
     {
      "detail": "No fields to update"
     }<br/>
    404 Not Found-<br/>
     {
      "detail": "Book not found"
     }
<br/>
5. Remove Book by "id" -          <br/>
     DELETE /api/books/{id}               <br/>
   Description: Deletes a specific book by its unique ID.     <br/>
   Response:     <br/>
     200 OK-     <br/>
       {
        "message": "Book deleted"
       }<br/>
     404 Not Found-     <br/>
       {
        "message": "Book deleted"
       }
<br/>
6. Search books by title, author, or genre- <br/>
        GET /api/books/search               <br/>
   Description: Search for books by title, author, or genre.<br/>
   Response:                    <br/>
        status code- 200 OK     <br/>
        body-                   <br/>
             [
                 {
                   "id": "63d0fdfd1234567890abcdef",<br/>
                   "title": "The Great Gatsby",<br/>
                   "author": "F. Scott Fitzgerald",<br/>
                   "isbn": "9783161484100",<br/>
                   "price": 10.99,<br/>
                   "quantity": 5,<br/>
                   "published_date": "1925-04-10T00:00:00",<br/>
                   "genre": "Classic",<br/>
                   "description": "A novel about the American dream.",<br/>
                   "created_at": "2025-01-01T12:00:00",<br/>
                   "updated_at": "2025-01-10T15:00:00"<br/>
                 }
             ]
