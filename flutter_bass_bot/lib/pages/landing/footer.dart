import 'package:flutter/material.dart';

class Footer extends StatelessWidget {
  const Footer({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return const Column(
      crossAxisAlignment: CrossAxisAlignment.center,
      children: [
        Text(
          '© 2024 Bass Weather Bot. All rights not reserved.',
          style: TextStyle(color: Colors.black),
        ),
        SizedBox(height: 8),
        Text(
          'Powered by hedgehog magic! 🦔✨',
          style: TextStyle(color: Colors.black),
        ),
      ],
    );
  }
}
