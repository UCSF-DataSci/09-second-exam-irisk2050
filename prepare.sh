# Q1



# Q1.1: Run generate_dirty_data.py.

# Q1.2: Clean ms_data_dirty.csv.

# Set working directory.
cd /Users/iriskim/Desktop/09-second-exam-irisk2050
# Remove comment lines.
# Remove empty lines
# Remove extra commas.
# Extract essential columns: patient_id, visit_date, age, education_level, walking_speed.
grep -v '^\s*#' ms_data_dirty.csv | sed '/^$/d' | sed 's/,,*/,/g' | cut -d "," -f1,2,4,5,6 > temp_file
# Walking speed should be between 2.0-8.0 feet/second.
awk -F, '$5 >= 2 && $5 <= 8' temp_file > ms_data.csv

# Q1.3: Create insurance.lst, listing unique labels for a new variable 'insurance_type'. 
echo "Medicare\nMedicaid\nPrivate\nOther" > insurance.lst

# Q1.4: Generate a summary of the process data.

# Count the total number of visits (rows, excluding header)
wc -l ms_data.csv
# Display the first few records.
head ms_data.csv