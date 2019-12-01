# comments = [
#     "Implementation note",
#     "Changed",
#     "ABC for generator",
# ]
comments = (
    "Implementation note",
    "Changed",
    "ABC for generator",
)
c = tuple(comments)
def add_ellipsis(com):
    if isinstance(com, tuple):
        com = list(com)
    for num, i in enumerate(com):
        if len(i) > 10:
            com[num] = com[num][0:10] + '...'
    return com



# add_ellipsis(comments)
# print(comments)
if isinstance(c, tuple):
    c = tuple(add_ellipsis(c))
else:
    add_ellipsis(c)
print(c)
