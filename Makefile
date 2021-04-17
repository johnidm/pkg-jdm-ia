install:
	@pip install -r requirements-dev.txt

pip:
	@pip install -e .

test:
	pytest .
	
notebook:
	@jupyter notebook --notebook-dir=notebooks


lint:
	black --check .


lintf:
	black .
