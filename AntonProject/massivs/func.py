import scipy


def massivs(a, b, c, d):

    w = scipy.array([[a, b], [c, d]])
    return scipy.fliplr(w)
