# HMS-Backend

#### This is the backend for the Hospital Management System (HMS), built using Flask and SQLAlchemy. It provides API endpoints for managing doctors, patients, appointments, and reviews.

#### By **Yakubu Esuza**

## Features

- Full CRUD operations for appointments (Create, Read, Update, Delete).
- Create & read operations for doctors, patients, and reviews.
- Many-to-many relationship between doctors and patients via the appointment table.
- One-to-many relationships:

A doctor can have multiple appointments.
A patient can have multiple appointments.
- Form validation using SQLAlchemy's @validates.
- Serialization using SerializerMixin.
- Database seeding with Faker for testing data.
- CORS enabled for frontend integration.


#### Installation Process

1. Clone this repository using:

   ```bash
   git clone git@github.com:Esuza-arch/HMS-Backend.git
   ```

   or by downloading a ZIP file of the code.

2. Navigate to the project directory:

   ```bash
   cd HMS-Backend
   ```

3. Install the required dependencies:

   ```bash
   pipenv install
   pipenv install -r requirements.txt
   ```

4. Set up database:

   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

5. Seed the database:

   ```bash
   python seed.py
   ```

6. Start the flask server:

   ```bash
   flask run
   ```

7. Open your browser and visit `http://127.0.0.1:5555`

## Technologies Used
- Flask (Backend framework)
- SQLAlchemy (ORM for database)
- SQLite / PostgreSQL (Database)
- Flask-CORS (Handles cross-origin requests)
- Faker (Generates fake data for testing)


### Backend API

- Deployed API: [Live API URL](https://hms-backend-2-lmbv.onrender.com/)

## Support and Contact Details

If you have any questions, suggestions, or need assistance, please contact:

- Email: <yakubuesuza@gmail.com>

## License

MIT License

Copyright &copy; 2025 Yakubu Esuza

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.