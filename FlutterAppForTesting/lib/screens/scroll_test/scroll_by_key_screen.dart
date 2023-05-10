import 'package:flutter/material.dart';

class ScrollByKeyScreen extends StatefulWidget {
  static const route = "/ScrollByKeyScreen";
  static const heading = "Scroll By Key Screen";

  const ScrollByKeyScreen({Key? key}) : super(key: key);

  @override
  State<ScrollByKeyScreen> createState() => _ScrollByKeyScreenState();
}

class _ScrollByKeyScreenState extends State<ScrollByKeyScreen> {
  bool vertical = true;
  final ScrollController scrollController = ScrollController();
  late Size size;
  bool showFirst = true;
  bool showMid = false;
  bool showEnd = false;

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
          !showMid &&
          !showEnd) {
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
  void dispose() {
    scrollController.dispose();
    super.dispose();
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
                scrollController.jumpTo(0);
                showFirst = true;
                showMid = false;
                showEnd = false;
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
          controller: scrollController,
          key: const ValueKey("single_child_scroll_view"),
          scrollDirection: vertical ? Axis.vertical : Axis.horizontal,
          child: vertical
              ? Column(
                  crossAxisAlignment: CrossAxisAlignment.stretch,
                  children: [
                    if(showFirst)
                    const Text(
                      "Start",
                      textAlign: TextAlign.center,
                      key: ValueKey("start_key"),
                    ),
                    SizedBox(
                      height: size.height * 2,
                    ),
                    if(showMid)
                    const Text(
                      "Mid",
                      textAlign: TextAlign.center,
                      key: ValueKey("mid_key"),
                    ),
                    SizedBox(
                      height: size.height * 2,
                    ),
                    if(showEnd)
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
                    if(showFirst)
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
                    if(showMid)
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
                    if(showEnd)
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
