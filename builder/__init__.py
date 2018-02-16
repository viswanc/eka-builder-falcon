r"""
Falcon REST server builder for Eka.
"""

__plugin_name__ = 'falcon'
__keywords__ = 'Falcon REST server'
__author__ = 'Viswanath Chidambaram'
__email__ = 'viswanc@thoughtworks.com'
__version__ = '0.0.1'

def build(Data):
  from os import mkdir
  from os.path import dirname

  from eka.classes.builders.jinja import jinjaBuilder
  from eka.helpers import createTempDir, readFile, writeFile

  buildTgt = createTempDir()
  buildSrc = dirname(__file__)

  from shutil import copytree
  copytree('%s/res' % buildSrc, '%s/res' % buildTgt)
  mkdir('%s/src' % buildTgt)

  writeFile('%s/src/main.py' % buildTgt, jinjaBuilder().build(readFile('%s/main.jinja' % buildSrc), Data))

  return buildTgt
