version ?= latest
IMAGE = leocbs/globocomtrends:$(version)

image: 
	docker build -t $(IMAGE) .

check: image
	docker run --rm $(IMAGE) python globocomtrends/tests/test_parse_item.py

