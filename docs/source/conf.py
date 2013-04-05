import sys, os

sys.path.insert(0, os.path.abspath('../../xnt'))

import xnt.version

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.todo',
              'sphinx.ext.coverage',
              'sphinx.ext.intersphinx']

templates_path = []

source_suffix = '.rst'

master_doc = 'index'

project = u'Xnt'
copyright = u'2013, Kenny Ballou'

version = '.'.join(map(str, xnt.version.__version_info__[:2]))
release = xnt.version.__version__

exclude_patterns = []

pygments_style = 'sphinx'

html_theme = 'default'

html_static_path = []

htmlhelp_basename = 'Xntdoc'


latex_elements = {
}

latex_documents = [
  ('index', 'Xnt.tex', u'Xnt Documentation',
   u'Kenny Ballou', 'manual'),
]

man_pages = [
    ('index', 'xnt', u'Xnt Documentation',
     [u'Kenny Ballou'], 1)
]
texinfo_documents = [
  ('index', 'Xnt', u'Xnt Documentation',
   u'Kenny Ballou', 'Xnt', 'A wrapper build tool',
   'Miscellaneous'),
]
