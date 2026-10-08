import os
import time
import functools
from src.logger import get_logger

logger = get_logger("Decorators")


def retry_and_screenshot(exceptions, retries=3, delay=1):
    """
    Retries a function. If it completely fails, takes a screenshot using
    the class's webdriver and logs it to docs/error.md.
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            for attempt in range(1, retries + 1):
                try:
                    return func(self, *args, **kwargs)
                except exceptions as e:
                    logger.warning(
                        f"Attempt {attempt}/{retries} failed in '{func.__name__}': {e}"
                    )

                    if attempt == retries:
                        os.makedirs("docs", exist_ok=True)
                        timestamp = int(time.time())
                        screenshot_name = f"error_{func.__name__}_{timestamp}.png"
                        img_path = os.path.join("docs", screenshot_name)
                        md_path = os.path.join("docs", "error.md")

                        if hasattr(self, "driver"):
                            self.driver.save_screenshot(img_path)
                            logger.error(
                                f"Critical Failure! Screenshot saved at: {img_path}"
                            )

                            with open(md_path, "a", encoding="utf-8") as f:
                                f.write(f"## Error in `{func.__name__}`\n")
                                f.write(f"**Timestamp:** {time.ctime()}\n\n")
                                f.write(
                                    f"**Exception Details:**\n```\n{str(e)}\n```\n\n"
                                )
                                f.write(
                                    f"**Screenshot Proof:**\n![Error Screenshot]({screenshot_name})\n\n---\n\n"
                                )

                        raise e

                    time.sleep(delay)

        return wrapper

    return decorator


def track_time(func):
    """Tracks how long a function takes to execute."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        logger.info(
            f"Function '{func.__name__}' completed in {time.time() - start_time:.2f} seconds."
        )
        return result

    return wrapper
