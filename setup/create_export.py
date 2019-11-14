#!/usr/bin/env python
from aiida import orm
from aiida.manage.tests import test_manager
from aiida.cmdline.commands import cmd_computer, cmd_code
from aiida.tools.importexport import export_zip
from click.testing import CliRunner
from glob import glob
import os

print("Setting up test profile")

export_file = "export.aiida"
try:
    os.remove(export_file)
except OSError:
    pass

with test_manager() as test_mgr:
    cli_runner = CliRunner()

    for computer in ['fidis', 'deneb']:
        computer_yml = '{c}/{c}.yml'.format(c=computer)
        print("Setting up {}".format(computer))
        options = ['--config', computer_yml]
        result = cli_runner.invoke(cmd_computer.computer_setup, options)
        print(result)

        for code_yml in glob('{c}/*@*.yml'.format(c=computer)):
            print("Setting up {}".format(code_yml))
            options = ['--config', code_yml]
            result = cli_runner.invoke(cmd_code.setup_code, options)
            print(result)

    computers = orm.QueryBuilder().append(orm.Code).all()
    codes = orm.QueryBuilder().append(orm.Code).all()
    flat_list = [ item for sublist in computers+codes for item in sublist]

    print("Exporting to {}".format(export_file))
    export_zip(flat_list, outfile=export_file)

#    yield fixture_mgr

#print("Creating profile {}".format(profile))
#sys.call("verdi quicksetup
