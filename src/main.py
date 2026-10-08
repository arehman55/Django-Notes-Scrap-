from src.logger import get_logger
from src.scraper import DjangoDocsScraper

logger = get_logger("MainExecutor")


def main():
    logger.info("Starting Enterprise Web Scraper Pipeline...")
    scraper = DjangoDocsScraper()

    try:
        start_url = "https://docs.djangoproject.com/en/6.1/intro/tutorial01/"
        scraper.load_page(start_url)

        for current_part in range(1, 4):
            page_data = scraper.extract_snippets(part_number=current_part)

            scraper.save_markdown(page_data)

            if current_part < 3:
                next_part = current_part + 1
                logger.info(
                    f"Transitioning from Part {current_part} to Part {next_part}..."
                )
                scraper.navigate_to_next_part(next_part_number=next_part)

        logger.info(
            "Automation pipeline completed successfully! Check the 'docs' folder."
        )

    except Exception as e:
        logger.error(f"Pipeline completely halted due to error: {e}")
        logger.error(
            "Check 'docs/error.md' for visual screenshot evidence of the failure."
        )

    finally:
        scraper.close()


if __name__ == "__main__":
    main()
