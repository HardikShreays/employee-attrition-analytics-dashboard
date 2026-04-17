# IBM HR Attrition Analytics — Team Presentation Guide

**Purpose:** This document serves as a structured guide for presenting the IBM HR Employee Attrition Analysis project. Use this as your script, talking points, and reference during the team presentation.

---

## Slide-by-Slide Breakdown

---

### SLIDE 1 — Title Slide

**Title:** IBM HR Employee Attrition — Data Quality Audit & Analytics  
**Subtitle:** Understanding Why Employees Leave and What We Can Do About It  
**Team:** [Your Team Name]  
**Date:** April 2026  
**Course:** Data & Visual Analytics

> **Talking Point:** "Today we'll walk you through our comprehensive analysis of IBM's HR dataset — from raw data quality issues all the way to actionable business recommendations."

---

### SLIDE 2 — Agenda

1. Project Overview & Objectives
2. Dataset Description
3. Data Quality Audit (7 Domains)
4. Exploratory Data Analysis & Key Visualizations
5. Business Insights & Key Findings
6. Strategic Recommendations
7. Q&A

---

### SLIDE 3 — Project Objectives

**What we set out to do:**

- Conduct a **7-domain dataset quality audit** on the raw IBM HR data
- Perform **exploratory data analysis** with 14+ chart types
- Answer **8 critical business questions** about employee attrition
- Deliver **actionable recommendations** to reduce turnover

**Why it matters:**
- Employee attrition costs companies **50-200% of annual salary** per departure
- For this dataset: estimated **$7M - $14M annual cost** from 16% attrition

> **Talking Point:** "Before we could trust any insights, we first had to ensure the data itself was reliable. That's where our 7-domain audit comes in."

---

### SLIDE 4 — Dataset Overview

| Detail | Value |
|--------|-------|
| **Source** | IBM HR Analytics (Kaggle) |
| **Records** | 1,470 employees |
| **Features** | 35 original → 40 after engineering |
| **Target Variable** | Attrition (Yes/No) |
| **Attrition Rate** | 16.1% (237 employees left) |

**Feature Categories:**
- Demographics: Age, Gender, Marital Status, Education
- Job Details: Department, Job Role, Job Level, Business Travel
- Compensation: Monthly Income, Daily Rate, Hourly Rate, Stock Options
- Satisfaction: Job Satisfaction, Environment Satisfaction, Work-Life Balance
- Tenure: Years at Company, Years in Current Role, Years Since Promotion

> **Talking Point:** "This is a cross-sectional dataset — a snapshot in time. We engineered 5 additional features like AgeBand and IncomeBand to enable segmentation analysis."

---

### SLIDE 5 — Data Quality Audit Overview

**We audited the raw data across 7 domains before analysis:**

| Domain | What We Checked | Status |
|--------|----------------|--------|
| Statistical Analysis | Outliers, impossible values, distributions | NEEDS FIX |
| Data Formatting | Data types, mixed formats, encoding | NEEDS FIX |
| Relational Integrity | Cross-column rules, primary key | PASS |
| Deduplication | Exact & near-duplicates | PASS |
| Visual & Trend Analysis | Spikes, drops, anomalies in charts | COMPLETE |
| Completeness & Coverage | Null rates, population coverage | NEEDS FIX |
| Categorical Data Quality | Valid value sets, ordinal ranges | PASS |

**Result: 4/7 PASS | 3/7 NEED FIX**

> **Talking Point:** "Finding 3 domains with issues actually validated our audit process. In a perfect world, all data would be clean — but real-world data rarely is."

---

### SLIDE 6 — Domain 01: Statistical Anomalies Found

**Critical Findings:**

| Issue | Details | Severity |
|-------|---------|----------|
| Impossible ages | Values: 1, 5, 7 (too young), 150, 169, 200 (impossible) | HIGH |
| Corrupted income | String `2543+S427` in MonthlyIncome column | HIGH |
| Sentinel values | 5 records with MonthlyIncome = 999,999 | MEDIUM |

**Show:** Box plots from the notebook (Section 1D)

> **Talking Point:** "An employee aged 200 or one earning $999,999 are clear data entry errors. These 12 records were flagged and handled during cleaning."

---

### SLIDE 7 — Domain 06: Completeness Issues

**Three columns had missing data:**

| Column | Missing Count | Missing % | Impact |
|--------|:---:|:---:|--------|
| YearsAtCompany | 67 | 4.6% | Affects tenure analysis |
| MonthlyIncome | 31 | 2.1% | Affects compensation analysis |
| JobRole | 30 | 2.0% | Affects role-level insights |

**Show:** Missing value heatmap and population rate bar chart from the notebook

