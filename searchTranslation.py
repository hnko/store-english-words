import webbrowser

FROM = 'english'
TO = 'spanish'
WEBSITE = 'https://dictionary.cambridge.org/dictionary/'+FROM+'-'+TO+'/'

def search_translation(word):
	"""
	open the cambridge dictionary and search an translation of the word passed
	:param: word we want to know the translation
	"""
	webbrowser.get('chrome').open(WEBSITE + word)
	

def config_language(from_, to):
	"""
	configurate the language translator
	:param: from_ the language we are writting, to the language we want the translation
	:return: True if the parameters are es or en. It accept just english and spanish
	"""
	global FROM, TO
	
	FROM = from_
	TO = to