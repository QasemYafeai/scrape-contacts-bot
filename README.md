# 🔍 Web Contact Scraper Bot

This project is a Python-based tool that automates the process of finding contact information for potential installers, contractors, or dealers (for example, Generac installers in Texas). It combines multiple powerful libraries to search, extract, and save data from the web.

---

## ⚙️ How It Works

1. **Google Custom Search API** - Performs a web search based on your query.
2. **Selenium + ChromeDriver** - Loads each webpage (including JavaScript content).
3. **BeautifulSoup** - Parses the rendered HTML to get all visible text.
4. **Regex (Regular Expressions)** - Extracts phone numbers and email addresses.
5. **CSV Module** - Saves the results to a file for analysis or outreach.

---

## 🧩 Technologies Used

### ✅ Google Custom Search API
- Returns a list of relevant website URLs for any search query.
- You must have a valid **Google API key** and **Custom Search Engine ID (CX)**.

### ✅ Selenium + ChromeDriver
- Selenium automates browser tasks to render JavaScript-heavy pages.
- ChromeDriver is required to run Selenium with the Chrome browser.

### ✅ BeautifulSoup
- Parses HTML content and extracts clean text for regex scanning.

### ✅ Regex (Regular Expressions)
- Locates phone numbers and email addresses based on pattern matching.

### ✅ CSV
- Saves the scraped results in a format compatible with Excel and Google Sheets.

---

## 📦 Requirements

- **Python 3.11+**
- **Dependencies:**
  ```bash
  pip install selenium beautifulsoup4 requests python-dotenv

ChromeDriver

Download from: https://sites.google.com/chromium.org/driver/

Make sure the version matches your installed Chrome version.

Google API Credentials

Create a .env file in your root directory with:

GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY_HERE
GOOGLE_CX=YOUR_CUSTOM_SEARCH_ENGINE_ID_HERE

🛠️ Setup Instructions
Clone or Download the Project Files

Create a Virtual Environment (Recommended)

python -m venv venv
Activate the Environment

On Windows:

venv\Scripts\activate
On macOS/Linux:

source venv/bin/activate
Install Required Packages


pip install selenium beautifulsoup4 requests python-dotenv
Update Your ChromeDriver Path

Open scrape_contacts.py and update this line to match your downloaded driver path:


CHROMEDRIVER_PATH = "C:\\Users\\your_username\\Downloads\\chromedriver-win64\\chromedriver.exe"
🏃 Running the Script
In the terminal, run:

py -3.11 scrape_contacts.py

It will:

Use Google to search for URLs related to your query.

Scrape each site for phone numbers and emails.

Save the data to contacts.csv.

🔄 Customizing Your Query
You are not limited to HVAC contractors! You can modify the query inside scrape_contacts.py to target anything you want.

Open scrape_contacts.py, find this line inside the search_generac_installers() function:

query = "hvac contractor in texas"

Change it to any search you'd like:

query = "solar panel installer in California"
query = "electricians in New York contact email phone"
query = "Generac generator dealers Arkansas"
query = "plumbing contractors in Michigan"
Be creative with keywords! Just make sure they return real business pages that likely contain contact info.

📄 Output
A file called contacts.csv is generated with three columns:

URL

Phones

Emails

👨‍💻 Author
Created by Qasem Yafeai — built for scraping and lead generation automation.

📜 License
MIT License – Free to use and modify.
