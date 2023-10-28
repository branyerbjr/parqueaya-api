# ParqueaYA! - REST API

Welcome to the Parqueaya REST API project! This API is designed to provide a seamless experience for managing parking reservations and related data. Below, you'll find information about the technologies used and how to get started with the project.

## Technologies Used

- **Django**: Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It's used as the foundation for building the Parqueaya API.

- **Django REST framework**: This powerful and flexible toolkit is an extension to Django for building Web APIs. It makes it easy to create, update, and manage RESTful web services.

## Getting Started

To get started with the Parqueaya API, follow these steps:

1. **Clone the Repository**: Start by cloning this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/parqueaya-api.git
   cd parqueaya-api

2. **Virtual Environment**: It's recommended to create a virtual environment for your project to manage dependencies. Use virtualenv or conda for this purpose:
   ```bash
   # Using virtualenv
   virtualenv venv
   source venv/bin/activate

   # Using conda
   conda create -n parqueaya-api python=3.x
   conda activate parqueaya-api
3. **Install Dependencies**: Install the required Python packages using pip:
   ```bash
   pip install -r requirements.txt

4. **Database Setup**: Configure your database settings in the project's settings file ' .env ' :
   ```.env
   DB_NAME=mydatabase
   DB_USER=myuser
   DB_PASSWORD=mypassword
   DB_HOST=localhost
   DB_PORT=3306
   ```
5. **Migrate Database**:  Apply database migrations to set up the database schema:
   ```bash
   python manage.py migrate
   ```
6. **Run the Development Server**: Start the development server to run the Parqueaya API:
   ```bash
   python manage.py runserver
   ```
7. **API Documentation**: Visit the API documentation page in your browser to explore the available endpoints and test the functionality:
   ```
   http://localhost:8000/api/docs/
   ```
8. **Start Building**: You are now ready to build your application on top of the Parqueaya REST API!:
