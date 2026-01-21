# Testing Library Search Using REST API (Python)

## Overview
This project focuses on the robust testing of REST API endpoints designed for a Library Management System. The primary goal is to validate resource management functionalities, specifically focusing on the `/resources` and `/book` endpoints. The project covers Functional Testing (CRUD), Performance Testing, Error Handling, and Accessibility validation.

## Objectives
* **Resource Management:** Implement and test CRUD (Create, Read, Update, Delete) operations for library resources.
* **Performance Testing:** Measure and analyze API response times and latency.
* **Validation:** Ensure proper HTTP status codes and response structures for valid and invalid parameters.
* **Error Handling:** Evaluate how the API handles edge cases and non-existent resources.
* **Accessibility:** Verify API accessibility via HTTP/HTTPS.

## Tech Stack
* **Language:** Python
* **Frontend:** Streamlit
* **Database/ORM:** SQLAlchemy
* **Testing Tools:**
    * Postman (Manual API Testing)
    * Python `requests` library (Automated Testing)

## Features & Endpoints
The following API operations were implemented and tested:

### 1. CRUD Operations
* **GET** `/book`: List and retrieve all books.
* **GET** `/book/{id}`: Fetch a specific book by ID.
* **POST** `/book`: Add a new book to the library.
* **PATCH** `/book/{id}`: Update specific attributes (e.g., year) of an existing book.
* **DELETE** `/book/{id}`: Remove a book from the system.

### 2. Search Functionality (Frontend)
* Get Book by ID
* Get Books by Name
* Get Books by Writer

### 3. Testing Scenarios
* **Latency Checks:** Measuring response time (e.g., ~15ms for GET requests).
* **Error Handling:** Verifying `404 Not Found` for non-existent IDs and `409 Conflict` for duplicate entries.
* **Protocol Validation:** Ensuring the API protocol is correctly identified (HTTP vs HTTPS).

## Installation & Usage

  **Install Dependencies**
    Ensure you have `streamlit`, `sqlalchemy`, `requests`, and `watchdog` installed.
    ```bash
    pip install streamlit sqlalchemy requests watchdog
    ```

 **Run the Application**
    Launch the Streamlit frontend:
    ```bash
    streamlit run front.py
    ```
    *The app will be accessible at `http://localhost:8501`.*

## References
* [Real Python: API Integration](https://realpython.com/api-integration-in-python/)
* [W3Schools: Python Requests Module](https://www.w3schools.com/python/module_requests.asp)
