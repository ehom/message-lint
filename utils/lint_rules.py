import json
import os

path = os.path.dirname(__file__) + "/lint_rules.json"
# print("path:", path)

with open(path) as f:
    rules = json.load(f)
