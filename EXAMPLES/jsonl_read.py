import json

with open('people.jsonl') as people_in:
    for line in people_in:
        data = json.loads(line)
        print(data)