# maybe - see what a program does before deciding whether you really want it to happen
#
# Copyright (c) 2016 Philipp Emanuel Weidmann <pew@worldwidemann.com>
#
# Nemo vir est qui mundum non reddat meliorem.
#
# Released under the terms of the GNU General Public License, version 3
# (https://gnu.org/licenses/gpl.html)


from blessings import Terminal


T = Terminal()


def initialize_terminal(style_output):
    # This hack works around two issues:
    # 1. The global object T is imported into the context of other modules,
    #    so (re)assigning T here has no effect.
    # 2. Setting T._does_styling to True does not call setupterm, resulting in
    #    an error unless styling was already enabled anyway.
    # Invoking the constructor manually keeps the imported references valid
    # and calls setupterm (again) if necessary.
    T.__init__(force_styling={
        "yes": True,
        "no": None,
        "auto": False,
    }[style_output])


SYSCALL_FILTERS = {}


def register_filter(filter_scope, syscall, filter_function):
    if filter_scope not in SYSCALL_FILTERS:
        SYSCALL_FILTERS[filter_scope] = {}
    SYSCALL_FILTERS[filter_scope][syscall] = filter_function
