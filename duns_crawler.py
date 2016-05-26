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
import ttk
import tkMessageBox
from static_content import *
from duns_utils import search_callback
import ui_utility


def main():
    """
    This is the main function.
    """
    countries = sorted(get_country_dict().keys())
    # states are useless if we don't need US company.
    # states = sorted(get_state_dict().keys())

    root = Tkinter.Tk()
    root.title("duns助手")

    # Frame layout level one.
    f_permilinary = Tkinter.LabelFrame(root, text="必填项")
    f_permilinary.grid(column=0, row=0)
    f_trival = Tkinter.LabelFrame(root, text="可空项")
    f_trival.grid(column=1, row=0, sticky="NW")
    f_action = Tkinter.Frame(root)
    f_action.grid(column=2, row=0)
    f_result = Tkinter.LabelFrame(root, text="结果")
    f_result.grid(column=0, row=1, columnspan=3, sticky="WE")

    ff_country = Tkinter.Frame(f_permilinary)
    ff_country.grid(column=0, row=0)
    ff_name = Tkinter.Frame(f_permilinary)
    ff_name.grid(column=0, row=1)

    ff_city = Tkinter.Frame(f_trival)
    ff_city.grid(column=0, row=1)
    ff_zip = Tkinter.Frame(f_trival)
    ff_zip.grid(column=0, row=2)
    ff_address = Tkinter.Frame(f_trival)
    ff_address.grid(column=0, row=3)

    ff_button = Tkinter.Frame(f_action)
    ff_button.grid()

    ff_treeview = Tkinter.Frame(f_result)
    ff_treeview.grid(sticky="WE")

    label_country = Tkinter.Label(ff_country, text="国家")
    label_country.grid(column=0, row=0, sticky="WE")
    list_country = Tkinter.Listbox(ff_country, exportselection=False)
    for country in reversed(countries):
        list_country.insert(0, country)
    list_country.grid(column=0, row=1, sticky="WE")

    label_name = Tkinter.Label(ff_name, text="名称：")
    label_name.grid(column=0, row=0)
    entry_name = Tkinter.Entry(ff_name)
    entry_name.grid(column=1, row=0)

    label_city = Tkinter.Label(ff_city, text="城市：")
    label_city.grid(column=0, row=0)
    entry_city = Tkinter.Entry(ff_city)
    entry_city.grid(column=1, row=0)

    label_zip = Tkinter.Label(ff_zip, text="邮编：")
    label_zip.grid(column=0, row=0)
    entry_zip = Tkinter.Entry(ff_zip)
    entry_zip.grid(column=1, row=0)

    label_address = Tkinter.Label(ff_address, text="地址：")
    label_address.grid(column=0, row=0)
    entry_address = Tkinter.Entry(ff_address)
    entry_address.grid(column=1, row=0)

    def search_callback_wrapper():
        # curselection returns str list.
        country_idx = map(int, list_country.curselection())
        try:
            assert len(country_idx) == 1
            country_idx = country_idx[0]
        except AssertionError:
            tkMessageBox.showerror("国家", "请选择国家！")
            return
        country = countries[country_idx]

        name = entry_name.get()
        try:
            assert name != ""
            # assert ' ' not in name
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
            result_path = search_callback(country, "", name, city, zip_code,
                                          address)
        except Exception, e:
            tkMessageBox.showerror("底层错误", e)
            return
        tkMessageBox.showinfo("结果", "查询成功，结果保存在文件%s中！" % result_path)

    butt_search = Tkinter.Button(ff_button,
                                 text="查询",
                                 command=search_callback_wrapper)
    butt_search.grid()
    enum_callback_wrapper = lambda x: x
    butt_enum = Tkinter.Button(ff_button,
                               text="穷举",
                               command=enum_callback_wrapper)
    butt_enum.grid()

    tree = ttk.Treeview(ff_treeview)
    tree.grid()
    tree["columns"] = ("country", "city", "duns", "address")
    tree.heading("country", text="国家")
    tree.heading("city", text="城市")
    tree.heading("duns", text="duns")
    tree.heading("address", text="地址")

    root.mainloop()


if __name__ == '__main__':
    main()
