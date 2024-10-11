import 'package:flutter/material.dart';
import 'package:telegram_web_app/telegram_web_app.dart';

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  String? city;
  String? country;
  double? temp;
  double? feelsLike;
  int? humidity;
  double? windSpeed;
  String? description;

  @override
  void initState() {
    super.initState();
    _initializeWeatherData();
  }

  void _initializeWeatherData() {
    var data = TelegramWebApp.instance.initData.toString();
    // Here you can simulate data or replace this method to receive actual data from Telegram
    setState(() {
      data = data;
      city = "Salto";
      country = "UY";
      temp = 25.0;
      feelsLike = 26.5;
      humidity = 60;
      windSpeed = 5.0;
      description = "Despejado";
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.primary,
        title: const Text('🌦️ Clima'),
      ),
      body: Center(
        child: city == null
            ? const CircularProgressIndicator()
            : Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Text(
                    '📍 $city, $country',
                    style: Theme.of(context).textTheme.headlineMedium,
                  ),
                  const SizedBox(height: 16),
                  Text(
                    '🌡️ ${temp?.toStringAsFixed(1)}°C',
                    style: Theme.of(context).textTheme.displayLarge,
                  ),
                  const SizedBox(height: 8),
                  Text(
                    '🌬️ Sensación térmica: ${feelsLike?.toStringAsFixed(1)}°C',
                    style: Theme.of(context).textTheme.bodyLarge,
                  ),
                  const SizedBox(height: 8),
                  Text(
                    '🌞 Condición: $description',
                    style: Theme.of(context).textTheme.bodyLarge,
                  ),
                  const SizedBox(height: 8),
                  Text(
                    '💧 Humedad: $humidity%',
                    style: Theme.of(context).textTheme.bodyLarge,
                  ),
                  const SizedBox(height: 8),
                  Text(
                    '🌬️ Viento: ${windSpeed?.toStringAsFixed(1)} m/s',
                    style: Theme.of(context).textTheme.bodyLarge,
                  ),
                ],
              ),
      ),
    );
  }
}
