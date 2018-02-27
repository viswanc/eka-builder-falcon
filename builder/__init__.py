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
    from os.path import dirname
    from eka.classes.builders.jinja import jinjaBuilder

    Structure = self.Structure
    buildTgt = Structure['buildBase']
    buildSrc = dirname(__file__)

    return jinjaBuilder().build(buildSrc, buildTgt, Structure)
