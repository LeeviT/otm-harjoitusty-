from pybuilder.core import use_plugin, init
#from structures.quadtree import main

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "nbodysim"
default_task = "publish"


@init
def set_properties(project):
    project.set_property("dir_source_main_python",'src/')
    project.set_property("coverage_break_build", False)
