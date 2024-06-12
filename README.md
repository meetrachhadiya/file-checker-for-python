# Django Python File Format Checker

This Django web application checks whether a Python file is properly formatted or not using the AST (Abstract Syntax Trees) module in Python.

## Prerequisites

- Python 3.x
- Django

## Installation

1. Clone the repository:

    ```bash
    git clone <repository_url>
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

2. Open your web browser and navigate to `http://localhost:8000/` to access the file upload page.

3. Upload a Python file using the provided form.

4. The application will display whether the uploaded file is a valid Python file or not.

## Code Structure

- `upload/views.py`: Contains the Django view functions for handling file uploads and checking Python file format.
- `upload/forms.py`: Defines the form used for file uploads.
- `templates/upload.html`: HTML template for the file upload page.
- `templates/result.html`: HTML template for displaying the result of the Python file format check.

## How it works

The application utilizes the AST module in Python to parse the uploaded Python file. If the parsing is successful, it considers the file as valid; otherwise, it treats it as invalid.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
