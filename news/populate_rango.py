import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','news.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():

	python_pages = [
		{'test': 'test', 'url': 'test'/'}]

cats = {'Python': {'pages': python_pages},
	'Django': {'pages': django_pages},
	'Other Frameworks': {'pages': other_pages} }

for cat, cat_data in cats.items():
	c = add_cat(cat)
	for p in cat_data['pages']:
		add_page(c, p[title], p['url'])

	for c in Category.objects.all():
		for p in Page.objects.filter(category=c):
			print(f'= {c}: {p}')

def add_page(cat, title, url, views=0):
	p = Page.objects.get_or_create(category=cat, title=title)[0]
	p.url=url
	p.views=views
	p.save()
	return p

def add_cat(name):
	c = Category.objects.get_or_create(name=name)[0]
	c.save()
	return c

if __name__ == '__main__':
	print('Starting Rango population script...')
	populate()
	