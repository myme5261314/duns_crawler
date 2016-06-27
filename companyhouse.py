#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2016 Peng Liu <myme5261314@gmail.com>
#
# Distributed under terms of the gplv3 license.
"""
This is a crawler for companieshouse.gov.uk website.
"""

import requests as rs
import os
import csv
from multiprocessing import Pool
import time
from progress.bar import Bar

auth_pass = ("LpffPCgySID2-SNz-tC7p7OwHI-mueKOPsNrBfjS", "")
url_t = "https://api.companieshouse.gov.uk/company/%s"
dir_json = "json/"
bunch_num = 600
bunch_interval = 300  # seconds.


def generate_json_path(company_no):
    return os.path.join(dir_json, company_no + ".json")


def handle_single_company(company_no):
    path = generate_json_path(company_no)
    if os.path.isfile(path) and os.stat(path).st_size > 0:
        return False
    else:
        try:
            content = rs.get(url_t % company_no, auth=auth_pass)
            with open(path, "w") as f:
                f.write(content.text.encode("utf8"))
                return True
        except Exception as e:
            print e
            return False


def extract_company_no_from_url(url):
    return url.split('/')[-2]


def generate_bunch_data(csv_path, bunch_split_num):
    with open(csv_path, "rb") as f:
        entry_reader = csv.reader(f, delimiter="|", quotechar='"')
        result = []
        entry_reader.next()
        for row in entry_reader:
            company_no = extract_company_no_from_url(row[-1])
            result.append(company_no)
            if len(result) == bunch_split_num:
                yield result
                result = []
        if len(result) > 0:
            yield result


def keep_working():
    pool = Pool(5)
    with open("endole.csv", "r") as f:
        lines_num = sum(1 for _ in f)
    bar = Bar("Processing",
              max=lines_num / bunch_num,
              suffix="%(percent).1f%% - %(eta)ds\n")
    for bunch_data in generate_bunch_data("endole.csv", bunch_num):
        start_time = time.time()
        result = pool.map(handle_single_company, bunch_data)
        total_handle = sum(result)
        elapsed_time = time.time() - start_time
        sleep_time = bunch_interval * total_handle / float(bunch_num) * 1.1 - elapsed_time
        if sleep_time > 0:
            print "Elapased for %d seconds, Sleep for %d seconds." % (
                elapsed_time, sleep_time)
            time.sleep(sleep_time)
        bar.next()


def main():
    keep_working()


if __name__ == '__main__':
    main()
