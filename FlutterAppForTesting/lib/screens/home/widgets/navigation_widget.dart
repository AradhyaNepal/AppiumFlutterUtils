import 'package:flutter/material.dart';

class NavigationWidget extends StatelessWidget {
  final String heading;
  final String route;

  const NavigationWidget({
    required this.heading,
    required this.route,
    Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Semantics(
      label: route,
      child: ElevatedButton(
        key: ValueKey(route),
          onPressed: (){
            Navigator.pushNamed(context,route);
          },
          child: Text(
            heading,
          ),
      ),
    );
  }
}
