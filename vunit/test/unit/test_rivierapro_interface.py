# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2014-2019, Lars Asplund lars.anders.asplund@gmail.com

"""
Test the RivieraPro interface
"""


import unittest
from os.path import join, dirname, exists
import os
from shutil import rmtree
from vunit.rivierapro_interface import RivieraProInterface
from vunit.test.mock_2or3 import mock
from vunit.project import Project
from vunit.ostools import renew_path, write_file


class TestRivieraProInterface(unittest.TestCase):
    """
    Test the RivieraPro interface
    """

    @mock.patch("vunit.simulator_interface.check_output", autospec=True, return_value="")
    @mock.patch("vunit.rivierapro_interface.Process", autospec=True)
    def test_compile_project_vhdl_2019(self, process, check_output):
        simif = RivieraProInterface(prefix="prefix",
                                    output_path=self.output_path)
        project = Project()
        project.add_library("lib", "lib_path")
        write_file("file.vhd", "")
        project.add_source_file("file.vhd", "lib", file_type="vhdl", vhdl_standard="2019")
        simif.compile_project(project)
        process.assert_any_call([join("prefix", "vlib"), "lib", "lib_path"],
                                cwd=self.output_path, env=simif.get_env())
        process.assert_called_with([join("prefix", "vmap"), "lib", "lib_path"],
                                   cwd=self.output_path, env=simif.get_env())
        check_output.assert_called_once_with(
            [join('prefix', 'vcom'),
             '-quiet',
             '-j',
             self.output_path,
             '-2018',
             '-work',
             'lib',
             'file.vhd'], env=simif.get_env())

    @mock.patch("vunit.simulator_interface.check_output", autospec=True, return_value="")
    @mock.patch("vunit.rivierapro_interface.Process", autospec=True)
    def test_compile_project_vhdl_2008(self, process, check_output):
        simif = RivieraProInterface(prefix="prefix",
                                    output_path=self.output_path)
        project = Project()
        project.add_library("lib", "lib_path")
        write_file("file.vhd", "")
        project.add_source_file("file.vhd", "lib", file_type="vhdl", vhdl_standard="2008")
        simif.compile_project(project)
        process.assert_any_call([join("prefix", "vlib"), "lib", "lib_path"],
                                cwd=self.output_path, env=simif.get_env())
        process.assert_called_with([join("prefix", "vmap"), "lib", "lib_path"],
                                   cwd=self.output_path, env=simif.get_env())
        check_output.assert_called_once_with(
            [join('prefix', 'vcom'),
             '-quiet',
             '-j',
             self.output_path,
             '-2008',
             '-work',
             'lib',
             'file.vhd'], env=simif.get_env())

    @mock.patch("vunit.simulator_interface.check_output", autospec=True, return_value="")
    @mock.patch("vunit.rivierapro_interface.Process", autospec=True)
    def test_compile_project_vhdl_2002(self, process, check_output):
        simif = RivieraProInterface(prefix="prefix",
                                    output_path=self.output_path)
        project = Project()
        project.add_library("lib", "lib_path")
        write_file("file.vhd", "")
        project.add_source_file("file.vhd", "lib", file_type="vhdl", vhdl_standard="2002")
        simif.compile_project(project)
        process.assert_any_call([join("prefix", "vlib"), "lib", "lib_path"],
                                cwd=self.output_path, env=simif.get_env())
        process.assert_called_with([join("prefix", "vmap"), "lib", "lib_path"],
                                   cwd=self.output_path, env=simif.get_env())
        check_output.assert_called_once_with(
            [join('prefix', 'vcom'),
             '-quiet',
             '-j',
             self.output_path,
             '-2002',
             '-work',
             'lib',
             'file.vhd'], env=simif.get_env())

    @mock.patch("vunit.simulator_interface.check_output", autospec=True, return_value="")
    @mock.patch("vunit.rivierapro_interface.Process", autospec=True)
    def test_compile_project_vhdl_93(self, process, check_output):
        simif = RivieraProInterface(prefix="prefix",
                                    output_path=self.output_path)
        project = Project()
        project.add_library("lib", "lib_path")
        write_file("file.vhd", "")
        project.add_source_file("file.vhd", "lib", file_type="vhdl", vhdl_standard="93")
        simif.compile_project(project)
        process.assert_any_call([join("prefix", "vlib"), "lib", "lib_path"],
                                cwd=self.output_path, env=simif.get_env())
        process.assert_called_with([join("prefix", "vmap"), "lib", "lib_path"],
                                   cwd=self.output_path, env=simif.get_env())
        check_output.assert_called_once_with(
            [join('prefix', 'vcom'),
             '-quiet',
             '-j',
             self.output_path,
             '-93',
             '-work',
             'lib',
             'file.vhd'], env=simif.get_env())

    @mock.patch("vunit.simulator_interface.check_output", autospec=True, return_value="")
    @mock.patch("vunit.rivierapro_interface.Process", autospec=True)
    def test_compile_project_vhdl_extra_flags(self, process, check_output):
        simif = RivieraProInterface(prefix="prefix",
                                    output_path=self.output_path)
        project = Project()
        project.add_library("lib", "lib_path")
        write_file("file.vhd", "")
        source_file = project.add_source_file("file.vhd", "lib", file_type="vhdl")
        source_file.set_compile_option("rivierapro.vcom_flags", ["custom", "flags"])
        simif.compile_project(project)
        process.assert_any_call([join("prefix", "vlib"), "lib", "lib_path"],
                                cwd=self.output_path, env=simif.get_env())
        process.assert_called_with([join("prefix", "vmap"), "lib", "lib_path"],
                                   cwd=self.output_path, env=simif.get_env())
        check_output.assert_called_once_with([join('prefix', 'vcom'),
                                              '-quiet',
                                              '-j',
                                              self.output_path,
                                              'custom',
                                              'flags',
                                              '-2008',
                                              '-work',
                                              'lib',
                                              'file.vhd'], env=simif.get_env())

    @mock.patch("vunit.simulator_interface.check_output", autospec=True, return_value="")
    @mock.patch("vunit.rivierapro_interface.Process", autospec=True)
    def test_compile_project_verilog(self, process, check_output):
        library_cfg = join(self.output_path, "library.cfg")
        simif = RivieraProInterface(prefix="prefix",
                                    output_path=self.output_path)
        project = Project()
        project.add_library("lib", "lib_path")
        write_file("file.v", "")
        project.add_source_file("file.v", "lib", file_type="verilog")
        simif.compile_project(project)
        process.assert_any_call([join("prefix", "vlib"), "lib", "lib_path"],
                                cwd=self.output_path, env=simif.get_env())
        process.assert_called_with([join("prefix", "vmap"), "lib", "lib_path"],
                                   cwd=self.output_path, env=simif.get_env())
        check_output.assert_called_once_with([join('prefix', 'vlog'),
                                              '-quiet',
                                              '-lc',
                                              library_cfg,
                                              '-work',
                                              'lib',
                                              'file.v',
                                              '-l', 'lib'],
                                             env=simif.get_env())

    @mock.patch("vunit.simulator_interface.check_output", autospec=True, return_value="")
    @mock.patch("vunit.rivierapro_interface.Process", autospec=True)
    def test_compile_project_system_verilog(self, process, check_output):
        library_cfg = join(self.output_path, "library.cfg")
        simif = RivieraProInterface(prefix="prefix",
                                    output_path=self.output_path)
        project = Project()
        project.add_library("lib", "lib_path")
        write_file("file.sv", "")
        project.add_source_file("file.sv", "lib", file_type="systemverilog")
        simif.compile_project(project)
        process.assert_any_call([join("prefix", "vlib"), "lib", "lib_path"],
                                cwd=self.output_path, env=simif.get_env())
        process.assert_called_with([join("prefix", "vmap"), "lib", "lib_path"],
                                   cwd=self.output_path, env=simif.get_env())
        check_output.assert_called_once_with([join('prefix', 'vlog'),
                                              '-quiet',
                                              '-lc',
                                              library_cfg,
                                              '-sv2k12',
                                              '-work',
                                              'lib',
                                              'file.sv',
                                              '-l', 'lib'],
                                             env=simif.get_env())

    @mock.patch("vunit.simulator_interface.check_output", autospec=True, return_value="")
    @mock.patch("vunit.rivierapro_interface.Process", autospec=True)
    def test_compile_project_verilog_extra_flags(self, process, check_output):
        library_cfg = join(self.output_path, "library.cfg")
        simif = RivieraProInterface(prefix="prefix",
                                    output_path=self.output_path)
        project = Project()
        project.add_library("lib", "lib_path")
        write_file("file.v", "")
        source_file = project.add_source_file("file.v", "lib", file_type="verilog")
        source_file.set_compile_option("rivierapro.vlog_flags", ["custom", "flags"])
        simif.compile_project(project)
        process.assert_any_call([join("prefix", "vlib"), "lib", "lib_path"],
                                cwd=self.output_path, env=simif.get_env())
        process.assert_called_with([join("prefix", "vmap"), "lib", "lib_path"],
                                   cwd=self.output_path, env=simif.get_env())
        check_output.assert_called_once_with([join('prefix', 'vlog'),
                                              '-quiet',
                                              '-lc',
                                              library_cfg,
                                              'custom',
                                              'flags',
                                              '-work',
                                              'lib',
                                              'file.v',
                                              '-l', 'lib'], env=simif.get_env())

    @mock.patch("vunit.simulator_interface.check_output", autospec=True, return_value="")
    @mock.patch("vunit.rivierapro_interface.Process", autospec=True)
    def test_compile_project_verilog_include(self, process, check_output):
        library_cfg = join(self.output_path, "library.cfg")
        simif = RivieraProInterface(prefix="prefix",
                                    output_path=self.output_path)
        project = Project()
        project.add_library("lib", "lib_path")
        write_file("file.v", "")
        project.add_source_file("file.v", "lib", file_type="verilog", include_dirs=["include"])
        simif.compile_project(project)
        process.assert_any_call([join("prefix", "vlib"), "lib", "lib_path"],
                                cwd=self.output_path, env=None)
        process.assert_called_with([join("prefix", "vmap"), "lib", "lib_path"],
                                   cwd=self.output_path, env=simif.get_env())
        check_output.assert_called_once_with([join('prefix', 'vlog'),
                                              '-quiet',
                                              '-lc',
                                              library_cfg,
                                              '-work',
                                              'lib',
                                              'file.v',
                                              '-l', 'lib',
                                              '+incdir+include'], env=simif.get_env())

    @mock.patch("vunit.simulator_interface.check_output", autospec=True, return_value="")
    @mock.patch("vunit.rivierapro_interface.Process", autospec=True)
    def test_compile_project_verilog_define(self, process, check_output):
        library_cfg = join(self.output_path, "library.cfg")
        simif = RivieraProInterface(prefix="prefix",
                                    output_path=self.output_path)
        project = Project()
        project.add_library("lib", "lib_path")
        write_file("file.v", "")
        project.add_source_file("file.v", "lib", file_type="verilog", defines={"defname": "defval"})
        simif.compile_project(project)
        process.assert_any_call([join("prefix", "vlib"), "lib", "lib_path"],
                                cwd=self.output_path, env=simif.get_env())
        process.assert_called_with([join("prefix", "vmap"), "lib", "lib_path"],
                                   cwd=self.output_path, env=simif.get_env())
        check_output.assert_called_once_with([join('prefix', 'vlog'),
                                              '-quiet',
                                              '-lc',
                                              library_cfg,
                                              '-work',
                                              'lib',
                                              'file.v',
                                              '-l', 'lib',
                                              '+define+defname=defval'], env=simif.get_env())

    def setUp(self):
        self.output_path = join(dirname(__file__), "test_rivierapro_out")
        renew_path(self.output_path)
        self.project = Project()
        self.cwd = os.getcwd()
        os.chdir(self.output_path)

    def tearDown(self):
        os.chdir(self.cwd)
        if exists(self.output_path):
            rmtree(self.output_path)
