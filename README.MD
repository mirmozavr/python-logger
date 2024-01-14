# Logger Module

A Python logging module for streamlined and flexible logging configuration.

## Overview

This module provides a convenient setup for Python logging with customizable configurations. It enables you to easily
integrate logging into your projects, allowing you to capture important information and errors efficiently.

## Features

- **Structured Logging:** Log messages include timestamps, log levels, filenames, line numbers, function names, and the
  actual log message for comprehensive information.
- **Multiple Handlers:** Supports logging to standard output, standard error, and rotating log files simultaneously.
- **Filtering:** Filters log records based on the specified log level, ensuring that only relevant messages are
  processed.
- **Configurability:** Easily adapt the logging setup to your needs by modifying the provided configuration dictionary.

## Installation

To use this logging module, simply copy the `logger.py` file into your project.

## Usage

1. Import the module at the entrypoint of your application:  
  It will handle logging configuration.

```python
import logger
```

2. Create a logger object instance:  
   In example below module name used to created named logger.
   Predefined logger names are in `logging_configuration_dict`.

```python
import logging
log = logging.getLogger(__name__)
```

3. Configure the logging setup (optional):  
   Modify the logging_configuration_dict dictionary in the logger.py file according to your preferences.
   You can adjust formatting, handlers, log levels, and more.

#### Example configuration for `logging_configuration_dict`

```python
{
    "version": 1,
    "formatters": {
        "fmt_long": {
            # ... (format details)
        },
        "fmt_short": {
            # ... (format details)
        },
    },
    "filters": {
        "warnings_and_below": {
            "()": "logger.level_filter_maker",
            "level": "WARNING",
        }
    },
    "handlers": {
        "stdout": {
            # ... (stdout handler details)
        },
        "stderr": {
            # ... (stderr handler details)
        },
        "rotating_fh": {
            # ... (rotating file handler details)
        },
    },
    "loggers": {
        "main": {
            # ... (main logger details)
        },
    },
    "root": {
        # ... (root logger details)
    }
}
```

Feel free to customize the configuration based on your project's requirements.

4. Start logging in your application:

```python
log.debug("Debug message")
log.info("Informational message")
log.warning("Warning message")
log.error("Error message")
log.critical("Critical message")
```

## License

This module is released under the [MIT License](LICENSE). 
Feel free to use, modify, and distribute it as needed. 
If you find it helpful, consider giving it a star.

For more details and advanced usage, please refer to the [python official logging documentation](https://docs.python.org/3/library/logging.html).