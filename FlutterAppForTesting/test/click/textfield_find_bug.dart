import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter_app_for_testing/main.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  group("Text Field Find", () {
    testWidgets('Finds TextField By Key', (WidgetTester tester) async {
      await tester.pumpWidget(const MyApp());
      expect(find.bySemanticsLabel("/EnterTextTestScreen"), findsOneWidget);
      await tester.tap(find.bySemanticsLabel("/EnterTextTestScreen"));
      await tester.pumpAndSettle();
      expect(find.byKey(const ValueKey("by-value-key_text_field")),
          findsOneWidget);
    });

    testWidgets('Finds TextField By Semantic', (WidgetTester tester) async {
      await tester.pumpWidget(const MyApp());
      expect(find.bySemanticsLabel("/EnterTextTestScreen"), findsOneWidget);
      await tester.tap(find.bySemanticsLabel("/EnterTextTestScreen"));
      await tester.pumpAndSettle();
      expect(find.bySemanticsLabel("BySemanticTextField"), findsOneWidget);
      expect(find.bySemanticsLabel("BySemanticTextFormField"), findsOneWidget);
    });

    testWidgets('Finds TextField By Semantic', (WidgetTester tester) async {
      await tester.pumpWidget(const MyApp());
      expect(find.bySemanticsLabel("/EnterTextTestScreen"), findsOneWidget);
      await tester.tap(find.bySemanticsLabel("/EnterTextTestScreen"));
      await tester.pumpAndSettle();
      expect(
          find.descendant(
              of: find.bySemanticsLabel("BySemanticTextFormField"),
              matching: find.byType(TextField)),
          findsOneWidget);
      expect(
          find.descendant(
              of: find.bySemanticsLabel("BySemanticTextField"),
              matching: find.byType(TextField)),
          findsOneWidget);
    });
  });
}
