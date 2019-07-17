'''第一版：我们接到一个需求：
有一个列表，里面装着很多用户评论，为了在页面正常展示，
需要将所有超过一定长度(10个字符)的评论用省略号替代,
请写出 一个add_ellipsis 函数方法来实现
第二版:如果评论不再是被装在列表里，而是在不可变的元组里呢？'''

c1 = [
    "Implementation note",
    "Changed",
    "ABC for generator",
]

def add_ellipsis(comments, n=10):
    for i, comment in enumerate(comments):
        if len(comment) > n:
            comments[i] = comment[:n] + '...'
    return comments


print(add_ellipsis(c1))

c2 =(
    "Implementation note",
    "Changed",
    "ABC for generator",
)


def add_ellipsis2(comments, n=10):
    for i, comment in enumerate(comments):
        if len(comment) > n:
            yield comment[:n] + '...'
        else:
            yield comment


print(tuple(add_ellipsis2(c2)))