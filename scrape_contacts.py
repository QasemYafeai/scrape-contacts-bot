import os
import re
import time
import csv
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv


load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CX = os.getenv("GOOGLE_CX")

# Set your ChromeDriver executable path 
CHROMEDRIVER_PATH = "C:\\Users\\qasem\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

# Regex patterns to match phone numbers and emails
phone_pattern = re.compile(
    r'(\+?\d{1,2}\s*(?:[-.\s])?\(?\d{3}\)?\s*(?:[-.\s])?\d{3}\s*(?:[-.\s])?\d{4})'
)
email_pattern = re.compile(
    r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
)

def search_generac_installers(total_results=10):
   
    query = "hvac contractor in texas"
    base_url = "https://www.googleapis.com/customsearch/v1"
    results = []
    
    
    pages = total_results // 10
    if total_results % 10:
        pages += 1

    for page in range(pages):
        start = page * 10 + 1
        params = {
            "key": GOOGLE_API_KEY,
            "cx": GOOGLE_CX,
            "q": query,
            "num": 10,  
            "start": start
        }
        resp = requests.get(base_url, params=params)
        if resp.status_code != 200:
            print("Google search error on page", page + 1, ":", resp.text)
            continue
        data = resp.json()
        items = data.get("items", [])
        urls = [item.get("link") for item in items if item.get("link")]
        results.extend(urls)
    return results

def scrape_contact_info(url: str):
   
    # Configure Selenium Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    
    # Create a Service object for ChromeDriver
    service = Service(CHROMEDRIVER_PATH)
    
    try:
        driver = webdriver.Chrome(service=service, options=chrome_options)
    except Exception as e:
        print("Error initializing ChromeDriver:", e)
        return None

    try:
        driver.get(url)
        # Wait for JavaScript to load
        time.sleep(5)
        rendered_html = driver.page_source
    except Exception as e:
        print(f"Error loading {url}: {e}")
        return None
    finally:
        driver.quit()

    # Parse the rendered HTML with BeautifulSoup
    soup = BeautifulSoup(rendered_html, "html.parser")
    text_content = soup.get_text(separator=" ", strip=True)

    # Use regex to extract phone numbers and emails
    phones = list(set(phone_pattern.findall(text_content)))
    emails = list(set(email_pattern.findall(text_content)))

    return {"url": url, "phones": phones, "emails": emails}

def write_contacts_to_csv(contacts, filename="contacts.csv"):
    """
    Writes a list of contact dictionaries to a CSV file.
    Each dictionary should have keys: 'url', 'phones', 'emails'.
    """
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Write header row
        writer.writerow(["URL", "Phones", "Emails"])
        # Write each contact info row
        for contact in contacts:
            phones_str = "; ".join(contact.get("phones", []))
            emails_str = "; ".join(contact.get("emails", []))
            writer.writerow([contact.get("url", ""), phones_str, emails_str])
    print(f"Contacts written to {filename}")

def main():
    urls = search_generac_installers(total_results=10)
    if not urls:
        print("No URLs found from Google search.")
        return
    
    print("Found URLs:")
    for url in urls:
        print(" -", url)
    
    # Step 2: For each URL, scrape the page for phone numbers and emails
    all_contacts = []
    for url in urls:
        print("\nScraping:", url)
        info = scrape_contact_info(url)
        if info:
            print("Contact info found:", info)
            all_contacts.append(info)
        else:
            print("Failed to scrape", url)
    
    # Step 3: Output aggregated results to console
    print("\nAggregated Contact Information:")
    for contact in all_contacts:
        print(contact)
    
    # Step 4: Write the results to a CSV file
    write_contacts_to_csv(all_contacts)

if __name__ == "__main__":
    main()
