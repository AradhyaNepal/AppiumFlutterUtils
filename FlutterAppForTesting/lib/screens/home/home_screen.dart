import 'package:flutter/material.dart';
import 'package:flutter_app_for_testing/screens/click_test/click_test_screen.dart';
import 'package:flutter_app_for_testing/screens/home/widgets/navigation_widget.dart';

import '../click_test/click_test_screen_bugs.dart';

class HomeScreen extends StatelessWidget {
  static const String route="/";
  static const String heading="HomeScreen";
  const HomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final size=MediaQuery.of(context).size;
    return SafeArea(
      child: SizedBox(
        height: size.height,
        width: size.width,
        child: Scaffold(
          appBar: AppBar(
            title: const Text(
              HomeScreen.heading,
            ),
          ),
          body: SingleChildScrollView(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: const [
                NavigationWidget(
                    heading: ClickTestScreen.heading,
                    route: ClickTestScreen.route,
                ),
                NavigationWidget(
                    heading: ClickTestScreenBugs.heading,
                    route: ClickTestScreenBugs.route,
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
