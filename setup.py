#!/usr/bin/env python
from aiida import orm
from aiida.manage.tests import test_manager
from aiida.cmdline.commands import cmd_computer, cmd_code
import click
from click.testing import CliRunner
from glob import glob
import os
import ruamel.yaml as yaml
from jinja2 import Template

from jinja2 import Template

def render(template_file, **kwargs):
    """Produce yaml file from template.

    :param template_file: name of template file
    :param kwargs: will be forwarded to jinja2.Template
    """
    with open(template_file, 'r') as handle:
        content = handle.read()

    template = Template(content)
    yml_content = template.render(**kwargs)
    yml_file = os.path.splitext(template_file)[0]+'.yml'
    with open(yml_file, 'w') as handle:
        handle.write(yml_content)

#@click.option('--AIIDA_PATH', default=os.getenv('AIIDA_PATH'), help='Number of greetings.')
#@click.option('--name', prompt='Your name',
#              help='The person to greet.')
#@click.option('--name', prompt='Your name',
#              help='The person to greet.')

THIS_DIR = os.path.dirname(os.path.realpath(__file__))

@click.command()
@click.option('--computer', type=click.Choice(['localhost', 'fidis', 'fidis-debug', 'gacrux']), prompt="Computer to set up:")
def setup(computer):
    """Set up a given computer & codes ."""

    cli_runner = CliRunner()

    computer_yml = 'setup/{c}/{c}.yml'.format(c=computer)
    print("Setting up {}".format(computer))

    if computer == 'localhost':
        work_dir = click.prompt('Work directory: ', default=os.getenv('AIIDA_PATH', '/tmp') + '/aiida_run')
        codes_dir = click.prompt('Codes directory: ', default=THIS_DIR)
        render('setup/{c}/{c}.j2'.format(c=computer), work_dir=work_dir)

    options = ['--config', computer_yml]
    result = cli_runner.invoke(cmd_computer.computer_setup, options)
    print(result)

    for code_yml in glob('setup/{c}/*@*'.format(c=computer)):
        if computer == 'localhost':
            render(code_yml, work_dir=work_dir, codes_dir=codes_dir)
            code_yml = os.path.splitext(code_yml)[0]+'.yml'

        print("Setting up {}".format(code_yml))
        options = ['--config', code_yml]
        result = cli_runner.invoke(cmd_code.setup_code, options)
        print(result)

if __name__ == '__main__':
    setup()
