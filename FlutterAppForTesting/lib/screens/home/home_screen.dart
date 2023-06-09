import 'package:flutter/material.dart';
import 'package:flutter_app_for_testing/screens/click_test/click_test_screen.dart';
import 'package:flutter_app_for_testing/screens/enter_text_test/enter_text_test_screen.dart';
import 'package:flutter_app_for_testing/screens/home/widgets/navigation_widget.dart';
import 'package:flutter_app_for_testing/screens/scroll_test/scroll_test_screen.dart';
import 'package:flutter_app_for_testing/screens/wait_test/wait_test_screen.dart';

class HomeScreen extends StatelessWidget {
  static const String route = "/";
  static const String heading = "HomeScreen";

  const HomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final size = MediaQuery.of(context).size;
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
              children:const  [
                NavigationWidget(
                  heading: ClickTestScreen.heading,
                  route: ClickTestScreen.route,
                ),
                NavigationWidget(
                  heading: WaitTestScreen.heading,
                  route: WaitTestScreen.route,
                ),
                NavigationWidget(
                  heading: EnterTextTestScreen.heading,
                  route: EnterTextTestScreen.route,
                ),
                NavigationWidget(
                  heading: ScrollTestScreen.heading,
                  route: ScrollTestScreen.route,
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
