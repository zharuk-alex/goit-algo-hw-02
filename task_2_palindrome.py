import collections

def is_palindrome(string):
    string = string.lower().replace(" ", "")
    dqueue = collections.deque(string)

    while len(dqueue) >= 2:
        if dqueue.popleft() != dqueue.pop():
            return False

    return True

print(is_palindrome("L-o-l"))
print(is_palindrome("madaM"))
print(is_palindrome(" civic  "))
print(is_palindrome("qwerty"))