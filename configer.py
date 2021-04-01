import configparser
import os

# コンフィグファイルの名前とエンコードを受け取って、要求された値を読み込むクラス
# 設定読み込みエラーを吐く責任を持つ。コンフィグが、設計が意図した記述でない場合にエラーを出すこと。
# 設定読み込みメソッドを  「get_型名」  とすることで、設定から何を受け取るかを分かりやすくする
# デバッグオプションONで読み込むたびに出力？


class Configer():

    # config_file, config
    def __init__(self, filepath='config.ini', section='DEFAULT', Encoding='utf-8', debug=False):
        self.config_file = configparser.ConfigParser()
        assert os.path.isfile(filepath), 'Configer: 存在しないファイルを指定しました'
        self.config_file.read(filepath, encoding=Encoding)
        self.config = self.config_file[section]

    # TODO 意図した記述でない場合のエラー処理
    def get_int(self, name):
        ret = self.config[name]
        return int(ret)

    # TODO 意図した記述でない場合のエラー処理
    def get_str_list(self, name):
        # カンマ区切りを文字列のリストに変換。このままでは空白が残る可能性あり。
        str_list = self.config[name].split(',')
        # 各々の文字列に対し、頭と末尾の不要文字を取り除いたものをretとする
        ret = [s.strip() for s in str_list]
        return ret

    # TODO 意図した記述でない場合のエラー処理
    def get_str(self, name):
        ret = self.config[name]
        return ret
