import wikipediaapi

def ask_wikipedia(query, language="en"):
    """
    Query Wikipedia and return a direct summary.

    :param query: The search query or topic to look up on Wikipedia.
    :param language: The language code for Wikipedia (default is "en" for English).
    :return: A summary of the Wikipedia page or an error message if the page is not found.
    """
    # Initialize the Wikipedia API with the specified language
    wiki_wiki = wikipediaapi.Wikipedia(language)

    # Fetch the page
    page = wiki_wiki.page(query)

    # Check if the page exists
    if page.exists():
        # Return the summary of the page
        return page.summary
    else:
        return "Sorry, I couldn't find any information on that topic."