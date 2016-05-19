#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Peng Liu <liupeng@imscv.com>
#
# Distributed under terms of the GNU GPL3 license.
"""
This file provides some unchanged contents.
"""


def get_country_dict():
    """
    This function helps generate the unchanged country full name to its abbrev dict.

    :return: the dict which is name -> abbrev.
    """
    pairs = [
        ("United States", "US"),
        ("United Kingdom", "UK"),
        ("Africa (Northern)", "af"),
        ("Argentina", "AR"),
        ("Australia", "AU"),
        ("Austria", "OS"),
        ("Bahrain", "BR"),
        ("Bangladesh", "BA"),
        ("Belgium", "BL"),
        ("Bhutan", "BT"),
        ("Brazil", "BZ"),
        ("Brunei Darussalam", "bn"),
        ("Bulgaria", "BU"),
        ("Cambodia", "KA"),
        ("Canada", "CA"),
        ("China", "cn"),
        ("Czech Republic", "XC"),
        ("Denmark", "DK"),
        ("East Timor", "TP"),
        ("Eastern Europe", "ee"),
        ("Finland", "SF"),
        ("France", "FR"),
        ("Germany", "DE"),
        ("Greece", "GR"),
        ("Hong Kong", "HK"),
        ("Hungary", "HU"),
        ("India", "IN"),
        ("Indonesia", "ID"),
        ("Iraq", "IQ"),
        ("Ireland", "IR"),
        ("Israel", "IS"),
        ("Italy", "IT"),
        ("Japan", "JA"),
        ("Jordan", "JO"),
        ("Korea", "kr"),
        ("Kuwait", "KU"),
        ("Laos", "LA"),
        ("Latin America", "la"),
        ("Lebanon", "LE"),
        ("Malaysia", "MS"),
        ("Maldives", "MV"),
        ("Mediterranean Europe", "md"),
        ("Mexico", "MX"),
        ("Middle East", "me"),
        ("Myanmar", "KA"),
        ("Nepal", "NE"),
        ("Netherlands", "NL"),
        ("New Zealand", "NZ"),
        ("Norway", "NO"),
        ("Oman", "OM"),
        ("Pakistan", "PA"),
        ("Peru", "PR"),
        ("Philippines", "PH"),
        ("Poland", "PL"),
        ("Portugal", "PO"),
        ("Qatar", "QA"),
        ("Russia-CIS", "ru"),
        ("Romania", "RO"),
        ("Saudi Arabia", "SD"),
        ("Singapore", "SI"),
        ("Slovakia", "SK"),
        ("Slovenia", "SB"),
        ("South Africa", "SA"),
        ("Sri Lanka", "SR"),
        ("Spain", "ES"),
        ("Sweden", "SW"),
        ("Switzerland", "CH"),
        ("Syria", "SY"),
        ("Taiwan", "CT"),
        ("Thailand", "TH"),
        ("Turkey", "TK"),
        ("UAE", "UA"),
        ("Vietnam", "VI"),
        ("Yemen", "YE"),
    ]
    return dict(pairs)


def get_state_dict():
    """
    This function helps generate state full name to its abbrev dict.

    :return: a dict which maps US state's name to its abbrev.
    """
    pairs = [
        ("Alabama", "AL"),
        ("Alaska", "AK"),
        ("Arizona", "AZ"),
        ("Arkansas", "AR"),
        ("California", "CA"),
        ("Colorado", "CO"),
        ("Connecticut", "CT"),
        ("Delaware", "DE"),
        ("District of Columbia", "DC"),
        ("Florida", "FL"),
        ("Georgia", "GA"),
        ("Hawaii", "HI"),
        ("Idaho", "ID"),
        ("Illinois", "IL"),
        ("Indiana", "IN"),
        ("Iowa", "IA"),
        ("Kansas", "KS"),
        ("Kentucky", "KY"),
        ("Louisiana", "LA"),
        ("Maine", "ME"),
        ("Maryland", "MD"),
        ("Massachusetts", "MA"),
        ("Michigan", "MI"),
        ("Minnesota", "MN"),
        ("Mississippi", "MS"),
        ("Missouri", "MO"),
        ("Montana", "MT"),
        ("Nebraska", "NE"),
        ("Nevada", "NV"),
        ("New Hampshire", "NH"),
        ("New Jersey", "NJ"),
        ("New Mexico", "NM"),
        ("New York", "NY"),
        ("North Carolina", "NC"),
        ("North Dakota", "ND"),
        ("Ohio", "OH"),
        ("Oklahoma", "OK"),
        ("Oregon", "OR"),
        ("Pennsylvania", "PA"),
        ("Puerto Rico", "PR"),
        ("Rhode Island", "RI"),
        ("South Carolina", "SC"),
        ("South Dakota", "SD"),
        ("Tennessee", "TN"),
        ("Texas", "TX"),
        ("Utah", "UT"),
        ("Vermont", "VT"),
        ("Virginia", "VA"),
        ("Virgin Islands", "VI"),
        ("Washington", "WA"),
        ("West Virginia", "WV"),
        ("Wisconsin", "WI"),
        ("Wyoming", "WY"),
    ]
    return dict(pairs)


