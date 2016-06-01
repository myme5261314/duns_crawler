#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Peng Liu <liupeng@imscv.com>
#
# Distributed under terms of the GNU GPL3 license.
"""
This file defines some utility functions for duns crawler.
"""

import urllib2
import json
import csv
import datetime
from multiprocessing import Pool
from static_content import *

"https://www.dandb.com/search/?search_type=duns&duns=557700898&country="


def get_search_url(country,
                   name,
                   state=None,
                   city=None,
                   zip_code=None,
                   address=None):
    """
    Help generate search url based on provided information.

    :country: the country full name, converted to its abbrev.
    :name: the company name keyword.
    :state: used only if country is US, provided as full name, converted to its
    abbrev.
    :city: the city of the company
    :zip: the zipcode of the city or district.
    :address: part of the company address.

    :return: the url to get the information of some search conditions.
    """
    base_url = "http://www.dnb.com/apps/dnb/thirdparty/dunslookup?"
    default_country = ["", "United States"]
    key_str = ""
    key_str += "country=%s&" % ("" if country in default_country else
                                get_country_dict()[country])
    try:
        assert name != ""
    except AssertionError:
        raise Exception("company name required!")
    name = name.replace(' ', "%20")
    key_str += "name=%s&" % name
    try:
        if country in ["", "United States"]:
            assert state is not None
    except AssertionError:
        raise Exception("state required while country is US!")
    key_str += "state=%s&" % get_state_dict()[
        state] if country in default_country and state is not None else ""
    key_str += "" if city is None and city != "" else "city=%s&" % city
    key_str += "" if zip_code is None else "zip=%s&" % zip_code
    if address is not None:
        address = address.replace(' ', "%20")
    key_str += "" if address is None else "address=%s&" % address
    key_str = key_str[:-1]
    return base_url + key_str


def get_search_result(url):
    """
    This function helps get result of the search.

    :url: the string of search url.

    :return: the list of results.
    """
    contents = urllib2.urlopen(url).read()
    result_js = json.loads(contents)
    try:
        assert result_js["meta"]["code"] == 200
    except AssertionError:
        raise Exception(result_js["error"][0])
    return result_js["response"]["results"]


def parse_to_csv(result, path_str):
    """
    This function helps parse the searched result to a csv file.

    :result: the result list(dict).
    :path_str: the string to store the csv file.

    :return:
    """
    if len(result) == 0:
        raise Exception("查询结果为空！")
    key_set = set()
    all_keys = [set(element.keys()) for element in result]
    key_set.update(*all_keys)
    csv_rows = [[str(element[k]) for k in key_set] for element in result]
    with open(path_str, "wb") as csv_file:
        csv_writer = csv.writer(csv_file,
                                delimiter='|',
                                quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([_ for _ in key_set])
        for row in csv_rows:
            csv_writer.writerow(row)
    return True


def search_callback(country, state, name, city, zip_code, address):
    """
    helps finish a search.

    :country: the full name of country, string, not empty.
    :state: the full name of selected US state, string, could be empty.
    :name: the user input name string, not empty.
    :city: the user input name string, could be empty.
    :zip_code: the int for user input zip, -1 for no zip.
    :address: the user input address, could be empty.

    """
    state = state if state != "" else None
    city = city if city != "" else None
    zip_code = zip_code if zip_code != -1 else None
    address = address if address != "" else None
    url = get_search_url(country, name, state, city, zip_code, address)
    result = get_search_result(url)
    search_keyword = ""
    search_keyword += country + "-"
    search_keyword += name + "-"
    search_keyword += (state + "-") if state is not None else ""
    search_keyword += (city + "-") if city is not None else ""
    search_keyword += (zip_code + "-") if zip_code is not None else ""
    search_keyword += datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    parse_to_csv(result, "%s.csv" % search_keyword)
    return search_keyword + ".csv"


def filter_result(result):
    """This function helps squeeze out some definitely useless entry of result.
    Keyword Arguments:
    result --
    """
    num = len(result)
    del_idx = []
    for i in xrange(num):
        test_valid = dict()
        # May need more conditions in the future.
        test_valid["out_of_business_indicator"] = ["", "0"]
        test_valid["duns_support_indicator"] = [""]
        test_valid["match_indicator"] = ["", "C"]
        test_valid["branch_indicator"] = ["", 0]
        for test_valid_key, test_valid_list in test_valid.iteritems():
            if test_valid_key in result[i] and result[i][
                    test_valid_key] not in test_valid_list:
                del_idx.append(i)
                break
    new_result = [result[_] for _ in xrange(num) if _ not in del_idx]
    return new_result


def pool_enum_search(pool, country, name_list, city, zip_code, address):
    """This function use a Pool to execute the search operations.
    Keyword Arguments:
    country   --
    name_list --
    city      --
    zip_code  --
    address   --
    """
    url_list = map(
        lambda x: get_search_url(country, x, city, zip_code, address),
        name_list)
    # Seems osx has some problem with this pool code. Need investigate how to fix.
    # pool = Pool(10)
    result_list = pool.map(get_search_result, url_list)
    # result_list = map(get_search_result, url_list)
    result_list = map(filter_result, result_list)
    return result_list


def main():
    """
    Test function.
    """
    print get_search_result(get_search_url("", "google", state="California"))
    print get_search_result(get_search_url("Australia", "google"))
    alphabet = list(string.ascii_lowercase)
    name_list = []
    for char in alphabet:
        name_list.append("a"+char)
    url_list = map(
        lambda x: get_search_url("Brazil", x, "", "", ""),
        name_list)
    pool = Pool(10)
    result_list = pool.map(get_search_result, url_list)


if __name__ == '__main__':
    main()
