import csv

INPUT_PATH = "input.csv"
OUTPUT_PATH = "output.csv"

def main():
    mapping = {}
    with open(INPUT_PATH, mode="r", newline="", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            work_email = row["work_email"]
            course = f"<{row['CourseID/Link']}|{row['CourseName']}>"

            if work_email in mapping:
                mapping[work_email]["courses"].append(course)
            else:
                pe_onleave = row["pe_name"]
                mapping[work_email] = {
                    "pe_onleave": pe_onleave,
                    "courses": [course],
                }
    with open(OUTPUT_PATH, mode="w", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["email", "courses", "pe_onleave"])
        for email, data in mapping.items():
            writer.writerow([email, ";".join(data["courses"]), data["pe_onleave"]])

if __name__ == '__main__':
    main()