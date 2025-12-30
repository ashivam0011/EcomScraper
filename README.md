# EcomScraper
A Python web scraper that extracts e-commerce product data and exports to Excel
# Web Scraping Project: E-commerce Product Data Extraction

A Python-based web scraping project that extracts product information from e-commerce websites and exports the data to Excel format. This project demonstrates fundamental web scraping techniques using BeautifulSoup and requests libraries.

## 📋 Overview

This project scrapes product data from a test e-commerce website, extracting valuable information such as product names, prices, descriptions, ratings, and review counts. The scraped data is then organized into a structured format and saved as an Excel file for easy analysis and review.

## ✨ Features

- **Product Name Extraction**: Scrapes product titles from the e-commerce site
- **Price Extraction**: Captures product pricing information
- **Description Scraping**: Extracts detailed product descriptions
- **Rating System**: Counts and extracts star ratings for each product
- **Review Counts**: Gathers the number of reviews for each product
- **Excel Export**: Automatically saves all scraped data to an Excel file
- **Data Summary**: Displays a comprehensive summary of extracted data

## 🛠️ Technologies Used

- **Python 3**: Core programming language
- **Requests**: HTTP library for making web requests
- **BeautifulSoup4**: HTML parsing library for extracting data
- **Pandas**: Data manipulation and DataFrame creation
- **OpenPyXL**: Excel file generation (dependency for pandas)

## 📦 Installation

### Prerequisites

Make sure you have Python 3.6 or higher installed on your system.

### Install Dependencies

```bash
pip install requests beautifulsoup4 pandas openpyxl
```

Or install all at once:

```bash
pip install -r requirements.txt
```

*(Note: Create a `requirements.txt` file with the dependencies if needed)*

## 🚀 Usage

1. Navigate to the project directory:
   ```bash
   cd scrappingDoc
   ```

2. Run the script:
   ```bash
   python Practice/01_Basics.py
   ```

3. The script will:
   - Fetch the webpage from the target URL
   - Extract all product information
   - Display a summary of scraped data in the console
   - Save the data to `products_details.xlsx` in the current directory

## 📁 Project Structure

```
scrappingDoc/
│
├── Practice/
│   └── 01_Basics.py          # Main scraping script
│
├── README.md                  # Project documentation
└── products_details.xlsx      # Output file (generated after running)
```

## 📊 Output

The script generates an Excel file (`products_details.xlsx`) containing the following columns:

| Column | Description |
|--------|-------------|
| Name | Product name/title |
| Price | Product price |
| Description | Product description |
| Ratings | Star rating (out of 5) |
| Reviews | Number of reviews |

## 🔍 How It Works

1. **HTTP Request**: Sends a GET request to the target e-commerce website
2. **HTML Parsing**: Uses BeautifulSoup to parse the HTML content
3. **Data Extraction**: Extracts data using CSS selectors and HTML class names:
   - Product names from `<a class="title">` tags
   - Prices from `<h4 class="price">` tags
   - Descriptions from `<p class="description">` tags
   - Ratings by counting star icons
   - Reviews from review count elements
4. **Data Organization**: Creates a pandas DataFrame to structure the data
5. **Export**: Saves the DataFrame to an Excel file

## 📝 Code Highlights

- **Error Handling**: Checks HTTP response status before processing
- **Clean Data Extraction**: Uses `.strip()` to remove extra whitespace
- **Structured Output**: Organizes data in a pandas DataFrame for easy manipulation
- **Progress Feedback**: Provides console output to track scraping progress

## 🎯 Target Website

The script currently targets:
- **URL**: `https://webscraper.io/test-sites/e-commerce/allinone/phones/touch`
- **Content**: Touch phone products from a test e-commerce site

## ⚠️ Important Notes

- This script is designed for educational purposes and uses a test website
- Always respect websites' `robots.txt` and terms of service
- Be mindful of rate limiting when scraping production websites
- Some websites may require headers or cookies for successful requests

## 🔧 Customization

To scrape a different website:

1. Update the `url` variable in the script
2. Inspect the target website's HTML structure
3. Modify the CSS selectors and class names accordingly
4. Adjust the data extraction logic as needed

## 📚 Learning Resources

This project demonstrates:
- Web scraping fundamentals
- HTML parsing with BeautifulSoup
- Data extraction techniques
- Data manipulation with pandas
- File export operations

## 👤 Author

Shivam Vaishnav

---

**Note**: This is a learning project showcasing web scraping techniques. Always ensure you have permission to scrape websites and comply with their terms of service.

