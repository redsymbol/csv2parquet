# csv2parquet: Create Parquet files from CSV

This simple tool creates Parquet files from CSV input. It requires [Apache Drill](https://drill.apache.org) to be installed.

Much credit for this goes to Tugdual "Tug" Grall; `csv2parquet`
essentially automates the process he documents in [Convert a CSV File
to Apache Parquet With
Drill](http://tgrall.github.io/blog/2015/08/17/convert-csv-file-to-apache-parquet-dot-dot-dot-with-drill/).

`csv2parquet` is now in **public beta**. Feedback, comments, bug
reports, and feature requests are all appreciated. See "About and
Contact" below to reach the author.

# Usage

```csv2parquet CSV_INPUT PARQUET_OUTPUT [--column-names ...]```

`csv_input` is a CSV file, whose first line defines the column names.
`parquet_output` is the Parquet output (i.e., directory in which one or
more Parquet files are written.)

## Column Names

By default, Parquet column names have the same name as the CSV header.
You can specify a different name for each output column with the
`--column-names` option.  When used, it must be followed by an even
number of strings, constituting the key-value pairs:

```
csv2parquet data.csv data.parquet --column-names "First Column" "Primary Column" "Another Column" "Special Name"
```

In this example, two of the CSV columns are named "First Column" and
"Another Column". The created Parquet file will store data from these
columns under "Primary Column" and "Special Name", respectively.

(A perfectly good CSV column name may not be valid as a Parquet column
name - for example, a header name with a period, like
"Min. Investment". In this situation, you *must* use `--column-names`
to provide a column name that Parquet can accept, or edit the source
CSV file.)

## Column Types

By default, `csv2parquet` assumes all columns are of type string. You
can define specific columns to be any Drill data type. You do this
using the `--type-names` option, whose syntax is similar to
`--column-names`. On the command line, you write `--type-names`,
followed by an even number of strings that encode a sequence of
pairs. In each pair, the first string matches the name of the CSV
column. (*Not* the Parquet column name, if that is different.) The
second string is one of the [Drill data
types](https://drill.apache.org/docs/supported-data-types/), such as
"INT", "FLOAT", "DATE", and so on. For example:

```
csv2parquet data.csv data.parquet --type-names "First Column" "INT" "Another Column" "FLOAT"
```

Note you can pass both `--type-names` and `--column-names` to
`csv2parquet` at once:

    # On one long line:
    csv2parquet data.csv data.parquet --column-names "First Column" "Primary Column" "Another Column" "Special Name" --type-names "First Column" "INT" "Another Column" "FLOAT"
    
    # Split across lines, for readability:
    csv2parquet data.csv data.parquet \
        --column-names "First Column" "Primary Column" "Another Column" "Special Name" \
        --type-names "First Column" "INT" "Another Column" "FLOAT"


## Troubleshooting

If you encounter a bug, run again with the `--debug` option. and note
the directory name which is printed out at startup. Many files, logs,
and other info useful for troubleshooting are stored in a temporary
folder. `--debug` prevents this from being deleted after the program
completes. See in particular `script`, `script_stderr` and
`script_stdout` from that folder. To report bugs, see "About and
Contact" below.

# Installation

Your system must have:

 * [Apache Drill](https://drill.apache.org), version 1.4 or later. Specifically, `drill-embedded` must be in your path.
 * Python 3 (version 3.5 or later).

There are no other dependencies. You can simply copy the `csv2parquet` script wherever you'd like, and run it.

Currently, `csv2parquet` runs on OS X and Linux. It has not been tested
on Windows, though Windows support is intended, and I appreciate
comments, pull requests, etc. to support Windows users.

# Future Work

In terms of priority:

 * Adding certain important features, such as delimiters other than commas
 * Running `csv2parquet` on Windows
 * Porting to work on versions of Python earlier than 3.5

Regarding Python versions: I'd like to make it work on 2.7 eventually
as well, though I consider this lower priority than anything
else. Note that Python 3 safely installs alongside Python 2 with no
conflict: even the executables are named differently ("python" for
2.7, and "python3" for 3.x). So you can [simply install
it](https://www.python.org/downloads/) to run `csv2parquet` today on
any system you control.

# About and Contact

Written by [Aaron Maxwell](http://redsymbol.net). Contact him at amax@redsymbol.net.

Licensed under GPLv3.

For bug reports, please run with the `--debug` option (see
"Troubleshooting" above), and email the `script`, `script_stderr` and
`script_stdout` files to the author, along with a description of what
happened, and a CSV file that will reproduce the error.