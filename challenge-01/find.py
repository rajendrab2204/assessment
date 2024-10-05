import pandas as pd

# Load the Excel file
excel_file = 'table_data.xlsx'

# Read the employee and device sheets
employees_df = pd.read_excel(excel_file, sheet_name="Employees")  # First sheet for employees
devices_df = pd.read_excel(excel_file, sheet_name="Devices")    # Second sheet for devices

# Get the employee IDs from the devices
device_employee_ids = set(devices_df['employee_id'].dropna().astype(int))

# Find employees without devices
missing_device_employees = employees_df[~employees_df['id'].isin(device_employee_ids)]

# Print the names, IDs, and departments of employees without recorded devices
print("Employees without recorded devices:")
print("ID\tFirst Name\tLast Name\tDepartment")
for index, row in missing_device_employees.iterrows():
    print(f"{row['id']}\t{row['first_name']}\t{row['last_name']}\t{row['department']}")

