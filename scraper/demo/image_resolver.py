def parse_url(url):
	parsed = None
	if url.endswith('.jpg'):
		parsed = url
	elif 'imgur.com' in url:
		if '/a/' not in url and '/gallery/' not in url:
			parsed = 'http://i.imgur.com/{id}.jpg'.format(id=url.split('/')[-1])

	return parsed