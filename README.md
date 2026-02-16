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
- Flask is used to expose the chatbot as a REST API
- Frontend sends user messages via HTTP POST requests
- Backend processes input and returns bot responses as JSON


## Technologies Used

* Python 3  
* Flask – backend REST API  
* HTML, CSS, JavaScript – frontend chat interface  
* re – input validation using regular expressions  
* datetime – appointment date generation  
* flask-cors – for frontend-backend communication


## Project Structure

healthcare-appointment-bot/
│
├── app.py              # Flask backend API
├── bot.py              # Healthcare chatbot logic
├── index.html          # Frontend UI
├── style.css           # Chat UI styling
├── script.js           # Frontend logic
├── README.md           # Project documentation

## How to Run the Project

** Clone the repository

** git clone https://github.com/your-username/healthcare-appointment-bot.git

### Web Version (Recommended)

1. Install dependencies
   pip install flask flask-cors

2. Start the backend server
   python app.py

3. Open index.html in a browser
   (or use Live Server in VS Code)

4. Start chatting by typing "hello"


## System Architecture

Frontend (HTML/CSS/JS)
        ↓ HTTP POST
Flask REST API
        ↓
Healthcare Appointment Chatbot (Python Logic)


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

** React-based frontend

** Authentication & user profiles


## Use Case

This project is ideal for:

-Python beginners
-Chatbot & NLP fundamentals
-Mini-projects / academic submissions
-Resume & portfolio projects
-Full-stack mini project (Frontend + Backend integration)
