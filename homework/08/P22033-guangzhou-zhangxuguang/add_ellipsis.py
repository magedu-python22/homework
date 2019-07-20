
"""
第一版：我们接到一个需求：有一个列表，里面装着很多用户评论，为了在页面正常展示，需要将所有超过一定长度(10个字符)的评论用省略号替代,
请写出 一个add_ellipsis 函数方法来实现

第二版:我们接到一个需求：有一个列表，里面装着很多用户评论，为了在页面正常展示，需要将所有超过一定长度的评论用省略号替代，
如果有一天，我们拿到的评论不再是被继续装在列表里，而是在不可变的元组里呢？
请写出 一个add_ellipsis 函数方法来实现
"""
# 第一版
comments = [
    "Implementation note",
    "Changed",
    "ABC for generator",
]


def add_ellipsis():
    for i, comment in enumerate(comments):
        if len(comment) > 10:
            comment = comment[:9] + '...'
            comments[i] = comment
    return comments

print(add_ellipsis())


# 第二版
comments2 = (
    "Implementation note",
    "Changed",
    "ABC for generator",
)


def add_ellipsis2(temp=[]):
    for comment in comments2:
        if len(comment) > 10:
            comment = comment[:9] + '...'
        temp.append(comment)
    return tuple(temp)


print(add_ellipsis2())