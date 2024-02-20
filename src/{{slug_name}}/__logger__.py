import logging

logger: logging.Logger = logging.getLogger("{{slug_name}}")
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.NullHandler())

log_fmter = logging.Formatter(
    "[{levelname:^4.4}] {asctime} 📟 {message}",
    "%Y-%m-%d %H:%M:%S",
    style="{",
)