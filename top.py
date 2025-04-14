import json
from collections import Counter

# JSONファイルを読み込む（ファイル名を適宜変更）
with open('watch-history.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# タイトルを収集
titles = [item['title'] for item in data if 'title' in item]

# タイトルの出現回数をカウント
title_counts = Counter(titles)

# 上位30個を取得
top_30 = title_counts.most_common(30)

# 結果を表示
print("タイトル重複ランキング（Top 30）:")
for i, (title, count) in enumerate(top_30, 1):
    print(f"{i}. {title} - {count}回")