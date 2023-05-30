# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleError, AnsibleConnectionFailure
from ansible.module_utils.common.text.converters import to_native, to_text
from ansible.module_utils.common.collections import is_string
from ansible.plugins.action import ActionBase
from ansible.utils.display import Display
import numpy
import matplotlib
import matplotlib.pyplot as plt
import json
import os

display = Display()


class TimedOutException(Exception):
    pass


class ActionModule(ActionBase):
    TRANSFERS_FILES = False
    _VALID_ARGS = frozenset((
        'scenarios',
        'exec_mode',
        'fail_mode',
    ))

    def __init__(self, *args, **kwargs):
        super(ActionModule, self).__init__(*args, **kwargs)

    def run(self, tmp=None, task_vars=None):

        self._supports_check_mode = False
        self._supports_async = False

        if task_vars is None:
            task_vars = {}

        result = super(ActionModule, self).run(tmp, task_vars)
        module_args = self._task.args
        # check results    
        result['module_args'] = module_args
        result['ravi'] = True
        result['changed'] = True

        return result
