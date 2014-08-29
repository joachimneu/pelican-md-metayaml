import sys
import os

from pelican import signals
from pelican.readers import BaseReader
from pelican.utils import pelican_open

try:
	from markdown import Markdown
except ImportError:
	Markdown = False

class MarkdownYAMLReader(BaseReader):
	"""Reader for Markdown files with YAML metadata"""

	enabled = bool(Markdown)
	file_extensions = ['md', 'markdown', 'mkd', 'mdown']

	def __init__(self, *args, **kwargs):
		super(MarkdownYAMLReader, self).__init__(*args, **kwargs)
		self.settings = args[0]
		self.extensions = list(self.settings['MD_EXTENSIONS'])
		if 'meta_yaml' not in self.extensions:
			self.extensions.append('meta_yaml')

	def _parse_metadata(self, meta):
		"""Return the dict containing document metadata"""

		output = {}
		for name, value in meta.items():
			name = name.lower()
			output[name] = value
		return output

	def read(self, source_path):
		"""Parse content and metadata of Markdown files with YAML metadata"""

		self.__set_plugin_path()

		self._md = Markdown(extensions=self.extensions)
		with pelican_open(source_path) as text:
			content = self._md.convert(text)
		metadata = self._parse_metadata(self._md.Meta)

		self.__unset_plugin_path()

		return content, metadata

	def __set_plugin_path(self):
		self.__sys_path_old = sys.path[:]
		for pluginpath in self.settings['PLUGIN_PATHS']:
			sys.path.insert(0, pluginpath)
			sys.path.insert(0, os.path.join(pluginpath, 'md_yaml'))

	def __unset_plugin_path(self):
		sys.path = self.__sys_path_old

def add_reader(readers):
	for k in MarkdownYAMLReader.file_extensions:
		readers.reader_classes[k] = MarkdownYAMLReader

def register():
	signals.readers_init.connect(add_reader)
