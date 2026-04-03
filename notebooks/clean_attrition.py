import pandas as pd

df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')

# Check for nulls
print(df.isnull().sum())

# Drop useless columns (constant values, no analytical value)
df.drop(columns=['EmployeeCount', 'StandardHours', 'Over18'], inplace=True)

# Convert Attrition to binary (useful for calculated fields in Tableau)
df['AttritionBinary'] = df['Attrition'].apply(lambda x: 1 if x == 'Yes' else 0)

# Map Education numbers to labels
edu_map = {1:'Below College', 2:'College', 3:'Bachelor', 4:'Master', 5:'Doctor'}
df['EducationLabel'] = df['Education'].map(edu_map)

# Map satisfaction scores to labels
sat_map = {1:'Low', 2:'Medium', 3:'High', 4:'Very High'}
df['JobSatisfactionLabel'] = df['JobSatisfaction'].map(sat_map)
df['EnvironmentSatisfactionLabel'] = df['EnvironmentSatisfaction'].map(sat_map)
df['WorkLifeBalanceLabel'] = df['WorkLifeBalance'].map(sat_map)

# Age buckets
df['AgeBand'] = pd.cut(df['Age'], bins=[18,25,35,45,60], labels=['18-25','26-35','36-45','46-60'])

# Tenure buckets
df['TenureBand'] = pd.cut(df['YearsAtCompany'], bins=[-1,2,5,10,40], labels=['0-2 yrs','3-5 yrs','6-10 yrs','10+ yrs'])

# Income band
df['IncomeBand'] = pd.cut(df['MonthlyIncome'], bins=[0,3000,6000,10000,20000],
                           labels=['Low (<3k)','Mid (3-6k)','High (6-10k)','Very High (10k+)'])

print(df.shape)
df.to_csv('attrition_clean.csv', index=False)
print("Saved: attrition_clean.csv")