> **Talking Point:** "While 4.6% missing in YearsAtCompany isn't catastrophic, it does mean 67 employees have incomplete tenure records. Our cleaning script handles this appropriately."

---

### SLIDE 8 — Overall Attrition Picture

**Show:** Donut chart (Section 5G)

- **83.9%** retained (1,233 employees)
- **16.1%** attrited (237 employees)

**Context:** Industry benchmark is 10-15% (SHRM). This company is above the danger zone.

---

### SLIDE 9 — Top Attrition Drivers

**Show:** Horizontal bar chart of feature correlations (Section 5B)

**Top 5 drivers of attrition:**
1. **Overtime** (+0.246) — THE strongest predictor
2. **Total Working Years** (−0.171) — Experience = retention
3. **Job Level** (−0.169) — Seniority = stability
4. **Monthly Income** (−0.160) — Pay matters
5. **Age** (−0.159) — Older employees stay

> **Talking Point:** "Notice that overtime has the strongest POSITIVE correlation — meaning it INCREASES attrition. Meanwhile, income, experience, and age all DECREASE it. This tells us a clear story: well-compensated, experienced employees don't leave. Overworked, underpaid juniors do."

---

### SLIDE 10 — The Overtime Effect

**Show:** Count plot of Overtime × Attrition (Section 5I, top-left)

| Metric | No Overtime | Works Overtime |
|--------|:---:|:---:|
| Attrition Rate | ~10.4% | ~30.5% |
| Risk Multiplier | 1× | **3×** |

**Show:** Department × Overtime grouped bar chart (Section 5J, right)
- Sales + Overtime → **~38% attrition**
- R&D + Overtime → **~25% attrition**

> **Talking Point:** "If we could do just ONE thing to reduce attrition, it would be reforming our overtime policy. Employees working overtime are 3× more likely to leave."

---

### SLIDE 11 — The Compensation Story

**Show:** Income Band bar chart (Section 5M, left) + Box plot (Section 5H)

| Income Band | Attrition Rate |
|-------------|:---:|
| Low (< $3k) | **~30%** |
| Mid ($3-6k) | ~15-18% |
| High ($6-10k) | ~10-12% |
| Very High ($10k+) | **~5%** |

**Key Stat:** Low earners are **6× more likely** to leave than top earners.

> **Talking Point:** "There's a clear, almost linear relationship between pay and retention. This isn't surprising, but the magnitude is striking — a 6× difference between the lowest and highest income bands."

---

### SLIDE 12 — Role-Level Risk

**Show:** Job Role horizontal bar chart (Section 5C, middle)

**Highest-risk roles:**
| Rank | Job Role | Attrition Rate |
|------|----------|:---:|
| 1 | Sales Representative | **~39.8%** |
| 2 | Laboratory Technician | ~23.8% |
| 3 | Human Resources | ~23.1% |

**Lowest-risk roles:**
| Rank | Job Role | Attrition Rate |
|------|----------|:---:|
| 1 | Research Director | ~2.5% |
| 2 | Manager | ~4.9% |

> **Talking Point:** "Nearly 4 out of 10 Sales Representatives leave. This is a hemorrhaging point for the organization. Meanwhile, senior roles like Manager and Research Director have near-zero attrition."

---

### SLIDE 13 — The Age & Tenure Story

**Show:** Dual-axis line chart (Section 5E) + Line charts (Section 5F)

- **Age 18-25:** ~30%+ attrition (early-career flight risk)
- **Age 46-60:** ~8-10% (most stable)
- **0-2 years tenure:** Highest attrition (new employees)
- **10+ years tenure:** Lowest attrition (committed employees)

> **Talking Point:** "The first 2 years are make-or-break. If an employee stays past year 5, they're likely in it for the long haul. This tells us: invest heavily in onboarding and early-career engagement."

---

### SLIDE 14 — Correlation Heatmap Deep Dive

**Show:** Full correlation heatmap (Section 5A)

**Notable correlations:**
- Age ↔ TotalWorkingYears (0.68) — natural progression
- MonthlyIncome ↔ JobLevel (0.95) — pay tied to level
- YearsAtCompany ↔ YearsInCurrentRole (0.76) — internal mobility
- YearsAtCompany ↔ YearsWithCurrManager (0.77) — manager stability

> **Talking Point:** "This heatmap reveals the internal structure of the data. The near-perfect correlation between income and job level (0.95) tells us the pay bands are well-structured. But it also means if you want to give someone a raise, you might need to promote them."

---

### SLIDE 15 — Job Role × Education Heatmap

**Show:** Pivot heatmap (Section 5N)

**Interesting pockets:**
- Sales Rep + Below College: very high attrition
- Lab Technician + College: elevated attrition
- Research Director + any education: near-zero attrition

