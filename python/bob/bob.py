def response(hey_bob):
    hey_bob = hey_bob.rstrip()
    if not hey_bob:
        return "Fine. Be that way!"
    if hey_bob.isupper():
        if hey_bob.endswith('?'):
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    if hey_bob.endswith('?'):
        return "Sure."
    return "Whatever."
