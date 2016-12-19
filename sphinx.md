# Sphinx

Notes on using Sphinx for technical documentation and PDF creation. All
commands and examples are based on macOS. More information about Sphinx is
available at http://www.sphinx-doc.org

## Installation and Getting Started

Procedures for installing Sphinx and getting a basic project started are
described in this section.

Sphinx can be installed using pip or as part of the
[Anaconda](https://www.continuum.io/downloads) distribution.

```bash
pip install Sphinx
```

After installing Sphinx, the quickstart script will create a basic project
template for the documentation. Run the script in the directory that will
contain the documentation, then follow the on screen instructions to configure
the project.

```bash
sphinx-quickstart
```

## Themes

The theme used by readthedocs.org is available on GitHub at
[snide/sphinx_rtd_theme](https://github.com/snide/sphinx_rtd_theme). To install
the theme, copy the files in `sphinx_rtd_theme/sphinx_rtd_theme` into a folder
such as `_themes` then edit the `conf.py` file to use the new theme.

```bash
html_theme = 'sphinx_rtd_theme'
html_theme_path = ['_themes']
```

## PDF

This section provides examples of creating a PDF from the Sphinx documentation.

When creating a PDF with Sphinx, make sure the following Latex packages are
installed by using the `tlmgr` package manager:

```bash
tlmgr install titlesec framed threeparttable wrapfig multirow collection-fontsrecommended
```

