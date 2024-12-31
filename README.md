# Sports Inventory Management System

This Django project is designed to manage the inventory of sports equipment. It uses Django Rest Framework for API creation and Postgres for data storage.

## Prerequisites

- Docker
- Docker Compose

## Running the Project

To get the project up and running, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory where the `docker-compose.yml` file is located.
3. Run the following command to build and start the containers:

```bash
docker-compose up --build
```

This will start the Django development server and the PostgreSQL database. The Django server will be available at `http://localhost:8000/`.

## API Endpoints

The project includes the following REST API endpoints for managing inventory items:

- `GET /items/`: List all inventory items.
- `POST /items/`: Create a new inventory item.
- `GET /items/{id}/`: Retrieve a specific inventory item by ID.
- `PUT /items/{id}/`: Update a specific inventory item by ID.
- `DELETE /items/{id}/`: Delete a specific inventory item by ID.
- `GET /items/?quantity=<quantity>`: Retrieve inventory items that have a specific quantity.

## Running Tests

To run tests within the Docker container, use the following command:

```bash
docker-compose run web sh -c "python manage.py inventory.tests"
```


This command initiates the Django test runner inside the `web` service container.

## Running the Python Script for Zero Quantity Items

There is a Python script included in the project that retrieves all inventory items with a quantity of 0 and saves the output to a file in the `data` folder. To execute this script, run the following command:

```bash
docker-compose run web sh -c "python scripts/get_zero_quantity_items.py"
```

## Data Persistence

The PostgreSQL data is persisted using Docker volumes as specified in the `docker-compose.yml` file. This ensures that the data remains intact even if the containers are stopped or removed.

## Environment Configuration

The database and other configurations are managed through environment variables as specified in the `.env` file and the `docker-compose.yml` file. Ensure that the `.env` file is present in the root directory with the correct configurations before starting the project.

