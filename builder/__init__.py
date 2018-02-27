r"""
Falcon REST server builder for Eka.
"""

# Meta
__plugin_name__ = 'rest.server.falcon'
__keywords__ = 'Falcon REST server'
__author__ = 'Viswanath Chidambaram'
__email__ = 'viswanc@thoughtworks.com'
__version__ = '0.0.1'

# Imports
from eka.plugins import define, getPluginClass
RestServer = getPluginClass('rest.server')

# Plugin
@define(__plugin_name__)
class Falcon(RestServer):
  def __init__(self, Structure, Scopes):
    RestServer.__init__(self, Structure, Scopes)

  def build(self):
    from os import mkdir
    from os.path import dirname

    from eka.classes.builders.jinja import jinjaBuilder
    from eka.helpers import createTempDir, readFile, writeFile

    buildTgt = createTempDir()
    buildSrc = dirname(__file__)

    from shutil import copytree
    copytree('%s/res' % buildSrc, '%s/res' % buildTgt)
    mkdir('%s/src' % buildTgt)

    writeFile('%s/src/main.py' % buildTgt, jinjaBuilder().build(readFile('%s/main.jinja' % buildSrc), self.Structure))

    return buildTgt
