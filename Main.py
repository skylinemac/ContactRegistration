import pandas as pd

df = pd.read_csv('userdata.tsv', sep="\t")

df.columns.values[1] = 'Name'
df.columns.values[2] = 'Email'
df.columns.values[3] = 'Grade'

df_no_duplicates = df.drop_duplicates(subset="Email")

grade_ranking = {
    "8th (incoming freshman for the 2025-2026 school year)" :1,
    "Freshman":2,
    "Sophmore":3,
    "Junior":4,
    "Senior":5
}
df_no_duplicates['Grade_Rank'] = df_no_duplicates['Grade'].map(grade_ranking)

# Sort the data by Grade_Rank (ascending) to prioritize better grades
df_sorted = df_no_duplicates.sort_values(by="Grade_Rank", ascending=True)

#Transfer data to 'result.tsv' with grade labels
with open('result.tsv', 'w') as file:
    for grade, group in df_sorted.groupby('Grade'):
        # Write the header for the grade
        file.write(f"{grade}:\n")
        # Write the entries under this grade
        formatted_entries = group.apply(lambda row: f"{row['Name']} <{row['Email']}>,", axis=1)
        file.write("\n".join(formatted_entries) + "\n\n")  # Add an extra newline for separation


print("Data processing complete.")

