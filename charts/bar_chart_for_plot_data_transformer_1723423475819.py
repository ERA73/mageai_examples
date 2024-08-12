grouped_df = df_1.groupby('companyName')['annualSalaryMax'].mean().reset_index()
x = grouped_df['companyName'].tolist()
y = grouped_df['annualSalaryMax'].tolist()
