# Growth-Mindset-Challange-in-Streamlit
Growth Mindset Challenge: Web App with Streamlit
Task Management Application
Introduction
The Task Management Application is a simple and intuitive tool designed to help you organize and manage your daily tasks efficiently. The app features a sleek dark theme, user-friendly interface, and a variety of functionalities to keep your tasks in check.

Features
Add Tasks: Easily add new tasks with a single input.

View Tasks: Display all your tasks in a neatly organized table.

Update Task Status: Update the status of your tasks to "Complete" or "Incomplete".

Delete Tasks: Remove tasks that are no longer needed.

Dark Theme: Enjoy a visually appealing dark theme with a modern look.

Project Structure
task_manager/
│
├── app.py               # Main Python file for Streamlit app
├── styles.css           # CSS file for custom styling
└── data/
    └── tasks.csv        # CSV file for storing tasks
Requirements
Python 3.6 or higher

Streamlit

Pandas

How to Run the Application
Clone the Repository:

bash
git clone https://github.com/yourusername/task_manager.git
cd task_manager
Install Dependencies:

bash
pip install -r requirements.txt
Run the Application:

bash
streamlit run app.py
Enhancements
The application can be further enhanced with the following features:

Task Categories: Add functionality to categorize tasks (e.g., Work, Personal, Urgent).

Task Deadlines: Integrate a date picker for task deadlines and highlight overdue tasks.

Progress Bar: Add a progress bar to visually show task completion status.

User Authentication: Implement user authentication for personalized task management.
