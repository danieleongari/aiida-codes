# To install a new computer, run:

## generate ssh keypair 

If you haven't done so already, you need to generate a ssh keypair using `ssh-keygen -t rsa` and `ssh-copy-id username@remote`.
More detailed instructions are [one the AiiDA documentation](https://aiida-core.readthedocs.io/en/latest/get_started/computers.html).

## setup computer
```
cat {computer}.computer | verdi computer setup 
```

## configure computer

```
verdi computer configure {computer}
```

```
=> username = ongari
=> port = 22
=> look_for_keys = 
=> key_filename = 
=> timeout = 60
=> allow_agent = 
=> proxy_command = 
=> compress = True
=> gss_auth = False
=> gss_kex = False
=> gss_deleg_creds = False
=> gss_host = fidis.epfl.ch
=> load_system_host_keys = True
=> key_policy = AutoAddPolicy
```
Note that `key_policy = AutoAddPolicy` is different from the defautl settings!

## test computer

```
verdi computer test {computer}
```

# To install a new code, run:

```
cat {code}_{computer}.code | verdi code setup 
```

NB: check the path of the code, 
    you can have access to the executable on clusters,
    but on localhost you need to adapt the path!
