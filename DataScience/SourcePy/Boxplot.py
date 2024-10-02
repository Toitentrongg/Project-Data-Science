import pandas as pd
import matplotlib.pyplot as plt

# Đọc tập dữ liệu từ tệp CSV
file_path = 'Data/Dataa.csv'
data = pd.read_csv(file_path)

# Lọc tập dữ liệu, chỉ chọn các cột liên quan
cleaned_data = data[['age', 'ejection_fraction', 'platelets']]

# Vẽ các biểu đồ boxplot
plt.figure(figsize=(12, 6))  # Thiết lập kích thước của toàn bộ hình vẽ

# Boxplot cho cột tuổi (age)
plt.subplot(1, 3, 1)  # Thiết lập vị trí biểu đồ đầu tiên (1 hàng, 3 cột, vị trí 1)
plt.boxplot(cleaned_data['age'])  # Vẽ boxplot cho cột tuổi
plt.title('Age')  # Đặt tiêu đề cho biểu đồ
plt.ylabel('Value')  # Đặt nhãn cho trục y

# Boxplot cho cột ejection_fraction
plt.subplot(1, 3, 2)  # Thiết lập vị trí biểu đồ thứ hai (1 hàng, 3 cột, vị trí 2)
plt.boxplot(cleaned_data['ejection_fraction'])  # Vẽ boxplot cho cột ejection_fraction
plt.title('Ejection Fraction')  # Đặt tiêu đề cho biểu đồ
plt.ylabel('Value')  # Đặt nhãn cho trục y

# Boxplot cho cột platelets
plt.subplot(1, 3, 3)  # Thiết lập vị trí biểu đồ thứ ba (1 hàng, 3 cột, vị trí 3)
plt.boxplot(cleaned_data['platelets'])  # Vẽ boxplot cho cột platelets
plt.title('Platelets')  # Đặt tiêu đề cho biểu đồ
plt.ylabel('Value')  # Đặt nhãn cho trục y

plt.tight_layout()  # Điều chỉnh bố cục cho các biểu đồ không bị chồng chéo
plt.show()  # Hiển thị các biểu đồ
