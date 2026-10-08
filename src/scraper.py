import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException,
)
from selenium.webdriver.common.action_chains import ActionChains

from src.logger import get_logger
from src.models import PageData, CodeSnippet
from src.utils import retry_and_screenshot, track_time

logger = get_logger("DjangoScraper")


class DjangoDocsScraper:
    def __init__(self):
        logger.info("Initializing Native Google Chrome WebDriver...")
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 15)
        self.action = ActionChains(self.driver)

    @track_time
    @retry_and_screenshot(exceptions=(TimeoutException,))
    def load_page(self, url: str) -> None:
        """Navigates to the initial URL and scrolls."""
        logger.info(f"Navigating to URL: {url}")
        self.driver.get(url)
        self._scroll_page_purely()

    def _scroll_page_purely(self) -> None:
        """Scrolls the page safely using Keyboard simulation instead of JS."""
        logger.info("Scrolling down using pure keyboard Actions...")

        body_element = self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        for _ in range(5):
            body_element.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.3)

        body_element.send_keys(Keys.HOME)
        time.sleep(0.5)

    @track_time
    def extract_snippets(self, part_number: int) -> PageData:
        """Extracts scripts and a 1-2 line summary strictly using XPath."""
        logger.info(f"Extracting scripts for Part {part_number}...")
        snippets_list = []

        code_blocks = self.driver.find_elements(
            By.XPATH, "//div[contains(@class, 'highlight')]"
        )

        for block in code_blocks:
            try:
                summary_element = block.find_element(By.XPATH, "./preceding::p[1]")

                raw_summary = summary_element.text.strip()
                raw_code = block.text.strip()

                if not raw_code:
                    continue

                short_summary = (
                    raw_summary[:150] + "..." if len(raw_summary) > 150 else raw_summary
                )

                snippet = CodeSnippet(
                    part_number=part_number, summary=short_summary, code=raw_code
                )
                snippets_list.append(snippet)
            except Exception as e:
                logger.debug(f"Skipped a snippet gracefully: {e}")

        logger.info(f"Successfully extracted {len(snippets_list)} valid scripts.")
        return PageData(part_title=f"Part_{part_number}", snippets=snippets_list)

    @retry_and_screenshot(
        exceptions=(TimeoutException, ElementClickInterceptedException)
    )
    def navigate_to_next_part(self, next_part_number: int) -> None:
        """Finds the 'Next Part' link, scrolls to it, and clicks using ActionChains."""
        link_text = f"Writing your first Django app, part {next_part_number}"
        logger.info(f"Looking for next page link: '{link_text}'")

        next_link = self.wait.until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, link_text))
        )

        self.action.move_to_element(next_link).perform()
        time.sleep(0.5)

        next_link = self.wait.until(
            EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, link_text))
        )

        next_link.click()
        logger.info(f"Successfully navigated to Part {next_part_number}.")
        time.sleep(1.5)

    def save_markdown(self, data: PageData) -> None:
        """Saves data into a clean Markdown structure."""
        os.makedirs("docs", exist_ok=True)
        file_path = os.path.join("docs", f"{data.part_title}.md")

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(f"# {data.part_title.replace('_', ' ')} - Extracted Scripts\n\n")
            for idx, snippet in enumerate(data.snippets, 1):
                file.write(f"### Script {idx}\n")
                file.write(f"**Summary:** {snippet.summary}\n\n")
                file.write("```python\n")
                file.write(f"{snippet.code}\n")
                file.write("```\n\n---\n\n")

        logger.info(f"Data safely written to {file_path}")

    def close(self):
        logger.info("Tearing down browser resources...")
        self.driver.quit()
