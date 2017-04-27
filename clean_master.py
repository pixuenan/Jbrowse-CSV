"""
Clean the master list.
The master list should have three column chrome, start position, end position of the variant
The master list should not have headers
Xuenan Pi
27/04/2017
"""

def read_file(master_list, size):
    loc_dict = dict()
    with open(master_list, 'r') as master_file:
        lines = master_file.readlines()
    for line in lines:
        if not line.strip(): # skip empty line
            pass
        else:
            chrome, loc1, loc2 = line.strip().split("\t")
            if chrome not in loc_dict.keys():
                loc_dict[chrome] = [(int(loc1)-size, int(loc2)+size)]
            else:
                loc_dict[chrome] += [(int(loc1)-size, int(loc2)+size)]
    return loc_dict

def clean_overlap_loc(loc_dict):
    # sort the locations
    new_loc_dict = dict()
    for key in loc_dict.keys():
        loc_dict[key] = sorted(loc_dict[key])
        new_loc_dict[key] = []
        # clean the overlap
        pre_loc, cur_loc = [], []
        for idx, location in enumerate(loc_dict[key]):
            if idx == 0:
                pre_loc = location
                pass
            else:
                cur_loc = location
                # overlap
                if cur_loc[0] <= pre_loc[1]:
                    if cur_loc[1] >= pre_loc[1]:
                        pre_loc = (pre_loc[0], cur_loc[1])
                    else:
                        pre_loc = (pre_loc[0], pre_loc[1])
                # non-overlap
                else:
                    new_loc_dict[key] += [pre_loc]
                    pre_loc = cur_loc
            if idx == len(loc_dict[key])-1:
                if pre_loc == cur_loc:
                    new_loc_dict[key] += [cur_loc]
                else:
                    new_loc_dict[key] += [pre_loc]
    return new_loc_dict

def write_result(new_loc_dict):
    with open("cleaned_master_list.txt", "w") as result:
        for key in sorted(new_loc_dict.keys()):
            for loc in new_loc_dict[key]:
                result.write("%s:%s-%s\n" % (key, loc[0], loc[1]))

if __name__=="__main__":
    master_list = "CAP_NGSHM-A_2017_master_list.txt" # the master list file should not have empty lines
    size = 300
    loc_list = read_file(master_list, 300)
    new_loc_list = clean_overlap_loc(loc_list)
    write_result(new_loc_list)




