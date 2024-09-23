"""
Copyright (c) 2024 Liibaan Egal
All rights reserved.

Date: September 19, 2024

This code is intended for educational purposes. Use it responsibly.
"""

import sys
import os
import time
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTimeEdit, QMessageBox
from PyQt5.QtCore import QTimer, QTime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class GitHubAutoCommitGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # GitHub Username
        username_layout = QHBoxLayout()
        username_layout.addWidget(QLabel('GitHub Username:'))
        self.username_input = QLineEdit()
        username_layout.addWidget(self.username_input)
        layout.addLayout(username_layout)

        # GitHub Password
        password_layout = QHBoxLayout()
        password_layout.addWidget(QLabel('GitHub Password:'))
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        password_layout.addWidget(self.password_input)
        layout.addLayout(password_layout)

        # Repository URL
        repo_layout = QHBoxLayout()
        repo_layout.addWidget(QLabel('Repository URL:'))
        self.repo_input = QLineEdit()
        repo_layout.addWidget(self.repo_input)
        layout.addLayout(repo_layout)

        # Chrome Driver Path
        driver_layout = QHBoxLayout()
        driver_layout.addWidget(QLabel('Chrome Driver Path:'))
        self.driver_input = QLineEdit()
        driver_layout.addWidget(self.driver_input)
        layout.addLayout(driver_layout)

        # Schedule Time
        time_layout = QHBoxLayout()
        time_layout.addWidget(QLabel('Schedule Time:'))
        self.time_input = QTimeEdit()
        self.time_input.setTime(QTime(10, 0))  # Default to 10:00
        time_layout.addWidget(self.time_input)
        layout.addLayout(time_layout)

        # Start Button
        self.start_button = QPushButton('Start Auto-Commit')
        self.start_button.clicked.connect(self.start_auto_commit)
        layout.addWidget(self.start_button)

        self.setLayout(layout)
        self.setWindowTitle('GitHub Auto-Commit')
        self.show()

    def start_auto_commit(self):
        global GITHUB_USERNAME, GITHUB_PASSWORD, REPO_URL, driver_path

        GITHUB_USERNAME = self.username_input.text()
        GITHUB_PASSWORD = self.password_input.text()
        REPO_URL = self.repo_input.text()
        driver_path = self.driver_input.text()

        if not all([GITHUB_USERNAME, GITHUB_PASSWORD, REPO_URL, driver_path]):
            QMessageBox.warning(self, 'Input Error', 'Please fill in all fields.')
            return

        schedule_time = self.time_input.time().toString('HH:mm')
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_and_run)
        self.timer.start(60000)  # Check every minute

        QMessageBox.information(self, 'Auto-Commit Started', f'Auto-commit scheduled for {schedule_time} daily.')

    def check_and_run(self):
        current_time = QTime.currentTime().toString('HH:mm')
        schedule_time = self.time_input.time().toString('HH:mm')
        
        if current_time == schedule_time:
            self.github_auto_commit()

    def github_auto_commit(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        try:
            driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)
            
            driver.get('https://github.com/login')
            
            username_input = driver.find_element(By.ID, 'login_field')
            password_input = driver.find_element(By.ID, 'password')
            
            username_input.send_keys(GITHUB_USERNAME)
            password_input.send_keys(GITHUB_PASSWORD)
            password_input.send_keys(Keys.RETURN)
            
            time.sleep(3)
            
            driver.get(REPO_URL)
            time.sleep(2)
            
            driver.find_element(By.LINK_TEXT, "Add file").click()
            time.sleep(2)
            
            driver.find_element(By.LINK_TEXT, "Create new file").click()
            time.sleep(2)
            
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f'commit_{timestamp}.txt'
            
            filename_input = driver.find_element(By.NAME, 'filename')
            filename_input.send_keys(filename)
            
            commit_message = f'Automated commit on {timestamp}'
            driver.find_element(By.CLASS_NAME, 'CodeMirror-code').send_keys(commit_message)
            
            commit_button = driver.find_element(By.ID, 'submit-file')
            commit_button.click()
            
            driver.quit()

            QMessageBox.information(self, 'Success', 'Auto-commit completed successfully.')
        except Exception as e:
            QMessageBox.warning(self, 'Error', f'An error occurred: {str(e)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GitHubAutoCommitGUI()
    sys.exit(app.exec_())
