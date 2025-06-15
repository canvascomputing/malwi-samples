import argparse
import importlib
import importlib.util
import json
import logging
import os
import re
import sys
from typing import List, Tuple

from ucap.common import Event


def create_ucap_events_from_files(
    data_directory: str
) -> List[Tuple[str, Event]]:
    """
    Returns events created from files in a specified directory.

    Files in that directory should be a JSON serialization of a singular Event

    Parameters
    ----------
    data_directory : str
        the location of a directory containing json files of Event (one file per one event)

    Returns
    -------
    List[Tuple[str, Event]]
        a list of filename-Event pairs
    """
    ucap_events: List[Tuple[str, Event]] = []
    if os.path.isdir(data_directory):
        file_list = os.listdir(data_directory)
        file_list.sort()
        for file in file_list:
            if file.endswith(".json"):
                path_to_file = os.path.join(data_directory, file)
                f = open(path_to_file)
                json_data = json.load(f)
                ucap_events.append((file, Event._create_from_json(json_data)))
    else:
        print("no such folder: " + data_directory)

    return ucap_events


def test_converter(converter_file: str, test_data_directory: str):
    """
    Tests a converter by feeding recorded inputs into it.

    Parameters
    ----------
    converter_file : str
        the location of a converter file
    test_data_directory : str
        the location of a directory containing the recorded inputs

    Returns
    -------
    List
        converter results
    """
    module_name = converter_file.split("/")[-1].split(".")[0]
    module_path = converter_file[: converter_file.rfind("/")]
    logging.getLogger(__name__).info(module_name)
    logging.getLogger(__name__).info(module_path)
    sys.path.insert(0, module_path)

    converter = importlib.import_module(module_name)

    # load events
    events = create_ucap_events_from_files(test_data_directory)
    results = []
    # run converter on each event
    for event in events:
        try:
            logging.getLogger(__name__).debug("Transforming: %s", event[0])
            result = converter.convert(event[1])  # type: ignore
            logging.getLogger(__name__).debug("Result: %s", result)
            results.append(result)
        except Exception as e:
            logging.getLogger(__name__).exception(e)

    return results


def handler(args: argparse.Namespace) -> None:
    logging.basicConfig(
        format="%(asctime)s %(levelname)s: %(message)s [%(filename)s:%(lineno)d]",
        level=logging.INFO,
    )

    if args.debug:
        logging.getLogger(__name__).setLevel(logging.DEBUG)

    converter_file: str = args.converter_file
    test_data_directory: str = args.test_data_directory
    logging.getLogger(__name__).info("Converter file: %s", converter_file)
    logging.getLogger(__name__).info(
        "Test data directory: %s", test_data_directory
    )

    test_converter(converter_file, test_data_directory)
    logging.getLogger(__name__).info("Offline test finished.")


def main() -> None:
    command: str = re.split("[\\/]", sys.argv[0])[-1]

    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        prog=command,
        description="Test a converter with recorded test inputs.",
        epilog=os.linesep.join(
            (
                "Examples:",
                f" - {command} my_converter.py test_data/",
                f" - {command} my_converter.py test_data/ --debug",
            )
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument("converter_file", help="Converter file")
    parser.add_argument(
        "test_data_directory", help="Directory containing recorded test inputs."
    )
    parser.add_argument(
        "--debug",
        dest="debug",
        action="store_true",
        help="Enable debug logging.",
    )

    handler(parser.parse_args())


if __name__ == "__main__":
    main()
