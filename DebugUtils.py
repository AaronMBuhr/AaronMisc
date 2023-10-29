import copy
import datetime
import json
import yaml


class YamlDumper:
    @staticmethod
    def yaml_compatible_deepcopy(source):
        """
        Deep copy a object (may not be dict), replacing any values that can't be converted to YAML with None.
        """

        def process_value(value):
            """
            Convert a value to YAML, replacing it with None if it can't be converted.
            """
            if not isinstance(value, (dict, list, tuple, set)) and not isinstance(value, str) and not isinstance(value, (int, float, bool, type(None))):
                value = {name: getattr(value, name) for name in dir(value) if not name.startswith('__') and not callable(getattr(value, name))}

            try:
                yaml.safe_dump({ "test_key": value })  # Test the conversion with a temporary dictionary
                return value  # If it succeeded, return the original value
            except yaml.YAMLError:
                return None  # If it failed, return None

        def process_dict(d):
            """
            Recursively process a dictionary, replacing any values that can't be converted to YAML.
            """
            if isinstance(d, dict):
                for key, value in d.items():
                    if isinstance(value, dict):
                        d[key] = process_dict(value)  # If the value is a dictionary, process it recursively
                    elif isinstance(value, list) or isinstance(value, tuple) or isinstance(value, set):  # Handle list, tuple and set
                        d[key] = [process_value(v) for v in value]
                    else:
                        d[key] = process_value(value)  # Otherwise, process the value directly
                return d
            elif isinstance(d, list) or isinstance(d, tuple) or isinstance(d, set):  # Handle list, tuple and set at the top level
                return [process_value(v) for v in d]
            else:
                return process_value(d)

        return process_dict(source)

    @staticmethod
    def to_yaml_compatible_str(o):
        return yaml.safe_dump(YamlDumper.yaml_compatible_deepcopy(o))
    

class DebugUtils:
    # Log level constants
    DEBUG = 0
    VERBOSE = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    CRITICAL = 5

    # Set initial log level
    _log_level = DEBUG
    _debug_vars = {}

    @staticmethod
    def get_log_level():
        return DebugUtils._log_level

    @staticmethod
    def _get_timestamp():
        return datetime.datetime.now().strftime("%Y%m%d/%H%M%S")

    @staticmethod
    def set_log_level(level):
        DebugUtils._log_level = level

    @staticmethod
    def debug(message, omit_header: bool=False):
        if DebugUtils._log_level <= DebugUtils.DEBUG:
            if omit_header:
                print(message)
            else:
                print(f"[{DebugUtils._get_timestamp()}] [DEBG] {message}")

    @staticmethod
    def verbose(message, omit_header: bool=False):
        if DebugUtils._log_level <= DebugUtils.VERBOSE:
            if omit_header:
                print(message)
            else:
                print(f"[{DebugUtils._get_timestamp()}] [VERB] {message}")

    @staticmethod
    def info(message, omit_header: bool=False):
        if DebugUtils._log_level <= DebugUtils.INFO:
            if omit_header:
                print(message)
            else:
                print(f"[{DebugUtils._get_timestamp()}] [INFO] {message}")

    @staticmethod
    def warning(message, omit_header: bool=False):
        if DebugUtils._log_level <= DebugUtils.WARNING:
            if omit_header:
                print(message)
            else:
                print(f"[{DebugUtils._get_timestamp()}] [WARN] {message}")

    @staticmethod
    def error(message, omit_header: bool=False):
        if DebugUtils._log_level <= DebugUtils.ERROR:
            if omit_header:
                print(message)
            else:
                print(f"[{DebugUtils._get_timestamp()}] [ERRR] {message}")

    @staticmethod
    def critical(message, omit_header: bool=False):
        if DebugUtils._log_level <= DebugUtils.CRITICAL:
            if omit_header:
                print(message)
            else:
                print(f"[{DebugUtils._get_timestamp()}] [CRIT] {message}")
    
    @staticmethod
    def set_var(debug_level, var_name, var_value):
        if debug_level >= DebugUtils._log_level:
            DebugUtils._debug_vars[var_name] = var_value

    @staticmethod
    def get_var(var_name, default_value=None):
        try:
            return DebugUtils._debug_vars[var_name]
        except:
            return default_value

    # @staticmethod
    # def yaml_compatible_deepcopy(source_dict):
    #     """
    #     Deep copy a dictionary, replacing any values that can't be converted to YAML with None.
    #     """
    #     copied_dict = copy.deepcopy(source_dict)  # Start with a deep copy of the source dictionary

    #     def process_value(value):
    #         """
    #         Convert a value to YAML, replacing it with None if it can't be converted.
    #         """
    #         try:
    #             yaml.safe_dump({ "test_key": value })  # Test the conversion with a temporary dictionary
    #             return value  # If it succeeded, return the original value
    #         except yaml.YAMLError:
    #             return None  # If it failed, return None

    #     def process_dict(d):
    #         """
    #         Recursively process a dictionary, replacing any values that can't be converted to YAML.
    #         """
    #         for key, value in d.items():
    #             if isinstance(value, dict):
    #                 d[key] = process_dict(value)  # If the value is a dictionary, process it recursively
    #             else:
    #                 d[key] = process_value(value)  # Otherwise, process the value directly
    #         return d

    #     return process_dict(copied_dict)

    # @staticmethod
    # def to_compatible_yaml(dict_obj):
    #     try:
    #         return yaml.safe_dump(dict_obj)
    #     except yaml.YAMLError as exc:
    #         print(exc)

    # @staticmethod
    # def convert_all_values_to_str(dict_obj):
    #     """
    #     This function will convert all the non-convertible types to string
    #     so that they can be converted to YAML.
    #     """
    #     new_dict = {}
    #     for key, value in dict_obj.items():
    #         if isinstance(value, dict):
    #             new_dict[key] = DebugUtils.convert_all_values_to_str(value)
    #         elif isinstance(value, list):
    #             new_dict[key] = [str(i) for i in value]
    #         else:
    #             try:
    #                 json.dumps(value) # Try to convert the value into json.
    #                 new_dict[key] = value
    #             except (TypeError, OverflowError):
    #                 new_dict[key] = str(value)
    #     return new_dict

