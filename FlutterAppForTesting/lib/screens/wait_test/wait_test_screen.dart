import 'package:flutter/material.dart';

class WaitTestScreen extends StatefulWidget {
  static const String route = "/WaitTestScreen";
  static const String heading = "Wait Test Screen";

  const WaitTestScreen({Key? key}) : super(key: key);

  @override
  State<WaitTestScreen> createState() => _WaitTestScreenState();
}

class _WaitTestScreenState extends State<WaitTestScreen> {
  Widget outputBox = const ResetOutputBox();

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
              WaitTestScreen.heading,
            ),
            actions: [
              Semantics(
                label: "Reset",
                child: IconButton(
                  onPressed: () {
                    updateOutput(
                      const ResetOutputBox(),
                    );
                  },
                  icon: const Icon(
                    Icons.lock_reset,
                  ),
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
              outputBox,
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
                        label: "ByValueKey",
                        explicitChildNodes: true,
                        excludeSemantics: true,
                        child: ElevatedButton(
                          onPressed: () {
                            updateOutput(const Text(
                                key: ValueKey("by_value_key"), "By Value Key"));
                          },
                          child: const Text("ByValueKey"),
                        ),
                      ),
                      Semantics(
                        label: "ByType",
                        explicitChildNodes: true,
                        excludeSemantics: true,
                        child: ElevatedButton(
                          onPressed: () {
                            updateOutput(const ByTypeWidget());
                          },
                          child: const Text("ByType"),
                        ),
                      ),
                      Semantics(
                        label: "ByText",
                        explicitChildNodes: true,
                        excludeSemantics: true,
                        child: ElevatedButton(
                          onPressed: () {
                            updateOutput(const Text("ByTextOutput"));
                          },
                          child: const Text("ByText"),
                        ),
                      ),
                      Semantics(
                        label: "BySemanticLabel",
                        explicitChildNodes: true,
                        excludeSemantics: true,
                        child: ElevatedButton(
                          onPressed: () {
                            updateOutput(const Text(
                                "BySemanticOutput",
                                semanticsLabel: "BySemanticLabelOutput",
                            ));
                          },
                          child: const Text("By Semantic Output"),
                        ),
                      ),
                      Semantics(
                        label: "ByHardCoded",
                        explicitChildNodes: true,
                        excludeSemantics: true,
                        child: ElevatedButton(
                          onPressed: () {
                            updateOutput(Column(
                              children: [
                                const ByTypeWidget(),
                                Row(
                                  children: const [
                                    ByTypeWidget(),
                                    Text("ByHardCoded",semanticsLabel: "ByHardCodedOutput",),
                                  ],
                                ),
                              ],
                            ));
                          },
                          child: const Text("By Hard Coded"),
                        ),
                      ),
                      Semantics(
                        label: "TimeOut",
                        explicitChildNodes: true,
                        excludeSemantics: true,
                        child: ElevatedButton(
                          onPressed: () {
                            updateOutput(
                              const Text("TimeOut",semanticsLabel: "TimeOutOutput",),
                              true,
                            );
                          },
                          child: const Text("TimeOut"),
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

  ///So that when long wait reset is called, it long waits too.
  bool wasLongWait = false;

  void updateOutput(Widget value, [bool longWait = false]) async {
    await Future.delayed(
        Duration(milliseconds: wasLongWait || longWait ? 5100 : 500));
    setState(() {
      outputBox = value;
      wasLongWait = longWait;
    });
  }
}

class ResetOutputBox extends StatelessWidget {
  const ResetOutputBox({
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return Semantics(
      label: "ResetOutputBox",
      child: const SizedBox(),
    );
  }
}

class ByTypeWidget extends StatelessWidget {
  const ByTypeWidget({
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return const Text("By Type");
  }
}
