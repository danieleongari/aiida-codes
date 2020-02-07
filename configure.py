#!/usr/bin/env python
from aiida.cmdline.commands import cmd_computer, cmd_code
import click
from click.testing import CliRunner
from glob import glob
import os
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

def print_success(result):
    if not result.exit_code == 0:
        click.secho(result.output, fg='red')
    else:
        click.secho('Sucess', fg='green')

THIS_DIR = os.path.dirname(os.path.realpath(__file__))
SETUP_DIR = os.path.join(THIS_DIR, 'setup')

local_computers =  ['localhost_macosx15', 'localhost_ubu18', 'fidis', 'localhost_workhorse']

remote_computers = ['fidis', 'fidis-debug', 'fidis-s6g1', 'deneb-serial', 'workhorse']

all_computers = local_computers + remote_computers

@click.command()
@click.option('--computer', type=click.Choice(all_computers), prompt="Computer to set up")
def setup(computer):
    """Set up a given computer & codes."""

    cli_runner = CliRunner()

    # computer setup
    computer_yml = SETUP_DIR + '/{c}/{c}.yml'.format(c=computer)
    print("Setting up {}".format(computer))

    if computer in local_computers:
        computer_yml = SETUP_DIR + '/{}/localhost.yml'.format(computer)
        work_dir = click.prompt('Work directory', default=os.getenv('AIIDA_PATH', '/tmp') + '/aiida_run')
        render(SETUP_DIR + '/{}/localhost.j2'.format(computer), work_dir=work_dir)
    else:
        username = click.prompt('{} user name'.format(computer))
        ssh_key = click.prompt('Path to SSH key', default="{}/.ssh/id_rsa".format(os.path.expanduser("~")))
        computer_yml = SETUP_DIR + '/{c}/{c}.yml'.format(c=computer)

    options = ['--config', computer_yml]
    result = cli_runner.invoke(cmd_computer.computer_setup, options)
    print_success(result)

    print("Configuring {}".format(computer))

    if computer in local_computers:
        options = ['local', 'localhost', '--non-interactive', '--safe-interval', 0]
    else:
        options = ['ssh', computer, '--username', username, '--safe-interval', 10, '--look-for-keys',
                   '--key-policy', 'AutoAddPolicy', '--non-interactive', '--key-filename', ssh_key]
    result = cli_runner.invoke(cmd_computer.computer_configure, options)
    print_success(result)

    for code_yml in glob(SETUP_DIR + '/{c}/*@*'.format(c=computer)):
        # code setup
        if computer[:9] == 'localhost':
            if code_yml.split(".")[-1] == "j2":
                render(code_yml, work_dir=work_dir, codes_dir=THIS_DIR)
                code_yml = os.path.splitext(code_yml)[0]+'.yml'
            else:
                continue # to avoid old yaml

        print("Setting up {}".format(code_yml))
        options = ['--config', code_yml]
        result = cli_runner.invoke(cmd_code.setup_code, options)
        print_success(result)


if __name__ == '__main__':
    setup()
