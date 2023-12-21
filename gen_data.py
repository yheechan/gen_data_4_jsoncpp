#!/usr/bin/python3
import subprocess as sp
import argparse

from utils import myCommander as cc
from utils import myDatabase as dd

failing_file = [
    'src/lib_json/json_reader.cpp',
    'src/lib_json/json_value.cpp'
]

failing_line = [
    (
        'src/lib_json/json_reader.cpp',
        'Json::OurReader::decodeNumber(Json::OurReader::Token&, Json::Value&)'
    ),
    (
        'src/lib_json/json_reader.cpp',
        'Json::OurReader::skipBom(bool)'
    ),
    (
        'src/lib_json/json_reader.cpp',
        "Json::Reader::readObject(Json::Reader::Token&)"
    ),
    (
        'src/lib_json/json_value.cpp',
        'Json::Value::resize(unsigned int)'
    )
]

failing_line = [
    ('src/lib_json/json_reader.cpp', 467),
    ('src/lib_json/json_reader.cpp', 1279),
    ('src/lib_json/json_reader.cpp', 1630),
    ('src/lib_json/json_value.cpp', 915)
]


failing_tc = [
    'CharReaderTest/failingTestCaseIntegerOverflows',
    'CharReaderTest/failingTestCaseHeapOverflows',
    'ReaderTest/allowNumericKeysTest',
    'ValueTest/resizePopulatesAllMissingElements'
]

passing_tc = [
    'CharReaderTest/parseWithNoErrors',
    'FastWriterTest/writeArrays',
    'StyledWriterTest/multiLineArray',
    'StyledStreamWriterTest/writeNumericValue',
    'StyledStreamWriterTest/writeArrays',
    'ReaderTest/parseString'
]
    
def make_parser():
    parser = argparse.ArgumentParser(
        description='Generate Data.'
    )

    parser.add_argument(
        '--command',
        required=False,
        default='spectra-data',
        choices=[
            'spectra-data',
            'summary',
            'list-tc',
            'html',
            'pretty-json',
            'tc-criterion',
            'tc-relation'
        ],
        help='select which operation to run.'
    )

    parser.add_argument(
        '--tcNum',
        type=int,
        nargs='?',
        const=0,
        default=None,
        help='test case number (optional)')

    return parser

if __name__ == "__main__":
    parser = make_parser()
    args = parser.parse_args()

    db = dd.myDatabase()
    cc.assign_test_cases(db, failing_tc)

    if args.command == 'spectra-data':
        cc.spectra_data(db, failing_tc, passing_tc)
    elif args.command == 'list-tc':
        cc.list_test_cases(db, failing_tc)
    elif args.command == 'summary':
        cc.summary_coverage_json_target_TC(db, args.tcNum)
    elif args.command == 'html':
        cc.html_target_TC(db, args.tcNum)
    elif args.command == 'pretty-json':
        cc.pretty_json_TC(db, args.tcNum)
    elif args.command == 'tc-criterion':
        pass
    elif args.command == 'tc-relation':
        pass
