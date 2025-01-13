# Serviceパッケージ
## 目的
viewで表示するためのデータを取得する機能を提供する

ReadMeでは使用方法を提供する
## spread_sheat.py
#### 参考URL https://qiita.com/venect_qiita/items/4e0f00a70c1b57f948dd

* キーのデータは./sample_sheet.jsonに格納（GCPから取得したサービスアカウントのキーデータ）
* Client.open_by_keyの引数はSpreadSheetのキーを指定
    * https://docs.google.com/spreadsheets/d/14JiPn02nCSXhh7gwJIjUcV-PfMI6Kt6Gw_rA8cKgSds/edit?hl=ja&gid=0#gid=0 の場合は"14JiPn02nCSXhh7gwJIjUcV-PfMI6Kt6Gw_rA8cKgSds"がキー

