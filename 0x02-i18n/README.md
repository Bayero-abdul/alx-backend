# ALX-BACKEND - 0x02. i18n

## Project Overview
This project focuses on internationalization and localization (i18n) in a Flask web application. You will set up a basic Flask app and use Flask-Babel for i18n. The project tasks include configuring available languages, parametrizing templates, and allowing users to select their preferred locale and timezone. By the end of this project, you will have gained experience in i18n best practices and implemented multilingual support in a web application.

## Running the Tasks
The project consists of several tasks:

1. **Basic Flask App**: Create a basic Flask app with a single route and an HTML template. The template should display "Welcome to Holberton" as the page title and "Hello world" as the header.

2. **Basic Babel Setup**: Install the Babel Flask extension and configure it in your app. Set up available languages, default locale, and timezone using the Config class.

3. **Get Locale from Request**: Create a `get_locale` function using the `babel.localeselector` decorator to determine the best match for the user's preferred language based on request headers.

4. **Parametrize Templates**: Use the `_` or `gettext` function to parametrize your templates. Create message IDs for the title and header, and use a `babel.cfg` file to manage translations. Generate translation dictionaries and compile them.

5. **Force Locale with URL Parameter**: Implement a way to force a particular locale by passing the `locale` parameter to your app's URLs. Modify the `get_locale` function to detect and return the specified locale if present.

6. **Mock Logging In**: Emulate user login by creating a user table and allowing users to log in with the `login_as` URL parameter. Display a welcome message or a default message in the HTML template based on whether a user is logged in.

7. **Use User Locale**: Modify the `get_locale` function to prioritize the user's preferred locale if it is supported. The order of priority should be locale from URL parameters, locale from user settings, locale from request header, and default locale.

8. **Infer Appropriate Time Zone**: Define a `get_timezone` function and use the `babel.timezoneselector` decorator. The function should find the timezone from URL parameters, user settings, or default to UTC. Validate the time zone to ensure it is valid.

Follow the instructions in each task to complete the project successfully.

For detailed task descriptions and code examples, please refer to the provided project files.

## Project Structure
The project directory structure is organized as follows:

- `0-app.py`, `1-app.py`, `2-app.py`, `3-app.py`, `4-app.py`, `5-app.py`, `6-app.py`, `7-app.py`: Contains Flask applications for different tasks.
- `babel.cfg`: Configuration file for translations.
- `templates/0-index.html`, `templates/1-index.html`, `templates/2-index.html`, `templates/3-index.html`, `templates/4-index.html`, `templates/5-index.html`, `templates/6-index.html`, `templates/7-index.html`: HTML templates used in different tasks.
- `translations/en/LC_MESSAGES/messages.po`, `translations/fr/LC_MESSAGES/messages.po`: Message templates for English and French translations.
- `translations/en/LC_MESSAGES/messages.mo`, `translations/fr/LC_MESSAGES/messages.mo`: Compiled translation files for English and French.
- `README.md`: A README file providing an overview of the project.
