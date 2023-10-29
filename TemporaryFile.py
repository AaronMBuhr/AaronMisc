import DebugUtils

class TemporaryFile:
    @property
    def filename(self) -> str:
        return self._filename

    def __init__(self, suffix=None):
        if DebugUtils.get_log_level() <= DebugUtils.DEBUG:
            current_temp_file_num = DebugUtils.get_var("temp_file_num", 0)
            self._filedescriptor, self._filename = None, f"tempfile_{current_temp_file_num:03}{suffix or ''}"
            DebugUtils.set_var(DebugUtils.DEBUG, "temp_file_num", current_temp_file_num + 1)
        else:
            self._filedescriptor, self._filename = tempfile.mkstemp(suffix=suffix)
            os.close(self._filedescriptor)

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if DebugUtils.get_log_level() > DebugUtils.DEBUG:
            try:
                os.remove(self._filename)
            except:
                DebugUtils.error(f"Temporary file [{self._filename}]: could not remove")
                pass
