def mensaje(nombres, precio, metacritic):
    msg = "DESCUENTOS...\n"
    for p in zip(nombres, precio, metacritic):
        msg += p[0].text.lstrip().rstrip() + "\n"
        msg += p[1].text.replace('\n',' ').lstrip() + "\n"
        msg += p[2].text.replace('\n','') + "\n"
        msg += "---------------------------\n"
    return msg
