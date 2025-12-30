"""
Web Scraping Example: E-commerce Product Data Extraction
This script scrapes product information from a test e-commerce website
and saves it to an Excel file.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Target URL - E-commerce test site for phones
url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'

# Send GET request to the website
print("Fetching webpage...")
response = requests.get(url)

# Check if request was successful
if response.status_code != 200:
    print(f"Error: Failed to fetch webpage. Status code: {response.status_code}")
    exit(1)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')
print("Webpage fetched and parsed successfully!")

# Initialize lists to store scraped data
list_names = []
list_prices = []
list_descriptions = []
list_ratings = []  # For star ratings
list_reviews = []  # For review counts

# Extract product names from anchor tags with 'title' class
print("\nExtracting product names...")
names = soup.findAll('a', {'class': 'title'})
for name in names:
    list_names.append(name.text.strip())

# Extract product prices from h4 tags with 'price' class
print("Extracting product prices...")
prices = soup.findAll('h4', {'class': 'price'})
for price in prices:
    list_prices.append(price.text.strip())

# Extract product descriptions from paragraph tags with 'description' class
print("Extracting product descriptions...")
descriptions = soup.findAll('p', {'class': 'description'})
for description in descriptions:
    list_descriptions.append(description.text.strip())

# Extract star ratings by counting star icons in each product div
print("Extracting star ratings...")
product_divs = soup.findAll('div', {'class': 'col-md-4 col-xl-4 col-lg-4'})
for product_div in product_divs:
    star_icons = product_div.findAll('span', class_='ws-icon ws-icon-star')
    star_count = len(star_icons)
    list_ratings.append(f'{star_count} star out of 5')

# Extract review counts from paragraph tags with 'review-count float-end' class
print("Extracting review counts...")
review_counts = soup.findAll('p', {'class': 'review-count float-end'})
for review in review_counts:
    list_reviews.append(review.text.strip())

# Display extracted data summary
print("\n" + "="*50)
print("SCRAPED DATA SUMMARY")
print("="*50)
print(f"Total products found: {len(list_names)}")
print(f"\nProduct Names: {list_names}")
print(f"\nPrices: {list_prices}")
print(f"\nDescriptions: {list_descriptions}")
print(f"\nRatings: {list_ratings}")
print(f"\nReviews: {list_reviews}")

# Create a pandas DataFrame from the scraped data
print("\n" + "="*50)
print("Creating DataFrame...")
data = pd.DataFrame({
    'Name': list_names,
    'Price': list_prices,
    'Description': list_descriptions,
    'Ratings': list_ratings,
    'Reviews': list_reviews
})

# Save to Excel file
# Using relative path - creates file in current directory
output_file = 'products_details.xlsx'
data.to_excel(output_file, index=False)
print(f"Data successfully saved to '{output_file}'")
print(f"File location: {os.path.abspath(output_file)}")