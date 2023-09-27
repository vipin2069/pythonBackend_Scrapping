import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # Import MongoClient from pymongo

# Set up your MongoDB connection
MONGO_URI = "mongodb://localhost:27017"
client = MongoClient(MONGO_URI)

# Define the MongoDB collection
db = client['mydatabase']
books_collection = db['books']  # Define the collection you want to use

# Function to scrape and store books data
def scrape_and_store_books():
    base_url = "http://books.toscrape.com/catalogue/page-{}.html"

    for page_num in range(1, 51):
        url = base_url.format(page_num)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract book attributes
        for book in soup.find_all('article', class_='product_pod'):
            title = book.h3.a.attrs['title']
            price = book.select('div p.price_color')[0].text
            availability = book.select('div p.availability')[0].text.strip()
            rating = book.select('p.star-rating')[0]['class'][1]

            book_data = {
                'title': title,
                'price': price,
                'availability': availability,
                'rating': rating
            }

            # Insert the book data into the 'books' collection
            books_collection.insert_one(book_data)

if __name__ == "__main__":
    scrape_and_store_books()
