from django import template

register = template.Library()

@register.filter

def get_at_index(l, i):
	try:
		return l[i]
	except:
		return None