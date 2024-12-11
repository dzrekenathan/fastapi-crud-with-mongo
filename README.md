# FastAPI CRUD with MongoDB

This is a simple CRUD FastAPI application that uses MongoDB for data storage.

## How to Set Up the Project

### 1. Clone the Project
```bash
git clone <repository_url>
```

### 2. Open the Project Directory
```bash
cd fastapi-crud-with-mongo
```

### 3. Create a Virtual Environment
```bash
python -m venv venv
```

### 4. Activate the Virtual Environment
#### On Windows:
```bash
venv\Scripts\activate
```
#### On Linux/macOS:
```bash
source venv/bin/activate
```

### 5. Install Required Dependencies
```bash
pip install -r requirements.txt
```

### 6. Configure MongoDB
1. Install the MongoDB extension in VS Code (optional but recommended).
2. Follow the steps to establish a connection to your local MongoDB instance.
3. Create a `users` collection in the MongoDB database.

## Running the Application

### Start the FastAPI Development Server
```bash
uvicorn main:app --reload
```

The API will be available at:
- REST API Base URL: [http://localhost:8000](http://localhost:8000)

## API Documentation
FastAPI automatically generates interactive API documentation:
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

These interfaces allow you to explore and test API endpoints.

## Example Endpoints

### Create a New User
**POST /**
- Request body: JSON object with user details.

### Retrieve All Users
**GET /**

### Retrieve a User by ID
**GET /{id}**
- Path parameter: `id` (user ID).

### Update a User
**PUT /{id}**
- Path parameter: `id` (user ID).
- Request body: JSON object with updated user details.

### Delete a User
**DELETE /{id}**
- Path parameter: `id` (user ID).

