"""Convert templates and configuration file into production HTML files."""

import configparser
import jinja2
import os.path

# Which language to run for
LANGUAGE = 'en'
assert LANGUAGE in ('en', 'ch')

# Directory to output all files in
OUT_DIRECTORY = os.path.join('dist', LANGUAGE)

try:
    os.mkdir(OUT_DIRECTORY)
except FileExistsError:
    pass

# Directory containing all templates
TEMPLATE_DIRECTORY = './templates'

config = configparser.ConfigParser()
config.read(LANGUAGE + '.config')
env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIRECTORY))


for filename, context in config.items():
    if not filename.endswith('html'):
        continue
    source_path = os.path.join(TEMPLATE_DIRECTORY, filename)
    out_path = os.path.join(OUT_DIRECTORY, filename)
    with open(out_path, 'w') as f:
        f.write(env.get_template(filename).render(context))
