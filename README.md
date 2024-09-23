Repo Ruse
Repo Ruse is a Python-based desktop application designed to automate GitHub commits. It helps you maintain an active GitHub profile effortlessly, simulating constant activity with automated commits at scheduled times. Perfect for developers who want to boost their commit history and showcase consistent contributions.

Features
Automated GitHub Commits: Schedule daily commits to any GitHub repository of your choice.
Customizable Timing: Set the exact time for your daily commits.
GUI Interface: Simple, user-friendly GUI for easy setup and scheduling.
Headless Automation: Runs in the background using Selenium and Chrome WebDriver.
Requirements
Python 3.x
PyQt5
Selenium
Google Chrome and ChromeDriver
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/repo-ruse.git
Navigate to the project directory:

bash
Copy code
cd repo-ruse
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Download and install ChromeDriver, ensuring it's in your system's PATH or providing its path during setup.

Usage
Run the application:

bash
Copy code
python repo_ruse.py
Enter your GitHub username, password, repository URL, and the path to your ChromeDriver.

Set the time for the daily auto-commits.

Click Start Auto-Commit, and the application will handle the rest.

How It Works
Repo Ruse logs into your GitHub account and creates a new file in the repository at the scheduled time.
A file with a timestamp is created, and an automated commit is pushed to your repository, simulating regular activity.
License
yaml
Copy code
Copyright (c) 2024 Liibaan Egal
All rights reserved.

Date: September 19, 2024

This code is intended for educational purposes. Use it responsibly.
Disclaimer
Repo Ruse is intended for educational purposes. Please use it responsibly and ensure compliance with GitHub's terms of service.
