import sys
import json


def make_pairs(vals):
    return {v.get("id"): v.get("value") for v in vals}


def set_up_value(tes, pairs_):
    for t in tes:
        t["value"] = pairs_.get(t.get("id"))
        if t.get("values"):
            t = set_up_value(t.get("values"), pairs_)
    return tes


def make_report(dict_tests_, dict_values_):
    tests_ = dict_tests_.get("tests")
    values_ = dict_values_.get("values")
    pairs = make_pairs(values_)
    return set_up_value(tests_, pairs)


if __name__ == "__main__":
    tests = sys.argv[1]
    values = sys.argv[2]
    with open(tests, "r") as f:
        content_tests = f.read()
    with open(values, "r") as f:
        content_values = f.read()
    dict_tests = json.loads(content_tests)
    dict_values = json.loads(content_values)
    output = make_report(dict_tests, dict_values)
    print(output)
    with open("report.json", "w") as report:
        report.write(json.dumps(output, indent=4))
