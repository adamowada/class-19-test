from playwright.sync_api import sync_playwright, expect
from bs4 import BeautifulSoup


def scraper(topic):
    with sync_playwright() as playwright:
        # Open chrome and navigate to my target page
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"https://apnews.com/search?q={topic}#nt=navsearch")

        # Now that we have the HTML, bring in bs4
        soup = BeautifulSoup(page.content(), "html.parser")

        search_results = soup.find("div", class_="SearchResultsModule-results")
        top_link = search_results.find("div", class_="PagePromo-title").find("a")

        # Navigate to the top link
        page.goto(top_link["href"])
        soup = BeautifulSoup(page.content(), "html.parser")

        story_body = soup.find("div", class_="RichTextStoryBody")
        story_p_elements = story_body.find_all("p")

        # Build string
        story = ""

        for elem in story_p_elements:
            story += elem.get_text()

    return story


if __name__ == "__main__":
    # scraper("cars")
    print(scraper("trump"))
