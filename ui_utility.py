#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Peng Liu <liupeng@imscv.com>
#
# Distributed under terms of the GNU GPL3 license.
"""
This file defines some derived UI class to help GUI works better.
"""

import Tkinter as tk
import re


def get_country_info(list_country):
    """This function helps handle the country selected.
    Keyword Arguments:
    list_country -- a Tkinter.Listbox object that used to select country.
    Return Value:
    the selected country abbrev or raised Exception.
    """
    # curselection returns str list.
    country_idx = map(int, list_country.curselection())
    try:
        assert len(country_idx) == 1
        country_idx = country_idx[0]
    except AssertionError:
        raise Exception("请选择国家！")
    countries = sorted(get_country_dict().keys())
    country = countries[country_idx]
    return country


def get_name_info(entry_name):
    """This function helps handle the name typed.
    Keyword Arguments:
    entry_name -- a Tkinter.Entry object that used to select name.
    Return Value:
    the typed company name or raised Exception.
    """
    name = entry_name.get()
    try:
        assert name != ""
        assert re.match("\d", name) == None
        return name
    except AssertionError:
        raise Exception("公司名称不能为空，或包含数字！")


def get_city_info(entry_city):
    """This function helps handle the city typed.
    Keyword Arguments:
    entry_city -- a Tkinter.Entry object that used to select city.
    Return Value:
    the typed company city or raised Exception.
    """
    city = entry_city.get()
    try:
        assert re.match("\d", city) == None
        return city
    except AssertionError:
        raise Exception("城市名称包含数字！")


def get_zip_info(entry_zip):
    """This function helps handle the zip typed.
    Keyword Arguments:
    entry_zip -- a Tkinter.Entry object that used to select zip.
    Return Value:
    the typed company zip or raised Exception.
    """
    zip_code = entry_zip.get()
    return zip_code


def get_address_info(entry_address):
    """This function helps handle the address typed.
    Keyword Arguments:
    entry_address -- a Tkinter.Entry object that used to select address.
    Return Value:
    the typed company address or raised Exception.
    """
    address = entry_address.get()
    return address


def get_query_info(list_country, entry_name, entry_city, entry_zip,
                   entry_address):
    """This function helps get the needed info for the query while raise
    Exception if one of them is invalid.

    Keyword Arguments:
    list_country  -- a Tkinter.Listbox object that used to select country.
    entry_name    -- a Tkinter.Entry object that used to recieve name.
    entry_city    -- a Tkinter.Entry object that used to recieve city.
    entry_zip     -- a Tkinter.Entry object that used to recieve zip_code.
    entry_address -- a Tkinter.Entry object that used to recieve address.

    """
    try:
        country = get_country_info(list_country)
        name = get_name_info(entry_name)
        city = get_name_info(entry_city)
        zip_code = get_name_info(entry_zip)
        address = get_name_info(entry_address)
        return [country, name, city, zip_code, address]
    except Exception as e:
        raise Exception(e)
