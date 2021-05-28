T = True
N = False


def function(a, b, index):
    if index < 1 or index > 16:
        index = 1

    if index == 1:
        # return false
        return N
    elif index == 2:
        # return a and b
        if a:
            if b:
                return True
            else:
                return False
        else:
            return False
    elif index == 3:
        # return a and not b
        if a:
            if b:
                return False
            else:
                return True
        else:
            return False
    elif index == 4:
        # return a
        return a
    elif index == 5:
        # return not a and b
        if a:
            return False
        else:
            if b:
                return True
            else:
                return False
    elif index == 6:
        # return b
        return b
    elif index == 7:
        # return (not a and b) or (a and not b)
        if a:
            if b:
                return False
            else:
                return True
        else:
            if b:
                return True
            else:
                return False
    elif index == 8:
        # return a or b
        if a:
            return True
        else:
            if b:
                return True
            else:
                return False
    elif index == 9:
        # return not (a or b)
        if a:
            return False
        else:
            if b:
                return False
            else:
                return True
    elif index == 10:
        # return (a and b) or (not a and not b)
        if a:
            if b:
                return True
            else:
                return False
        else:
            if b:
                return False
            else:
                return True
    elif index == 11:
        # return not b
        if b:
            return False
        else:
            return True
    elif index == 12:
        # return a or not b
        if a:
            return True
        else:
            if b:
                return False
            else:
                return True
    elif index == 13:
        # return not a
        if a:
            return False
        else:
            return True
    elif index == 14:
        # return not a or b
        if a:
            if b:
                return True
            else:
                return False
        else:
            return True
    elif index == 15:
        # return not (a and b)
        if a:
            if b:
                return False
            else:
                return True
        else:
            return True
    elif index == 16:
        # return True
        return T
