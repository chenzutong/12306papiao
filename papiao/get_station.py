import requests
import re
import os


def getStation():
    url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9141"
    response = requests.get(url, verify=True)
    station = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
    station = dict(station)
    station = str(station)
    write(station)


def write(station):
    file = open('station.text', 'w', encoding='utf-8_sig')
    file.write(station)
    file.close()


def read():
    file = open('station.text', 'r', encoding='utf-8_sig')
    data = file.readline()
    file.close()
    return data


def isStation():
    isStation = os.path.exists('station.text')
    return isStation
