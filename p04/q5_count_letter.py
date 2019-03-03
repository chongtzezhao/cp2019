def count_letter(s, ch):
    if ch not in s: #check if char is in string
        return 0
    for i in range(len(s)):
        if s[i]==ch: #if char in string
            #new_s=s[:i]+s[i+1:]
            return(count_letter(s[:i]+s[i+1:], ch)+1) #plus 1
