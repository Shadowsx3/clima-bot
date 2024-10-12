# Telegram Bot Automation with Playwright and Python

This project uses [Playwright](https://playwright.dev/python/docs/intro) with Python to automate interactions with the web version of Telegram.

## Prerequisites

- **Python**: Ensure you have Python 3.7+ installed. You can download it from [python.org](https://www.python.org/).
- **Node.js**: Playwright requires Node.js for setup. Download and install it from [nodejs.org](https://nodejs.org/).

## Installation

### Step 1: Clone the Repository

Clone the project repository from GitHub. If you haven't already created one, you can create your own repository or initialize a new directory:

```bash
git clone https://github.com/yourusername/telegram-playwright-bot.git
cd telegram-playwright-bot
```

### Step 2: Set Up a Virtual Environment

It's a good idea to create a virtual environment to keep dependencies organized. Use the following commands to create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Python Dependencies

Install the required Python libraries using `pip`:

```bash
pip install playwright
pip install -r requirements.txt
```

### Step 4: Install Playwright Browsers

Playwright requires browser binaries to be installed. You can install them using:

```bash
playwright install
```

This will download and install the necessary browsers (Chromium, Firefox, and WebKit) for Playwright to interact with.

## Usage

To start the bot, please read the top level readme and use docker.

Then use:

```bash
pytest e2e
```

### Notes

- **Headless Mode**: By default, the browser runs in headless mode (without a visible UI). Set `headless=False` to see the browser window during execution.
- **Timeouts and Delays**: Use `page.wait_for_timeout()` for delays, and ensure you wait for elements to load properly to avoid errors.

## Additional Resources

- [Playwright Python Documentation](https://playwright.dev/python/docs/intro)
- [Telegram Bot API Documentation](https://core.telegram.org/bots/api)