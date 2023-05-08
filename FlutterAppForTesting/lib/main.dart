import 'package:flutter/material.dart';
import 'package:flutter_app_for_testing/screens/click_test/click_test_screen.dart';
import 'package:flutter_app_for_testing/screens/enter_text_test/enter_text_test_screen.dart';
import 'package:flutter_app_for_testing/screens/home/home_screen.dart';
import 'package:flutter_app_for_testing/screens/scroll_test/scroll_by_key_screen.dart';
import 'package:flutter_app_for_testing/screens/scroll_test/scroll_by_semantic_screen.dart';
import 'package:flutter_app_for_testing/screens/scroll_test/scroll_by_type_screen.dart';
import 'package:flutter_app_for_testing/screens/scroll_test/scroll_material_screen.dart';
import 'package:flutter_app_for_testing/screens/scroll_test/scroll_test_screen.dart';
import 'package:flutter_app_for_testing/screens/wait_test/wait_test_screen.dart';
import 'package:flutter_driver/driver_extension.dart';

void main() {
  enableFlutterDriverExtension();
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter App For Testing',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      initialRoute: HomeScreen.route,
      routes: {
        HomeScreen.route: (context) => const HomeScreen(),
        ClickTestScreen.route: (context) => const ClickTestScreen(),
        WaitTestScreen.route: (context) => const WaitTestScreen(),
        EnterTextTestScreen.route: (context) => const EnterTextTestScreen(),
        ScrollTestScreen.route: (context) => const ScrollTestScreen(),
        ScrollMaterialScreen.route: (context) => const ScrollMaterialScreen(),
        ScrollByTypeScreen.route: (context) => const ScrollByTypeScreen(),
        ScrollByKeyScreen.route: (context) => const ScrollByKeyScreen(),
        ScrollBySemanticScreen.route: (context) => const ScrollBySemanticScreen(),
      },
    );
  }
}
