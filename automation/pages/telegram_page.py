from pages.base_page import BasePage

class TelegramPage(BasePage):
    BASE_TELEGRAM_URL = "https://web.telegram.org/k/#"

    def goto_telegram(self, bot_handle: str):
        # Construct the URL to open the bot chat directly
        url = f"{self.BASE_TELEGRAM_URL}{bot_handle}"
        self.goto(url)

    def send_message(self, message: str):
        # Send a message to the bot
        self.type("div[contenteditable='true']", message)
        self.page.keyboard.press("Enter")

    def get_last_message(self):
        # Retrieve the last message sent in the chat
        return self.page.locator("div.message").last.inner_text()
