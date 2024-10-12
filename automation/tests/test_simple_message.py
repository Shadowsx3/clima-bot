import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from pages.telegram_page import TelegramPage
from utils.mongo_client import MongoClient

load_dotenv()

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://localhost:9222")
        yield browser
        # browser.close()

@pytest.fixture(scope="class")
def page(browser):
    context = browser.contexts[0]
    page = context.new_page()
    yield page
    # context.close() I dont want to close it now

@pytest.fixture(scope="class")
def mongo_client():
    client = MongoClient()
    yield client

@pytest.fixture(scope="class", autouse=True)
def setup_telegram(page):
    telegram_page = TelegramPage(page)
    telegram_page.goto_telegram(os.getenv("TELEGRAM_BOT_HANDLE"))

@pytest.mark.usefixtures("page", "mongo_client", "setup_telegram")
class TestSimpleCount:
    def test_send_message_to_bot(self, page, mongo_client):
        telegram_page = TelegramPage(page)
        user_id = os.getenv("TELEGRAM_USER_ID")

        mongo_client.set_count(user_id, 5)
        telegram_page.send_message("/contar")
        page.wait_for_timeout(3000)

        updated_count = mongo_client.get_count(user_id)
        assert updated_count == 6, f"Expected count to be 6 but got {updated_count}."

        last_message = telegram_page.get_last_message().split("\n")[0]
        expected_message = f"El contador es: {updated_count}"
        assert last_message == expected_message, f"Expected last message to be '{expected_message}' but got '{last_message}'."

    def test_send_two_message_to_bot(self, page, mongo_client):
        telegram_page = TelegramPage(page)
        user_id = os.getenv("TELEGRAM_USER_ID")

        mongo_client.set_count(user_id, 555)
        telegram_page.send_message("/contar")
        page.wait_for_timeout(3000)

        telegram_page.send_message("/contar")
        page.wait_for_timeout(3000)

        updated_count = mongo_client.get_count(user_id)
        assert updated_count == 557, f"Expected count to be 557 but got {updated_count}."

        last_message = telegram_page.get_last_message().split("\n")[0]
        expected_message = f"El contador es: {updated_count}"
        assert last_message == expected_message, f"Expected last message to be '{expected_message}' but got '{last_message}'."
