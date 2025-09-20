# ------------------------------------------------------------
# 0.  Imports
# ------------------------------------------------------------
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display

sns.set_style("whitegrid")          # prettier default plots
plt.rcParams["figure.figsize"] = (8, 5)

# ------------------------------------------------------------
# 1.  Load & Inspect
# ------------------------------------------------------------
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df  = pd.read_csv(url)

print("First 5 rows:")
display(df.head())

print("\nData types + missing-value count:")
display(df.info())

print("\nMissing values per column:")
display(df.isna().sum())

# ------------------------------------------------------------
# 2.  Clean
# ------------------------------------------------------------
# (The Iris set has no missing values, but we show the pattern.)
df_clean = df.dropna()              # or .fillna(method="ffill") etc.
print(f"Rows after cleaning: {len(df_clean)}")

# ------------------------------------------------------------
# 3.  Basic Descriptive Statistics
# ------------------------------------------------------------
print("\nNumerical summary:")
display(df_clean.describe())

print("\nMean petal length per species:")
group_stats = df_clean.groupby("species")["petal_length"].mean()
display(group_stats)

# ------------------------------------------------------------
# 4.  Visualizations
# ------------------------------------------------------------
# 4a. Line chart  (dummy time series created for demo)
# ---------------------------------------------------------
# Fabricate a “year” column so we can show a trend line
df_clean["year"] = 2010 + (df_clean.index % 13)   # cycles 2010-2022
yearly_avg = df_clean.groupby("year")["sepal_length"].mean()

plt.figure()
yearly_avg.plot(marker="o")
plt.title("Average Sepal Length per Year (Iris data – synthetic years)")
plt.xlabel("Year")
plt.ylabel("Mean Sepal Length (cm)")
plt.show()

# 4b. Bar chart – average petal length per species
# ---------------------------------------------------------
plt.figure()
sns.barplot(x=group_stats.index, y=group_stats.values, palette="pastel")
plt.title("Average Petal Length by Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 4c. Histogram – distribution of sepal width
# ---------------------------------------------------------
plt.figure()
sns.histplot(df_clean["sepal_width"], kde=True, color="skyblue", bins=15)
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.show()

# 4d. Scatter plot – sepal length vs. petal length
# ---------------------------------------------------------
plt.figure()
sns.scatterplot(data=df_clean,
                x="sepal_length", y="petal_length",
                hue="species", style="species", palette="deep")
plt.title("Sepal Length vs. Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()