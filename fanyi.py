#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    dict
    ~~~~

    Chinese/English Translation

    :date:      09/12/2013
    :author:    Feei <feei@feei.cn>
    :homepage:  https://github.com/wufeifei/dict
    :license:   MIT, see LICENSE for more details.
    :copyright: Copyright (c) 2017 Feei. All rights reserved
"""
import re
import sys
import time
import json
import signal
import threading
import pyperclip
from urllib.request import urlopen
from urllib.parse import quote


class Dict:
    key = '716426270'
    keyFrom = 'wufeifei'
    api = 'http://fanyi.youdao.com/openapi.do' \
          '?keyfrom=wufeifei&key=716426270&type=data&doctype=json&version=1.1&q='
    content = None

    def __init__(self, argv):
        try:
            self.api = self.api + quote(argv)
            self.translate()
        except:
            print("Input invalid！！")


    def translate(self):
        try:
            content = urlopen(self.api).read()
            self.content = json.loads(content.decode('utf-8'))
            self.parse()
        except Exception as e:
            print('ERROR: Network or remote service error!')
            print(e)

    def parse(self):
        code = self.content['errorCode']
        if code == 0:  # Success
            c = None
            try:
                u = self.content['basic']['us-phonetic']  # English
                e = self.content['basic']['uk-phonetic']
            except KeyError:
                try:
                    c = self.content['basic']['phonetic']  # Chinese
                except KeyError:
                    c = 'None'
                u = 'None'
                e = 'None'

            try:
                explains = self.content['basic']['explains']
            except KeyError:
                explains = 'None'

            try:
                phrase = self.content['web']
            except KeyError:
                phrase = 'None'

            print('\033[1;31m################################### \033[0m')
            print('\033[1;31m# \033[0m {0} {1}'.format(
                self.content['query'], self.content['translation'][0]))
            if u != 'None':
                print('\033[1;31m# \033[0m (U: {0} E: {1})'.format(u, e))
            elif c != 'None':
                print('\033[1;31m# \033[0m (Pinyin: {0})'.format(c))
            else:
                print('\033[1;31m# \033[0m')

            print('\033[1;31m# \033[0m')

            if explains != 'None':
                for i in range(0, len(explains)):
                    print('\033[1;31m# \033[0m {0}'.format(explains[i]))
            else:
                print('\033[1;31m# \033[0m Explains None')

            print('\033[1;31m# \033[0m')

            if phrase != 'None':
                for p in phrase:
                    print('\033[1;31m# \033[0m {0} : {1}'.format(
                        p['key'], p['value'][0]))
                    if len(p['value']) > 0:
                        if re.match('[ \u4e00 -\u9fa5]+', p['key']) is None:
                            blank = len(p['key'].encode('gbk'))
                        else:
                            blank = len(p['key'])
                        for i in p['value'][1:]:
                            print('\033[1;31m# \033[0m {0} {1}'.format(
                                ' ' * (blank + 3), i))

            print('\033[1;31m################################### \033[0m')
            # Phrase
            # for i in range(0, len(self.content['web'])):
            #     print self.content['web'][i]['key'], ':'
            #     for j in range(0, len(self.content['web'][i]['value'])):
            #         print self.content['web'][i]['value'][j]
        elif code == 20:  # Text to long
            print('WORD TO LONG')
        elif code == 30:  # Trans error
            print('TRANSLATE ERROR')
        elif code == 40:  # Don't support this language
            print('CAN\'T SUPPORT THIS LANGUAGE')
        elif code == 50:  # Key failed
            print('KEY FAILED')
        elif code == 60:  # Don't have this word
            print('DO\'T HAVE THIS WORD')

class Clipboard (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.raw = "Welcome!!"

    def run(self):
        global exitflag
        while not exitflag:
            time.sleep(0.5)
            new_raw = pyperclip.paste()
            if new_raw != self.raw:
                self.raw = new_raw
                words = self.raw.split(",")
                print()
                for word in words:
                    Dict(word)
                # 这里为什么不显示诶????
                print(">>>", end="", flush=True)


class Outinput (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global exitflag
        while not exitflag:
            raw = input(">>>")
            words = raw.split(",")
            if words == ['exit']:
                exitflag = True
            else:
                for word in words:
                    Dict(word)


def quit():
    print("bye!!")
    sys.exit()

if __name__ == '__main__':
    exitflag = False

    try:
        signal.signal(signal.SIGINT, quit)
        signal.signal(signal.SIGTERM, quit)
        
        thread1 = Clipboard()
        thread2 = Outinput()

        thread1.setDaemon(True)
        thread1.start()

        thread2.setDaemon(True)     
        thread2.start()
        
        thread1.join()
        thread2.join()
        print("bye!!")
    except:
        print()
