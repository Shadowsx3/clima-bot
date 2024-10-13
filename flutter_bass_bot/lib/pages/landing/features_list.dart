import 'package:flutter/material.dart';
import 'package:flutter_bass_bot/pages/landing/feature_item.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';

class FeaturesList extends StatelessWidget {
  const FeaturesList({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final features = [
      {
        'icon': FontAwesomeIcons.globe,
        'title': 'Real-time Weather',
        'description': 'Get up-to-date weather info for any location.'
      },
      {
        'icon': FontAwesomeIcons.comments,
        'title': 'Persistent Conversations',
        'description':
            'The bot remembers your last location for quicker future requests.'
      },
      {
        'icon': FontAwesomeIcons.userCheck,
        'title': 'User Tracking',
        'description': 'Keeps track of your interactions and stores your count.'
      },
      {
        'icon': FontAwesomeIcons.mobileScreen,
        'title': 'Mini Flutter App',
        'description':
            'A companion app hosted on Vercel to display weather information.'
      },
      {
        'icon': FontAwesomeIcons.laptop,
        'title': 'Web Landing Page',
        'description': 'OHHH!!!! It is this page!!'
      },
      {
        'icon': FontAwesomeIcons.ban,
        'title': 'Not Nahuel Approved',
        'description':
            'Our code and design decisions were not approved by Nahuel. And we are proud of that. I guess.'
      },
      {
        'icon': FontAwesomeIcons.searchengin,
        'title': 'Traffic Proxy',
        'description': 'Inspect bot traffic on the local environment.'
      },
      {
        'icon': FontAwesomeIcons.rocket,
        'title': 'Continuous Deployment',
        'description': 'Automatic deployments to Azure container app.'
      },
      {
        'icon': FontAwesomeIcons.chartLine,
        'title': 'Grafana Monitoring',
        'description': 'Access comprehensive logs and metrics.'
      },
      {
        'icon': FontAwesomeIcons.bug,
        'title': 'Observability with Sentry',
        'description': 'Detailed tracking of issues and performance.'
      },
      {
        'icon': FontAwesomeIcons.docker,
        'title': 'Docker Compose Setup',
        'description': 'Simplified testing setup using Docker Compose.'
      },
      {
        'icon': FontAwesomeIcons.github,
        'title': 'GitHub Actions Pipeline',
        'description': 'Automated testing to ensure code quality.'
      },
      {
        'icon': FontAwesomeIcons.server,
        'title': 'Cloud Infrastructure',
        'description':
            'Stable production environment with MongoDB Atlas and Azure.'
      },
      {
        'icon': FontAwesomeIcons.vial,
        'title': 'UI E2E Tests',
        'description': 'End-to-end tests with Python and Playwright.'
      },
    ];

    return Card(
      elevation: 8,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
      child: Padding(
        padding: const EdgeInsets.all(24.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            const Text(
              'Features 🦔',
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 16),
            Wrap(
              spacing: 16,
              runSpacing: 16,
              children: features
                  .map((feature) => FeatureItem(
                        icon: feature['icon'] as IconData,
                        title: feature['title'] as String,
                        description: feature['description'] as String,
                      ))
                  .toList(),
            ),
          ],
        ),
      ),
    );
  }
}
