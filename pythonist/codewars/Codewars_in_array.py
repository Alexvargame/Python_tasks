
def in_array2(array,ar):
    if [arr for arr in array if ar in arr]:
        return True
    return False
def in_array(array1, array2):
    return sorted(list(set([ar1 for ar1 in array1 if in_array2(array2,ar1)])))





def main():

    print(in_array(["arp", "live", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]))

if __name__ == "__main__":
    main()

#
