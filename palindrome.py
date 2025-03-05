def isPalindrome(phrase):
    left = 0
    right = len(phrase) -1

    while left < right:
        while left < right and not phrase[left].isalpha():
            left += 1
        while left < right and not phrase[right].isalpha():
            right -= 1
        if phrase[left].lower() != phrase[right].lower():
            return False
        left += 1
        right -= 1

    return True