> **Talking Point:** "This cross-dimensional view reveals that attrition isn't uniform within a role — education level creates sub-segments with different risk profiles."

---

### SLIDE 16 — The Flight Risk Persona

Based on our analysis, the **highest-risk employee profile** is:

| Attribute | High-Risk Value |
|-----------|----------------|
| Overtime | Yes |
| Monthly Income | < $3,000 |
| Age | 18-25 |
| Marital Status | Single |
| Job Role | Sales Rep or Lab Tech |
| Tenure | 0-2 years |
| Job Satisfaction | Low |

**Estimated attrition probability: 45-55%**

> **Talking Point:** "If this person is on your team right now, there's a coin-flip chance they'll be gone within the year."

---

### SLIDE 17 — Strategic Recommendations

#### Immediate (0-3 months)
1. **Reform overtime policy** — Cap mandatory OT, introduce comp time
2. **Sales Rep retention package** — Increase base salary, restructure commissions
3. **Entry-level salary benchmark** — Ensure <$3k earners match market rates

#### Medium-Term (3-12 months)
4. **Early-career mentorship** — Pair 18-25 year olds with senior mentors
5. **Stay interviews** — Proactive conversations with high-risk profiles
6. **Career path transparency** — Clear promotion timelines for Lab Techs and Sales Reps

#### Long-Term (12+ months)
7. **Predictive attrition model** — ML model using these features for early warning
8. **Culture pulse surveys** — Quarterly engagement tracking linked to attrition KPIs

---

### SLIDE 18 — Financial Impact

| Scenario | Annual Cost of Attrition |
|----------|:---:|
| Current (237 leavers, 50% replacement cost) | **~$7.0M** |
| Current (237 leavers, 100% replacement cost) | **~$14.0M** |
| After recommendations (reduce by 30%) | **~$4.9M - $9.8M** |
| **Annual savings** | **$2.1M - $4.2M** |

> **Talking Point:** "Even at the conservative end, implementing these recommendations could save the company over $2 million annually. The ROI on a mentorship program or salary adjustment is massive compared to the cost of constant rehiring."

---

### SLIDE 19 — Tools & Methodology

| Component | Tool |
|-----------|------|
| Data Cleaning | Python (pandas) |
| Quality Audit | Python (7-domain framework) |
| Visualization | matplotlib, seaborn |
| Dashboard | Tableau |
| Report Generation | Markdown |
| Version Control | Git / GitHub |

**Methodology:**
1. Raw data ingested from Excel (1,470 × 35)
2. 7-domain quality audit performed on raw data
3. Cleaning script applied (drop constants, engineer features)
4. 18+ visualizations generated across all chart types
5. Business insights extracted and validated
6. Recommendations formulated based on data evidence

---

### SLIDE 20 — Q&A

**Possible questions your audience may ask:**

**Q: "How confident are we in these numbers?"**
> A: Very confident for the clean data subset. We flagged 12 records with quality issues out of 1,470 (<1%), and our audit shows 4/7 domains pass cleanly.

**Q: "Why didn't we build a predictive model?"**
> A: That's our recommended next step. This analysis provides the feature understanding needed to build an effective ML model. We know which features matter most.

**Q: "Can we replicate this for other datasets?"**
> A: Absolutely. The 7-domain audit framework is reusable. We've structured the notebook as a template that can be applied to any HR dataset.

**Q: "What about the data quality issues — do they affect our conclusions?"**
> A: The 12 flagged records (6 bad ages, 1 corrupted income, 5 sentinels) represent <1% of the data. After cleaning, our conclusions are robust. The 128 missing values across 3 columns (2-5% each) were handled appropriately.

---

## File References

| File | Location | Description |
|------|----------|-------------|
| Raw Data | `data/HR-Employee-Attrition.xlsx` | Original 1,470 × 35 dataset |
| Clean Data | `data/attrition_clean.csv` | Processed 1,470 × 40 dataset |
| Cleaning Script | `notebooks/clean_attrition.py` | Data cleaning & feature engineering |
| Analysis Notebook | `notebooks/attrition_analysis.ipynb` | Full 7-domain audit + 18 visualizations |
| Business Report | `reports/business_report.md` | Detailed findings & recommendations |
| This Document | `reports/presentation_guide.md` | Team presentation guide |

---

## Presentation Tips

1. **Open the notebook live** during the presentation — running cells in real-time adds credibility
2. **Start with the quality audit** — it shows rigor and professionalism before insights
3. **Highlight the $7-14M cost** early to establish business relevance
4. **Use the flight risk persona** as a storytelling anchor — make it personal
5. **End with recommendations** — always leave the audience with actionable next steps
6. **Keep each slide to 1-2 minutes** — total presentation should be 25-35 minutes

---

*Good luck with the presentation!*
