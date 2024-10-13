# 🦔 Bass Weather Bot 🦔

Welcome to **Bass Weather Bot**! 🌦️🤖 This bot provides real-time weather information and even tracks your interactions with it.  
Built with `Python`, `MongoDB`, `OpenAI`'s ChatGPT, and `OpenWeather` API, the Bass Weather Bot offers up-to-date weather info with a hint of hedgehog charm!

## Features 🦔

- **Real-time Weather** 🌍: Just ask for the weather in any location, and the bot will provide up-to-date info.
- **Persistent Conversations** 💾: Remembers your last location to make future requests even quicker.
- **User Tracking** 👥: Keeps track of your interactions and stores preferences.
- **Mini Flutter App** 📱: A companion Flutter mini-app hosted on Vercel and integrated with the bot to display weather information.
- **Web Landing Page** 🖥️: A small landing page hosted on Vercel with a custom domain, accessible at [https://bot.bassmd0.com/](https://bot.bassmd0.com/).
- **Traffic Proxy** 🔍: A proxy on `proxy_helper` to inspect bot traffic on the local env.
- **Continuous Deployment** 🚀: Automatic deployments from the main branch to a container app on Azure.
- **Grafana Monitoring** 📊: Access to comprehensive logs and metrics via Grafana hosted on Azure.
- **Observability with Sentry** 🔍: Detailed tracking of issues and performance.
- **Docker Compose Setup** 🐳: Simplified testing setup using Docker Compose to minimize overhead.
- **GitHub Actions Pipeline** ⚙️: Automated testing pipeline to ensure code quality and functionality.
- **MongoDB Atlas and Azure Container Apps** 🦔: A stable production environment running in the cloud.
- **UI E2E Tests with Playwright** 🧪: End-to-end tests for the bot's user interface, built with Python and Playwright to ensure smooth, real-world interactions.

## Requirements 🧰

- Docker 🐳
- Docker Compose
- Mitmproxy -> To debug connections (optional)
- Telegram Bot API Token
- OpenWeather API Key 🌤️
- OpenAI API Key 🔑

## Setup & Installation 🛠️

### 1. Clone the Repository

```bash
git clone https://github.com/Shadowsx3/clima-bot.git
cd clima-bot
```

### 2. Configure Environment

Copy the `.env.example` file to `.env` and fill in the required variables.

```bash
cp .env.example .env
```

In your `.env` file, include:
```
TELEGRAM_TOKEN=your_telegram_bot_token
WEATHER_API_KEY=your_openweather_api_key
OPENAI_API_KEY=your_openai_api_key
```

Copy the `example.mongo-init.js` file to `mongo-init.js` and update the MongoDB credentials.

### 3. Build and Run with Docker 🐳

Use `docker-compose` to build and run the project. This will create the containers necessary for the bot, MongoDB, and other services.

```bash
docker-compose up --build
```

This will start both the `mongo` and `bot` containers, as well as any supporting services for local testing. The bot will now be live and listening for commands on Telegram!

## Usage 🚀

To interact with the bot:

1. Open Telegram and search for your bot by the name you configured.
2. Use `/start` to initiate a conversation.
3. Use `/clima` to get the weather in any location. 
4. Use `/contar` to count!!!!!
5. The bot will remember the last location you asked about and will ask if you'd like to reuse it the next time you request weather info.

### Available Commands 🗂️

- **/start**: Begin a new conversation.
- **/clima**: Get the weather for a specified location. The bot will remember this location for future queries.
- **/contar**: View the interaction count and details the bot remembers about you.

## Testing 🧪

Unit testing for the bot code is included. You can run tests locally using the following command:

```bash
pytest tests/
```

### UI End-to-End Testing

End-to-end testing for the bot’s user interface is performed with **Playwright** and **Python**. These tests simulate real user interactions, ensuring the bot performs correctly in real-world scenarios.

To run these tests, open the automation folder and check the readme, then in that folder run:

```bash
pytest tests/
```

### GitHub Actions Pipeline

The project includes a GitHub Actions pipeline to automate testing on every push and pull request to the `main` branch. This ensures all new changes are tested before merging.

The pipeline configuration is in `.github/workflows/python-test.yml`, which includes the following steps:

1. **Setup Environment**: Checks out the code and sets up a Python environment.
2. **Install Dependencies**: Installs all necessary dependencies specified in `requirements.txt`.
3. **Run Tests**: Executes unit tests using `pytest` to then generate and upload a report.

The pipeline automatically runs on GitHub when new commits are pushed or a pull request is opened.

## Observability 🔍

- **Grafana**: To monitor application performance and logs.
- **Sentry**: Any errors or performance issues will be logged to Sentry, providing detailed information for debugging.

## Troubleshooting 🐞

### Common Issues

- **MongoDB Connection**: If the bot has trouble connecting to MongoDB, ensure that your `MONGO_URI` in the `.env` file is correct and reachable.
- **API Keys**: Double-check that your API keys are correct and haven’t expired...
- **Grafana or Sentry Access**: Ensure that you have access... to an Azure account on the tenant

## Contributing 🧑‍💻

We welcome contributions! Feel free to ~~open issues~~ or create pull requests. Here are some areas where you can help:

- Everything

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Thanks for using **Bass Weather Bot**! Enjoy your interactions with our ~~hedgehog~~ Bass bot. 🦔