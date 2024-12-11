install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black library/main.py

lint:
	ruff check library/main.py

test:
	python -m pytest -vv --nbval --cov=library --cov=main test_*.py

all: install format lint test