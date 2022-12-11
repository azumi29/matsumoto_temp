import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
 
#CSVファイルをANSI形式で読み込む
data = pd.read_csv('matsumoto_temp.csv',encoding = 'ANSI')
print(data)

# グラフに出力
df_matsumoto_temp = data.iloc[:, [0,1]]
df_matsumoto_temp.plot()
plt.title('2021年1月 松本市の気温')
plt.xlabel('日付')
plt.ylabel('気温')
plt.show()

# グラフをpngに保存
plt.savefig("matsumoto_temp.png")
