// This is a basic Flutter widget test.
//
// To perform an interaction with a widget in your test, use the WidgetTester
// utility in the flutter_test package. For example, you can send tap and scroll
// gestures. You can also use WidgetTester to find child widgets in the widget
// tree, read text, and verify that the values of widget properties are correct.


import 'package:flutter_app_for_testing/screens/bugs_unit_test/test_gesture_detector_semantics.dart';
import 'package:flutter_app_for_testing/screens/bugs_unit_test/test_icon_button_semantics.dart';
import 'package:flutter_app_for_testing/screens/bugs_unit_test/test_ink_well_semantics.dart';
import 'package:flutter_test/flutter_test.dart';



void main() {
  testWidgets('Finds Gesture Detector by semantic', (WidgetTester tester) async {
    await tester.pumpWidget(const TestGestureDetectorSemantics());
    await tester.pumpAndSettle();
    expect(find.bySemanticsLabel("GestureDetector"), findsOneWidget);
  });

  testWidgets('Finds Icon Button by semantic', (WidgetTester tester) async {
    await tester.pumpWidget(const TestIconButtonSemantics());
    await tester.pumpAndSettle();
    expect(find.bySemanticsLabel("IconButton"), findsOneWidget);
  });

  testWidgets('Finds InkWell by semantics', (WidgetTester tester) async {
    await tester.pumpWidget(const TestInkWellSemantics());
    await tester.pumpAndSettle();
    expect(find.bySemanticsLabel("InkWell"), findsOneWidget);
  });

}
