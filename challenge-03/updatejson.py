import json
import csv
import argparse
import os

def update_json(env, json_file, csv_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    # Read the CSV file and update the JSON data for the specified environment
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['ENV'] == env:
                data[env].update({key: row[key] for key in row if key != 'ENV'})
                break

    # Write the updated JSON data back to the file
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    parser = argparse.ArgumentParser(description='Update JSON configuration based prod/dev environment.')
    parser.add_argument('--env', required=True, help='Environment to update (e.g., DEV, PROD)')
    parser.add_argument('--json', required=True, help='JSON configuration file path')
    parser.add_argument('--csv', required=True, help='CSV input file path')

    args = parser.parse_args()

    update_json(args.env, args.json, args.csv)

if __name__ == '__main__':
    main()

