import argparse

def make_parser():
    parser = argparse.ArgumentParser(
        description='Generate Spectrum-Based Data.'
    )

    parser.add_argument(
        '--spectra_data',
        action='store_true',
        help='Generates spectrum-based data with selected Failing & Passing TC.'
    )

    parser.add_argument(
        '--criteria_data',
        action='store_true',
        help='Generates CSV file for all TC to a criteria.'
    )

    parser.add_argument(
        '--relation_data',
        action='store_true',
        help='Generates TC-to-TC relation csv on per-file, per-function, per-line intersections.'
    )

    parser.add_argument(
        '--list_tc',
        action='store_true',
        help='Generates a text file containing the list of test cases.'
    )

    parser.add_argument(
        '--summary_json',
        type=int,
        default=None,
        help='Generates coverage summary in json format for a selected TC. (ex. --summary-json <tcNum>)'
    )

    parser.add_argument(
        '--html',
        type=int,
        default=None,
        help='Generates html of coverage data for a selected TC. (ex. --html <tcNum>)'
    )

    parser.add_argument(
        '--pretty_json',
        type=int,
        default=None,
        help='Generates coverage in pretty json format for a selected TC. (ex. --html <tcNum>)'
    )

    return parser