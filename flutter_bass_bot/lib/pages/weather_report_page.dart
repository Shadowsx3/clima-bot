import 'package:flutter/material.dart';

import '../weather.dart';

class WeatherReport extends StatelessWidget {
  const WeatherReport({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final uri = Uri.base;
    final queryParams = uri.queryParameters;

    final weather = Weather(
      city: queryParams['city'] ?? '',
      country: queryParams['country'] ?? '',
      temp: double.tryParse(queryParams['temp'] ?? '') ?? 0,
      feelsLike: double.tryParse(queryParams['feels_like'] ?? '') ?? 0,
      humidity: int.tryParse(queryParams['humidity'] ?? '') ?? 0,
      windSpeed: double.tryParse(queryParams['wind_speed'] ?? '') ?? 0,
      description: queryParams['description'] ?? '',
    );

    return Scaffold(
      body: Container(
        decoration: const BoxDecoration(
          color: Color(0xFFB5FE01),
        ),
        child: Center(
          child: Card(
            elevation: 8,
            shape:
                RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
            child: Padding(
              padding: const EdgeInsets.all(24.0),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Text(
                    '📍 ${weather.city}, ${weather.country}',
                    style: Theme.of(context).textTheme.headlineMedium,
                  ),
                  const SizedBox(height: 16),
                  Text(
                    '🌡️ ${weather.temp.toStringAsFixed(1)}°C',
                    style: Theme.of(context).textTheme.displayLarge,
                  ),
                  const SizedBox(height: 8),
                  Text(
                    '🌬️ Sensación térmica: ${weather.feelsLike.toStringAsFixed(1)}°C',
                    style: Theme.of(context).textTheme.bodyLarge,
                  ),
                  const SizedBox(height: 8),
                  Text(
                    '🌞 Condición: ${weather.description}',
                    style: Theme.of(context).textTheme.bodyLarge,
                  ),
                  const SizedBox(height: 8),
                  Text(
                    '💧 Humedad: ${weather.humidity}%',
                    style: Theme.of(context).textTheme.bodyLarge,
                  ),
                  const SizedBox(height: 8),
                  Text(
                    '🌬️ Viento: ${weather.windSpeed.toStringAsFixed(1)} m/s',
                    style: Theme.of(context).textTheme.bodyLarge,
                  ),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}
