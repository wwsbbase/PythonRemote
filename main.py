#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ptvsd
ptvsd.settrace(None, ('0.0.0.0', 18110))


from time import sleep
from random import random

import pymysql
conn = pymysql.connect(host='111.231.228.46', user='bopy', passwd='yousendit', db='tempDB')
cur = conn.cursor()


def init():
    """init"""
    cur.execute("use tempDB")

def uninit():
    cur.close()
    conn.close()

def store(temp):
    cur.execute("INSERT INTO tempRecord (temp) VALUES (%s)",(temp))
    conn.commit()

def get_cpu_temp():
    cpu_temp_file = open( "/sys/class/thermal/thermal_zone0/temp" )
    cpu_temp = cpu_temp_file.read()
    cpu_temp_file.close()
    return float(cpu_temp)/1000

def measure_temp():
    """vcgencmd measure_temp"""
    temp = get_cpu_temp()
    # store(get_cpu_temp())
    store(int(temp))
    print(temp)


def main():
    """docstring for main"""
    print("main start")
    # ptvsd.wait_for_attach()
    init()

    for _ in range(0, 50):
        sleep(5)
        # i = random()
        # print(i)
        measure_temp()

    uninit()
    print("main done")
    
if __name__ == '__main__':
    main()
