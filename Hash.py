# author   =   Aashutosh Mallik (Aashu)
prime = 101
def pattern_matching(text, pattern): #pattern matching
    m = len(pattern)
    n = len(text)
    pattern_hash = create_hash(pattern, m - 1)
    text_hash = create_hash(text, m - 1)

    for i in range(1, n - m + 2):
        if pattern_hash == text_hash:
            if check_equal(text[i-1:i+m-1], pattern[0:]) is True:
                return i - 1;
        if i < n - m + 1:    
            text_hash = recalculate_hash(text, i-1, i+m-1, text_hash, m)
    return -1;
    
def check_equal(str1, str2): #check if the pattern is equal
    if len(str1) != len(str2):
        return False;
    i = 0
    j = 0
    for i, j in zip(str1, str2):
        if i != j:
            return False;
    return True
    
def create_hash(input, end): #create hash functions of the selected pattern
    hash = 0
    for i in range(end + 1):
        hash = hash + ord(input[i])*pow(prime, i)
    return hash

def recalculate_hash(input, old_index, new_index, old_hash, pattern_len) #check if the selected hash function is in the mother case
    new_hash = old_hash - ord(input[old_index])
    new_hash = new_hash/prime
    new_hash += ord(input[new_index])*pow(prime, pattern_len - 1)
    return new_hash;

# test case
index = pattern_matching("AshuMallik", "M")
print("Index ", index)
index = pattern_matching("EricRozier", "c")
print("Index ", index)
