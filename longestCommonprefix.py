def longestCommonPrefix(strs):
    if 1 <= len(strs) <= 200:
        prefix = strs[0]
        for i in strs[0:]:
            if 0 <= len(strs) <= 200:
                while not i.startswith(prefix):
                    prefix = prefix[:-1]
                    if not prefix:
                        return ""
                    else:
                        print("Not enough length:")
        return prefix
    else:
        print("Not acceptable length:")
        return ""

# Test cases
print(longestCommonPrefix(['flower', 'flow', 'float']))
print(longestCommonPrefix([]))
print(longestCommonPrefix(['dog', 'cat', 'racecar']))
