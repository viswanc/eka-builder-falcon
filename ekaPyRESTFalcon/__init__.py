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
CrudApp = getPluginClass('crud.app')

# Data
builderClass = 'python.crud.app'

# Plugin
@define(__plugin_name__)
class Falcon(CrudApp):
  def __init__(self, Structure, Scopes):
    CrudApp.__init__(self, Structure, Scopes)

  def build(self):
    from os.path import dirname
    from eka.classes.builders.jinja import jinjaBuilder

    Structure = self.Structure
    buildTgt = Structure['buildBase']
    buildSrc = '%s/res' % dirname(__file__)
    builtPath = jinjaBuilder().build(buildSrc, buildTgt, Structure)

    # Build the CRUD App
    Structure['buildBase'] = '%s/src/crud' % builtPath
    getPluginClass(builderClass)(self.Structure, self.Scopes).build()
    Structure['buildBase'] = buildTgt

    return builtPath
