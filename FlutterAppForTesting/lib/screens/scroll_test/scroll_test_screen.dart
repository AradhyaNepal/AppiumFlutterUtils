import 'package:flutter/material.dart';
import 'package:flutter_app_for_testing/screens/scroll_test/scroll_by_key_screen.dart';
import 'package:flutter_app_for_testing/screens/scroll_test/scroll_by_semantic_screen.dart';
import 'package:flutter_app_for_testing/screens/scroll_test/scroll_by_type_screen.dart';
import 'package:flutter_app_for_testing/screens/scroll_test/scroll_material_screen.dart';

import '../home/widgets/navigation_widget.dart';

class ScrollTestScreen extends StatelessWidget {
  static const String route="/ScrollTestScreen";
  static const String heading="Scroll Test Screen";
  const ScrollTestScreen({Key? key}) : super(key: key);

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
              ScrollTestScreen.heading,
            ),
          ),
          body: SingleChildScrollView(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children:const  [
                NavigationWidget(
                  heading: ScrollMaterialScreen.heading,
                  route: ScrollMaterialScreen.route,
                ),
                NavigationWidget(
                  heading: ScrollByTypeScreen.heading,
                  route: ScrollByTypeScreen.route,
                ),
                NavigationWidget(
                  heading: ScrollBySemanticScreen.heading,
                  route: ScrollBySemanticScreen.route,
                ),
                NavigationWidget(
                  heading: ScrollByKeyScreen.heading,
                  route: ScrollByKeyScreen.route,
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
