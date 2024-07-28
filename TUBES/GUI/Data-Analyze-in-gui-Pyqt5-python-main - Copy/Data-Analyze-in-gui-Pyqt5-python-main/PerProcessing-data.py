import pandas as pd

file_path = 'c:/Users/niqan/OneDrive/Documents/Semester 4/Proyek 2/Proyek 2/TUBES/GUI/Data-Analyze-in-gui-Pyqt5-python-main/Data-Analyze-in-gui-Pyqt5-python-main/Ayam.csv'

try:
    # Attempt to read the CSV file with latin1 encoding and semicolon delimiter
    df = pd.read_csv(file_path, delimiter=';', encoding='latin1', engine='python', on_bad_lines='skip')
    print("CSV loaded successfully.")
    print(df.head())
except Exception as e:
    print(f"Error loading CSV file: {e}")

# Display the dataframe to check for issues
print(df.head())

# Clean any specific issues you find, for example:
# df['column_name'] = df['column_name'].str.replace('unwanted_string', '')

# Save the cleaned data to a new CSV file
cleaned_file_path = 'c:/Users/niqan/OneDrive/Documents/Semester 4/Proyek 2/Proyek 2/TUBES/GUI/Data-Analyze-in-gui-Pyqt5-python-main/Data-Analyze-in-gui-Pyqt5-python-main/Ayam_cleaned.csv'
df.to_csv(cleaned_file_path, index=False)
