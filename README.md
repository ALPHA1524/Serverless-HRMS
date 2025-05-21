# 🧑‍💼 Serverless HR Management System (HRMS)

A fully serverless Human Resource Management System built using AWS services and a lightweight frontend. This project demonstrates scalable architecture and modular backend logic to manage core HR functionalities such as employee records, leave tracking, payroll, performance reviews, and document handling.

## 🚀 Features

- Add and manage employee details
- Submit and track leave requests
- Payroll processing interface
- Submit performance reviews
- Upload and manage HR documents
- Secure and scalable backend integration via AWS

## 🧰 Tech Stack

### Frontend
- HTML5, CSS3, JavaScript
- Clean UI with form-based interaction

### Backend (Serverless Architecture)
- **AWS Lambda** – Function logic for HR operations
- **API Gateway** – REST API integration
- **Amazon DynamoDB** – NoSQL data storage
- **Amazon S3** – File/document storage
- **(Planned)** Amazon Cognito – User authentication and role-based access

## 🧱 Architecture

The system follows a modular and scalable architecture:


Each Lambda function is responsible for a specific operation (e.g., `addEmployee`, `submitLeave`, `processPayroll`, etc.).

## 🔐 Authentication (Planned)

- Designed role-based authentication using **Amazon Cognito**
- Roles: `HRManager` and `Employee`
- Intended support for JWT-based secure API access (to be implemented)

## 📊 Data Models (DynamoDB Tables)

- `EmployeeTable`
- `LeaveTable`
- `PayrollTable`
- `AttendanceTable`
- `PerformanceTable`
- `DocumentTable`

## 🛠 Setup Instructions

> This project assumes you're using the AWS Console or AWS CLI to deploy functions manually.

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/serverless-hrms.git
   cd serverless-hrms
