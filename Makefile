.PHONY: deploy update

# usage: make deploy m="commit message"
deploy:
	git pull
	rm -rf published
	gulp global_json
	gulp preview
	git add .
	git commit -m "deploy: $(m)" --allow-empty
	git push
	make update

# Pushes the published folder to gh-pages to update the staging webpage.
update:
	git push origin `git subtree split --prefix dist master`:gh-pages --force
	git subtree split --rejoin --prefix=dist master
