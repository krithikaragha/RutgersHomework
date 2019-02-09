import pandas as pd
import csv

us_state_abbrev = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
    'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
    'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
    'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
    'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
    'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK',
    'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD',
    'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
    'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'}

# Create a path for the file and read it
emp_file = "Resources/employee_data1.csv"
emp_pd = pd.read_csv(emp_file)

# 1 - Split "Name" column into "First Name" and "Last Name"
    # Split "Name" in 2 based on " " as delimiter
    first_last = emp_pd["Name"].str.split(" ", n = 1, expand = True) 
    
    # Make seperate"First Name" column from new data frame 
    emp_pd["First Name"]= first_last[0]
    
    # Make seperate "Last Name" column from new data frame 
    emp_pd["Last Name"]= first_last[1] 

    # Drop the redundant "Name" column
    emp_pd.drop(["Name"], inplace = True, axis=1)  

    # Re-organize the columns
    emp_pd = emp_pd[["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"]]

# 3 - Rewrite SSN Column to have first five numbers hidden from view
emp_pd["SSN"] = emp_pd["SSN"].apply(lambda x: "***-**" + x[6:])

# 4 - Change State Column to have abbreviations using a dictionary with state and abbreviation mappings
emp_pd['State'] = emp_pd['State'].map(us_state_abbrev).fillna(emp_pd['State'])

# Export the converted data to a new CSV file
emp_pd.to_csv(output/employee_data2.csv, sep='\t', encoding='utf-8')

