class WhereToEnter:
    BY_LABEL = 1
    BY_VALUE_KEY = 2
    BY_TYPE = 3
    # If semantics causes some error, in Semantic Widget do :
    # excludeSemantics: true or explicitChildNodes:true depending on scenario,
    # View this issue :https://github.com/flutter/flutter/issues/126059
    BY_SEMANTIC_LABEL = 4  # Default and recommended
    HARD_CODED = 5  # Have no test coverage
