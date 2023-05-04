// This is a basic Flutter widget test.
//
// To perform an interaction with a widget in your test, use the WidgetTester
// utility in the flutter_test package. For example, you can send tap and scroll
// gestures. You can also use WidgetTester to find child widgets in the widget
// tree, read text, and verify that the values of widget properties are correct.

import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import 'package:flutter_app_for_testing/main.dart';

void main() {
  testWidgets('Finds Gesture Detector', (WidgetTester tester) async {
    // Build our app and trigger a frame.
    await tester.pumpWidget(const MyApp());
    expect(find.bySemanticsLabel("/ClickTestScreenBugs"), findsOneWidget);
    await tester.tap(find.bySemanticsLabel("/ClickTestScreenBugs"));
    await tester.pumpAndSettle();
    expect(find.bySemanticsLabel("GestureDetectorTest"), findsOneWidget);
  });

  testWidgets('Finds InkWell', (WidgetTester tester) async {
    // Build our app and trigger a frame.
    await tester.pumpWidget(const MyApp());
    expect(find.bySemanticsLabel("/ClickTestScreenBugs"), findsOneWidget);
    await tester.tap(find.bySemanticsLabel("/ClickTestScreenBugs"));
    await tester.pumpAndSettle();
    expect(find.bySemanticsLabel("InkWellParent"), findsOneWidget);
  });

  testWidgets('Finds IconButtonParent', (WidgetTester tester) async {
    // Build our app and trigger a frame.
    await tester.pumpWidget(const MyApp());
    expect(find.bySemanticsLabel("/ClickTestScreenBugs"), findsOneWidget);
    await tester.tap(find.bySemanticsLabel("/ClickTestScreenBugs"));
    await tester.pumpAndSettle();
    expect(find.bySemanticsLabel("InkWellParent"), findsOneWidget);
  });
}
