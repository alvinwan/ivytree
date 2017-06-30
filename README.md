# IvyTree Website

Whoa, how do I run this thing? Start by installing below. Then, see `editing` and `deploying` instructions for updating the website.

# Installation

First, we want to clone the repository locally. Open your "Terminal" app on the Mac, and type in the following.

```
git clone https://github.com/alvinwan/ivytree.git
```

Start by changing your directory into the repository root.

```
cd ivytree
```

We need to install dependencies in Python. The following installs all requirements listed in `requirements.txt`.

```
pip install -r requirements.txt
```

# Editing

Edit `en.config` or `ch.config` to change content. Then, run the Python script to regenerate the website. The following regenerates the English version of the website.

```
python convert.py en
```

Use `python convert.py ch` to generate the Chinese version of the website. To preview your website, change into the generated files directory, and launch a mini server.

```
cd dist
python -m http.server
```

Once you see the following, your local website preview has been launched.

```
Serving HTTP on 0.0.0.0 port 8000 ...
...
```

Then, access `localhost:8000` in your browser. You should see your browser preview. Verify that everything looks as you planned.

If you are making more edits, make sure to go back to the correct directory, with the config files in it. To do this, run the following to "go back".

```
cd ..
```

# Deploying

Run `make deploy m="some message here"` to deploy. You can refresh the website immediately, but changes usually take 30-60 seconds.
