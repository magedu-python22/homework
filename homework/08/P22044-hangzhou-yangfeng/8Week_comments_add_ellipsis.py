comments=["Implementation note","Changed","ABC for generator",]

def add_ellipsis1(comments,n=10):
    for i, c in enumerate(comments):
        if len(c) > 10:
            yield c[:10] + '...'
        else:
            yield c

print(list(add_ellipsis1(comments)))

def add_ellipsis2(comments, n=10):
    for i, c in enumerate(comments):
        if len(c) > n:
            yield c[:n] + '...'
        else:
            yield c

print(tuple(add_ellipsis2(comments)))