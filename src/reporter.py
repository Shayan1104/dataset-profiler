import json

def generate_report(missing, duplicates):
    report = {
        "missing_values": missing,
        "duplicate_rows": int(duplicates)
    }

    with open("quality_report.json", "w") as f:
        json.dump(report, f, indent=4)

    print("\n=== DATA QUALITY REPORT ===")
    print(json.dumps(report, indent=4))