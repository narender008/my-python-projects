#! /opt/homebrew/Caskroom/miniconda/base/envs/mlbox/bin/python3
import re
import sys

pattern = r"\((\w+)\)\s+CMD\s+\(([^)]+)\)"


def parsing_logs(logfile):
    holder_name = {}
    holder_cmd = {}
    with open(logfile, "r") as file:
        for line in file:
            if not "CRON" in line:
                continue
            name, cmd = re.search(pattern, line).group(1, 2)


if __name__ == "__main__":
    logfile = sys.argv[1]
    result = parsing_logs(logfile)
