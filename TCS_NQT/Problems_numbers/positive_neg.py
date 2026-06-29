def pos_neg(n):
    if n < 0:
        return ' Negative'
    elif n > 0:
        return 'Positive'
    else:
        return None
n = -12354
print(pos_neg(n))