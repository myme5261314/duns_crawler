#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Peng Liu <liupeng@imscv.com>
#
# Distributed under terms of the GNU GPL3 license.
"""
This is a crawler to get duns.
"""

import Tkinter
import tkMessageBox
from static_content import *
from duns_utils import search_callback
import ui_utility


def main():
    """
    This is the main function.
    """
    countries = sorted(get_country_dict().keys())
    states = sorted(get_state_dict().keys())

    top = Tkinter.Tk()
    top.title("duns助手")

    frame_country = Tkinter.Frame(top)
    frame_country.pack()
    label_country = Tkinter.Label(frame_country, text="国家")
    label_country.pack()
    list_country = Tkinter.Listbox(frame_country, exportselection=False)
    for country in reversed(countries):
        list_country.insert(0, country)
    list_country.pack(fill="both")
    list_country.config(width=0)

    frame_state = Tkinter.Frame(top)
    frame_state.pack()
    label_state = Tkinter.Label(frame_state, text="州")
    label_state.pack()
    list_state = Tkinter.Listbox(frame_state, exportselection=False)
    for state in reversed(states):
        list_state.insert(0, state)
    list_state.pack(fill="both")
    list_state.config(width=0)

    frame_name = Tkinter.Frame(top)
    frame_name.pack(fill="both")
    label_name = Tkinter.Label(frame_name, text="名称（必需）：")
    label_name.pack(side="left")
    entry_name = Tkinter.Entry(frame_name)
    entry_name.pack(fill="both")

    frame_city = Tkinter.Frame(top)
    frame_city.pack(fill="both")
    label_city = Tkinter.Label(frame_city, text="城市（可空）：")
    label_city.pack(side="left", fill="both")
    entry_city = Tkinter.Entry(frame_city)
    entry_city.pack(fill="both")

    frame_zip = Tkinter.Frame(top)
    frame_zip.pack(fill="both")
    label_zip = Tkinter.Label(frame_zip, text="邮编（可空）：")
    label_zip.pack(side="left")
    entry_zip = Tkinter.Entry(frame_zip)
    entry_zip.pack(fill="both")

    frame_address = Tkinter.Frame(top)
    frame_address.pack(fill="both")
    label_address = Tkinter.Label(frame_address, text="地址（可空）:")
    label_address.pack(side="left")
    entry_address = Tkinter.Entry(frame_address)
    entry_address.pack(fill="both")

    def search_callback_wrapper():
        country_idx = list_country.curselection()
        try:
            assert len(country_idx) == 1
            country_idx = country_idx[0]
        except AssertionError:
            tkMessageBox.showerror("国家", "请选择国家！")
            return
        country = countries[country_idx]

        state_idx = list_state.curselection()
        if country == "United States":
            try:
                assert len(state_idx) == 1
            except AssertionError:
                tkMessageBox.showerror("国家为美国", "请选择州！")
                return
            state = states[state_idx[0]]
        else:
            state = ""

        name = entry_name.get()
        try:
            assert name != ""
            assert ' ' not in name
        except AssertionError:
            tkMessageBox.showerror("名称", "名称不能为空！")
            return

        city = entry_city.get()
        zip_code = entry_zip.get()
        try:
            zip_code = int(zip_code) if zip_code != "" else -1
        except ValueError:
            tkMessageBox.showerror("邮编", "邮编必须为数字！")
            return
        address = entry_address.get()
        result_path = ""
        try:
            result_path = search_callback(country, state, name, city, zip_code,
                                          address)
        except Exception, e:
            tkMessageBox.showerror("底层错误", e.what())
            return
        tkMessageBox.showinfo("结果", "查询成功，结果保存在文件%s中！" % result_path)

    frame_button = Tkinter.Frame(top)
    frame_button.pack(fill="both")
    butt = Tkinter.Button(frame_button,
                          text="查询",
                          command=search_callback_wrapper)
    butt.pack()

    top.mainloop()


if __name__ == '__main__':
    main()
