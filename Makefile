init:
	poetry install

install:
	rm -f ./poetry.lock
	poetry install

test:
	poetry run pytest --capture=no ./tests/test__ec2__stop_instance_by_tags.py
