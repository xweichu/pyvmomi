# Copyright (c) 2018-2020 VMware, Inc.  All rights reserved.
# -- VMware Confidential
""" Python VMOMI tests

This module provides a place to add tests for pyVmomi.
Also, it can be used as a playground to experiment with new utilities.
"""

import os
import subprocess
import sys
import unittest

thisFile = os.path.realpath(__file__)

# The pyVmomi dir.
pyVmomiDir = os.path.dirname(thisFile)


'''
Commenting the test and its required imports because it requires a published
pyVmomi to run it and we want to run flake8 on the source code as part of these
tests.
Uncomment it when there is some clarity for the pyVmomi unittests.

# The pyVmomi package root.
pyVmomiPath = os.path.dirname(os.path.dirname(thisFile))

# The pyVmomi modules depend on six.py.
sixPath = os.path.join(os.environ.get("TCROOT", "/build/toolchain"), "noarch",
                       "six-1.9.0", "lib", "python2.7", "site-packages")

# Both of those enable the importing of pyVmomi.
sys.path.insert(0, pyVmomiPath)
sys.path.insert(0, sixPath)

import pyVmomi


class VersionTest(unittest.TestCase):
    """Test the version support for pyVmomi

    This class contains tests for various VMODL version uitilites.
    """
    def test_GetVersionProps(self):
        """GetVersionProps() doesn't crash"""

        for vmodlNamespace in ["vim", "vpx"]:
            ver = pyVmomi.VmomiSupport.ltsVersions.GetName(vmodlNamespace)

            self.assertTrue(
                pyVmomi.VmomiSupport.GetVersionProps(ver) is not None)
'''


class RunPythonTools(unittest.TestCase):
    """Run python sanitizing tools like flake8 and pylint

    Having those here allows to test every change with a single command.
    """

    def test_flake8(self):
        """Run flake8 on all nearby python sources"""

        flake8 = "/build/toolchain/noarch/flake8-2.2.5/bin/flake8"

        flake8Config = os.path.join(pyVmomiDir, "config", "setup.cfg")

        args = ["--config"]
        args.append(flake8Config)

        cmd = [flake8]
        cmd.extend(args)
        cmd.append(pyVmomiDir)

        subprocess.check_call(cmd)


if "__main__" == __name__:
    sys.exit(unittest.main())
