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
  final scrollController = ScrollController();
  bool showFirst = true;
  bool showMid = false;
  bool showEnd = false;

  @override
  void dispose() {
    scrollController.dispose();
    super.dispose();
  }

  late Size size;

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    size = MediaQuery.of(context).size;
  }

  @override
  void initState() {
    super.initState();
    scrollController.addListener(() {
      if (((scrollController.offset > size.width * 2 && !vertical) ||
              (scrollController.offset > size.height * 1 && vertical)) &&
          !showMid && !showEnd) {
        showMid = true;
        showFirst = false;
      } else if (((scrollController.offset > size.width * 5 && !vertical) ||
              (scrollController.offset > size.height * 3 && vertical)) &&
          !showEnd) {
        showEnd = true;
        showMid = false;
      }
      setState(() {});
    });
  }

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: size.height,
      width: size.width,
      child: Scaffold(
        appBar: AppBar(
          actions: [
            IconButton(
              key: const ValueKey("axis_swift"),
              onPressed: () {
                vertical = !vertical;
                scrollController.jumpTo(0);
                showFirst = true;
                showMid = false;
                showEnd = false;
                setState(() {});
              },
              icon: const Icon(
                Icons.swipe,
              ),
            ),
          ],
        ),
        body: SingleChildScrollView(
          controller: scrollController,
          scrollDirection: vertical ? Axis.vertical : Axis.horizontal,
          child: vertical
              ? Column(
                  crossAxisAlignment: CrossAxisAlignment.stretch,
                  children: [
                    if (showFirst)
                      const Text(
                        "Start",
                        textAlign: TextAlign.center,
                        key: ValueKey("start_key"),
                      ),
                    SizedBox(
                      height: size.height * 2,
                    ),
                    if (showMid)
                      const Text(
                        "Mid",
                        textAlign: TextAlign.center,
                        key: ValueKey("mid_key"),
                      ),
                    SizedBox(
                      height: size.height * 2,
                    ),
                    if (showEnd)
                      const Text(
                        "End",
                        textAlign: TextAlign.center,
                        key: ValueKey("end_key"),
                      ),
                  ],
                )
              : Row(
                  crossAxisAlignment: CrossAxisAlignment.stretch,
                  children: [
                    if (showFirst)
                      const Align(
                        alignment: Alignment.center,
                        child: Text(
                          "Start",
                          key: ValueKey("start_key"),
                        ),
                      ),
                    SizedBox(
                      width: size.width * 3,
                    ),
                    if (showMid)
                      const Align(
                        alignment: Alignment.center,
                        child: Text(
                          "Mid",
                          textAlign: TextAlign.center,
                          key: ValueKey("mid_key"),
                        ),
                      ),
                    SizedBox(
                      width: size.width * 3,
                    ),
                    if (showEnd)
                      const Align(
                        alignment: Alignment.center,
                        child: Text(
                          "End",
                          textAlign: TextAlign.center,
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
