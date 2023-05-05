import 'package:flutter/material.dart';

class TestIconButtonSemantics extends StatelessWidget {
  const TestIconButtonSemantics({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter App For Testing',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: Scaffold(
        body: Semantics(
          label: "IconButton",
          child: IconButton(
            onPressed: (){

            },
            icon: const Icon(
              Icons.safety_divider,
            ),
          ),
        ),
      ),
    );
  }
}



class TestIconButtonSemanticsInsteadContainer extends StatelessWidget {
  const TestIconButtonSemanticsInsteadContainer({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter App For Testing',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: Semantics(
        label: "IconButton",
        child: Container(),
      ),
    );
  }
}
