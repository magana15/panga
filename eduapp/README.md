# EduWear

EduWear is an application for ordering school uniforms. It provides a catalog of uniforms, size guides, a feedback form, and a color verification feature for uniform distributors.

## Features

- Browse uniform catalog
- View size guides
- Place orders for uniforms
- Provide feedback on uniforms and app functionality
- Verify uniform colors

## Directory Structure

EduWear/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│   │   ├── layout.html
│   │   ├── index.html
│   │   ├── catalog.html
│   │   ├── size_guide.html
│   │   ├── order.html
│   │   ├── feedback.html
│   │   ├── color_verification.html
│   │   ├── cart.html
│   ├── static/
│   │   ├── css/
│   │   │   ├── styles.css
│   │   ├── js/
│   │   │   ├── scripts.js
│   │   ├── images/
│   │   │   ├── logo.png
│   │   │   ├── uniform_sample.jpg
│   ├── utils.py
├── tests/
│   ├── test_app.py
├── config.py
├── run.py
├── requirements.txt
├── README.md
├── .gitignore
└── docs/
    ├── architecture_diagram.png
    ├── data_model.png
    ├── user_stories.md

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

