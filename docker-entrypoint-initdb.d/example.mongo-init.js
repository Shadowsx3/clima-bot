db = db.getSiblingDB('weather_bot_db');
db.createUser({
    user: "root",
    pwd: "", // Update with the pass
    roles: [{ role: "readWrite", db: "weather_bot_db" }]
});
db.createCollection('user_data');