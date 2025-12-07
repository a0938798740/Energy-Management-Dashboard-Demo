# Energy Management System - Web Dashboard (Demo)

This repository serves as the **control plane** for an IoT-based energy management system. It provides a RESTful API and web interface for users to authenticate, monitor device status, and dispatch asynchronous tasks (such as data crawling) to background workers.

>⚠️ Note on UI/Frontend:
To comply with confidentiality agreements, the frontend interface (HTML/JS templates) and proprietary visualization logic have been excluded from this repository. This demo focuses strictly on the backend architecture, specifically the integration between the Flask web server, MySQL database, and RabbitMQ message broker.

## 🏗️ System Architecture

The system follows a microservices-inspired architecture, separating the Web Interface (Frontend/API) from the Heavy Processing (Backend Workers):

1.  **Web Layer (Flask)**: Handles HTTP requests, user authentication, and API routing.
2.  **Task Queue (RabbitMQ)**: Decouples the web server from blocking operations. When a user requests a data update, the web app pushes a message to the queue, ensuring immediate UI response.
3.  **Data Layer (MySQL)**: Stores user profiles, billing records, and device logs via SQLAlchemy ORM.

## 📂 Project Structure

*   **`app.py`** (formerly `operation_flask.py`):
    *   The core Flask application entry point.
    *   Defines REST API endpoints for login and task triggering.
*   **`message_queue.py`**:
    *   A custom wrapper class for **RabbitMQ (Pika)** interactions.
    *   Encapsulates connection handling and message publishing logic to ensure reliability.
*   **`login_manager.py`**:
    *   Manages user sessions and authentication flows using `Flask-Login`.
*   **`database.py`**:
    *   Centralized database connection instance (`SQLAlchemy`) to prevent circular imports.

## 🚀 Key Features Demonstrated

*   **Full-Stack Integration**: Connecting a Python Web Framework (Flask) with Database and Message Broker services.
*   **Asynchronous Pattern**: Implementing the **Producer** pattern in the Web App to dispatch tasks to Consumer workers (e.g., the Crawler).
*   **Secure Authentication**: Implementing user session management and protected routes (`@login_required`).

## 🛠️ Tech Stack

*   **Framework**: Flask
*   **Database**: MySQL, SQLAlchemy
*   **Queue**: RabbitMQ, Pika
*   **Auth**: Flask-Login

## Usage

1.  Install dependencies:
    ```
    pip install -r requirements.txt
    ```
2.  Configure connection strings in `config.py`.
3.  Start the server:
    ```
    python app.py
    ```
