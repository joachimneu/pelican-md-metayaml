# -*- coding: utf-8 -*-

from mdx_meta_yaml.extension import MetaYamlExtension

def makeExtension(configs=None):
	if isinstance(configs, list):
		configs = dict(configs)
        elif configs is None:
		configs  = {}
	return MetaYamlExtension(configs=configs)
