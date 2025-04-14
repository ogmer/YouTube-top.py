# YouTube-Top xx

自分のYouTubeの履歴から動画の再生回数のランキングを抽出するプログラムです。

1. [履歴のエクスポート](https://takeout.google.com/settings/takeout)
2. 今回は履歴をjsonで持ってきています。
3. エクスポートを作成し、メールにて届いたらダウンロードします。
4. top.pyを適宜出したいランキング数に変えて(初期ではTop30)、ディレクトリに移動させて``python top.py``で動かします。
