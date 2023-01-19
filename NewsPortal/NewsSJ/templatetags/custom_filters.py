from django import template

register = template.Library()

words = ['Leo', 'captain', 'place']


@register.filter()
def censor(value):
    value_split = value.split()
    i = -1
    for j in value_split:
        i += 1
        if j in words:
            for_len_j = (len(j) - 1) * '*'
            j = j.replace(j[1:], for_len_j)
            value_split[i] = j
    return f'{" ".join(value_split)}'
