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
import traceback
import copy
from static_content import *
import duns_utils
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

    tree = ttk.Treeview(ff_treeview)

    def search_callback_wrapper():
        try:
            country, name, city, zip_code, address = ui_utility.get_query_info(
                list_country, entry_name, entry_city, entry_zip, entry_address)
            url = duns_utils.get_search_url(country, name, city, zip_code,
                                            address)
            result = duns_utils.get_search_result(url)
            result = duns_utils.filter_result(result)
            ui_utility.update_tree_content(tree, result)
        except Exception as e:
            traceback.print_exc()
            tkMessageBox.showerror("错误", e)

    butt_search = Tkinter.Button(ff_button,
                                 text="查询",
                                 command=search_callback_wrapper)
    butt_search.grid()
    enum_callback_wrapper = lambda x: x
    butt_enum = Tkinter.Button(ff_button,
                               text="穷举",
                               command=enum_callback_wrapper)
    butt_enum.grid()

    tree.grid()
    cols = ["duns", "country", "city", "name"]
    tree["columns"] = cols
    tree.column("#0", width=0)
    # http://stackoverflow.com/questions/20079989
    def sort_wrapper(col):
        _col = col
        return lambda: ui_utility.treeview_sort_column(tree, _col, False)
    for col in cols:
        tree.heading(col,
                     command=sort_wrapper(col))
    tree.heading("duns", text="duns")
    tree.heading("country", text="国家")
    tree.heading("city", text="城市")
    tree.heading("name", text="名称")
    # tree.heading("address", text="地址")

    root.mainloop()


if __name__ == '__main__':
    main()
