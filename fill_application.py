#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Peng Liu <liupeng@imscv.com>
#
# Distributed under terms of the GNU GPL3 license.
"""
This file helps fill in the information while applying.
"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


def main():
    start_ulr = "https://developer.apple.com/programs/enterprise/enroll/"
    username = "addison_edward@angolasuperior-auto.com"
    password = "Addisonedward1956"
    name = "123"
    duns = 456
    website = "789"
    phone = "012"
    num_emp_idx = 2
    work_email = "345@678.com"

    # b = Browser("chrome")
    # b.visit(start_ulr)
    # b.click_link_by_text("Start Your Enrollment")
    options = webdriver.ChromeOptions()
    # options.add_argument("user-data-dir=/home/deeplearn/.config/google-chrome")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(start_ulr)
    driver.find_element_by_link_text("Start Your Enrollment").click()
    # Login
    driver.find_element_by_id("accountname").send_keys(username)
    driver.find_element_by_id("accountpassword").send_keys(password)
    driver.find_element_by_id("submitButton2").click()
    # Select Organization
    Select(driver.find_element_by_id("entity-type")).select_by_index(1)
    time.sleep(0.5)
    driver.find_element_by_id("submit").click()
    # Provide information
    driver.find_element_by_id("owner-condition-true").click()
    driver.find_element_by_id("lg-entity-name").send_keys(name)
    driver.find_element_by_id("duns-number").send_keys(str(duns))
    driver.find_element_by_id("website").send_keys(website)
    driver.find_element_by_id("cmpny-phone-number").send_keys(phone)
    Select(driver.find_element_by_id("company-size")).select_by_index(
        num_emp_idx)
    driver.find_element_by_id("email").send_keys(work_email)

    raw_input("wait till input.")


if __name__ == '__main__':
    main()
