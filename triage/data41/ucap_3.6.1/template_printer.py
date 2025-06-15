import os
import re
import sys
from datetime import datetime


def main():
    # TODO use argparse?
    if len(sys.argv) != 2:
        command: str = re.split("[\\/]", sys.argv[0])[-1]
        print(f"Usage: {command} TEMPLATE-NAME", file=sys.stderr)
        print("", file=sys.stderr)
        print("Template name can be:", file=sys.stderr)
        print(" - one-to-one / o2o", file=sys.stderr)
        print(" - one-to-many / o2m", file=sys.stderr)
        print(" - event-to-one / e2o", file=sys.stderr)
        print(" - event-to-many / e2m", file=sys.stderr)
        print("", file=sys.stderr)
        print("Examples:", file=sys.stderr)
        print(f" - {command} one-to-one > my_converter.py", file=sys.stderr)
        print(f" - {command} e2m > my_converter.py", file=sys.stderr)
        sys.exit(1)

    template_name: str = sys.argv[1].casefold().strip()

    if template_name in ["one-to-one", "one_to_one", "onetoone", "o2o"]:
        file_name = "one_to_one_converter_template.py"
    elif template_name in ["one-to-many", "one_to_many", "onetomany", "o2m"]:
        file_name = "one_to_many_converter_template.py"
    elif template_name in ["event-to-one", "event_to_one", "eventtoone", "e2o"]:
        file_name = "event_to_one_converter_template.py"
    elif template_name in [
        "event-to-many",
        "event_to_many",
        "eventtomany",
        "e2m",
    ]:
        file_name = "event_to_many_converter_template.py"
    else:
        print(f"No template defined for: {template_name}", file=sys.stderr)
        sys.exit(1)

    file_to_open: str = os.path.join(os.path.dirname(__file__), file_name)
    with open(file_to_open) as f:
        year: int = datetime.now().year
        print(f.read().replace("@YEAR@", str(year)))


if __name__ == "__main__":
    main()
