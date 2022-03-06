run-cms:
	cd cms && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run

setup-cms:
	cd cms && python setup.py bdist_wheel --universal