"""Main module"""
#!/usr/bin/env python
from ipykernel.kernelapp import IPKernelApp
from .kernel import janscobolkernel
IPKernelApp.launch_instance(kernel_class=janscobolkernel)
