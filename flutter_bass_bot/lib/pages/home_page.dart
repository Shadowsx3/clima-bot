import 'package:flutter/material.dart';

import 'landing_page.dart';
import 'weather_report_page.dart';

class HomePage extends StatelessWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final uri = Uri.base;
    final hasQueryParams = uri.queryParameters.isNotEmpty;

    return Scaffold(
      body: Container(
        decoration: const BoxDecoration(
          color: Color(0xFFB5FE01),
        ),
        child: Center(
          child: hasQueryParams ? const WeatherReport() : const LandingPage(),
        ),
      ),
    );
  }
}
