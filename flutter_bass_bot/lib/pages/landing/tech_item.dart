import 'package:flutter/material.dart';

class TechItem extends StatelessWidget {
  final IconData icon;
  final String name;

  const TechItem({
    Key? key,
    required this.icon,
    required this.name,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Icon(icon, size: 32, color: Colors.blue),
        const SizedBox(height: 8),
        Text(name, style: const TextStyle(fontSize: 14)),
      ],
    );
  }
}
