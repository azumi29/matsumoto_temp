import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
 
#CSVファイルをANSI形式で読み込む
data = pd.read_csv('matsumoto_temp.csv',encoding = 'ANSI')
print(data)

# グラフに出力
data.plot()
plt.title('松本市の気温')
plt.xlabel('日付')
plt.ylabel('気温')

# グラフをpngに保存
plt.savefig("matsumoto_temp.png")

plt.show()