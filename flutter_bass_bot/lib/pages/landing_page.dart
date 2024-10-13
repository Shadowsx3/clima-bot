import 'package:flutter/material.dart';
import 'package:flutter_bass_bot/pages/landing/call_to_action.dart';
import 'package:flutter_bass_bot/pages/landing/features_list.dart';
import 'package:flutter_bass_bot/pages/landing/footer.dart';
import 'package:flutter_bass_bot/pages/landing/header.dart';
import 'package:flutter_bass_bot/pages/landing/introduction.dart';
import 'package:flutter_bass_bot/pages/landing/technology_stack.dart';

class LandingPage extends StatelessWidget {
  const LandingPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        decoration: const BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
            colors: [Color.fromARGB(255, 55, 206, 145), Color(0xFFB5FE01)],
          ),
        ),
        child: SingleChildScrollView(
          child: Center(
            child: ConstrainedBox(
              constraints: const BoxConstraints(maxWidth: 800),
              child: const Padding(
                padding: EdgeInsets.all(24.0),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  crossAxisAlignment: CrossAxisAlignment.center,
                  children: [
                    Header(),
                    SizedBox(height: 40),
                    Introduction(),
                    SizedBox(height: 40),
                    FeaturesList(),
                    SizedBox(height: 40),
                    TechnologyStack(),
                    SizedBox(height: 40),
                    CallToAction(),
                    SizedBox(height: 40),
                    Footer(),
                  ],
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}
