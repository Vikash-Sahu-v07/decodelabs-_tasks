# %% [markdown]
# # Project 2: Exploratory Data Analysis (EDA) Pipeline
# **Framework:** Input -> Process -> Output (IPO Framework)
# **Target File:** Cleaned_Dataset_Data_Analytics.xlsx (Output from Project 1 Verification Gate)

# %%
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. INPUT: Load the clean "Gold Standard" Dataset
filepath = "Cleaned_Dataset_Data_Analytics.xlsx"
df = pd.read_excel(filepath)

print("--- INPUT ARCHITECTURE ---")
print(f"Dataset successfully loaded. Dimensions: {df.shape[0]} rows x {df.shape[1]} columns\n")

# %%
# 2. PROCESS: Descriptive Statistics & Five-Number Summary
print("--- 1. BASIC DESCRIPTIVE STATISTICS ---")
# Focus on primary numerical business variables
numerical_cols = ['Quantity', 'UnitPrice', 'TotalPrice', 'ItemsInCart']
summary_stats = df[numerical_cols].describe()
print(summary_stats.round(2))

# %%
print("\n--- 2. UNIVARIATE ANALYSIS & SKEWNESS ---")
# Calculating skewness coefficients to define the shape of the data
skew_values = df[numerical_cols].skew()
for col, val in skew_values.items():
    if val > 0.5:
        shape = "Right-Skewed (Positive Skew)"
    elif val < -0.5:
        shape = "Left-Skewed (Negative Skew)"
    else:
        shape = "Symmetrical (Normal Distribution)"
    print(f"Variable: {col:<12} | Skewness: {val:>6.2f} | Shape: {shape}")

# %%
print("\n--- 3. OUTLIER INVESTIGATION (IQR METHOD) ---")
# Applying Q1 - 1.5*IQR and Q3 + 1.5*IQR thresholds
q1 = df['TotalPrice'].quantile(0.25)
q3 = df['TotalPrice'].quantile(0.75)
iqr = q3 - q1

lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)

# Isolate outliers flag anomalies
outliers = df[df['TotalPrice'] > upper_bound]

print(f"TotalPrice Five-Number Summary: Min={df['TotalPrice'].min():.2f}, Q1={q1:.2f}, Median={df['TotalPrice'].median():.2f}, Q3={q3:.2f}, Max={df['TotalPrice'].max():.2f}")
print(f"Calculated IQR Range Bounds: Lower Cap = {lower_bound:.2f} | Upper Cap = {upper_bound:.2f}")
print(f"Total Outlier Suspicious Detected: {len(outliers)} rows")

if len(outliers) > 0:
    print("\nSample of Detected Outlier Rows (Potential VIP Activity):")
    print(outliers[['OrderID', 'CustomerID', 'Product', 'Quantity', 'UnitPrice', 'TotalPrice']].head(5))

# %%
print("\n--- 4. RELATIONSHIP MAPPING (PEARSON CORRELATION) ---")
# Running Pearson's 'r' formula matrix
correlation_matrix = df[numerical_cols].corr(method='pearson')
print(correlation_matrix.round(2))

# %%
# 3. OUTPUT: Data Visualizations for Stakeholders
print("\n--- 5. GENERATING VISUAL EVIDENCE ---")
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot A: TotalPrice Distribution Curve
sns.histplot(df['TotalPrice'], kde=True, ax=axes[0], color='#2b6cb0')
axes[0].set_title('Distribution of Total Price (Right Skewed)', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Total Price ($)')
axes[0].set_ylabel('Transaction Count')

# Plot B: Linear Relationship Correlation Heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='Blues', fmt='.2f', ax=axes[1], cbar=True)
axes[1].set_title('Pearson Correlation Heatmap (r)', fontsize=12, fontweight='bold')

plt.tight_layout()
output_image = 'eda_plots.png'
plt.savefig(output_image)
print(f"Visualizations saved successfully as: {os.path.abspath(output_image)}")
print("Pipeline complete. Ready for executive write-up.")
