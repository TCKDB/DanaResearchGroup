"""
ARC's settings
"""

import os
import string
import sys

servers = {
    'local': {
        'path': '/storage/ce_dana/',
        'cluster_soft': 'HTCondor',
        'un': '[username]',
        'cpus': 5,
        'memory': 256,
    },
}

# List here servers you'd like to associate with specific ESS.
# An ordered list of servers indicates priority
# Keeping this dictionary empty will cause ARC to scan for software on the servers defined above
global_ess_settings = {
    'gaussian': 'local',
    'orca': 'local',
    'molpro': 'local',
}

# Electronic structure software ARC may access (use lowercase):
supported_ess = ['gaussian', 'molpro', 'orca']

