from dragonfly import AppContext
import subprocess
from subprocess import check_output


class VimContext(AppContext):
    #-----------------------------------------------------------------------
    # Initialization methods.

    def __init__(self, title=None, mode=None, exclude=False):
        executable = "vim.exe"
        AppContext.__init__(self, executable, title, exclude)

        if isinstance(mode, str):
            self._mode = mode
        elif mode is None:
            self._mode = None
        else:
            raise TypeError("mode argument must be a string or None;"
                        " received %r" % mode)

        self._str = "%s, %s, %s" % (self._executable, self._title,
                                    self._exclude)

    #-----------------------------------------------------------------------
    # Matching methods.

    def matches(self, executable, title, handle):
        executable = executable.lower()
        title = title.lower()
        if AppContext.matches(self, executable, title, handle):
            mode = str(get_mode(executable, title))
            if mode.find(self._mode) != -1:
                return True
            else:
                return False
        else:
            return False

        
        if self._log_match: self._log_match.debug("%s: Match." % (self))
        return True

def get_mode(executable, title):
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    the_exec = "\\".join(executable.split("\\")[:-1] + ["vim.exe"])
    vim_instance = title.split()[-1].upper()
    mode = check_output([the_exec, "--servername", vim_instance, "--remote-expr", "mode()"], startupinfo=si)
    return mode
