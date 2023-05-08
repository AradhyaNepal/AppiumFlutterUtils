import 'package:flutter/material.dart';

class EnterTextTestScreen extends StatefulWidget {
  static const String route = "/EnterTextTestScreen";
  static const String heading = "Enter Text Test Screen";

  const EnterTextTestScreen({Key? key}) : super(key: key);

  @override
  State<EnterTextTestScreen> createState() => _EnterTextTestScreenState();
}

class _EnterTextTestScreenState extends State<EnterTextTestScreen> {
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
              EnterTextTestScreen.heading,
            ),
            actions: [
              IconButton(
                key: const ValueKey("reset"),
                onPressed: () {
                  setState(() {
                    outputBox = "";
                  });
                },
                icon: const Icon(
                  Icons.lock_reset,
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
              Text(
                outputBox.isEmpty ? "No Output" : "Output is $outputBox",
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
                      TextFieldTestWidget(
                        updateOutput: updateOutput,
                      ),
                      TextFormFieldTestWidget(
                        updateOutput: updateOutput,
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

  void updateOutput(String value) {
    setState(() {
      outputBox = value;
    });
  }
}

class TextFieldTestWidget extends StatelessWidget {
  final Function(String) updateOutput;

  const TextFieldTestWidget({required this.updateOutput, Key? key})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        TextField(
          onChanged: (e) => updateOutput(e),
          decoration: const InputDecoration(
            label: Text(
              "ByLabelTextField",
            ),
          ),
        ),
        TextField(
          onChanged: (e) => updateOutput(e),
          key: const ValueKey("by-value-key_text_field"),
        ),
        ByTypeTextField(
          onChanged: updateOutput,
        ),
        Semantics(
          label: "BySemanticTextField",
          child: TextField(
            onChanged: (e) => updateOutput(e),
          ),
        ),
      ],
    );
  }
}

class ByTypeTextField extends StatelessWidget {
  final Function(String) onChanged;

  const ByTypeTextField({
    required this.onChanged,
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      child: TextField(
        onChanged: onChanged,
      ),
    );
  }
}

class TextFormFieldTestWidget extends StatelessWidget {
  final Function(String) updateOutput;

  const TextFormFieldTestWidget({required this.updateOutput, Key? key})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        TextFormField(
          onChanged: (e) => updateOutput(e),
          decoration: const InputDecoration(
            label: Text(
              "ByLabelTextFormField",
            ),
          ),
        ),
        TextFormField(
          onChanged: (e) => updateOutput(e),
          key: const ValueKey("by-value-key_text_form_field"),
        ),
        ByTypeTextFormField(
          onChanged: updateOutput,
        ),
        Semantics(
          label: "BySemanticTextFormField",
          child: TextFormField(
            onChanged: (e) => updateOutput(e),
          ),
        ),
      ],
    );
  }
}

class ByTypeTextFormField extends StatelessWidget {
  final Function(String) onChanged;

  const ByTypeTextFormField({
    required this.onChanged,
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.only(
        left: MediaQuery.of(context).size.width/2,
      ),
      child: TextFormField(
        onChanged: onChanged,
      ),
    );
  }
}
