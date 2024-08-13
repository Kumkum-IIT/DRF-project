# DRF Project

This repository contains a Django REST Framework (DRF) project that implements user authentication and registration using JSON Web Tokens (JWT). It includes views for user login, registration, and user management.

## Features

- **User Registration**: Allows new users to register and automatically generates a JWT token upon successful registration.
- **User Login**: Authenticates users and provides a JWT token for secure access.
- **User Management**: Allows authenticated users to view and manage their profiles.
- **JWT Authentication**: Secures API endpoints using JWT tokens.
- **Custom Permissions**: Includes custom permission classes to restrict access to certain views.

## Requirements

- Python 3.x
- Django
- Django REST Framework
- djangorestframework-simplejwt

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/drf_project.git
   cd drf_project

## Project Structure
1. views.py: Contains the viewsets for handling user login, registration, and user management.
2. serializers.py: Defines the serializers for user data and authentication.
3. permissions.py: Contains custom permission classes for restricting access to certain views.
4. urls.py: Maps the URLs to the corresponding viewsets.
5. settings.py: Configures Django settings, including JWT authentication.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue if you have any suggestions or find any bugs.

## Licence

This `README.md` file provides an overview of the project, installation instructions, API endpoints, and information about the project structure. Replace placeholders like `yourusername` with actual values as needed.
