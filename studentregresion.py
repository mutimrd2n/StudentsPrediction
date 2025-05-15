import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Dataset
df = pd.read_csv('student-mat.csv', sep=';')
print("Dataset shape:", df.shape)
print(df.head())

# 2. Pisahkan fitur dan target
X = df.drop(columns='G3')  # semua kolom kecuali target
y = df['G3']               # kolom target

# 3. Encoding fitur kategorikal
X_encoded = pd.get_dummies(X, drop_first=True)

# 4. Split data: 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# 5. Model: Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Prediksi dan evaluasi
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"\n✅ RMSE: {rmse:.2f}")

# 7. Visualisasi hasil
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred)
plt.xlabel("Nilai Asli (G3)")
plt.ylabel("Nilai Prediksi")
plt.title("Prediksi vs Nilai Asli - Student Performance")
plt.grid(True)
plt.show()