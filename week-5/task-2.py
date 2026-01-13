import json

def calculate_average_grade(students):
    res = []
    for s in students:
        grades = s["grades"]
        avg = sum(grades) / len(grades)
        s["average_grade"] = avg
        res.append(s)
    return res

def main():
    with open("students.json", "r") as f:
        data = json.load(f)
    updated_stats = calculate_average_grade(data)
    with open("updated_students.json", "w") as f:
        json.dump(updated_stats, f, indent=4)
    print("JSON file has been updated")

main()