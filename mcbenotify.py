from notifier import Notifier
from configer import Configer
from logmonitor import LogMonitor
from logprocessor import LogProcessor
import glob
import time
import datetime as dt


def find_latest_log():
    logfiles = glob.glob('*.log')
    assert logfiles, 'ログファイルが見つかりませんでした。'
    return sorted(logfiles)[-1]  # ソートして最も新しいものを選ぶ


def printlog(mes):
    print('['+str(dt.datetime.now())[:-7]+']', mes)


# config
configer = Configer()
UPDATE_INTERVAL = configer.get_int('UpdateInterval')
IGNORE_PLAYERS = configer.get_str_list('IgnorePlayers')
WEBHOOK_URL = configer.get_str('WebhookURL')

# メイン処理に必要なオブジェクト作成
logprocessor = LogProcessor()
LOGFILENAME = find_latest_log()
notifier = Notifier(WEBHOOK_URL)
logmonitor = LogMonitor(LOGFILENAME)

printlog(''+LOGFILENAME+'を監視します。')

while True:
    time.sleep(UPDATE_INTERVAL)
    diff = logmonitor.update()
    text = logprocessor.process(diff)
    bool_sent = notifier.notify(text)
    if bool_sent:
        printlog('Notification sent.')
    printlog('Updated. Time needed: '+str(
        (dt.datetime.now() - logmonitor.last_update).total_seconds()))
