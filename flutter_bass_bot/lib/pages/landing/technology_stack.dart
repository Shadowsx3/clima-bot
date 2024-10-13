import 'package:flutter/material.dart';
import 'package:flutter_bass_bot/pages/landing/tech_item.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';

class TechnologyStack extends StatelessWidget {
  const TechnologyStack({Key? key}) : super(key: key);

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
              'Technology Stack',
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 16),
            Wrap(
              spacing: 16,
              runSpacing: 16,
              alignment: WrapAlignment.center,
              children: [
                TechItem(icon: FontAwesomeIcons.python, name: 'Python'),
                TechItem(icon: FontAwesomeIcons.database, name: 'MongoDB'),
                TechItem(icon: FontAwesomeIcons.robot, name: 'OpenAI'),
                TechItem(icon: FontAwesomeIcons.cloud, name: 'OpenWeather API'),
                TechItem(icon: FontAwesomeIcons.docker, name: 'Docker'),
                TechItem(icon: FontAwesomeIcons.github, name: 'GitHub Actions'),
                TechItem(icon: FontAwesomeIcons.microsoft, name: 'Azure'),
                TechItem(icon: FontAwesomeIcons.chartBar, name: 'Grafana'),
                TechItem(icon: FontAwesomeIcons.bug, name: 'Sentry'),
                TechItem(icon: FontAwesomeIcons.flask, name: 'Playwright'),
                TechItem(icon: FontAwesomeIcons.searchengin, name: 'Mitmproxy'),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
