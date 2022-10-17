#def splitter(clean_list):
"""Split and list the folder paths in different list"""
    #* make a list for every piece of the path
    # count = {}
x = []
y = []
z = []
new_x_list = []
new_z_list = []
new_y_list = []
    # go through all the lines in clean_list
for line in clean_list:
        # remove videoin file from the list
    if 'videoin' not in line:
        if line in count:
                count[line]
            # add to the x list the main folder
        x.append(line.split('\\')[0] + '\n')
            # add to the y list the second
            #y.append(line.split('\\')[1] + '\n')
            # add to the z list the third or last
        z.append(line.split('\\')[-1] + '\n')
        # this will clean all the duplicates in the x list
        for a in x:
            if a not in new_x_list:
                new_x_list.append(a)
        # this will clean all the duplicates in the y list
        for b in y:
            if b not in new_y_list:
                new_y_list.append(b)
        # this will clean all the duplicates in the z list
        for c in z:
            if c not in new_z_list:
                new_z_list.append(c)