# Automated Messaging Platform

This project allows users to send automated messages to recipients on **Wellfound** or **LinkedIn** via a web-based frontend and a Python backend using Selenium for browser automation.

## Features

- **Platform Selection**: Choose between Wellfound and LinkedIn.
- **User-Friendly Interface**: Simple and clean UI for entering recipient details and message content.
- **Automated Messaging**: Backend leverages Selenium to automate message sending on selected platforms.
- **Custom Chrome Profiles**: Uses existing Chrome profiles to log in seamlessly.

## Installation

### Frontend

1. Navigate to the `frontend` directory.
2. Install dependencies:
   npm install
3. Run the development server:
   npm start

### Backend

1. Install Python dependencies:
   pip install flask flask-cors selenium webdriver-manager
2. Configure ChromeDriver in the backend script.
3. Start the backend server:
   python app.py

## Usage

1. Open the web application.
2. Select a platform (Wellfound or LinkedIn).
3. Enter recipient details and message.
4. Click **Send Message!**.
