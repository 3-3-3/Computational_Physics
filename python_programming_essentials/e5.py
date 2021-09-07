def volume(h):
    if h > 10:
        return f'invalid height {h}'
    elif h > 6:
        v = 6*8 + 12*(h-6)
    else:
        v = 6*h

    return f'your height is: {v}'

if __name__ == '__main__':
    h = float(input("What height?"))
    print(volume(h))
