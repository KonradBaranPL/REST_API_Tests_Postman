# Trello API Testing Project
Automated API testing project for Trello.
CRUD requests created in Postman with JavaScript test scripts, executed via Newman, and integrated with Python for reporting.

## Description
This project demonstrates automated testing of the public Trello API. The main goal was to design and execute a complete set of CRUD operations (GET, POST, PUT, DELETE) against Trello endpoints using Postman. Each request includes JavaScript-based test scripts to validate key elements of the API responses, such as status codes, response times, and returned data consistency.

The Postman collection and environment were exported to JSON files to enable test execution via Newman. To integrate with the Python ecosystem, a custom Python script was developed to run Newman commands, capture test results, and display them in the console for easier analysis.

This project illustrates a practical approach to API testing, combining manual design of test cases in Postman with automated execution and reporting through Newman and Python. It provides a clear example of how to validate REST APIs and integrate them into a broader development workflow.

## Technologies
Postman – creating requests and test scripts
JavaScript – test script logic in Postman
Newman – CLI tool for running Postman collections
Python – integration script to execute Newman and handle results
GitHub – version control and project hosting

## Getting started locally
Clone the repository:

```bash
git clone https://github.com/KonradBaranPL/REST_API_Tests_Postman.git
