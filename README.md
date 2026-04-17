# Employee Attrition Analytics Dashboard

## 📊 Overview

This project analyzes employee attrition using the **IBM HR Analytics dataset** to uncover key factors influencing employee turnover. The ultimate goal is to combine **data preprocessing (Python)** with **interactive visualization (Tableau)** to generate actionable, strategic business insights.

## 🎯 Problem Statement

Employee attrition is a critical challenge for modern organizations. Understanding *why employees leave* helps companies proactively improve retention strategies, reduce training and replacement costs, and optimize workforce planning.

## 💻 Tech Stack

* **Python** (Pandas, NumPy, Matplotlib, Seaborn) for EDA and pre-processing
* **Tableau** for robust, interactive dashboards
* **Data Engineering** for robust data cleaning, formatting, and feature engineering

## ⚙️ Data Preprocessing

The dataset was rigorously cleaned and enhanced using Python scripts to maximize its value. 

### Key Optimization Steps:
* **Data Pruning:** Removed redundant or low-variance columns (`EmployeeCount`, `StandardHours`, `Over18`).
* **Categorical Handling:** Transformed categorical attrition targets into a unified binary format (`AttritionBinary`) for correlation analysis.
* **Label Mapping:** Created intuitive categorical labels for metrics like Education levels, Job satisfaction, and Work-life balance.
* **Feature Engineering:** Developed custom features (e.g., **Age Bands**, **Tenure Bands**, **Income Bands**) to provide nuanced analytical depth to the dashboard.

## 💡 Key Insights

* **Departmental Risk:** The Sales and HR departments show significantly higher proportional attrition.
* **Compensation Gap:** Lower income groups exhibit a demonstrably higher likelihood of leaving the organization.
* **Tenure Vulnerability:** Employees with shorter tenure (0-2 years) are at the highest risk of attrition.
* **Satisfaction Correlation:** Job roles reflecting overall lower job satisfaction score concurrently show a marked increase in churn rates.

## 📂 Project Structure

```text
employee-attrition-analytics/
├── data/                  # Cleaned and raw datasets
├── scripts/               # Python processing and cleaning scripts
├── notebooks/             # Exploratory Data Analysis (EDA) notebooks
├── dashboard/             # Tableau workbook (tableau_dashboard.twbx)
├── reports/               # Automated data profiling reports
├── visuals/               # Generated analytical charts and dashboard previews
└── README.md
```

## 🚀 How to Run

1. **Pre-processing:** Check the `notebooks/` directory for exploratory scripts or run any root-level Python cleaning scripts to re-generate the cleaned datasets.
2. **Launch Dashboard:**
   * Open Tableau Desktop or Tableau Reader.
   * Open `dashboard/tableau_dashboard.twbx`.
3. **Explore:** Utilize the interactive filters (e.g., Department, Gender, Job Role) within the Tableau interface to dynamically slice the data.

---

## 📈 Dashboard and Key Visuals

Below is a curated selection of the most critical visuals generated during this analysis, culminating in the final interactive dashboard.

### 1. Interactive Dashboard Preview
The comprehensive dashboard enables cross-filtering across demographic and professional metrics.
![Dashboard Preview](visuals/dashboard_preview.png)

### 2. Overall Attrition Distribution
A macro-level view of the overarching attrition breakdown within the organization.
![Overall Attrition Donut](visuals/07_overall_attrition_donut.png)

### 3. Feature Correlation Heatmap
Highlights the strongest correlating factors driving employee turnover (e.g., lower job level, shorter tenure, lower income).
![Correlation Heatmap](visuals/01_correlation_heatmap.png)

### 4. Attrition by Department & Job Role
A granular breakdown illuminating exactly which teams and roles are most impacted by churn.
![Attrition by Dept & Role](visuals/03_attrition_by_dept_role_marital.png)

### 5. Attrition by Experience & Tenure
Demonstrates the high attrition risk clustered in the first 2-3 years of employment.
![Attrition by Experience](visuals/06_attrition_by_tenure_experience.png)

---
*Built as a comprehensive portfolio project demonstrating end-to-end data processing, analytical thinking, and dashboard design. If you found this useful, consider starring the repository!*