def get_country_ref_url():
    pairs = {
        "United States": "http://www.dnb.com",
        "United Kingdom": "http://www.dnb.co.uk",
        "Africa (Northern)": "http://www.dnbafrica.com",
        "Argentina": "https://www.dnbla.com/es/argentina",
        "Australia": "http://www.dnb.com.au",
        "Austria": "http://www.dnbaustria.at",
        "Bahrain": "http://www.dnbsame.com",
        "Bangladesh": "http://www.dnbsame.com",
        "Belgium": "http://www.dnb-belgium.be/nl",
        "Bhutan": "http://www.dnbsame.com",
        "Brazil": "http://www.dnb.com.br/eng_default.asp",
        "Brunei Darussalam": "http://www.dnbvietnam.com",
        "Bulgaria": "http://www.icap.bg",
        "Cambodia": "http://www.dnbvietnam.com",
        "Canada": "http://www.dnb.ca",
        "China": "http://www.huaxiadnb.com/english/default.htm",
        "Czech Republic": "http://www.dnbczech.cz",
        "Denmark": "http://www.dnbdenmark.dk/en/Contact/",
        "East Timor": "http://www.dnb.co.id",
        "Eastern Europe": "http://dbemc.dnb.com/",
        "Finland": "http://www.dnb.fi/en/",
        "France": "http://www.altares.fr",
        "Germany": "http://www.bisnode.de",
        "Greece": "http://www.icap.gr",
        "Hong Kong": "http://www.dnbasia.com/hk/english/",
        "Hungary": "http://www.dbhun.hu",
        "India": "http://www.dnb.co.in",
        "Indonesia": "http://www.dnb.co.id",
        "Iraq": "http://www.dnbsame.com",
        "Ireland": "http://www.dnb.co.uk",
        "Israel": "http://www.dbisrael.co.il/english/index.jsp",
        "Italy": "https://www.dnb.it/",
        "Japan": "http://www.tsr-net.co.jp",
        "Jordan": "http://www.dnbsame.com",
        "Korea": "http://global.nicednb.com",
        "Kuwait": "http://www.dnbsame.com",
        "Laos": "http://www.dnbvietnam.com",
        "Latin America": "http://www.dnbla.com",
        "Lebanon": "http://www.dnbsame.com",
        "Malaysia": "http://www.dnb.com.my",
        "Maldives": "http://www.dnbsame.com",
        "Mediterranean Europe": "http://www.dbemc.dnb.com",
        "Mexico": "http://www.dnbmex.com.mx",
        "Middle East": "http://www.dnbsame.com",
        "Myanmar": "http://www.dnbvietnam.com",
        "Nepal": "http://www.dnbsame.com",
        "Netherlands": "http://www.dnb-nederland.nl",
        "New Zealand": "http://www.dnb.com.au",
        "Norway": "http://www.db24.no",
        "Oman": "http://www.dnbsame.com",
        "Pakistan": "http://www.dnbsame.com",
        "Peru": "http://www.dnbperu.com.pe",
        "Philippines": "http://www.dnb.com.ph",
        "Poland": "http://www.dnb.com.pl",
        "Portugal": "https://www.informadb.pt/idbweb/",
        "Qatar": "http://www.dnbsame.com",
        "Russia-CIS": "http://www.dnb.ru",
        "Romania": "http://www.icap.ro",
        "Saudi Arabia": "http://www.dnbsame.com",
        "Singapore": "http://www.dnb.com.sg",
        "Slovakia": "http://www.dnbczech.cz/sk",
        "Slovenia": "http://dbemc.dnb.com",
        "South Africa":
        "http://www.transunion.co.za/business/industrySolutions/businessCredit/internationalBusInfo.html",
        "Sri Lanka": "http://www.dnbsame.com",
        "Spain": "http://www.informa.es",
        "Sweden": "http://www.dnbsweden.se/en",
        "Switzerland": "http://www.bisnode.ch/de/302/Home.htm",
        "Syria": "http://www.dnbsame.com",
        "Taiwan": "http://www.dnbasia.com",
        "Thailand": "http://www.dnb.co.th",
        "Turkey": "http://www.dnbturkey.com",
        "UAE": "http://www.dnbsame.com",
        "Vietnam": "http://www.dnbvietnam.com",
        "Yemen": "http://www.dnbsame.com"
    }
