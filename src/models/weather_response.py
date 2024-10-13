from dataclasses import dataclass

@dataclass
class WeatherResponse:
    city: str
    country: str
    temp: float
    feels_like: float
    humidity: int
    wind_speed: float
    description: str

    def __str__(self):
        return (
            f"El clima en {self.city}, {self.country} es actualmente {self.description}. "
            f"La temperatura es de {self.temp}°C, con una sensación térmica de {self.feels_like}°C. "
            f"La humedad es del {self.humidity}%, y la velocidad del viento es de {self.wind_speed} km/h."
        )
