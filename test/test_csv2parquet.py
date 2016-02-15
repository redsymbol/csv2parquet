import unittest
import os
from collections import OrderedDict

import csv2parquet
from csv2parquet import Columns, Column

THIS_DIR = os.path.dirname(__file__)
TEST_CSV = os.path.join(THIS_DIR, 'test-simple.csv')
TEST_CSV_MAP = os.path.join(THIS_DIR, 'test-header-mapping.csv')

class TestUtil(unittest.TestCase):
    def test_list2dict(self):
        from csv2parquet import list2dict
        with self.assertRaises(ValueError):
            list2dict(["foo"])
        with self.assertRaises(ValueError):
            list2dict(["foo", "bar", "baz"])
        self.assertEqual({}, list2dict([]))
        self.assertEqual({}, list2dict(None))
        self.assertEqual({"a":"b"}, list2dict(["a", "b"]))
        self.assertEqual({"a":"b", "x":"y"}, list2dict(["a", "b", "x", "y"]))
        self.assertEqual({"a":"b", "x":"y"}, list2dict(["x", "y", "a", "b"]))

class TestCsvSource(unittest.TestCase):
    def test_real_path_to_prevent_drill_script_errors(self):
        # Specifying a CSV file path of something like "../something.csv" will confuse Drill.
        # Prevent this by expanding the path.
        csv_src = csv2parquet.CsvSource('./test-simple.csv')
        self.assertEqual(csv_src.path, os.path.realpath(TEST_CSV))
    def test_headers_simple(self):
        csv_src = csv2parquet.CsvSource(TEST_CSV)
        expected_headers = [
            'Date',
            'Open',
            'High',
            'Low',
            'Close',
            'Volume',
            'ExDividend',
            'SplitRatio',
            'AdjOpen',
            'AdjHigh',
            'AdjLow',
            'AdjClose',
            'AdjVolume',
            ]
        self.assertEqual(expected_headers, csv_src.headers)
        # CSV and Parquet column names should be the same.
        expected_columns = [Column(header, header, None) for header in expected_headers]
        self.assertEqual(expected_columns, csv_src.columns.items)

    def test_columns_from_csv_source(self):
        # verify that an exception is raised if we don't override Parquet-invalid column names
        with self.assertRaises(csv2parquet.InvalidColumnNames):
            csv_src = csv2parquet.CsvSource(TEST_CSV_MAP)
        # now try again, with a mapping
        name_map = {
            'Adj. Open'   : 'Adj Open',
            'Adj. High'   : 'Adj High',
            'Adj. Low'    : 'Adj Low',
            'Adj. Close'  : 'Adj Close',
            'Adj. Volume' : 'Adj Volume',
            }
        csv_src = csv2parquet.CsvSource(TEST_CSV_MAP, name_map)
        expected_columns = [
            Column('Date', 'Date', None),
            Column('Open', 'Open', None),
            Column('High', 'High', None),
            Column('Low', 'Low', None),
            Column('Close', 'Close', None),
            Column('Volume', 'Volume', None),
            Column('Ex-Dividend', 'Ex-Dividend', None),
            Column('Split Ratio', 'Split Ratio', None),
            Column('Adj. Open', 'Adj Open', None),
            Column('Adj. High', 'Adj High', None),
            Column('Adj. Low', 'Adj Low', None),
            Column('Adj. Close', 'Adj Close', None),
            Column('Adj. Volume', 'Adj Volume', None),
            ]
        self.assertEqual(expected_columns, csv_src.columns.items)

class TestDrillScript(unittest.TestCase):
    def test_build_script(self):
        # .strip() the actual scripts to ignore leading/trailing whitespace
        expected_script = '''
alter session set `store.format`='parquet';
CREATE TABLE dfs.tmp.`/path/to/parquet_output/` AS
SELECT
CASE when columns[0]='When' then CAST(NULL AS DATE) else CAST(columns[0] as DATE) end as `Date`,
columns[1] as `Open`,
columns[2] as `High`,
columns[3] as `Low`,
columns[4] as `Close`,
columns[5] as `Volume`,
columns[6] as `Ex-Dividend`,
CASE when columns[7]='Split Ratio' then CAST(NULL AS FLOAT) else CAST(columns[7] as FLOAT) end as `Split Ratio`,
CASE when columns[8]='Adj. Open' then CAST(NULL AS DOUBLE) else CAST(columns[8] as DOUBLE) end as `Adj Open`
FROM dfs.`/path/to/input.csv`
OFFSET 1
'''.strip()
        columns = [
            Column('When', 'Date', 'DATE'),
            Column('Open', 'Open', None),
            Column('Day High', 'High', None),
            Column('Day Low', 'Low', None),
            Column('Close', 'Close', None),
            Column('Volume', 'Volume', None),
            Column('Ex-Dividend', 'Ex-Dividend', None),
            Column('Split Ratio', 'Split Ratio', 'FLOAT'),
            Column('Adj. Open', 'Adj Open', 'DOUBLE'),
            ]
        actual_script = csv2parquet.render_drill_script(columns, '/path/to/parquet_output/', '/path/to/input.csv').strip()
        self.assertEqual(expected_script, actual_script)
    maxDiff=None

class TestColumns(unittest.TestCase):
    def test_main(self):
        columns = Columns([], {}, {})
        self.assertEqual([], columns.items)
        
        columns = Columns(
            ["abc", "xyz", "foo", "bar", "baz"],
            {"foo": "whee", "baz": "magic"},
            {})
        items = [
            Column("abc", "abc", None),
            Column("xyz", "xyz", None),
            Column("foo", "whee", None),
            Column("bar", "bar", None),
            Column("baz", "magic", None),
        ]
        self.assertEqual(items, columns.items)
        self.assertEqual(items, list(columns))
