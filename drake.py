import requests
import time
from fake_useragent import UserAgent
import cloudscraper


ua = UserAgent()
scraper = cloudscraper.create_scraper()

url = "https://drake.exchange/email-api/subscribe/email"

with open("list.txt", "r") as file:
    emails = file.read().splitlines()

for email in emails:
    params = {"email": email}
    headers = {
        "User-Agent": ua.random
    }
    
    try:
        response = scraper.post(url, params=params, headers=headers)
        

        if response.status_code == 200:
            print(f"Sukses su asu {email}")
        else:
            print(f"Gagal su asu {email}. Status code: {response.status_code}")
    
    except Exception as e:
        print(f"Error jink cacat {email}: {e}")
    
    time.sleep(15)

print("Dah selesai kabeh.")