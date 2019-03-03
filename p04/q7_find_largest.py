def find_largest(alist):
    if len(alist)==1:
        return alist[0]
    alist[1]=max(alist[0], alist[1])
    del(alist[0])
    return find_largest(alist)
