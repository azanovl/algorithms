import hashlib
string = 'Save our selves'

def func(s):
    len_str = len(s)
    hash_list = []
    n = 1

    while n < len_str:
        for i in range(len_str):
            h_subs = hashlib.sha256(s[i:i + n].encode('utf-8')).hexdigest()
            if h_subs not in hash_list:
                hash_list.append(h_subs)
        n += 1
    return len(hash_list)

print(f"{func(string)}")
