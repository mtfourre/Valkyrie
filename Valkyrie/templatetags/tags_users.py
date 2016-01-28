from django import template
from Valkyrie.enums import *


register = template.Library()


@register.simple_tag
def entry_for_user_gender(dictionary):
    return Gender.Gender[int(dictionary.get("gender"))][1]
