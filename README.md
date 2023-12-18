# Project Evaluation System

## Overview

This Python script implements a simple project evaluation system using CSV files for data storage. It includes functionalities for user login, 
user management (admin only), project evaluations, and handling advisor pending requests (admin only).

## Key Features

- **User Authentication:** Login with username and password.
- **User Roles:** Admin, Student, Faculty (future implementations can include member and lead roles).
- **Project Evaluations:** Faculty members can evaluate projects submitted by students.
- **Advisor Pending Requests:** Students can request advisors, and admins can manage these requests.
- **CSV Data Storage:** Project information, user data, and evaluations are stored in CSV files.

## Usage

1. Clone the repository or download the script.
2. Run the script using Python: `python project_evaluation_system.py`
3. Login with your username and password.

Based on your role, you can perform different actions:

- **Admin:**
  - View and manage users.
  - Manage advisor requests.
  - View project evaluations.

- **Student:**
  - Request advisors.
  - View project evaluations (for submitted projects).

- **Faculty:**
  - Evaluate projects assigned to you.

## Role Actions Table

| Role    | Action                        | Method/Class                      |
|---------|-------------------------------|-----------------------------------|
| Admin   | View Usernames and IDs        | `show_user_info`                  |
| Admin   | Add User                      | `add_user`                        |
| Admin   | Delete User                   | `delete_user`                     |
| Admin   | View Advisor Pending Requests | `view_advisor_requests`           |
| Admin   | Respond to Advisor Requests   | `update_advisor_request_response` |
| Student | Request Advisor               | `insert_advisor_request`          |
| Faculty | Evaluate Project              | `evaluate_project`                |
| Faculty | View Project Evaluations      | `get_project_evaluations`         |

## Missing Features and Bugs

- Currently, only admin and student roles are implemented. Implementations for member and lead roles can be added.
- Further admin functionalities like managing project evaluations can be implemented.
- Testing procedures can be established to ensure system stability.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Additional Notes

- This is a basic version of the project. Consider adding features and functionalities to meet your specific requirements.
- You can customize the readme.md further with examples, screenshots, and contribution guidelines.

