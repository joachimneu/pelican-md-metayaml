pelican-md-yaml
===============

This [Pelican](https://github.com/getpelican/pelican) plugin adds a reader for Markdown files with [YAML](https://en.wikipedia.org/wiki/YAML) metadata.
As the well-known static site generator [Jekyll](https://github.com/jekyll/jekyll) uses Markdown files with YAML metadata, this eases migration from Jekyll to Pelican.
Also, YAML metadata allows for easier specification of more complex metadata, such as nested lists or dictionaries.

Installation
------------

Copy the `md_yaml` directory to the `plugins` directory of your Pelican project (or whatever directory you specified for plugins in Pelican's `PLUGIN_PATHS` setting) and add
`'md_yaml'` to the list of plugins (Pelican setting `PLUGINS`) of your project.

Usage
-----

All your Markdown files (ending in `.md`, `.markdown`, `.mkd` and `.mdown`) will now be interpreted as using YAML for their metadata.
The following example shows a very simple article (only one line of text at the bottom) but with quite complex metadata (everything between the `---`):

```
---
template: article_recipe
title: Tiramisù
components:
  - name: Tiramisù
    for: 10
    ingredients:
     - - 4
       - eggs
     - - 150g
       - sugar
     - - 10 small cups
       - espresso
     - - 500g
       - mascarpone
     - - 1 package
       - ladyfingers
    steps:
     - Cook the espresso, pour it into a soup plate.
     - Separate the eggs very carefully.
     - Add very little salt to the egg white.
     - Blend egg yolk and sugar and mix it extensively for some minutes using a mixer, until you obtain a homogenous mass.
     - Add mascarpone and mix again very extensively.
     - Beat the egg white and fold it into the other mass.
     - Construct the tiramisù: First a layer of cream, then a layer of ladyfingers dipped into espresso, cream, ladyfingers, ..., cream. Sprinkle with cacao.
     - Put the tiramisù into the fridge for about a night, serve cold!
---

Thank you Silvia for the recipe!
```

Warranty
--------

No warranty whatsoever is provided for either the code or the recipe provided above! ;) Use only at your own risk!

References
----------

* This Pelican plugin uses the Markdown extension `mdx_meta_yaml` found here: <https://github.com/teoric/python-markdown-yaml-meta-data>
* The Pelican plugin `markdown-pullquote` was used as an example for a Pelican plugin providing a Markdown extension and can be found here: <https://github.com/arocks/markdown-pullquote>
* A similar approach to YAML metadata in Markdown files can be found here: <http://ianbarton.net/posts/2013/Apr/06/blogging-with-emacs-org-mode-and-pelican/>
