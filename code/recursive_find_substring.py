def find_substring_loop(s, sub):
    i = 0
    while i < len(s):
        if s[i:i+len(sub)] == sub:
            return i
        i += 1
    return -1

print(find_substring_loop("hello great world", "world"))

def find_substring_recursive(s, sub, i=0):
    if i > len(s):
        return -1
    if s[i:i+len(sub)] == sub:
        return i
    else:
        return find_substring_recursive(s, sub, i + 1)
    
print(find_substring_recursive("hello great world", "world"))   