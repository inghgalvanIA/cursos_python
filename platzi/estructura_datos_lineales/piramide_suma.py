def piramide_suma (lim_bajo,lim_alta, margin=0):
    blanks = " " * margin
    print(blanks,lim_bajo,lim_alta)
    if lim_bajo > lim_alta:
        print(blanks,0)
        return 0
    else:
        result = lim_bajo + piramide_suma(lim_bajo + 1, lim_alta, margin + 4)
        print(blanks, result)
        return result

piramide_suma(1,4)