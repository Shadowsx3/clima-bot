import 'package:flutter/material.dart';
import 'package:telegram_web_app/telegram_web_app.dart';

import 'my_home_page.dart';

void main() async {
  try {
    if (TelegramWebApp.instance.isSupported) {
      TelegramWebApp.instance.ready();
      Future.delayed(
          const Duration(seconds: 1), TelegramWebApp.instance.expand);
    }
  } catch (e) {
    print("Error happened in Flutter while loading Telegram $e");
    await Future.delayed(const Duration(milliseconds: 200));
    main();
    return;
  }

  FlutterError.onError = (details) {
    print("Flutter error happened: $details");
  };

  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Weather App',
      theme: TelegramThemeUtil.getTheme(TelegramWebApp.instance),
      home: const MyHomePage(),
    );
  }
}
