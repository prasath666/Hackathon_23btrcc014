import requests
from bs4 import BeautifulSoup

def search_google(query, language="en"):
    """
    Perform a Google search and return a direct answer or suggest opening Chrome.

    :param query: The search query.
    :param language: The language code for search results (default is "en" for English).
    :return: A direct answer or a suggestion to open Chrome for more details.
    """
    try:
        # Perform a Google search
        url = f"https://www.google.com/search?q={query}&hl={language}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # Parse the HTML response
            soup = BeautifulSoup(response.text, "html.parser")
            # Extract the top result (usually in a <div> with class "BNeawe")
            top_result = soup.find("div", class_="BNeawe")
            if top_result:
                return top_result.get_text()
            else:
                # If no direct answer is found, suggest opening Chrome
                return f"I couldn't find a direct answer. Would you like me to open Chrome to search for '{query}'?"
        else:
            return "Sorry, I couldn't perform the search at the moment."
    except Exception as e:
        return f"Error performing the search: {e}"