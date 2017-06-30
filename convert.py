"""Convert templates and configuration file into production HTML files."""

import configparser
import jinja2
import os.path
import argparse

# Directory to output all files in
OUT_DIRECTORY = 'dist'

# Directory containing all templates
TEMPLATE_DIRECTORY = './templates'

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('language', metavar='L', type=str,
                    help='Which configuration file did you update? "en" or "ch"')
args = parser.parse_args()

try:
    os.mkdir(OUT_DIRECTORY)
    os.mkdir(os.path.join(OUT_DIRECTORY, args.language))
except FileExistsError:
    pass

config = configparser.ConfigParser()
config.read(args.language + '.config')
env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIRECTORY))

assert args.language in ('en', 'ch'), 'Language must be one of ("en", "ch")'

for filename, context in config.items():
    if not filename.endswith('html'):
        continue
    source_path = os.path.join(TEMPLATE_DIRECTORY, filename)
    out_path = os.path.join(OUT_DIRECTORY, args.language, filename)
    with open(out_path, 'w') as f:
        f.write(env.get_template(filename).render(context))
