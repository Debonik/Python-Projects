# Flask URL Shortener

This is a simple web application built with Flask that serves as a URL shortener, similar to services like Bit.ly or TinyURL.

## How It Works

- **Importing Libraries**: The application uses Flask for the web framework and Python's `string` and `random` libraries to generate random strings.

- **Application Setup**: The line `app = Flask(__name__)` initializes the Flask application.

- **URL Mapping**: A Python dictionary named `url_mapping` stores the mappings between the generated short codes and the original URLs.

- **Short Code Generation**: The function `generate_short_code()` creates a random 6-character string using letters and numbers. This string acts as the "shortened" URL identifier.

- **Home Page Route**: The `@app.route('/', methods=['GET', 'POST'])` decorator defines the application's behavior when the home page is accessed. If the user submits a URL through the form (`POST`), the application generates and displays a short URL.

- **Creating Short URLs**: Upon form submission, a short code is generated, stored in `url_mapping`, and the short URL is presented to the user.

- **Redirection Functionality**: The route `@app.route('/<short_code>')` takes the short code from the URL, looks it up in `url_mapping`, and if it's found, redirects the user to the original URL.

- **Application Execution**: The block `if __name__ == '__main__': app.run(debug=True)` starts the application with debugging features enabled.

## Usage

To use the application:

1. Navigate to the home page.
2. Enter the URL you wish to shorten in the form provided.
3. Submit the form to receive a shortened URL.
4. Access the shortened URL to be redirected to the original URL.
