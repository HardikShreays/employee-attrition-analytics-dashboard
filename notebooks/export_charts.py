"""
export_charts.py
================
Run this script to generate all charts from the attrition analysis
and save them as PNG images inside the ../visuals/ folder.

Usage:
    cd notebooks
    python export_charts.py

    OR from project root:
    venv/bin/python notebooks/export_charts.py
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Non-interactive backend for saving files
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings

warnings.filterwarnings('ignore')

# ============================================================
# CONFIGURATION
# ============================================================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
DATA_PATH = os.path.join(PROJECT_DIR, 'data', 'attrition_clean.csv')
VISUALS_DIR = os.path.join(PROJECT_DIR, 'visuals')

os.makedirs(VISUALS_DIR, exist_ok=True)

# Style
sns.set_theme(style='whitegrid', palette='muted', font_scale=1.1)
plt.rcParams.update({
    'axes.titlesize': 14,
    'axes.titleweight': 'bold',
    'figure.dpi': 150
})

ATTRITION_COLORS = {'Yes': '#e74c3c', 'No': '#2ecc71'}
PALETTE = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6', '#1abc9c']
FAIL_COLOR = '#e74c3c'
PASS_COLOR = '#2ecc71'
WARN_COLOR = '#f39c12'

# ============================================================
# LOAD DATA
# ============================================================
df = pd.read_csv(DATA_PATH)
print(f'Loaded {len(df)} rows from {DATA_PATH}')
print(f'Saving charts to: {VISUALS_DIR}/')
print()

chart_count = 0


def save(fig, name):
    """Save figure and print confirmation."""
    global chart_count
    path = os.path.join(VISUALS_DIR, f'{name}.png')
    fig.savefig(path, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    chart_count += 1
    print(f'  [{chart_count:02d}] Saved: visuals/{name}.png')


# ============================================================
# 1. CORRELATION HEATMAP
# ============================================================
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
numeric_cols = [c for c in numeric_cols if c != 'EmployeeNumber']
corr = df[numeric_cols].corr()

fig, ax = plt.subplots(figsize=(18, 14))
mask = np.triu(np.ones_like(corr, dtype=bool))
sns.heatmap(corr, mask=mask, annot=True, fmt='.2f', cmap='RdBu_r',
            center=0, vmin=-1, vmax=1, linewidths=0.5, square=True,
            cbar_kws={'shrink': 0.8, 'label': 'Correlation Coefficient'},
            annot_kws={'size': 7}, ax=ax)
ax.set_title('Correlation Heatmap — All Numerical Features', pad=20)
plt.tight_layout()
save(fig, '01_correlation_heatmap')

# ============================================================
# 2. TOP CORRELATIONS WITH ATTRITION
# ============================================================
attrition_corr = (corr['AttritionBinary']
                  .drop('AttritionBinary')
                  .sort_values(key=abs, ascending=False))

fig, ax = plt.subplots(figsize=(10, 8))
colors = [FAIL_COLOR if v > 0 else PALETTE[0] for v in attrition_corr.values]
attrition_corr.plot(kind='barh', color=colors, edgecolor='white', ax=ax)
ax.set_title('Feature Correlation with Attrition')
ax.set_xlabel('Correlation Coefficient')
ax.axvline(x=0, color='black', linewidth=0.8)
for i, (val, name) in enumerate(zip(attrition_corr.values, attrition_corr.index)):
    ax.text(val + (0.005 if val > 0 else -0.005), i, f'{val:.3f}',
            va='center', ha='left' if val > 0 else 'right', fontsize=8)
plt.tight_layout()
save(fig, '02_attrition_correlation_ranking')

# ============================================================
# 3. ATTRITION BY DEPARTMENT, JOB ROLE, MARITAL STATUS
# ============================================================
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

dept_attr = df.groupby('Department')['AttritionBinary'].mean().sort_values(ascending=False) * 100
bars = axes[0].bar(dept_attr.index, dept_attr.values, color=PALETTE[:len(dept_attr)],
                    edgecolor='white', width=0.6)
axes[0].set_title('Attrition Rate by Department')
axes[0].set_ylabel('Attrition Rate (%)')
axes[0].set_ylim(0, dept_attr.max() * 1.3)
for bar, val in zip(bars, dept_attr.values):
    axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                 f'{val:.1f}%', ha='center', va='bottom', fontweight='bold')

role_attr = df.groupby('JobRole')['AttritionBinary'].mean().sort_values(ascending=True) * 100
bars = axes[1].barh(role_attr.index, role_attr.values, color=FAIL_COLOR, edgecolor='white')
axes[1].set_title('Attrition Rate by Job Role')
axes[1].set_xlabel('Attrition Rate (%)')
for bar, val in zip(bars, role_attr.values):
    axes[1].text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2,
                 f'{val:.1f}%', ha='left', va='center', fontsize=9)

marital_attr = df.groupby('MaritalStatus')['AttritionBinary'].mean().sort_values(ascending=False) * 100
bars = axes[2].bar(marital_attr.index, marital_attr.values,
                    color=PALETTE[2:2+len(marital_attr)], edgecolor='white', width=0.5)
axes[2].set_title('Attrition Rate by Marital Status')
axes[2].set_ylabel('Attrition Rate (%)')
axes[2].set_ylim(0, marital_attr.max() * 1.3)
for bar, val in zip(bars, marital_attr.values):
    axes[2].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                 f'{val:.1f}%', ha='center', va='bottom', fontweight='bold')

plt.suptitle('Attrition Rate Across Key Categories', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
save(fig, '03_attrition_by_dept_role_marital')

# ============================================================
# 4. ATTRITION BY EDUCATION & BUSINESS TRAVEL
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

edu_order = ['Below College', 'College', 'Bachelor', 'Master', 'Doctor']
edu_attr = df.groupby('EducationLabel')['AttritionBinary'].mean().reindex(edu_order) * 100
bars = axes[0].bar(edu_attr.index, edu_attr.values, color='#9b59b6',
                    edgecolor='white', width=0.6)
axes[0].set_title('Attrition Rate by Education Level')
axes[0].set_ylabel('Attrition Rate (%)')
axes[0].set_ylim(0, edu_attr.max() * 1.3)
axes[0].tick_params(axis='x', rotation=20)
for bar, val in zip(bars, edu_attr.values):
    axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                 f'{val:.1f}%', ha='center', va='bottom', fontweight='bold')

travel_attr = df.groupby('BusinessTravel')['AttritionBinary'].mean().sort_values(ascending=False) * 100
bars = axes[1].bar(travel_attr.index, travel_attr.values, color='#f39c12',
                    edgecolor='white', width=0.5)
axes[1].set_title('Attrition Rate by Business Travel')
axes[1].set_ylabel('Attrition Rate (%)')
axes[1].set_ylim(0, travel_attr.max() * 1.3)
for bar, val in zip(bars, travel_attr.values):
    axes[1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                 f'{val:.1f}%', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
save(fig, '04_attrition_by_education_travel')

# ============================================================
# 5. ATTRITION RATE BY AGE (DUAL-AXIS LINE CHART)
# ============================================================
age_attr = df.groupby('Age')['AttritionBinary'].agg(['mean', 'count'])
age_attr['rate'] = age_attr['mean'] * 100

fig, ax1 = plt.subplots(figsize=(14, 6))
ax1.plot(age_attr.index, age_attr['rate'], color=FAIL_COLOR, linewidth=2.5,
         marker='o', markersize=5, label='Attrition Rate (%)', zorder=3)
ax1.fill_between(age_attr.index, age_attr['rate'], alpha=0.15, color=FAIL_COLOR)
ax1.set_xlabel('Age')
ax1.set_ylabel('Attrition Rate (%)', color=FAIL_COLOR)
ax1.tick_params(axis='y', labelcolor=FAIL_COLOR)

ax2 = ax1.twinx()
ax2.bar(age_attr.index, age_attr['count'], alpha=0.25, color=PALETTE[0],
        label='Employee Count')
ax2.set_ylabel('Employee Count', color=PALETTE[0])
ax2.tick_params(axis='y', labelcolor=PALETTE[0])

ax1.set_title('Attrition Rate & Employee Count by Age')
ax1.set_zorder(ax2.get_zorder() + 1)
ax1.patch.set_visible(False)

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right')

plt.tight_layout()
save(fig, '05_attrition_by_age_line')

# ============================================================
# 6. LINE CHARTS — YEARS AT COMPANY & TOTAL WORKING YEARS
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

for ax, col, color, title in [
    (axes[0], 'YearsAtCompany', PASS_COLOR, 'Years at Company'),
    (axes[1], 'TotalWorkingYears', PALETTE[0], 'Total Working Years')
]:
    grouped = df.groupby(col)['AttritionBinary'].mean() * 100
    ax.plot(grouped.index, grouped.values, color=color, linewidth=2.5,
            marker='o', markersize=4)
    ax.fill_between(grouped.index, grouped.values, alpha=0.15, color=color)
    ax.set_title(f'Attrition Rate by {title}')
    ax.set_xlabel(title)
    ax.set_ylabel('Attrition Rate (%)')

plt.tight_layout()
save(fig, '06_attrition_by_tenure_experience')

# ============================================================
# 7. DONUT CHART — OVERALL ATTRITION
# ============================================================
attrition_counts = df['Attrition'].value_counts()
fig, ax = plt.subplots(figsize=(7, 7))
wedges, texts, autotexts = ax.pie(
    attrition_counts.values,
    labels=attrition_counts.index,
    colors=[ATTRITION_COLORS[k] for k in attrition_counts.index],
    autopct='%1.1f%%', startangle=90,
    explode=(0.05, 0), shadow=True,
    textprops={'fontsize': 13}
)
for at in autotexts:
    at.set_fontweight('bold')

centre_circle = plt.Circle((0, 0), 0.50, fc='white')
ax.add_artist(centre_circle)
ax.text(0, 0, f'{len(df)}\nEmployees', ha='center', va='center',
        fontsize=14, fontweight='bold', color='#2c3e50')
ax.set_title('Overall Attrition Distribution', fontsize=15, fontweight='bold')
plt.tight_layout()
save(fig, '07_overall_attrition_donut')

# ============================================================
# 8. BOX PLOTS — INCOME & DISTANCE BY ATTRITION
# ============================================================
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

sns.boxplot(data=df, x='Attrition', y='MonthlyIncome',
            palette=ATTRITION_COLORS, ax=axes[0], width=0.5, fliersize=3)
axes[0].set_title('Monthly Income by Attrition')
axes[0].set_ylabel('Monthly Income ($)')

sns.boxplot(data=df, x='JobLevel', y='MonthlyIncome', hue='Attrition',
            palette=ATTRITION_COLORS, ax=axes[1], width=0.6, fliersize=3)
axes[1].set_title('Income by Job Level & Attrition')
axes[1].set_ylabel('Monthly Income ($)')
axes[1].legend(title='Attrition')

sns.boxplot(data=df, x='Attrition', y='DistanceFromHome',
            palette=ATTRITION_COLORS, ax=axes[2], width=0.5, fliersize=3)
axes[2].set_title('Distance from Home by Attrition')
axes[2].set_ylabel('Distance from Home')

plt.suptitle('Distribution Comparisons by Attrition Status',
             fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
save(fig, '08_boxplots_income_distance')

# ============================================================
# 9. COUNT PLOTS — OVERTIME, GENDER, SATISFACTION, WORK-LIFE
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
sat_order = ['Low', 'Medium', 'High', 'Very High']

sns.countplot(data=df, x='OverTime', hue='Attrition',
              palette=ATTRITION_COLORS, ax=axes[0, 0], edgecolor='white')
axes[0, 0].set_title('Attrition by Overtime Status')

sns.countplot(data=df, x='Gender', hue='Attrition',
              palette=ATTRITION_COLORS, ax=axes[0, 1], edgecolor='white')
axes[0, 1].set_title('Attrition by Gender')

sns.countplot(data=df, x='JobSatisfactionLabel', hue='Attrition',
              palette=ATTRITION_COLORS, order=sat_order,
              ax=axes[1, 0], edgecolor='white')
axes[1, 0].set_title('Attrition by Job Satisfaction')
axes[1, 0].set_xlabel('Job Satisfaction')

sns.countplot(data=df, x='WorkLifeBalanceLabel', hue='Attrition',
              palette=ATTRITION_COLORS, order=sat_order,
              ax=axes[1, 1], edgecolor='white')
axes[1, 1].set_title('Attrition by Work-Life Balance')
axes[1, 1].set_xlabel('Work-Life Balance')

for ax in axes.flat:
    for container in ax.containers:
        ax.bar_label(container, fontsize=9, padding=2)
    ax.legend(title='Attrition')

plt.suptitle('Employee Counts by Category & Attrition',
             fontsize=16, fontweight='bold', y=1.01)
plt.tight_layout()
save(fig, '09_countplots_overtime_gender_satisfaction')

# ============================================================
# 10. GROUPED BAR — AGE×GENDER, DEPARTMENT×OVERTIME
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(16, 7))

pivot1 = df.pivot_table(values='AttritionBinary', index='AgeBand',
                         columns='Gender', aggfunc='mean') * 100
pivot1.plot(kind='bar', ax=axes[0], color=[PALETTE[0], FAIL_COLOR],
            edgecolor='white', width=0.7)
axes[0].set_title('Attrition Rate by Age Band & Gender')
axes[0].set_ylabel('Attrition Rate (%)')
axes[0].tick_params(axis='x', rotation=0)
axes[0].legend(title='Gender')

pivot2 = df.pivot_table(values='AttritionBinary', index='Department',
                         columns='OverTime', aggfunc='mean') * 100
pivot2.plot(kind='bar', ax=axes[1], color=[PASS_COLOR, WARN_COLOR],
            edgecolor='white', width=0.6)
axes[1].set_title('Attrition Rate by Department & Overtime')
axes[1].set_ylabel('Attrition Rate (%)')
axes[1].tick_params(axis='x', rotation=15)
axes[1].legend(title='OverTime')

for ax in axes:
    for container in ax.containers:
        ax.bar_label(container, fmt='%.1f%%', fontsize=8, padding=2)

plt.tight_layout()
save(fig, '10_grouped_bar_age_gender_dept_overtime')

# ============================================================
# 11. KDE DISTRIBUTION PLOTS
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

continuous_vars = [
    ('MonthlyIncome', 'Monthly Income ($)'),
    ('Age', 'Age'),
    ('TotalWorkingYears', 'Total Working Years'),
    ('YearsAtCompany', 'Years at Company')
]

for ax, (col, label) in zip(axes.flat, continuous_vars):
    for status, color in ATTRITION_COLORS.items():
        subset = df[df['Attrition'] == status][col]
        sns.kdeplot(subset, ax=ax, color=color, fill=True, alpha=0.3,
                    linewidth=2, label=f'Attrition = {status}')
    ax.set_title(f'{label} Distribution by Attrition')
    ax.set_xlabel(label)
    ax.set_ylabel('Density')
    ax.legend()

plt.suptitle('Density Distributions — Attrition vs. Retention',
             fontsize=16, fontweight='bold', y=1.01)
plt.tight_layout()
save(fig, '11_kde_distributions')

# ============================================================
# 12. VIOLIN PLOT — INCOME BY DEPARTMENT & ATTRITION
# ============================================================
fig, ax = plt.subplots(figsize=(14, 7))
sns.violinplot(data=df, x='Department', y='MonthlyIncome', hue='Attrition',
               palette=ATTRITION_COLORS, split=True, inner='quart', ax=ax)
ax.set_title('Monthly Income by Department & Attrition', fontsize=14, fontweight='bold')
ax.set_ylabel('Monthly Income ($)')
ax.legend(title='Attrition')
plt.tight_layout()
save(fig, '12_violin_income_by_department')

# ============================================================
# 13. INCOME BAND & TENURE BAND
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

income_order = ['Low (<3k)', 'Mid (3-6k)', 'High (6-10k)', 'Very High (10k+)']
income_attr = df.groupby('IncomeBand')['AttritionBinary'].mean().reindex(income_order) * 100
bars = axes[0].bar(range(len(income_attr)), income_attr.values,
                    color=[FAIL_COLOR, WARN_COLOR, PASS_COLOR, PALETTE[0]],
                    edgecolor='white', width=0.6)
axes[0].set_xticks(range(len(income_attr)))
axes[0].set_xticklabels(income_attr.index, rotation=15)
axes[0].set_title('Attrition Rate by Income Band')
axes[0].set_ylabel('Attrition Rate (%)')
axes[0].set_ylim(0, income_attr.max() * 1.3)
for bar, val in zip(bars, income_attr.values):
    axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                 f'{val:.1f}%', ha='center', va='bottom', fontweight='bold')

tenure_order = ['0-2 yrs', '3-5 yrs', '6-10 yrs', '10+ yrs']
tenure_attr = df.groupby('TenureBand')['AttritionBinary'].mean().reindex(tenure_order) * 100
bars = axes[1].bar(range(len(tenure_attr)), tenure_attr.values,
                    color=[FAIL_COLOR, WARN_COLOR, PASS_COLOR, PALETTE[0]],
                    edgecolor='white', width=0.6)
axes[1].set_xticks(range(len(tenure_attr)))
axes[1].set_xticklabels(tenure_attr.index)
axes[1].set_title('Attrition Rate by Tenure Band')
axes[1].set_ylabel('Attrition Rate (%)')
axes[1].set_ylim(0, tenure_attr.max() * 1.3)
for bar, val in zip(bars, tenure_attr.values):
    axes[1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                 f'{val:.1f}%', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
save(fig, '13_attrition_by_income_tenure_band')

# ============================================================
# 14. PIVOT HEATMAP — JOB ROLE × EDUCATION
# ============================================================
pivot_heatmap = df.pivot_table(
    values='AttritionBinary', index='JobRole',
    columns='EducationLabel', aggfunc='mean'
) * 100
pivot_heatmap = pivot_heatmap.reindex(columns=edu_order)

fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(pivot_heatmap, annot=True, fmt='.1f', cmap='YlOrRd',
            linewidths=1, linecolor='white',
            cbar_kws={'label': 'Attrition Rate (%)'}, ax=ax)
ax.set_title('Attrition Rate (%) by Job Role & Education Level',
             fontsize=14, fontweight='bold', pad=15)
ax.set_ylabel('Job Role')
ax.set_xlabel('Education Level')
plt.tight_layout()
save(fig, '14_heatmap_jobrole_education')

# ============================================================
# DONE
# ============================================================
print()
print(f'All {chart_count} charts saved to: {VISUALS_DIR}/')
print('Done.')
