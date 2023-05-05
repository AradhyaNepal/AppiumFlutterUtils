import 'package:flutter/material.dart';

class TestInkWellSemantics extends StatelessWidget {
  const TestInkWellSemantics({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter App For Testing',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: Scaffold(
        body: Semantics(
          label: "InkWell",
          // explicitChildNodes: true,
          // container: true,
          excludeSemantics: true,
          child: const InkWell(
            child: Text("InkWell"),
          ),
        ),
      ),
    );
  }
}

class TestInkWellSemanticsInsteadContainer extends StatelessWidget {
  const TestInkWellSemanticsInsteadContainer({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter App For Testing',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: Semantics(
        label: "InkWell",
        child: Container(),
      ),
    );
  }
}
