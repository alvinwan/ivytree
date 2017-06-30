"""Convert templates and configuration file into production HTML files."""

import ConfigParser
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
except:
    pass

config = ConfigParser.ConfigParser()
config.read(args.language + '.config')
env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIRECTORY))

assert args.language in ('en', 'ch'), 'Language must be one of ("en", "ch")'

global_context = dict(config.items('DEFAULT'))
for filename in config.sections():
    context = dict(config.items(filename))
    if not filename.endswith('html'):
        continue
    source_path = os.path.join(TEMPLATE_DIRECTORY, filename)
    out_path = os.path.join(OUT_DIRECTORY, args.language, filename)
    local_context = global_context.copy()
    local_context.update(context)
    with open(out_path, 'w') as f:
        f.write(env.get_template(filename).render(local_context))
