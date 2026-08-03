

def ends_with_ab(string):
    state = 0

    for ch in string:
        if state == 0:
            if ch == 'a':
                state = 1
            else:
                state = 0

        elif state == 1:
            if ch == 'b':
                state = 2
            elif ch == 'a':
                state = 1
            else:
                state = 0

        elif state == 2:
            if ch == 'a':
                state = 1
            else:
                state = 0

    return state == 2


test_strings = ["ab", "cab", "aab", "abab", "abc", "baba", "baa"]

for s in test_strings:
    if ends_with_ab(s):
        print(f"{s} -> Accepted")
    else:
        print(f"{s} -> Rejected")
