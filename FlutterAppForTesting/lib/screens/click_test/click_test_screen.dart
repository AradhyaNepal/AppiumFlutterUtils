import 'package:flutter/material.dart';

class ClickTestScreen extends StatefulWidget {
  static const String route = "/ClickTestScreen";
  static const String heading = "Click Test Screen";

  const ClickTestScreen({Key? key}) : super(key: key);

  @override
  State<ClickTestScreen> createState() => _ClickTestScreenState();
}

class _ClickTestScreenState extends State<ClickTestScreen> {
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
              ClickTestScreen.heading,
            ),
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
                outputBox,
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
                        label: "ElevatedButtonParent",
                        child: ElevatedButton(
                          key: const ValueKey("elevated-button"),
                          onPressed: () {
                            updateOutput("ElevatedButton");
                          },
                          child: Semantics(
                            label: "ElevatedButtonChild",
                            child: const Text("ElevatedButton"),
                          ),
                        ),
                      ),
                      const SizedBox(
                        height: 20,
                      ),
                      Semantics(
                        label: "GestureDetectorParent",
                        child: GestureDetector(
                          key: const ValueKey("gesture-detector"),
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
                            label: "GestureDetectorDown",
                            child: const Text("GestureDetector"),
                          ),
                        ),
                      ),
                      const SizedBox(
                        height: 20,
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
                        height: 10,
                      ),
                      Semantics(
                        label: "TextButtonParent",
                        child: TextButton(
                          key: const ValueKey("text-button"),
                          onPressed: () {
                            updateOutput("TextButtonClick");
                          },
                          onLongPress: () {
                            updateOutput("TextButtonLongClick");
                          },
                          child: Semantics(
                            label: "TextButtonChild",
                            child: const Text("TextButton"),
                          ),
                        ),
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
          floatingActionButton: Semantics(
            label: "FloatingActionButtonParent",
            child: FloatingActionButton(
              key: const ValueKey("floating-action-button"),
              onPressed: () {
                updateOutput("FloatingActionButton");
              },
              child: Semantics(
                label: "FloatingActionButtonChild",
                child: const Icon(
                  Icons.touch_app,
                ),
              ),
            ),
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
