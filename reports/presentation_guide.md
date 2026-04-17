# IBM HR Attrition Analytics — Team Presentation Guide (10 Slides)

**Duration:** 15-20 minutes | **Audience:** DVA course / team review

---

### SLIDE 1 — Title

**Title:** IBM HR Employee Attrition — Data Quality Audit & Analytics  
**Subtitle:** Understanding Why Employees Leave and What We Can Do About It  
**Team:** [Your Team Name] | April 2026

> **Talking Point:** "We analyzed 1,470 employee records across a 7-domain quality audit and 18+ visualizations to uncover the key drivers behind a 16.1% attrition rate."

---

### SLIDE 2 — Dataset & Objectives

| Detail | Value |
|--------|-------|
| Records | 1,470 employees |
| Features | 35 original → 40 after engineering |
| Attrition Rate | 16.1% (237 employees left) |
| Estimated Cost | $7M – $14M annually |

**Objectives:** 7-domain data quality audit → EDA with 18+ charts → Business insights → Actionable recommendations

> **Talking Point:** "At an average replacement cost of 50-200% of salary, this 16% attrition rate is costing the company up to $14M per year."

---

### SLIDE 3 — Data Quality Audit Scorecard

| Domain | Status |
|--------|--------|
| 01 Statistical Analysis | NEEDS FIX — 6 impossible ages, corrupted income values |
| 02 Data Formatting | NEEDS FIX — MonthlyIncome mixed types (`2543+S427`) |
| 03 Relational Integrity | PASS — All cross-column rules verified |
| 04 Deduplication | PASS — 0 exact duplicates |
| 05 Visual & Trend Analysis | COMPLETE — 18+ charts produced |
| 06 Completeness & Coverage | NEEDS FIX — 128 nulls across 3 columns |
| 07 Categorical Data Quality | PASS — All categories valid |

**Result: 4/7 PASS | 3/7 NEED FIX**

> **Talking Point:** "Before trusting any insight, we validated the raw data. Finding 3 domains with issues proves the audit was necessary — real-world data is never perfect."

---

### SLIDE 4 — Top Attrition Drivers

**Show:** Correlation bar chart (Section 5B of notebook)

| Rank | Factor | Correlation | Effect |
|------|--------|:-----------:|--------|
| 1 | Overtime | +0.246 | Strongest driver — increases attrition |
| 2 | Total Working Years | −0.171 | Experience retains employees |
| 3 | Job Level | −0.169 | Seniority = stability |
| 4 | Monthly Income | −0.160 | Higher pay = lower attrition |
| 5 | Age | −0.159 | Older employees stay longer |

> **Talking Point:** "Overtime is the #1 predictor. Well-paid, experienced employees don't leave. Overworked, underpaid juniors do."

---

### SLIDE 5 — The Overtime & Compensation Effect

**Show:** Overtime count plot + Income band bar chart from notebook

| Overtime | Attrition Rate | | Income Band | Attrition Rate |
|----------|:-:|---|-------------|:-:|
| No | ~10% | | Low (< $3k) | **~30%** |
| Yes | **~30%** | | Very High ($10k+) | **~5%** |

- Overtime employees are **3× more likely** to leave
- Low earners are **6× more likely** to leave than top earners

> **Talking Point:** "These two levers alone — overtime and compensation — account for the majority of the attrition gap."

---

### SLIDE 6 — Department & Role Risk

**Show:** Job Role bar chart + Department bar chart from notebook

**Highest-risk roles:**
- Sales Representative: **~39.8%** attrition (2.5× company average)
- Laboratory Technician: **~23.8%**
- Human Resources: **~23.1%**

**Lowest-risk:** Research Director (~2.5%), Manager (~4.9%)

> **Talking Point:** "Nearly 4 out of 10 Sales Reps leave. This single role is a hemorrhaging point that demands immediate attention."

---

### SLIDE 7 — Age, Tenure & Demographics

**Show:** Age line chart + KDE distribution plots from notebook

| Segment | Attrition Rate |
|---------|:-:|
| Age 18-25 | **~30%+** |
| Age 46-60 | ~8-10% |
| Tenure 0-2 years | Highest |
| Tenure 10+ years | Lowest |
| Single employees | **~25.5%** |
| Married employees | ~12.5% |

> **Talking Point:** "The first 2 years are make-or-break. If we can retain someone past year 5, they're likely in it for the long haul."

---

### SLIDE 8 — Flight Risk Persona

The **highest-risk employee** matches 3+ of these:

| Attribute | High-Risk Value |
|-----------|----------------|
| Overtime | Yes |
| Monthly Income | < $3,000 |
| Age | 18-25, Single |
| Job Role | Sales Rep or Lab Tech |
| Tenure | 0-2 years |

**Estimated attrition probability: 45-55%**

> **Talking Point:** "If this person is on your team right now, there's a coin-flip chance they'll be gone within the year."

---

### SLIDE 9 — Strategic Recommendations

| Timeline | Action | Target | Expected Impact |
|----------|--------|--------|-----------------|
| **0-3 mo** | Reform overtime policy | All OT employees | Reduce OT attrition by 40-50% |
| **0-3 mo** | Sales Rep retention package | Sales Reps | Address 40% attrition |
| **0-3 mo** | Entry-level salary benchmarking | < $3k earners | Cut low-income attrition in half |
| **3-12 mo** | Early-career mentorship program | Age 18-25 | Improve engagement |
| **3-12 mo** | Stay interviews for high-risk profiles | Flight-risk persona | Early intervention |
| **12+ mo** | Build predictive attrition ML model | HR Analytics | Proactive warning system |

**Projected savings: $2.1M – $4.2M annually** (30% attrition reduction)

> **Talking Point:** "Even the conservative estimate saves over $2 million per year. The ROI on a mentorship program is massive compared to constant rehiring."

---

### SLIDE 10 — Summary & Q&A

**Key numbers to remember:**
- **16.1%** attrition rate (above industry benchmark)
- **3×** attrition multiplier for overtime employees
- **6×** gap between lowest and highest income bands
- **~40%** of Sales Representatives leave
- **$7-14M** annual cost; **$2-4M** saveable

**Tools used:** Python (pandas, matplotlib, seaborn), Tableau, Git/GitHub

**Files:** `notebooks/attrition_analysis.ipynb` (full audit + 18 charts) | `reports/business_report.md` (detailed report)

> **Talking Point:** "The data tells a clear story: reform overtime, fix entry-level pay, and invest in early-career engagement. These three actions alone can save the company millions."

---

*Total presentation time: 15-20 minutes (2 min per slide)*
