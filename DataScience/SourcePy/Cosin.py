import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import seaborn as sns
import matplotlib.pyplot as plt

# Đọc dữ liệu từ tập tin CSV
file_path = 'Data/Dataa.csv'
insurance_data = pd.read_csv(file_path)

# Chọn các cột quan trọng
selected_columns = ['age', 'anaemia', 'age_group']
insurance_data = insurance_data[selected_columns]

# Chuyển các biến phân loại thành dạng số
insurance_data['age_group'] = insurance_data['age_group'].astype('category').cat.codes

# Lấy 5 dòng đầu tiên
subset_data = insurance_data.head(5)

# Tính toán ma trận tương quan giữa các dòng, T là đảo chiều cột sang dòng
correlation_matrix = subset_data.T.corr()

# Tính toán ma trận độ đo cosin giữa các dòng
cosine_matrix = cosine_similarity(subset_data)

# Tạo DataFrame từ ma trận độ đo cosin
cosine_df = pd.DataFrame(cosine_matrix, index=subset_data.index, columns=subset_data.index)

# In ra ma trận tương quan và ma trận độ đo cosin
print("Ma trận tương quan:\n", correlation_matrix)
print("\nĐộ đo cosin:\n", cosine_df)
# Vẽ ma trận tương quan
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".6f")
plt.title('Ma trận tương quan')
plt.show()

# Vẽ ma trận độ đo cosin
plt.figure(figsize=(8, 6))
sns.heatmap(cosine_df, annot=True, cmap='coolwarm', fmt=".6f")
plt.title('Ma trận độ đo cosin')
plt.show()
