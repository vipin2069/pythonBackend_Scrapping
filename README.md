# Python Intern Assignment

## Part - A
### Objective
Use the below APIs to fetch Users and their corresponding posts data and store it in any Database of your choice.

### Functional Requirements
- Fetch Users data using this API - [https://dummyapi.io/data/v1/user](https://dummyapi.io/data/v1/user) and store it in the users table in the Database.
- Fetch users list from Database and fetch their corresponding posts data using this API - [https://dummyapi.io/data/v1/user/{{user_id}}/post](https://dummyapi.io/data/v1/user/{{user_id}}/post) and store it in the database.

## Part - B
### Objective
Scrape books data from [http://books.toscrape.com](http://books.toscrape.com) and store it in Database.

### Functional Requirements
- Scrape all books attributes like name, price, availability, and ratings of all 50 pages and store them in the Database.
  
---

## Setup

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/vipin2069/pythonBackend_Scrapping.git
   
2. Navigate to the project directory:

   ```bash
   cd python-intern-assignment
   
3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   
4. Set up MongoDB on your machine and replace the MONGO_URI in config.py with your MongoDB connection URI.

5. Install the required Python packages:

   ```bash
   pip install -r requirements.txt

### Database Details
- Database Type: MongoDB
- Database Name: mydatabase
- Collections: users, posts, books (for scraped books data)

## SCREENSHOTS
![Screenshot 1](./screenshots/Screenshot%202023-09-28%20003011.png) 
![Screenshot 2](./screenshots/Screenshot%202023-09-28%20003028.png) 
![Screenshot 3](./screenshots/Screenshot%202023-09-28%20003048.png)

