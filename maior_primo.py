def maior_primo(n):
    def eh_primo(k):
        if k < 2:
            return False
        for i in range(2, int(k**0.5) + 1):
            if k % i == 0:
                return False
        return True

    for i in range(n, 1, -1):
        if eh_primo(i):
            return i