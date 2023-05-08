import 'package:flutter/material.dart';

class ScrollMaterialScreen extends StatefulWidget {
  static const route = "/ScrollMaterialScreen";
  static const heading = "Scroll Material Screen";

  const ScrollMaterialScreen({Key? key}) : super(key: key);

  @override
  State<ScrollMaterialScreen> createState() => _ScrollMaterialScreenState();
}

class _ScrollMaterialScreenState extends State<ScrollMaterialScreen> {
  bool vertical = true;

  @override
  Widget build(BuildContext context) {
    final size=MediaQuery.of(context).size;
    return SizedBox(
      height:size.height,
      width: size.width,
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
        body: SingleChildScrollView(
          scrollDirection: vertical ? Axis.vertical : Axis.horizontal,
          child: vertical
              ? Column(
                  crossAxisAlignment: CrossAxisAlignment.stretch,
                  children: [
                    const Text(
                      "Start",
                      textAlign:TextAlign.center,
                      key: ValueKey("start_key"),
                    ),
                    SizedBox(
                      height: size.height * 2,
                    ),
                    const Text(
                      "Mid",
                      textAlign:TextAlign.center,
                      key: ValueKey("mid_key"),
                    ),
                    SizedBox(
                      height: size.height * 2,
                    ),
                    const Text(
                      "End",
                      textAlign:TextAlign.center,
                      key: ValueKey("end_key"),
                    ),
                  ],
                )
              : Row(
                  crossAxisAlignment: CrossAxisAlignment.stretch,
                  children: [
                    const Align(
                      alignment: Alignment.center,
                      child: Text(
                        "Start",
                        key: ValueKey("start_key"),
                      ),
                    ),
                    SizedBox(
                      width: size.width * 2,
                    ),
                    const Align(
                      alignment: Alignment.center,
                      child: Text(
                        "Mid",
                        textAlign:TextAlign.center,
                        key: ValueKey("mid_key"),
                      ),
                    ),
                    SizedBox(
                      width: size.width * 2,
                    ),
                    const Align(
                      alignment: Alignment.center,
                      child: Text(
                        "End",
                        textAlign:TextAlign.center,
                        key: ValueKey("end_key"),
                      ),
                    ),
                  ],
                ),
        ),
      ),
    );
  }
}
