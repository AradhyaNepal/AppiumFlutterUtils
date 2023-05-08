import 'package:flutter/material.dart';

class ScrollByTypeScreen extends StatefulWidget {
  static const route = "/ScrollByTypeScreen";
  static const heading = "Scroll By Type Screen";

  const ScrollByTypeScreen({Key? key}) : super(key: key);

  @override
  State<ScrollByTypeScreen> createState() => _ScrollByTypeScreenState();
}

class _ScrollByTypeScreenState extends State<ScrollByTypeScreen> {
  bool isListView = false;
  bool vertical = true;

  late List<Widget> widgetList = [
    const Text(
      "Start",
      key: ValueKey("start_key"),
    ),
    SizedBox(
      height: (vertical
              ? MediaQuery.of(context).size.height
              : MediaQuery.of(context).size.width) *
          2,
    ),
    const Text(
      "Mid",
      key: ValueKey("mid_key"),
    ),
    SizedBox(
      height: (vertical
              ? MediaQuery.of(context).size.height
              : MediaQuery.of(context).size.width) *
          2,
    ),
    const Text(
      "End",
      key: ValueKey("end_key"),
    ),
  ];

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: MediaQuery.of(context).size.height,
      width: MediaQuery.of(context).size.width,
      child: Scaffold(
        appBar: AppBar(
          actions: [
            IconButton(
              key: const ValueKey("type_swift"),
              onPressed: () {
                isListView = !isListView;
                setState(() {});
              },
              icon: const Icon(
                Icons.published_with_changes_sharp,
              ),
            ),
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
        body: isListView
            ? ListView(
                scrollDirection: vertical ? Axis.vertical : Axis.horizontal,
                children: widgetList,
              )
            : SingleChildScrollView(
                scrollDirection: vertical ? Axis.vertical : Axis.horizontal,
                child: vertical
                    ? Column(
                        crossAxisAlignment: CrossAxisAlignment.center,
                        children: widgetList,
                      )
                    : Row(
                        crossAxisAlignment: CrossAxisAlignment.center,
                        children: widgetList,
                      ),
              ),
      ),
    );
  }
}
