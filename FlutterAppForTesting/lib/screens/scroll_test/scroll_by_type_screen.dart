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
    List<Widget> widgetList = [
      if (showFirst || isListView)
        const Align(
          alignment: Alignment.center,
          child: Text(
            "Start",
            key: ValueKey("start_key"),
          ),
        ),
      SizedBox(
        height: (vertical ? size.height : 0) * 2,
        width: (vertical ? 0 : size.width) * 3,
      ),
      if (showMid || isListView)
        const Align(
          alignment: Alignment.center,
          child: Text(
            "Mid",
            key: ValueKey("mid_key"),
          ),
        ),
      SizedBox(
        height: (vertical ? size.height : 0) * 2,
        width: (vertical ? 0 : size.width) * 3,
      ),
      if (showEnd || isListView)
        const Align(
          alignment: Alignment.center,
          child: Text(
            "End",
            key: ValueKey("end_key"),
          ),
        ),
    ];
    return SizedBox(
      height: size.height,
      width: size.width,
      child: Scaffold(
        appBar: AppBar(
          actions: [
            IconButton(
              key: const ValueKey("type_swift"),
              onPressed: () {
                isListView = !isListView;
                _resetValues();
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
                _resetValues();
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
                controller: scrollController,
                scrollDirection: vertical ? Axis.vertical : Axis.horizontal,
                children: widgetList,
              )
            : SingleChildScrollView(
                controller: scrollController,
                scrollDirection: vertical ? Axis.vertical : Axis.horizontal,
                child: vertical
                    ? Column(
                        crossAxisAlignment: CrossAxisAlignment.stretch,
                        children: widgetList,
                      )
                    : Row(
                        crossAxisAlignment: CrossAxisAlignment.stretch,
                        children: widgetList,
                      ),
              ),
      ),
    );
  }

  void _resetValues() {
    scrollController.jumpTo(0);
    showFirst = true;
    showMid = false;
    showEnd = false;
  }
}
