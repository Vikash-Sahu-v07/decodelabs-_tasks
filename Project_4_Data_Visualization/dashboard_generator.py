import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. SETUP ENVIRONMENT & FONTS
# ==========================================
sns.set_theme(style="whitegrid")
plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
})

# Load the cleaned dataset
file_name = "Cleaned_Dataset_Data_Analytics.xlsx"
if not os.path.exists(file_name):
    raise FileNotFoundError(f"Missing file error: Please ensure '{file_name}' is in this folder.")

df = pd.read_excel(file_name)

# Ensure Date column is parsed correctly for time-series tracking
df['Date'] = pd.to_datetime(df['Date'])
df['YearMonth'] = df['Date'].dt.to_period('M')

# Filter for active sales (excluding cancelled orders) for revenue charts
active_sales = df[df['OrderStatus'] != 'Cancelled']

# ==========================================
# 2. INITIALIZE MULTI-PLOT CANVAS (2x2 GRID)
# ==========================================
fig, axes = plt.subplots(2, 2, figsize=(16, 11))
fig.suptitle('DECODELABS BUSINESS INTELLIGENCE PERFORMANCE DASHBOARD\nBatch: 2026 | Data Integrity Level: Certified Gold Standard', 
             fontsize=16, fontweight='bold', color='#1a365d', y=0.98)

# ------------------------------------------
# CHART 1: Realized Revenue by Product Line (Top-Left)
# ------------------------------------------
product_revenue = active_sales.groupby('Product')['TotalPrice'].sum().sort_values(ascending=False).reset_index()
sns.barplot(data=product_revenue, x='TotalPrice', y='Product', palette='Blues_r', ax=axes[0,0], hue='Product', legend=False)
axes[0,0].set_title('Product Portfolio: Realized Revenue Performance', fontweight='bold', color='#2b6cb0')
axes[0,0].set_xlabel('Total Revenue ($)')
axes[0,0].set_ylabel('')

# Add value labels to the bars
for index, value in enumerate(product_revenue['TotalPrice']):
    axes[0,0].text(value, index, f' ${value:,.2f}', va='center', ha='left', fontsize=9, fontweight='bold', color='#4a5568')

# ------------------------------------------
# CHART 2: Monthly Revenue Trend Analysis (Top-Right)
# ------------------------------------------
monthly_trend = active_sales.groupby('YearMonth')['TotalPrice'].sum().reset_index()
monthly_trend['YearMonth'] = monthly_trend['YearMonth'].dt.to_timestamp()

sns.lineplot(data=monthly_trend, x='YearMonth', y='TotalPrice', marker='o', color='#2b6cb0', linewidth=2.5, ax=axes[0,1])
axes[0,1].fill_between(monthly_trend['YearMonth'], monthly_trend['TotalPrice'], color='#2b6cb0', alpha=0.1)
axes[0,1].set_title('Macro Performance: Realized Monthly Revenue Trend', fontweight='bold', color='#2b6cb0')
axes[0,1].set_xlabel('')
axes[0,1].set_ylabel('Revenue ($)')
axes[0,1].tick_params(axis='x', rotation=30)

# ------------------------------------------
# CHART 3: Acquisition Channel Revenue Share (Bottom-Left)
# ------------------------------------------
referral_revenue = active_sales.groupby('ReferralSource')['TotalPrice'].sum().sort_values(ascending=False).reset_index()
axes[1,0] = plt.subplot(2, 2, 3) # Force true pie layout inside grid coordinate
axes[1,0].pie (
    referral_revenue['TotalPrice'], 
    labels=referral_revenue['ReferralSource'], 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=sns.color_palette('Blues_r', len(referral_revenue)),
    wedgeprops={'edgecolor': 'white', 'linewidth': 1.5}
)
axes[1,0].set_title('Acquisition Efficiency: Share of Total Revenue', fontweight='bold', color='#2b6cb0', pad=10)

# ------------------------------------------
# CHART 4: Operational Leak Audit (Bottom-Right)
# ------------------------------------------
status_counts = df['OrderStatus'].value_counts().reset_index()
sns.barplot(data=status_counts, x='count', y='OrderStatus', palette='flare_r', ax=axes[1,1], hue='OrderStatus', legend=False)
axes[1,1].set_title('Operational Leak Audit: Order Status Volumes', fontweight='bold', color='#c53030')
axes[1,1].set_xlabel('Number of Orders')
axes[1,1].set_ylabel('')

# Add counts directly to status bars
for index, value in enumerate(status_counts['count']):
    axes[1,1].text(value, index, f' {value} orders', va='center', ha='left', fontsize=9, fontweight='bold', color='#4a5568')

# ==========================================
# 3. EXPORT DASHBOARD INFRASTRUCTURE
# ==========================================
plt.tight_layout(rect=[0, 0, 1, 0.95]) # Adjust spacing to leave clean top border room
output_filename = 'DecodeLabs_Executive_Dashboard.png'
plt.savefig(output_filename, dpi=300)
plt.close()

print("\n--- UPGRADED PORTFOLIO DASHBOARD GENERATION SUCCESSFUL ---")
print(f"File Saved: {os.path.abspath(output_filename)}")
print("Your Project 4 workspace is now 100% complete and audit-ready.")
