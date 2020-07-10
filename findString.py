from collections import Counter

def count_substring(string, sub_string):
    total = Counter([string[i :i+len(sub_string)] for i in range(len(string))])
    return total[sub_string]

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
