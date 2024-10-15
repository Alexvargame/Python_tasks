import gzip
import io
import glob

def find_robots(filename):

# Находит в одном лог-файле все хосты, которые обращались к robots.txt

    robots = set()
    with gzip.open(filename) as f:
        print(f)
        for line in io.TextIOWrapper(f,encoding='ascii'):
            fields = line.split()
            if fields[6] == '/robots.txt':
                print(fields[0])
                robots.add(fields[0])
    return robots

def find_all_robots(logdir):

# Находит все хосты во всех файлах
    print(logdir)
    files = glob.glob(logdir+'/*.log.gz')
    print('f',files)
    all_robots = set()
    for robots in map(find_robots, files):
        print(robots)
        all_robots.update(robots)
    return all_robots

if  __name__ == '__main__':
    robots = find_all_robots('logs')
    for ipaddr in robots:
        print(ipaddr)
