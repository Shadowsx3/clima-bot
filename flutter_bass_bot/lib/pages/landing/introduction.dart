import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';

class Introduction extends StatelessWidget {
  const Introduction({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Card(
      elevation: 8,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
      child: const Padding(
        padding: EdgeInsets.all(24.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Text(
              '🌦️ Welcome to Bass Weather Bot! 🌦️',
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
              textAlign: TextAlign.center,
            ),
            SizedBox(height: 16),
            Text(
              'Get real-time weather information or count with your favorite hedgehog! Our bot provides up-to-date weather data and even tracks your interactions... please read the EULA.',
              style: TextStyle(fontSize: 16),
            ),
            Text(
              'I am NOT a web designer nor a person with good taste in colors.',
              style: TextStyle(fontSize: 16),
            ),
            SizedBox(height: 16),
            Wrap(
              alignment: WrapAlignment.spaceEvenly,
              spacing: 8,
              runSpacing: 8,
              children: [
                Chip(
                  avatar: Icon(FontAwesomeIcons.python, size: 16),
                  label: Text('Python'),
                ),
                Chip(
                  avatar: Icon(FontAwesomeIcons.database, size: 16),
                  label: Text('MongoDB'),
                ),
                Chip(
                  avatar: Icon(FontAwesomeIcons.robot, size: 16),
                  label: Text('OpenAI'),
                ),
                Chip(
                  avatar: Icon(FontAwesomeIcons.cloud, size: 16),
                  label: Text('OpenWeather API'),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
