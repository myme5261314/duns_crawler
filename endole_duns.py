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

import duns_utils


duns_dir = "duns"

def generate_duns_path(company_no):
    return os.join(duns_dir, company_no + ".json")

def handle_single_entry(entry):
    company_no = row[-1].split('/')[-2]
    zip_code = row[3].split(',')[-1].strip()
    print zip_code
    replace_char = ['(', ')', '&', '.', '-']
    cname = row[0]
    for c in replace_char:
        cname = cname.replace(c, ' ')
    cname = re.sub(r"\d\d+", " ", cname)
    num2eng = dict(
        zip(map(str, range(10)), ["zero", "one", "two", "three", "four", "five",
                    "six", "seven", "eight", "nine"]))
    for k, v in num2eng.items():
        cname = cname.replace(k, v)
    country = "United Kingdom"
    city = "London"
    query_url = duns_utils.get_search_url(country, cname, city=city)
    result = duns_utils.get_search_result(query_url)
    new_result = duns_utils.filter_result(result, postal_code=zip_code)
    if new_result == []:
        duns = 0
    elif len(new_result) > 1:
        duns = -1
    else:
        duns = new_result[0]["duns_number"]
        path = generate_duns_path(company_no)
        if not os.path.isfile(path) or os.stat(path).st_size == 0:
            with open(generate_duns_path, "w") as f:
                f.write(result[0].encode("utf8"))
    return duns


def main():
    with open("endole.csv", "r") as f:
        entry_reader = csv.reader(f, delimiter="|", quotechar='"')
        entry_reader.next()
        for row in entry_reader:
            handle_single_entry(row)


if __name__ == '__main__':
    main()
