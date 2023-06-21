"""Argument parsing helper."""
import argparse
import datetime
from typing import Optional, Sequence


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    """Parse command line arguments and return an arguments namespace.

    Parameters
    ----------
    argv : Optional[Sequence[str]], optional
        A sequence of strings representing the command line arguments. If specified,
        these arguments are used instead of the ones passed on the command line.

    Returns
    -------
    argparse.Namespace
        A namespace containing the parsed arguments.

    Notes
    -----
    This function uses Python's built-in `argparse` module to parse command line
    arguments. The following arguments are accepted:

    --all-time : bool, optional
        If True, read data from all time.
    --lookback-days : int, optional
        The number of days before `read_to_date` to read. If negative, a default value
        is used.
    --read-to-date : str, optional
        A date in ISO format (yyyy-mm-dd) to look back from. By default, today's date is
        used. Example: "2022-05-16".
    --log-level : str, optional
        The logging level to use. Default is 'WARNING'.

    Example
    -------
    >>> from pprint import pprint
    >>> pprint(parse_args(["--all-time", "--lookback-days", "3", "--read-to-date",
    ... "2023-02-01", "--log-level", "INFO"]))
    Namespace(all_time=True, log_level='INFO', lookback_days=3, read_to_date=datetime.date(2023, 2, 1))
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--all-time",
        action="store_true",
        help="Read data from all time.",
    )
    parser.set_defaults(all_time=False)

    parser.add_argument(
        "--lookback-days",
        help="Number of days before read_to_date to read, if negative use default value",
        default=2,
        type=int,
    )
    parser.add_argument(
        "--read-to-date",
        help=(
            "Look back from specified date (in isoformat [yyyy-mm-dd]),"
            " by default None = today"
        ),
        default=None,
        type=datetime.date.fromisoformat,
    )

    parser.add_argument(
        "--log-level", help=("Logging level."), default="WARNING", type=str
    )

    args, _ = parser.parse_known_args(argv)
    return args
