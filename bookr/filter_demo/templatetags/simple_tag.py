from django import template

register = template.Library()

@register.simple_tag
def greet_user(message, username):
    return "{greeting_meesage}, {user}!!!".format(greeting_meesage= message, user=username)