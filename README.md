###  Healthcare Appointment Booking Chatbot (Python + Flask Web App)

A rule-based conversational chatbot built in Python that simulates a healthcare appointment booking system.
The bot interacts with users via the command line, collects patient details, suggests specialists and doctors,
provides available dates & time slots, and confirms appointments with optional SMS reminders.The project also includes a web-based chat interface built using HTML, 
CSS, and JavaScript,with a Flask REST API connecting the frontend and backend chatbot logic.


##  Features

-Interactive command-line chatbot
 -Collects patient details:
    -Full Name
    -Date of Birth
    -Phone Number
  -Reason for Visit
  -Supports multiple specialties:
    -General Physician
    -Cardiologist
    -Dermatologist
    -Orthopedist
  -Doctor selection by name or number
  -Automatically generates future weekday appointment dates
  -Fixed time-slot scheduling
  -Optional SMS reminder confirmation
  -Help & restart flow at any stage
  -Exit anytime using quit, bye, or exit
  - Web-based chat interface (browser-based UI)
  - Real-time interaction using Flask REST API
  - Modern chat UI built with HTML, CSS, and JavaScript

  
  ## How It Works

The chatbot is implemented using:

-State-based conversation flow
-Regular Expressions (regex) for input validation
-Python dictionaries & lists for managing doctors and appointments
-Datetime module to generate valid future dates

## Technologies Used

Python 3

re – for pattern matching & validation

datetime – for date calculations

No external libraries required 

## Project Structure

healthcare-appointment-bot/
│
├── healthcare_bot.py   # Main chatbot implementation
├── README.md           # Project documentation

## How to Run the Project

** Clone the repository

** git clone https://github.com/your-username/healthcare-appointment-bot.git

** Navigate to the project folder

** cd healthcare-appointment-bot

** Run the chatbot

** python healthcare_bot.py

## Sample Interaction
You: Hello
Bot: Hello! I'm here to help you book a doctor's appointment. May I have your full name please?

You: Thomas Jacob
Bot: Thanks Thomas Jacob! What is your date of birth? (MM/DD/YYYY)

You: 08/12/2002
Bot: What is your phone number? (Format: 123-456-7890)

** Help Commands

You can type:

help – to get guidance for the current step

quit / exit / bye – to end the conversation

Doctor names directly (e.g., Dr. Smith) at any point

## Future Improvements

** Web interface (Flask / FastAPI)

** NLP-based intent detection

** Database integration (SQLite / MongoDB)

** Real SMS API integration

** Machine Learning–based chatbot logic

## Use Case

This project is ideal for:

-Python beginners
-Chatbot & NLP fundamentals
-Mini-projects / academic submissions
-Resume & portfolio projects
