# iPython Autoreload

The `autoreload` extension in iPython is used to reload modules before
executing code. This feature can be added to the `ipython_config.py` file if
you want it to automatically start every time the iPython shell is launched.

The iPython shell can be customized with a configuration file known as a
"profile". The profile can automate certain tasks such as executing a command
or importing a library. The default profile is usually located in a file named
`ipython_config.py`. If this file does not exist in
`~/.ipython/profile_default/`, then type the following command in the Terminal
to create a new default profile: `ipython profile create`.

In the new `ipython_config.py` file, add the following line at the top:

```python
c = get_config()
```

Next, uncomment and edit the following lines:

```python
c.InteractiveShellApp.exec_lines = ['%autoreload 2']
c.InteractiveShellApp.extensions = ['autoreload']
```

This will tell iPython to automatically reload modules before executing any code.

## Resources

Visit the links below for further reading about configuring the iPython shell and the autoreload feature.

[Introduction to iPython configuration](http://ipython.readthedocs.org/en/stable/config/intro.html)  
[Using iPython Profiles for More Effective Interactive Sessions](https://www.safaribooksonline.com/blog/2014/02/27/using-ipython-profiles/)  
[Documentation for autoreload](http://ipython.readthedocs.org/en/stable/config/extensions/autoreload.html)  
[Autoreload of modules in iPython](http://stackoverflow.com/questions/1907993/autoreload-of-modules-in-ipython)  

