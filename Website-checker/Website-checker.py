import csv
import requests
from fake_useragent import UserAgent
from http import HTTPStatus

csv_path = "websites.csv"

def get_websites(csv_path: str) -> list[str]:
    websites = []
    with open(csv_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if not row:
                continue
            url = row[1].strip() if len(row) > 1 else row[0].strip()
            if not url.startswith(('http://', 'https://')):
                url = f"https://{url}"
            websites.append(url)
    return websites

def get_user_agent() -> str:
    ua = UserAgent()
    return ua.chrome

def get_status_description(status_code: int) -> str:
    try:
        value = HTTPStatus(status_code)
        return f"{value.value} {value.phrase} : {value.description}"
    except ValueError:
        return "Unknown status code!"

def check_website(website: str, user_agent: str) -> str:
    try:
        response = requests.get(website, headers={'User-Agent': user_agent}, timeout=5)
        return f"{website} -> {get_status_description(response.status_code)}"
    except Exception as e:
        return f"Could not reach this site: {website} ({e.__class__.__name__})"

def main():
    sites = get_websites(csv_path)
    user_agent = get_user_agent()
    results = []

    for site in sites:
        result = check_website(site, user_agent)
        print(result)
        results.append(result)

    with open('website_status.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Website', 'Status'])
        for line in results:
            site, status = line.split(' -> ', 1) if '->' in line else (line, '')
            writer.writerow([site, status])

if __name__ == '__main__':
    main()
