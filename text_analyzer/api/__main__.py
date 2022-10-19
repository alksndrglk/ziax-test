"""
REST API сервис, анализирующий входящее предложение.
"""
import argparse
import logging
import os
import pwd

from aiohttp.web import run_app
from aiomisc import bind_socket
from aiomisc.log import LogFormat, basic_config
from configargparse import ArgumentParser

from text_analyzer.api.app import create_app
from text_analyzer.utils.argparse import clear_environ, positive_int


ENV_VAR_PREFIX = "ANALYZER_"


parser = ArgumentParser(
    auto_env_var_prefix=ENV_VAR_PREFIX,
    allow_abbrev=False,
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
parser.add_argument(
    "--user", required=False, type=pwd.getpwnam, help="Change process UID"
)

group = parser.add_argument_group("API Options")
group.add_argument(
    "--api-address",
    default="0.0.0.0",
    help="IPv4/IPv6 address API server would listen on",
)
group.add_argument(
    "--api-port",
    type=positive_int,
    default=8081,
    help="TCP port API server would listen on",
)

group = parser.add_argument_group("Logging options")
group.add_argument(
    "--log-level",
    default="info",
    choices=("debug", "info", "warning", "error", "fatal"),
)
group.add_argument("--log-format", choices=LogFormat.choices(), default="color")

group = parser.add_argument_group("ApiKeyAuth")
group.add_argument("--api-key", type=str, required=True)


def main():
    args = parser.parse_args()
    clear_environ(lambda i: i.startswith(ENV_VAR_PREFIX))
    basic_config(args.log_level, args.log_format, buffered=True)
    sock = bind_socket(address=args.api_address, port=args.api_port, proto_name="http")
    if args.user is not None:
        logging.info("Changing user to %r", args.user.pw_name)
        os.setgid(args.user.pw_gid)
        os.setuid(args.user.pw_uid)

    app = create_app(args)
    run_app(app, sock=sock)


if __name__ == "__main__":
    main()
