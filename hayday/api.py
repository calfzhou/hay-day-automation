#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from appium import webdriver


class HayDayPlayer(object):
    def __init__(self):
        self._driver = None

    def __enter__(self):
        server_url = 'http://localhost:4723/wd/hub'
        caps = {
            'platformName': 'Android',
            'platformVersion': '4.3',
            'deviceName': 'Android Emulator',
            'newCommandTimeout': 1200,
            'appPackage': 'com.supercell.hayday',
            'appActivity': '.GameApp',
        }
        self._driver = webdriver.Remote(server_url, caps)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._driver:
            self._driver.quit()
            self._driver = None
