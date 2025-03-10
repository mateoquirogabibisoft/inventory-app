# Inventory Management System

## Overview
This is a simple Flask-based Inventory Management System that allows users to create, read, update, and delete inventory items. The application runs inside a Docker container and uses MySQL as its database.

## Prerequisites
Before running the application, ensure you have the following installed:

- **Docker** (https://www.docker.com/get-started)
- **Docker Compose** (https://docs.docker.com/compose/install/)

## Project Structure
```
project-folder/
│── app.py               # Main Flask application
│── Dockerfile           # Dockerfile to build the application image
│── docker-compose.yml   # Configuration for Docker containers
│── requirements.txt     # Python dependencies
│── templates/           # HTML templates for the app
│── README.md            # Project documentation (this file)
```

## Installation and Setup
### 1. Clone the Repository
```sh
 git clone <repository-url>
 cd project-folder
```

### 2. Build and Start the Containers
Run the following command to build and start the application:
```sh
docker-compose up --build
```
This will:
- Pull the **MySQL 8.0** image and start a database container.
- Build the Flask application image.
- Start the Flask application container and connect it to the MySQL database.

### 3. Access the Application
Once the containers are running, open your browser and go to:
```
http://localhost:5000
```

### 4. Stopping the Application
To stop the running containers, use:
```sh
docker-compose down
```

## Environment Variables
The following environment variables are used in the application:
```
FLASK_ENV=development
DATABASE_URL=mysql+pymysql://root:password@db:3306/inventory_db
```

## Database Configuration
The MySQL container is configured with the following settings:
- **Database Name:** `inventory_db`
- **Username:** `root`
- **Password:** `password`

If you want to change these values, update them in the `docker-compose.yml` file.

## API Endpoints
| Method | Endpoint         | Description |
|--------|----------------|-------------|
| GET    | `/`            | List all inventory items |
| GET    | `/add`         | Show form to add new item |
| POST   | `/add`         | Add a new inventory item |
| GET    | `/edit/<id>`   | Show form to edit an item |
| POST   | `/edit/<id>`   | Update an existing item |
| GET    | `/delete/<id>` | Delete an inventory item |
