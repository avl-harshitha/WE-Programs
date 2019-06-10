import sys
delimiter = "/"


def clean_input(datestr):
    return datestr.replace(delimiter, "")


def check_ambig(datestr):
    return datestr[:2] != datestr[2:] and int(datestr[:2]) <= 12 and int(datestr[2:]) <= 12


def ambig_date(datestr):
    datestr = clean_input(datestr)
    return check_ambig(datestr[:4])


print(ambig_date("11/12/1300"))