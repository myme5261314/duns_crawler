#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2016 Peng Liu <myme5261314@gmail.com>
#
# Distributed under terms of the gplv3 license.
"""
This file defines crawler for www.endole.co.uk, an uk company information
platform.
"""

import datetime
import requests as rs
from bs4 import BeautifulSoup as bs
import csv
from multiprocessing import Pool
import itertools
from progress.bar import Bar

url_t = "https://www.endole.co.uk/explorer/company/?&fcounty=City+of+London&fstatus=l&fsize=3&fsize=4&femployee=0-50&ftype=2&fdate=%s"
domain = "https://www.endole.co.uk"
csv_path = "endole.csv"


def period_generate(startyear,
                    startmonth,
                    startday,
                    endyear,
                    endmonth,
                    endday,
                    intervalday=15):
    start = datetime.date(startyear, startmonth, startday)
    end = datetime.date(endyear, endmonth, endday)
    interval = datetime.timedelta(intervalday - 1)
    tomorrow = datetime.timedelta(1)
    str_format = "%Y%m%d"
    output_str = "%s-%s"
    while start < end:
        intermediate = start + interval
        yield output_str % (start.strftime(str_format),
                            intermediate.strftime(str_format))
        start = intermediate + tomorrow


def period2date(period_str):
    assert '-' in period_str
    assert len(period_str.split('-')) == 2
    temp = period_str.split('-')
    start_str = temp[0]
    end_str = temp[1]
    start_date = datetime.date(
        int(start_str[:3]), int(start_str[4:5]), int(start_str[6:7]))
    end_date = datetime.date(
        int(end_str[:3]), int(end_str[4:5]), int(end_str[6:7]))
    return (start_date, end_date)


def list_page_extractor(page_content):
    soup = bs(page_content, "html.parser")
    trs = soup.find_all("table", class_="data")[0].find_all("tr")[1:]
    for tr in trs:
        content = tr.find_all("td")[1:]
        company_name = content[0].a.text
        company_detail = domain + content[0].a["href"]
        properties = content[0].find_all("div")
        company_address = properties[0].text
        cash_in_bank = content[1].text[1:].replace(',', '')
        net_worth = content[2].text[1:].replace(',', '')
        yield [company_name, cash_in_bank, net_worth, company_address,
               company_detail]


def list_page_crawl(period_str):
    content = rs.get(url_t % period_str).text
    result = [entry for entry in list_page_extractor(content)]
    if len(result) > 50:
        start_date, end_date = period2date(period_str)
        split_period_list = period_generate(start_date.year, start_date.month,
                                            start_date.day, end_date.year,
                                            end_date.month, end_date.day, 5)
        result = []
        for split_period in split_period_list:
            result += [entry
                       for entry in list_page_extractor(rs.get(
                           url_t % split_period).text)]
    return result


def main():
    period_list = [_ for _ in period_generate(2000, 1, 1, 2016, 1, 1)]
    with open(csv_path, "w") as f:
        csv_writer = csv.writer(f,
                                delimiter='|',
                                quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)
        csv_head = ["name", "cash_in_bank", "net_worth", "company_address",
                    "company_detail"]
        csv_writer.writerow(csv_head)
        bar = Bar('Processing',
                  max=len(period_list),
                  suffix='%(percent).1f%% - %(eta)ds')
        for period_str in period_list:
            result = list_page_crawl(period_str)
            for _ in result:
                csv_writer.writerow(_)
            bar.next()


if __name__ == '__main__':
    main()
