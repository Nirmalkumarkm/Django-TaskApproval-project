
# Task Approval Django Application

This Django application is designed for managing tasks in a company with two departments: DEPT 1 and DEPT 2.

## Features

1. **User Management:**
   - Create users for each department.

2. **Task Creation:**
   - Admin can create tasks for DEPT 1.

3. **Task Assignment:**
   - Admin assigns tasks to users in DEPT 1.

4. **Automatic Task Creation:**
   - Upon completion of DEPT 1 tasks, tasks are automatically created for DEPT 2.

5. **Task Assignment for DEPT 2:**
   - Admin assigns tasks to users in DEPT 2.

6. **Task Reporting:**
   - Generates a report with the following format:
     ```
     task 1 DEPT 1 onProgress USER1_DEPT1
     task 2 DEPT 1 Completed USER2_DEPT1
     task 2 DEPT 2 onProgress USER3_DEPT2
     task 3 DEPT 1 onProgress USER1_DEPT1
     task 4 DEPT 1 onProgress USER2_DEPT1
     ```

## Setup

1. **Requirements:**
   - Python 3.x
   - Django

2. **Installation:**
   ```bash
   pip install -r requirements.txt

Database Setup:
python manage.py migrate

Create Superuser:
python manage.py createsuperuser

Run the Development Server:
python manage.py runserver

Access Admin Panel:

Open http://127.0.0.1:8000/admin/ in your browser.
Log in with the superuser credentials.
Usage
Create Users:

Use the admin panel to create users for DEPT 1 and DEPT 2.
Create Tasks:

Create tasks for DEPT 1 in the admin panel.
Assign Tasks:

Assign tasks to DEPT 1 users.
Task Completion:

Upon completion, tasks for DEPT 2 are automatically created.
Assign DEPT 2 Tasks:

Admin assigns tasks to DEPT 2 users.
Generate Report:

Visit http://127.0.0.1:8000/task-report/ to view the task report.
