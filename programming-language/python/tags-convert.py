#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import taglib

# {u'ALBUM': [u'\u8bfb\u6545\u4e8b\u8bb0\u5355\u8bcd'],
# u'ARTIST': [u'\u80e1\u654f'],
# u'COMMENT': [u'\u8bfb\u6545\u4e8b\u8bb0\u5355\u8bcd'],
# u'TITLE': [u'\u8bfb\u6545\u4e8b\u8bb0\u5355\u8bcd - 1']}
for mp3_file in os.listdir('.'):
    if not mp3_file.endswith('.mp3'):
        continue

    print "retagging " + mp3_file
    song = taglib.File(mp3_file)
    bn = os.path.basename(mp3_file)
    song.tags[u'TITLE'] = ur"读故事记单词 - " + bn
    song.tags[u'COMMENT'] = ur"读故事记单词"
    song.tags[u'ARTIST'] = ur"胡敏"
    song.tags[u'ALBUM'] = ur"胡敏读故事记单词"
    song.save()
