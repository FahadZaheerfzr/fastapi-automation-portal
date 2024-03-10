# FastAPI Automation Portal

This is an automation portal that allows running of APIs that perform small automations.

## Installation

1. Clone the repository:

  ```bash
  git clone https://github.com/FahadZaheerfzr/fastapi-automation-portal.git
  ```

2. Change into the project directory:

  ```bash
  cd fastapi-automation-portal
  ```

3. Create a virtual environment:

  ```bash
  python3 -m venv venv
  ```

4. Activate the virtual environment:

  ```bash
  source venv/bin/activate
  ```

5. Install the dependencies:

  ```bash
  pip install -r requirements.txt
  ```

## Usage

1. Start the server:

  ```bash
  uvicorn main:app --reload
  ```

2. Open your browser and navigate to `http://localhost:8000` to access the automation portal.

## API Endpoints

- `/`: GET request to know that the portal is running.
- `create-user`: POST request to create a user in the database.

## Contributing

Contributions are welcome! Please follow the [contribution guidelines](CONTRIBUTING.md) when making changes to the project.

## License

This project is licensed under the [MIT License](LICENSE).