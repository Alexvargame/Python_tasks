def get_ignore(l,alst):
    for a in alst:
        if a in l:
            return True
    return False


def task7_2():
    ignore = ["duplex", "alias", "configuration"]
    res_file_name=input('Enter file name')
    res_file_name=res_file_name+'.txt'
    with open('config_sw1.txt') as f, open(res_file_name,'w') as resf:
        for line in f.readlines():
            if not line.startswith('!') and not get_ignore(line,ignore):
                resf.write(line)

def main():
    task7_2()


if __name__ == "__main__":
    main()

#
