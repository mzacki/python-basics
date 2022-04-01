def parrot_trouble(trouble, hour):
    if trouble and (hour < 7 or hour > 20):
        return True
    else:
        return False
