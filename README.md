# 🦔 Bass Weather Bot 🦔

Welcome to **Bass Weather Bot**! 🌦️🤖 This bot provides real-time weather information and counting!!!!.  
Built with `Python`, `MongoDB`, `OpenAI`'s ChatGPT, and `OpenWeather` API, this bot is a great companion for anyone who wants weather updates with a hint of hedgehog cuteness!

## Features 🦔

- **Real-time Weather** 🌍: Just ask for the weather in any location, and the bot will provide up-to-date info.
- **Persistent Conversations** 💾: Remembers your last location to make future requests even quicker.
- **User Tracking** 👥: Keeps track of how many messages you've sent and stores your preferences.

## Requirements 🧰

- Docker 🐳
- Docker Compose
- Telegram Bot API Token
- OpenWeather API Key 🌤️
- OpenAI API Key 🔑

## Setup & Installation 🛠️

### 1. Clone the Repository

```bash
git clone https://github.com/Shadowsx3/clima-bot.git
cd clima-bot
```

### 2. Configure Environment Variables

Copy the `.env.example` file to `.env` and fill in the required variables.

```bash
cp .env.example .env
```

In your `.env` file, you should include:
```
TELEGRAM_TOKEN=your_telegram_bot_token
WEATHER_API_KEY=your_openweather_api_key
OPENAI_API_KEY=your_openai_api_key
MONGO_URI=mongodb://username:password@mongo:27017
```

Copy the `example.mongo-init.js` file to `mongo-init.js` and update the password.

### 3. Build and Run with Docker 🐳

Use `docker-compose` to build and run the project. This will create two containers: one for the bot and one for MongoDB.

```bash
docker-compose up --build
```

This will start both the `mongo` and `bot` containers. The bot will now be live and listening for commands on Telegram!

## Usage 🚀

To interact with the bot:

1. Open Telegram and search for your bot (by the name you configured it with).
2. Use `/start` to initiate a conversation.
3. You can ask for the weather in any location with the following command:
   - `/clima`
4. The bot will remember the last location you asked about and will ask if you'd like to reuse it the next time you request weather info.

### Commands Available 🗂️

- **/start**: Begin a new conversation.
- **/clima**: Get the weather for a specified location. The bot will remember this location for the next time.
- **/contar**: Show all the data the bot remembers about you (just the count).

## Troubleshooting 🐞

No

### Common Issues

- **MongoDB Connection**: If the bot has trouble connecting to MongoDB, ensure your `MONGO_URI` in the `.env` file matches the database credentials.
- **API Keys**: Double-check that your API keys are correct and haven't expired.

## Contributing 🧑‍💻

We love contributions! Feel free to open issues or create pull requests. Here are some areas where we could use help:

- Add more conversation types
- Integrate additional features like reminders or notifications
- Localize the bot for other languages

## License 📄

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Thanks for using **Bass Weather Bot**! We hope you enjoy your conversations with the ~~hedgehog~~ Bass bot. 🦔