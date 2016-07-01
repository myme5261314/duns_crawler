#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2016 Peng Liu <myme5261314@gmail.com>
#
# Distributed under terms of the gplv3 license.
"""
This file defines functions to help get duns number for each endole entry.
"""

import csv
import re
import os
import time
import string
import json
from multiprocessing import Pool
from progress.bar import Bar

import duns_utils

duns_dir = "duns"
batch_num = 150
batch_interval = 300


def generate_duns_path(company_no):
    return os.path.join(duns_dir, company_no + ".json")


def handle_single_entry(entry):
    """
    return 0 for processed entry, others for processing result. -1 for no valid
    result after filter, -2 for more than one result after filter, -3 for
    retrieve error.

    """
    company_no = entry[-1].split('/')[-2]
    path = generate_duns_path(company_no)
    if os.path.isfile(path) and os.stat(path).st_size > 0:
        with open(path, "r") as f:
            if json.load(f)["duns_number"] != "-3":
                return 0
    zip_code = entry[3].split(',')[-1].strip()
    cname = entry[0]
    for c in string.punctuation:
        cname = cname.replace(c, ' ')
    cname = re.sub(r"\d\d+", " ", cname)
    num2eng = dict(zip(
        map(str, range(10)), ["zero", "one", "two", "three", "four", "five",
                              "six", "seven", "eight", "nine"]))
    for k, v in num2eng.items():
        cname = cname.replace(k, v)
    country = "United Kingdom"
    city = "London"
    query_url = duns_utils.get_search_url(country, cname, city=city)
    try:
        result = duns_utils.get_search_result(query_url)
    except Exception as e:
        print company_no, query_url
        print e
        with open(path, "w") as f:
            json.dump({"duns_number": "-3"}, f)
        return -3
    new_result = duns_utils.filter_result(result, postal_code=zip_code)
    if new_result == []:
        duns = -1
    elif len(new_result) > 1:
        duns = -2
    else:
        duns = new_result[0]["duns_number"]
    with open(path, "w") as f:
        if duns > 0:
            json.dump(result[0], f)
        else:
            json.dump({"duns_number": str(duns)}, f)
    return duns


def generate_bunch_data(csv_path, bunch_split_num):
    with open(csv_path, "rb") as f:
        entry_reader = csv.reader(f, delimiter="|", quotechar='"')
        result = []
        entry_reader.next()
        for row in entry_reader:
            result.append(row)
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
              max=lines_num / batch_num,
              suffix="%(percent).1f%% - %(eta)ds\n")
    for bunch_data in generate_bunch_data("endole.csv", batch_num):
        start_time = time.time()
        result = pool.map(handle_single_entry, bunch_data)
        total_handle = sum([_ != 0 for _ in result])
        elapsed_time = time.time() - start_time
        sleep_time = batch_interval * total_handle / float(
            batch_num) * 1.1 - elapsed_time
        if sleep_time > 0:
            print "Elapased for %d seconds, Sleep for %d seconds." % (
                elapsed_time, sleep_time)
            time.sleep(sleep_time)
        bar.next()

    with open("endole_duns.csv", "w") as f:
        csv_writer = csv.writer(f, delimiter="|", quotechar='"')
        csv_writer.writerow(["name", "duns_number", "cash_in_bank",
                             "net_worth", "company_address", "company_detail"])
        for bunch_data in generate_bunch_data("endole.csv", batch_num):
            for entry in bunch_data:
                company_no = entry[-1].split('/')[-2]
                path = generate_duns_path(company_no)
                with open(path, "r") as fp:
                    duns_number = json.load(fp)["duns_number"]
                entry.insert(1, duns_number)
                csv_writer.writerow(entry)


def main():
    entry = [
        "Alchemy Energy Partners Ltd", "1792890", "6411214",
        "1512 City Point, 1 Ropemaker Street, London, EC2Y 9HT",
        "https://www.endole.co.uk/company/07555352/longacre-partners-limited"
    ]

    handle_single_entry(entry)
    keep_working()


if __name__ == '__main__':
    main()
