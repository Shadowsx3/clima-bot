# Telegram Bot Automation with Playwright and Python

This project uses [Playwright](https://playwright.dev/python/docs/intro) with Python to automate interactions with the web version of Telegram.

## Prerequisites

- **Python**: Ensure you have Python 3.7+ installed. You can download it from [python.org](https://www.python.org/).
- **Node.js**: Playwright requires Node.js for setup. Download and install it from [nodejs.org](https://nodejs.org/).

## Installation

### Step 1: Set Up a Virtual Environment

It's a good idea to create a virtual environment to keep dependencies organized. Use the following commands to create and activate a virtual environment:

```bash
python3 -m venv .venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 2: Install Python Dependencies

Install the required Python libraries using `pip`:

```bash
pip install playwright
pip install -r requirements.txt
```

### Step 3: Install Playwright Browsers

Playwright requires browser binaries to be installed. You can install them using:

```bash
playwright install
```

## Configuration

1. Copy `.env.example` to `.env` and fill in the required variables:
   ```bash
   cp .env.example .env
   ```
2. Set the `TELEGRAM_USER_ID` variable in your `.env` file. To get your Telegram user ID, follow these steps:
   - Open Telegram and search for the "UserInfoBot" (or any other bot that can retrieve user IDs).
   - Start a chat with the bot and send the command `/start`.
   - The bot will respond with your user ID.
   - Copy the user ID and paste it into your `.env` file.

### How to Run

To start the bot, please read the top level readme and use docker.

1. **Launch Chrome with Remote Debugging**:
   ```bash
   /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="$HOME/Library/Application Support/Google/Chrome"
   ```
   
   And then sign in on telegram web (only needed the first time)

2. **Run the Tests**:
   Navigate to the project root directory and run the tests using Pytest:
   ```bash
   pytest tests/
   ```
   
### Notes

- **Headless Mode**: By default, the browser runs in headless mode (without a visible UI). Set `headless=False` to see the browser window during execution.
- **Timeouts and Delays**: Use `page.wait_for_timeout()` for delays, and ensure you wait for elements to load properly to avoid errors.
