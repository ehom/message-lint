import re
from .lint_rules import rules


def lint(text) -> list:
    result = []
    for entry in rules:
        pattern = '|'.join(entry['regexp'])
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            result.append(entry)
    return result
