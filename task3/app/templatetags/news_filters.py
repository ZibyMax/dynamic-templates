from django import template
from time import time
from datetime import datetime

register = template.Library()


@register.filter
def format_date(value):
    now = time()
    ten_minutes = 60 * 10
    if now - value < ten_minutes:
        return 'только что'

    one_hour = 60 * 60
    one_day = 60 * 60 * 24
    if now - value < one_day:
        return f'{int(now - value) // one_hour} часов назад'

    date = datetime.fromtimestamp(value)
    return date.strftime('%Y-%m-%d')


@register.filter
def score(value):
    if value < -5:
        return 'все плохо'
    if value > 5:
        return 'хорошо'
    return 'нейтрально'


@register.filter
def format_num_comments(value):
    if value == 0:
        return 'Оставьте комментарий'
    if value > 50:
        return '50+'
    return value


@register.filter
def format_selftext(value, count):
    if value:
        end = value[-1] if value[-1] in ['.', '!', '?'] else ''
        text = ''.join(x for x in value if x.isalpha() or x == " ")
        words = text.strip().split(' ')
        if len(words) > count * 2:
            return ' '.join(words[:count]) + ' ... ' + ' '.join(words[len(words) - count:]) + end
        else:
            return ' '.join(words) + end
    return value
