import 'package:flutter/material.dart';

class TestGestureDetectorSemantics extends StatelessWidget {
  const TestGestureDetectorSemantics({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter App For Testing',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: Semantics(
        label: "GestureDetector",
        child: GestureDetector(
          child: const Text("GestureDetector2"),
        ),
      ),
    );
  }
}

class TestGestureDetectorSemanticsInsteadContainer extends StatelessWidget {
  const TestGestureDetectorSemanticsInsteadContainer({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter App For Testing',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: Semantics(
        label: "GestureDetector",
        child: Container(),
      ),
    );
  }
}
