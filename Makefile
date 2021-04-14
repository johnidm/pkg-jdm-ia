install:
	@pip install -r requirements-dev.txt

setup:
	@python setup.py install

clean:
	@rm -rf dist/
	@rm -rf build/
	@rm -rf *.egg-info/

pip:
	@pip install -e .