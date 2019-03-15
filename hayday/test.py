#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from hayday.api import HayDayPlayer


def main():
    with HayDayPlayer() as player:
        print player._driver


if __name__ == '__main__':
    main()
