import 'package:flutter/material.dart';

class ClickTestScreenBugs extends StatefulWidget {
  static const String route = "/ClickTestScreenBugs";
  static const String heading = "Click Test Screen Bugs";

  const ClickTestScreenBugs({Key? key}) : super(key: key);

  @override
  State<ClickTestScreenBugs> createState() => _ClickTestScreenBugsState();
}

class _ClickTestScreenBugsState extends State<ClickTestScreenBugs> {
  String outputBox = "";

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
              ClickTestScreenBugs.heading,
            ),
            actions: [
              IconButton(
                key: const ValueKey("reset"),
                onPressed: () {
                  setState(() {
                    outputBox = "";
                  });
                },
                icon: const Icon(
                  Icons.lock_reset,
                ),
              )
            ],
          ),
          body: Column(
            children: [
              const SizedBox(
                height: 10,
              ),
              const Text(
                "Output Box",
                style: TextStyle(
                  fontWeight: FontWeight.bold,
                  decoration: TextDecoration.underline,
                  fontSize: 17,
                ),
              ),
              const SizedBox(
                height: 10,
              ),
              Text(
                outputBox.isEmpty ? "No Output" : "Output is $outputBox",
                key: const ValueKey("output-box"),
                semanticsLabel: "OutputBox",
              ),
              const SizedBox(
                height: 10,
              ),
              const Divider(
                color: Colors.red,
              ),
              Expanded(
                child: SingleChildScrollView(
                  child: Column(
                    children: [
                      Semantics(
                        label: "GestureDetectorTest",
                        child: GestureDetector(
                          excludeFromSemantics:true,
                          onTap: () {
                            updateOutput("GestureDetectorClick");
                          },
                          onDoubleTap: () {
                            updateOutput("GestureDetectorDoubleClick");
                          },
                          onLongPress: () {
                            updateOutput("GestureDetectorLongClick");
                          },
                          child: Semantics(
                            label: "GestureDetectorChild",
                            child: const Text("GestureDetector2"),
                          ),
                        ),
                      ),
                      const SizedBox(
                        height: 40,
                      ),
                      Semantics(
                        label: "InkWellParent",
                        child: InkWell(
                          key: const ValueKey("ink-well"),
                          onTap: () {
                            updateOutput("InkWellClick");
                          },
                          onDoubleTap: () {
                            updateOutput("InkWellDoubleClick");
                          },
                          onLongPress: () {
                            updateOutput("InkWellLongClick");
                          },
                          child: Semantics(
                            label: "InkWellChild",
                            child: const Text("InkWell"),
                          ),
                        ),
                      ),
                      const SizedBox(
                        height: 40,
                      ),
                      Semantics(
                        label: "IconButtonParent",
                        child: IconButton(
                          key: const ValueKey("icon-button"),
                          onPressed: () {
                            updateOutput("IconButton");
                          },
                          icon: const Icon(
                            Icons.ads_click,
                            semanticLabel: "IconButtonChild",
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  void updateOutput(String value) {
    setState(() {
      outputBox = value;
    });
  }
}
