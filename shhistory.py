"""
    Project: shhistory (https://github.com/battleoverflow/shhistory)
    Author: battleoverflow (https://github.com/battleoverflow)
    License: BSD 2-Clause
"""

import platform, os, json

# Accepted platforms
platform_type = [
    "Linux",
    "Darwin"
]

file_types = [
    "bash_history",
    "csh_history",
    "dash_history",
    "ksh_history",
    "sh_history",
    "tcsh_history",
    "zsh_history",
    "history"
]

class ShellHistory:
    """
    Main class for the gathering shell history information.

    - get_shell_history(): Dump shell history in JSON format
    - dump_shell_history(): Dump shell history to a file in JSON format
    """

    def get_shell_history():
        """
        Dump shell history in JSON format.

        Currently supports:

        - /bin/bash
        
        - /bin/csh
        
        - /bin/dash
        
        - /bin/ksh
        
        - /bin/sh
        
        - /bin/tcsh
        
        - /bin/zsh

        @rtype: None (JSON)
        """

        for p in platform_type:
            if p == platform.system():
                for f_type in file_types:
                    filename = os.path.join(os.path.expanduser("~"), f".{f_type}")

                    if os.path.exists(filename):
                        history = []

                        with open(filename, 'r') as f:
                            for line in f:
                                history.append(line)

                shell_history = {
                    filename: history
                }

                return json.dumps(shell_history)

    def dump_shell_history() -> None:
        """
        Dump shell history to a file in JSON format.

        @rtype: None        
        """
        
        with open("history.json", "w") as hist:
            hist.write(ShellHistory.get_shell_history())
