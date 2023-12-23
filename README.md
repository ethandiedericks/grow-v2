# Budget App

This Django-based budget app allows users to manage their income, expenses, and investments. It provides a platform to track various financial sources and transactions.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository contains the code for a Django-based budget management application. It includes models for income sources, expense sources, investments, income transactions, expense transactions, and investment transactions.

## Features

- **User-specific Financial Tracking:** Users can manage their income sources, expenses, and investments individually.
- **Income Tracking:** Add and manage various sources of income, including future income projections.
- **Expense Tracking:** Record and monitor different expenses, including future expenses.
- **Investment Management:** Track investments made and future investment plans.
- **User Authentication:** Utilizes Django's built-in authentication system for user-specific data management.

## Setup

1. **Clone the Repository:** `git clone https://github.com/ethandiedericks/grow-v2.git`
2. **Create a Virtual Environment:** `python -m venv myenv`
3. **Activate the Virtual Environment:** 
    - On Windows: `myenv\Scripts\activate`
    - On macOS and Linux: `source myenv/bin/activate`
4. **Install Dependencies:** `pip install -r requirements.txt`
5. **Run Migrations:** `python manage.py migrate`
6. **Create Superuser:** `python manage.py createsuperuser`
7. **Start the Development Server:** `python manage.py runserver`

## Usage

- Access the application by visiting `http://localhost:8000/` in your web browser.
- Log in using the created superuser credentials.
- Explore the different sections to manage income, expenses, and investments.
- Add, edit, or delete transactions as necessary.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/awesome-feature`).
3. Make modifications and commit changes (`git commit -am 'Add an awesome feature'`).
4. Push the branch (`git push origin feature/awesome-feature`).
5. Create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
