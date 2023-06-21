"""Logger module."""
import argparse
import logging

from utilities._arg_parser import parse_args

args: argparse.Namespace = parse_args()

logging.basicConfig(
    format="%(asctime)s %(levelname)s : %(filename)s(%(lineno)d) : %(message)s",
    datefmt="%d/%m/%y %H:%M:%S",
)
log = logging.getLogger("TestAPP")
log.setLevel(args.log_level.upper())
