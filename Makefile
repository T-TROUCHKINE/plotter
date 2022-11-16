package:
	python setup.py sdist bdist_wheel

upload: clean package
	twine upload dist/*

pdf-readme:
	pandoc README.md -o README.pdf

html-readme:
	pandoc -s README.md -o README.html

clean:
	rm -rf *.pdf
	rm -rf __pycache__
	rm -rf dist
	rm -rf MANIFEST
	rm -rf build
	rm -rf *.egg-info
	rm -rf doc/_site
	rm -rf README.pdf
	rm -rf README.html
