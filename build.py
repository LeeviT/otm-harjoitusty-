from pybuilder.core import use_plugin, init, task, depends

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.coverage")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.sphinx")
use_plugin("python.distutils")

name = "nbodysim"
default_task = "publish"

@init
def set_properties(project):
    project.set_property("dir_source_unittest_python", "src/unittest/python")
    project.set_property("coverage_exceptions", ["__main__", "python/nbodysim_tests"])
    project.set_property("dir_source_main_python",'src/')
    project.set_property("coverage_branch_threshold_warn", 70)
    project.set_property("coverage_branch_partial_threshold_warn", 70)
    project.set_property("coverage_break_build", False)
    project.set_property("source_dist_ignore_patterns", ["*.pyc", ".hg*", ".svn", ".CVS", "unit*"])
