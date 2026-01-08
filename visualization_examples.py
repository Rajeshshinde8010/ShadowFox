# Beginner Task - Visualization Examples
# Internship: ShadowFox Data Science
# Libraries Used: Matplotlib & Seaborn

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# ---------------- Sample Data ----------------
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

# ---------------- Line Plot (Matplotlib) ----------------
plt.figure()
plt.plot(x, y)
plt.title("Line Plot Example")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()

# ---------------- Bar Chart (Matplotlib) ----------------
categories = ['A', 'B', 'C']
values = [5, 7, 3]

plt.figure()
plt.bar(categories, values)
plt.title("Bar Chart Example")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# ---------------- DataFrame for Seaborn ----------------
df = pd.DataFrame({
    'x': x,
    'y': y
})

# ---------------- Scatter Plot (Seaborn) ----------------
plt.figure()
sns.scatterplot(x='x', y='y', data=df)
plt.title("Scatter Plot Example")
plt.show()

# ---------------- Histogram (Seaborn) ----------------
plt.figure()
sns.histplot(df['y'], kde=True)
plt.title("Histogram Example")
plt.show()
