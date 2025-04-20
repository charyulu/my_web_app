# Python Web Application

## Overview
This is a Python web application with the following features:
- User login functionality
- Profile page displaying user photo

## Setup Instructions
### Manual Setup
1. Install Python 3.8+.
2. Clone the repository and navigate to the project directory.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python run.py
   ```
5. Navigate to `http://localhost:5000/login` in your browser.

### Jenkins Pipeline Setup
Refer to the [Jenkinsfile](Jenkinsfile) for CI/CD pipeline configuration.

### Database Setup
- Use SQLite for local development (default).
- For production, configure any SQL-based open-source database in `config.py`.

## Testing
Run the following commands for tests:
- Functional tests:
  ```bash
  pytest src/tests/functional
  ```
- Integration tests:
  ```bash
  pytest src/tests/integration
  ```