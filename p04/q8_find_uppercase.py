def find_num_uppercase(s):
    for i in range(len(s)):
        if s[i] in "QWERTYUIOPASDFGHJKLZXCVBNM":
            return find_num_uppercase(s[:i]+s[i+1:])+1
    return 0
