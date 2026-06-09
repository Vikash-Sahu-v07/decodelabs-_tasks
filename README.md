# 📊 DecodeLabs Business Intelligence & Analytics Portfolio
**Intern:** Vikash Sahu  
**Domain:** Data Analytics  
**Batch:** 2026  
**Status:** All Core Tasks Completed & Quality Audited  

Welcome to my professional data analytics portfolio repository compiled during the DecodeLabs Industrial Training program. This workspace contains a complete pipeline tracing an enterprise transaction dataset through automated cleaning, exploratory statistical profiling, relational SQL querying, and executive data storytelling dashboards.

---

## 📂 Project Repository Directory Blueprint

* **`Project_1_Data_Cleaning/`**: Python pipeline scripts enforcing reproducibility gates, whitespace removal, string casing corrections, and missing value literal configurations.
* **`Project_2_Exploratory_Data_Analysis/`**: Statistical script computing five-number matrices, identifying right-skewed data boundaries, and mapping outlier flags using IQR metrics.
* **`Project_3_SQL_Data_Analysis/`**: Declarative SQL execution queries solving target product performance metrics, tracking average invoice barriers, and uncovering cancellation revenue leaks.
* **`Project_4_Data_Visualization/`**: Python-powered 4-panel dashboard asset highlighting monthly trajectory volumes, category splits, and funnel performance tracking.

---

## 📑 COMPREHENSIVE REPOSITORY PIPELINE CHANGE LOG

### 🛠️ Phase 1: Project 1 — Automated Data Cleaning Ledger
The target raw record set was strictly scrubbed to establish a 100% compliant "Gold Standard" structural foundation.
* **Unique Identifier Error Rate:** 0.00% (All primary key `OrderID` fields verified unique).
* **Date Format Standardization:** 100% Compliance (Scattered temporal entries unified to ISO 8601).
* **Mathematical Formula Sync:** 100% Accuracy (Zero discrepancy deviation between raw totals and multi-attribute products).

| Change ID | Target Attribute | WHAT Was Changed | WHY It Was Changed & Business Impact | Status |
| :--- | :--- | :--- | :--- | :--- |
| **CR-001** | CouponCode | Imputed 309 blank rows with "NO_COUPON" string text. | Avoided listwise row deletion; preserved 100% of data sample volume. | Resolved |
| **CR-002** | Date | Normalized varying date setups into uniform YYYY-MM-DD. | Ensures stable database timelines and crash-free time-series sorting. | Resolved |
| **CR-003** | OrderID | Validated primary key constraints using index logical tests. | Eliminates duplicate sales lines from inflating total performance metrics. | Resolved |
| **CR-004** | Text Attributes | Stripped extra spacing gaps and applied Title Case styling. | Prevents reporting software from splitting identical words during group-bys. | Resolved |
| **CR-005** | Financial Fields | Rounded UnitPrice and TotalPrice strictly to 2 decimals. | Truncates raw Python float storage calculation noise for accounting logic. | Resolved |
| **CR-006** | Data Pipeline Audit | Cross-checked data metrics via manual math calculation checks. | Confirmed absolute revenue record truth; zero records showed variances. | Resolved |

### 📊 Phase 2: Project 2 — Exploratory Data Analysis Discoveries
Core statistical summaries running on the clean matrix data layer:
* **Total Revenue Per Order:** Mean baseline = $1,053.97 | Median midpoint = $823.62
* **Cart Configuration Profile:** Average individual transaction depth = 2.95 items

| Analysis ID | Statistical Phase | Core Discovery Found | Business Meaning & Actionable Direction | Status |
| :--- | :--- | :--- | :--- | :--- |
| **AN-201** | Univariate Check | TotalPrice skewness score calculated at a positive 0.89. | Right-Skewed Distribution. Proves revenue relies on high-end premium products. | Complete |
| **AN-202** | Outlier Tracking | IQR check isolated 8 records breaching the upper $3,330 limit. | True Business Signal. Identifies our highest-value corporate VIP buyers. | Complete |
| **AN-203** | Relationship Analysis | UnitPrice to TotalPrice linear connection shows strong r = 0.72. | Core Revenue Catalyst. High-ticket items directly grow total billings. | Complete |
| **AN-204** | Relationship Analysis | ItemsInCart to Quantity link tracks tightly at r = 0.65. | Cart Density Catalyst. Buyers with full profiles purchase higher item volumes. | Complete |

### 🗄️ Phase 3: Project 3 — Relational SQL Aggregations
Structured business intelligence scripts designed to prevent "Alias Traps" during declarative calculations.

| Query ID | Target Objective | Declarative SELECT Query Block | Logical Execution Plan Summary | Status |
| :--- | :--- | :--- | :--- | :--- |
| **SQL-301** | Total Revenue by Product | `SELECT Product, COUNT(OrderID) AS Orders, SUM(TotalPrice) AS Revenue FROM orders WHERE OrderStatus != 'Cancelled' GROUP BY Product ORDER BY Revenue DESC;` | FROM table -> WHERE filters out cancellations -> GROUP BY product categories -> SELECT computes metrics -> ORDER BY sorts high sales. | Verified |
| **SQL-302** | High-Value Payment Methods | `SELECT PaymentMethod, COUNT(OrderID) AS Counts, AVG(TotalPrice) AS AOV FROM orders GROUP BY PaymentMethod HAVING AVG(TotalPrice) > 1000.00 ORDER BY AOV DESC;` | FROM table -> GROUP BY payment tools -> HAVING drops buckets where average order value stays below $1,000 -> SELECT outputs winners. | Verified |
| **SQL-303** | Lost Revenue Leak Audit | `SELECT ReferralSource, COUNT(OrderID) AS CancelCount, SUM(TotalPrice) AS LostRev FROM orders WHERE OrderStatus = 'Cancelled' GROUP BY ReferralSource ORDER BY LostRev DESC;` | FROM table -> WHERE targets row-level cancelled rows -> GROUP BY marketing source channels -> SELECT tallies financial damage. | Verified |

---

## 🎯 SYSTEMIC EXECUTIVE DIAGNOSIS (THE "SO WHAT?" TEST)

1. **The Core Conversion Challenge:** Our analytical track proves that the platform does not suffer from data recording errors. Instead, it encounters an operational dropout risk. While product configurations display exceptional margins and strong structural linearity ($r = 0.72$), **20.8% of the transaction registry drops out due to cancellations (250 out of 1,200 orders)**.
2. **Strategic Action Plan:** Data tracking shows major checkout friction localized across specific digital referral paths. We must implement automated cart reminders, volume-based checkout modifiers (e.g., dynamic coupon applications), and proactive engagement for client tiers exceeding our upper IQR baseline ($>\$3,330$) to capture this leaking capital.

---

**Analyst Sign-off Certification:** *“I certify that this multi-phase analytics portfolio represents a verified, accurate exploration of our business infrastructure data. The pipeline scripts, relational queries, and dashboard architectures are optimized, fully reproducible, and ready for deployment.”* **Signature:** `Vikash Sahu` (Data Analytics Intern, Batch 2026)
