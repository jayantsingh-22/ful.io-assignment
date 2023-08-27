import requests
from bs4 import BeautifulSoup
import re
from email_scraper import scrape_emails

def get_social_links(soup):
    social_links = []
    social_patterns = [
        r"facebook\.com/[^/]+",
        r"linkedin\.com/[^/]+",
        r"twitter\.com/[^/]+",
        r"instagram\.com/[^/]+",
        r"youtube\.com/[^/]+"
    ]
    
    for pattern in social_patterns:
        matches = soup.find_all(href=re.compile(pattern, re.I))
        social_links.extend([match['href'] for match in matches])
    
    return social_links

def get_email(soup):
    emails = scrape_emails(str(soup))
    return emails

def get_contacts(soup):
    contact_patterns = [
        r"\+\d{1,9}[-\s]\d{0,9}[-\s]\d{0,9}[-\s]\d{4}",
    ]
    
    contacts = []
    for pattern in contact_patterns:
        matches = re.findall(pattern, str(soup))
        contacts.extend(matches)
    
    return contacts

def main():
    url = input("Enter the website URL: ")
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        social_links = get_social_links(soup)
        email = get_email(soup)
        contacts = get_contacts(soup)
        
        print("Social links -")
        for link in social_links:
            print(link)
        
        if email:
            print("Email:", email)
        
        if contacts:
            print("Contacts:")
            for contact in contacts:
                print(contact)

    else:
        print("Error: Unable to fetch the website.")

if __name__ == "__main__":
    main()
