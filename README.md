# Python Web Application

## Overview
This is a Python web application built with Flask and SQLite that includes the following features:
- User login functionality.
- Profile page displaying the user's photo after successful login.
- Functional and integration tests for robust application validation.
- CI/CD pipeline integration using Jenkins.

---

## Features
1. **Backend Database**: SQLite is used as the lightweight backend database.
2. **Authentication**: User login functionality with hashed passwords for security.
3. **Testing**: Functional and integration tests implemented using `pytest`.
4. **CI/CD Pipeline**: Jenkins pipeline with stages for dependency installation, testing, building, and deployment.

---

## Setup Instructions

### Prerequisites
- Python 3.8+ installed on your system.
- SQLite installed (comes pre-installed on macOS and most Linux distributions).
- `pip` (Python Package Manager) installed.

---

### **Manual Setup**

#### Step 1: Clone the Repository
```bash
git clone https://github.com/charyulu/my_web_app.git
cd my_web_app
```

#### Step 2: Install Dependencies
Install all required Python packages:
```bash
pip install -r requirements.txt
```

#### Step 3: Set Up the Database
1. Open the SQLite shell:
    ```bash
    sqlite3 database.db
    ```
2. Execute the database script to create tables and seed sample data:
    ```sql
    .read src/db/setup.sqlite.sql
    ```

#### Step 4: Run the Application
Start the Flask development server:
```bash
python run.py
```
Navigate to `http://localhost:5000/login` in your browser.

---

### **Jenkins Pipeline Setup**

#### Step 1: Configure Jenkins
1. Install Jenkins on your system. Refer to the [Jenkins documentation](https://www.jenkins.io/doc/) for installation instructions.
2. Install the following plugins:
   - Pipeline Plugin
   - Git Plugin
   - Python Plugin

#### Step 2: Set Up Jenkinsfile
1. Go to your Jenkins dashboard and create a new pipeline job.
2. Connect the pipeline to your GitHub repository.
3. Use the provided `Jenkinsfile` for the pipeline configuration.

#### Step 3: Run the Pipeline
Run the Jenkins pipeline to automate the build, test, and deploy stages.

---

## Database Setup

### **SQLite Script**
The `src/db/setup.sqlite.sql` script sets up the `users` table and inserts a sample user with a hashed password.

### **Generate Hashed Password**
To manually generate a hashed password for SQLite, use the following Python code:

```python
import bcrypt

password = "your_password_here"
hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
print("Hashed Password:", hashed_password.decode())
```

Replace the `hashed_password_here` placeholder in the database script with the generated hashed password.

---

## Testing
### Set Environment Var
export PYTHONPATH=[Project Root Folder]
### **Functional Tests**
Functional tests validate individual features like login functionality. To run functional tests:
```bash
pytest src/tests/functional/test_login.py
```

### **Integration Tests**
Integration tests ensure that multiple components work together seamlessly. To run integration tests:
```bash
pytest src/tests/integration/test_endpoints.py
```

---

## CI/CD Pipeline

The Jenkins pipeline includes the following stages:
1. **Install Dependencies**: Installs required Python packages.
2. **Run Functional Tests**: Runs `pytest` functional test cases.
3. **Run Integration Tests**: Runs `pytest` integration test cases.
4. **Build**: Prepares the application for deployment.
5. **Deploy**: Deploys the application to the specified environment.

Refer to the `Jenkinsfile` in the root directory for detailed pipeline configuration.

---

## Project Structure

```plaintext
my_web_app/
├── .github/
│   ├── workflows/
│   │   └── ci-cd.yml
├── docs/
│   └── setup.md
├── src/
│   ├── app/
│   │   ├── routes/
│   │   │   └── auth.py
│   │   ├── static/
│   │   │   ├── css/
│   │   │   ├── js/
│   │   │   └── images/
│   │   │       └── photo.jpg
│   │   ├── templates/
│   │   │   ├── login.html
│   │   │   └── profile.html
│   │   └── __init__.py
│   ├── db/
│   │   └── setup.sqlite.sql
│   ├── tests/
│   │   ├── functional/
│   │   │   └── test_login.py
│   │   ├── integration/
│   │   │   └── test_endpoints.py
│   │   └── __init__.py
├── Jenkinsfile
├── README.md
├── config.py
├── requirements.txt
└── run.py
```

---

## Notes
- Make sure the `photo.jpg` file is placed in the `src/app/static/images/` directory.
- Update the `config.py` file to use a production-ready database in a live environment.
- Follow the inline documentation in the code for better understanding.

Let me know if you encounter any issues!

## Request pattern
Generate a complete Python Flask web application project with SQLite integration, including user login functionality, hashed password storage, profile page with photo display, database setup script, functional and integration tests, CI/CD pipeline configuration using Jenkins, and all necessary files like auth.py, db.py, templates, and README.md. The project should follow a structured folder hierarchy.