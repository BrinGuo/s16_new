data = range(1,10000000)


def binary_search(find_str,data_set,count):
    mid = int(len(data_set)/2)
    if mid == 0:
        if data_set[mid] == find_str:
            print("find it finally",data_set[mid],count)
        else:
            print("not find num in list",find_str,count)
        return
    if data_set[mid] == find_str:
        print("find it:",mid,find_str)
    elif data_set[mid] > find_str:  #find_str in left side
        binary_search(find_str,data_set[0:mid],count+1)
        print("going go search in right",mid,data_set[mid],data_set[0:mid],count)
    else:      #find_str in right side
        print("going go search in right",mid,data_set[mid],data_set[mid+1:],count)

        binary_search(find_str,data_set[mid+1:],count+1)

binary_search(8,data,1)


