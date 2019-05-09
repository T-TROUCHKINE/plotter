all: readme

readme:
	pandoc README.md -o README.pdf

clean:
	rm -rf *.pdf
	rm -rf __pycache__
	rm -rf dist
	rm -rf MANIFEST
	rm -rf build
	rm -rf *.egg-info
