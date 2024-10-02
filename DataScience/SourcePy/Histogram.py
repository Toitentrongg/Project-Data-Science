import pandas as pd
import matplotlib.pyplot as plt

# Đọc tập dữ liệu từ tệp CSV
file_path = 'Data/Dataa.csv'
data = pd.read_csv(file_path)

# Thiết lập các khoảng giá trị cụ thể cho tuổi
bins = [40, 50, 60, 70, 80, 90, 100]

# Vẽ histogram cho cột tuổi (age) với các khoảng giá trị cụ thể
plt.figure(figsize=(8, 6))
plt.hist(data['age'], bins=bins, color='blue', edgecolor='black')
plt.title('Histogram of Age')
plt.xlabel('Age')
plt.xticks(bins)  # Đặt các nhãn cho trục x tại các khoảng giá trị
plt.show()

#Serum creatine
serum_creatinine = data['serum_creatinine']

# Plot the histogram
plt.figure(figsize=(10, 6))
plt.hist(serum_creatinine, bins=[0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5], edgecolor='black')
plt.title('Histogram of Serum Creatine')
plt.xlabel('Serum Creatine')
plt.show()

import scipy.stats as stats

plt.figure(figsize=(10, 6))
stats.probplot(data['serum_creatinine'], dist="norm", plot=plt)
plt.title('Q-Q Plot of Serum Creatinine - Age')
plt.xticks(ticks=[-3, -2, -1, 0, 1, 2, 3], labels=[30, 40, 50, 60, 70, 80, 90])  # Đặt nhãn cho trục x
plt.grid(True)
plt.xlabel("Age")
plt.ylabel("Serum Creatine")
plt.show()
