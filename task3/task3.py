import sys
import json


def make_report(dict_tests_: dict, dict_values_: dict) -> dict:
    tests_ = dict_tests_.get("tests")
    values_ = dict_values_.get("values")
    for test in tests_:
        id_ = test.get("id")
        for value in values_:
            if value.get("id") == id_:
                test["value"] = value.get("value")
            if value.get("values"):
                if value.get("id") == id_:
                    test["value"] = value.get("value")

    return tests_


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
    # with open("report.json", "w") as report:
    #     report.write(json.dump(output))
