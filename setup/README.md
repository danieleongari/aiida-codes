# To [install a new computer](https://aiida-core.readthedocs.io/en/latest/get_started/computers.html):

## generate ssh keypair

If you haven't done so already, you need to generate a ssh keypair using `ssh-keygen -t rsa` and `ssh-copy-id username@remote`.
More detailed instructions are [in the AiiDA documentation](https://aiida-core.readthedocs.io/en/latest/get_started/computers.html).

## setup computer
```
verdi computer setup --config computer_{computer}.yml
```

## configure computer

```
verdi computer configure ssh {computer}
```

```
Info: enter "?" for help
User name [daniele]: ongari
port Nr [22]:
Look for keys [False]: False #BUG: also using True asks for it!
SSH key file []: /home/daniele/.ssh/id_rsa
Connection timeout in s [60]:
Allow ssh agent [False]:
SSH proxy command []:
Compress file transfers [True]:
GSS auth [False]:
GSS kex [False]:
GSS deleg_creds [False]:
GSS host [fidis.epfl.ch]:
Load system host keys [True]:
Key policy (RejectPolicy, WarningPolicy, AutoAddPolicy) [RejectPolicy]: AutoAddPolicy
Connection cooldown time (s) [5]:
```

## test computer

```
verdi computer test {computer}
```

# To [install a new code](https://aiida-core.readthedocs.io/en/latest/get_started/codes.html), run:

## Install the plugin
Typically you do:
```
pip install aiida-{code}
```
or
```
git clone https://github.com/{aiidateam}/aiida-{code}
cd aiida-{code}
pip install -e .
```
Update your entrypoints and check that the new calculation has been added:
```
reentry scan
verdi plugin list aiida.calculations
```

## Setup the code
Check the path of the code, you can have access to the executable on clusters, but on localhost you need to adapt the path!

Adapt the yml and then use it:
```
verdi code setup --config {code}@{computer}.yml
```
