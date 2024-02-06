# Compliance Messaging CSV Script
This is a simple script to parse data from LearnUpon report CSV's to a CSV that can be used to message users. Changes include grouping courses for users and noting if their manager is on leave.

# Getting Started

```sh
mkdir compliance_script && cd compliance_script
git clone https://github.com/eddique/compliance_script.git .
python3 -m venv env
source env/bin/activate
```

# Usage
Download a CSV of the LearnUpon report, add to the root directory of the script, and rename it "input.csv".

Run the following command to parse the CSV and create "output.csv" which we will then add to an Okta Workflow table for messaging.
```sh
python3 script.py
```