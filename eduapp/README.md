# EduWear

EduWear is an application for ordering school uniforms. It provides a catalog of uniforms, size guides, a feedback form, and a color verification feature for uniform distributors.

## Features

- Browse uniform catalog
- View size guides
- Place orders for uniforms
- Provide feedback on uniforms and app functionality
- Verify uniform colors

## dir

## Running the Application

1. Set up the virtual environment and install dependencies:
    ```sh
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

2. Initialize the database and run the application:
    ```sh
    flask shell
    db.create_all()
    exit
    flask run
    ```

3. Open a web browser and navigate to `http://127.0.0.1:5000/`.

## Running Tests

```sh
python -m unittest discover tests

