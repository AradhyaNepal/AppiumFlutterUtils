import 'package:flutter/material.dart';

class ScrollBySemanticScreen extends StatefulWidget {
  static const route = "/ScrollBySemanticScreen";
  static const heading = "Scroll By Semantic Screen";

  const ScrollBySemanticScreen({Key? key}) : super(key: key);

  @override
  State<ScrollBySemanticScreen> createState() => _ScrollBySemanticScreenState();
}

class _ScrollBySemanticScreenState extends State<ScrollBySemanticScreen> {
  bool vertical = true;

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: MediaQuery.of(context).size.height,
      width: MediaQuery.of(context).size.width,
      child: Scaffold(
        appBar: AppBar(
          actions: [
            IconButton(
              key: const ValueKey("axis_swift"),
              onPressed: () {
                vertical = !vertical;
                setState(() {});
              },
              icon: const Icon(
                Icons.swipe,
              ),
            ),
          ],
        ),
        body: Semantics(
          label: "SingleChildScrollView",
          child: SingleChildScrollView(
            scrollDirection: vertical ? Axis.vertical : Axis.horizontal,
            child: vertical
                ? Column(
                    crossAxisAlignment: CrossAxisAlignment.center,
                    children: [
                      const Text(
                        "Start",
                        key: ValueKey("start_key"),
                      ),
                      SizedBox(
                        height: MediaQuery.of(context).size.height * 2,
                      ),
                      const Text(
                        "Mid",
                        key: ValueKey("mid_key"),
                      ),
                      SizedBox(
                        height: MediaQuery.of(context).size.height * 2,
                      ),
                      const Text(
                        "End",
                        key: ValueKey("end_key"),
                      ),
                    ],
                  )
                : Row(
                    crossAxisAlignment: CrossAxisAlignment.center,
                    children: [
                      const Text(
                        "Start",
                        key: ValueKey("start_key"),
                      ),
                      SizedBox(
                        height: MediaQuery.of(context).size.width * 2,
                      ),
                      const Text(
                        "Mid",
                        key: ValueKey("mid_key"),
                      ),
                      SizedBox(
                        height: MediaQuery.of(context).size.width * 2,
                      ),
                      const Text(
                        "End",
                        key: ValueKey("end_key"),
                      ),
                    ],
                  ),
          ),
        ),
      ),
    );
  }
}
