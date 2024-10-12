import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';

class LandingPage extends StatelessWidget {
  const LandingPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 8,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
      child: Padding(
        padding: const EdgeInsets.all(24.0),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            ShaderMask(
              shaderCallback: (bounds) => const LinearGradient(
                colors: [
                  Colors.red,
                  Colors.orange,
                  Colors.yellow,
                  Colors.green,
                  Colors.blue,
                  Colors.indigo,
                  Colors.purple,
                ],
              ).createShader(bounds),
              child: const Text(
                '🦔 Welcome to Hedgehog Weather! 🦔',
                style: TextStyle(
                  fontSize: 24,
                  fontWeight: FontWeight.bold,
                  color: Colors.white,
                ),
                textAlign: TextAlign.center,
              ),
            ),
            const SizedBox(height: 30),
            const Text(
              'Get weather updates and count with our Telegram bot!',
              style: TextStyle(fontSize: 18),
              textAlign: TextAlign.center,
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                launchUrl(Uri.parse('https://t.me/Bas5WeatherBot'));
              },
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.black,
                foregroundColor: Colors.white,
              ),
              child: const Text('Open @Bas5WeatherBot on Telegram'),
            ),
            const SizedBox(height: 40),
            const Wrap(
              spacing: 10,
              runSpacing: 10,
              alignment: WrapAlignment.center,
              children: [
                Text('🦔', style: TextStyle(fontSize: 40)),
                Text('🦔', style: TextStyle(fontSize: 40)),
                Text('🦔', style: TextStyle(fontSize: 40)),
                Text('🦔', style: TextStyle(fontSize: 40)),
                Text('🦔', style: TextStyle(fontSize: 40)),
                Text('🦔', style: TextStyle(fontSize: 40)),
                Text('🦔', style: TextStyle(fontSize: 40)),
                Text('🦔', style: TextStyle(fontSize: 40)),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
