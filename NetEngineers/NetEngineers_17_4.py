import csv
import re
from pprint import pprint
import datetime
import yaml
from tabulate import tabulate


def convert_str_to_datetime(datetime_str):
    """
    Конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
    """
    return datetime.datetime.strptime(datetime_str, "%d/%m/%Y %H:%M")


def convert_datetime_to_str(datetime_obj):
    """
    Конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
    """
    return datetime.datetime.strftime(datetime_obj, "%d/%m/%Y %H:%M")
def write_last_log_to_csv(source_log,output):
    headers=['Name','Email','Las Changed']
    res_dict={}
    res_lst=[]
    emails=[]
    with open (source_log,'r') as f:
        reader=csv.DictReader(f)
        for row in reader:
            if row['Email'] in emails:
                r=[r for r in res_lst if r['Email']==row['Email']][0]
                if convert_str_to_datetime(row['Last Changed'])<convert_str_to_datetime(r['Last Changed']):
                    continue
                else:
                    res_lst.remove(r)
                    res_lst.append(row)
            else:
                res_lst.append(row)
                emails.append(row['Email'])
    print('RSSS',res_lst)
    with open(output,'a') as f:
        writer=csv.DictWriter(f,fieldnames=list(res_lst[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
        for row in res_lst:
            writer.writerow(row)
def main():
    write_last_log_to_csv('mail_log.csv','mail_log_result.csv')

if __name__ == "__main__":
    main()

#
