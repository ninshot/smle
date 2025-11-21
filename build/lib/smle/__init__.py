import traceback
import sys
from smle.args import read_configuration_file
from smle.logging import init_logging_module, close_logging_module

class SMLEApp:

    """
    The base SMLEApp
    """

    def __init__(self):
        self._main_func = None
        self.config = {} # Placeholder for configuration

    def entrypoint(self, main_func):
        """
        The decorator to register the main execution function.
        (Equivalent to Flask's @app.route)
        """
        self._main_func = main_func
        return main_func

    def _read_configuration_file(self):
        """Simulates reading the config file."""
        # In a real app, this would load settings from disk/environment
        read_configuration_file()
        return self.config

    def _init_logging_module(self, args):
        init_logging_module(args)

    def _close_logging_module(self):
        close_logging_module()

    def run(self):
        """
        The method that executes the application's core logic.
        """

        if not self._main_func:
            print("Error: No main function registered. Did you use @app.entrypoint?")
            sys.exit(1)

        args = self._read_configuration_file()
        self._init_logging_module(args)

        try:
            # The execution of the decorated user function
            return self._main_func(args)
        except Exception:
            # Print the traceback on failure
            print(traceback.format_exc())
            sys.exit(1)
        finally:
            self._close_logging_module()