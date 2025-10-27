from typing import Final, Optional
import requests

API_KEY: Final[str] = "Your Key"
BASE_URL: Final[str] = "https://cutt.ly/api/api.php"


def shorten_link(full_link: str) -> Optional[str]:

    if not full_link.startswith(("http://", "https://")):
        full_link = "https://" + full_link

    try:
        response = requests.get(BASE_URL, params={"key": API_KEY, "short": full_link})
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Network/API error: {e}")
        return None
    except ValueError:
        print("Failed to decode response JSON.")
        return None

    url_data = data.get("url")
    if not url_data:
        print("Invalid response from API (No 'url' field).")
        return None

    status = url_data.get("status")
    if status == 7:
        return url_data.get("shortLink")
    else:
        print(f"API Error! Status code: {status}")
        return None


def main():
    full_link = input("Enter a link to shorten: ").strip()
    short_link = shorten_link(full_link)

    if short_link:
        print(f"Shortened Link: {short_link}")
    else:
        print("Failed to shorten the link.")


if __name__ == "__main__":
    main()
