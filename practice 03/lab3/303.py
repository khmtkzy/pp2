def is_triplet_calc():
    s = input().strip()

    word_to_digit = {
        "ZER": "0", "ONE": "1", "TWO": "2", "THR": "3", "FOU": "4",
        "FIV": "5", "SIX": "6", "SEV": "7", "EIG": "8", "NIN": "9"
    }

    digit_to_word = {v: k for k, v in word_to_digit.items()}

    for op in "+-*":
        if op in s:
            operator = op
            break

    left, right = s.split(operator)

    def convert(part):
        num = ""
        for i in range(0, len(part), 3):
            num += word_to_digit[part[i:i+3]]
        return int(num)

    a = convert(left)
    b = convert(right)

    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    else:
        result = a * b

    answer = ""
    for d in str(result):
        answer += digit_to_word[d]

    print(answer)


is_triplet_calc()
