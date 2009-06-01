try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

from bibo import __version__

setup(name="PyBibo",
      version=__version__,
      description="rdf-object mapping for BIBO",
      long_description="""\
This is an RDF-Python object mapping for the Bibliographic 
Ontology (BIBO). It provides the core classes and attributes 
in the model, and some related stuff.
""",
      author="Bruce D'Arcus",
      author_email="bdarcus@gmail.com",
      url="http://github.com/bdarcus/py-bibo",
      packages=find_packages(exclude='tests'),
      install_requires=['RDFAlchemy>=0.2b2'],
      )

