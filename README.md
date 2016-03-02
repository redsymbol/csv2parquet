# csv2parquet: Create Parquet files from CSV

This simple tool creates Parquet files from CSV input, using a minimal
installation of [Apache Drill](https://drill.apache.org). As a data
format, [Parquet](https://parquet.apache.org) offers strong advantages
over comma-separated values for big data and cloud computing needs;
`csv2parquet` is designed to let you experience those benefits more
easily.

Much credit for this goes to Tugdual "Tug" Grall; `csv2parquet`
essentially automates the process he documents in [Convert a CSV File
to Apache Parquet With
Drill](http://tgrall.github.io/blog/2015/08/17/convert-csv-file-to-apache-parquet-dot-dot-dot-with-drill/).

`csv2parquet` is now in **public beta**. Feedback, comments, bug
reports, and feature requests are all appreciated. See "About and
Contact" below to reach the author.

# Usage

```csv2parquet CSV_INPUT PARQUET_OUTPUT [--column-map ...] [--types ...] ```

`csv_input` is a CSV file, whose first line defines the column names.
`parquet_output` is the Parquet output (i.e., directory in which one
or more Parquet files are written.) Note that `csv2parquet` is
currently specifically designed to work with CSV files whose first
line defines header/column names.

## Customizing Column Names

By default, Parquet column names have the same name as the CSV header.
You can specify a different name for each output column with the
`--column-map` option.  When used, it must be followed by an even
number of strings, i.e. a sequence of pairs. In each pair, the first
string is the CSV file column name, and the second is the Parquet
column name to use instead:

```
csv2parquet data.csv data.parquet --column-map "First Column" "Primary Column" "Another Column" "Special Name"
```

In this example, two of the CSV columns are named "First Column" and
"Another Column". The created Parquet file will store data from these
columns under "Primary Column" and "Special Name", respectively.

(A perfectly good CSV column name may not be valid as a Parquet column
name - for example, a header name with a period, like
"Min. Investment". In this situation, you *must* use `--column-map`
to provide a column name that Parquet can accept, or edit the source
CSV file.)

## Column Types

By default, `csv2parquet` assumes all columns are of type string, but
you can declare specific columns to be any Drill data type. You do
this using the `--types` option, whose syntax is similar to
`--column-map`. On the command line, you write `--types`, followed by
an even number of strings that encode a sequence of pairs. In each
pair, the first string matches the name of the CSV column. (*Not* the
Parquet column name, if that is different.) The second string is one
of the [Drill data
types](https://drill.apache.org/docs/supported-data-types/), such as
"INT", "FLOAT", "DATE", and so on. For example:

```
csv2parquet data.csv data.parquet --types "First Column" "INT" "Another Column" "FLOAT"
```

Note you can pass both `--types` and `--column-map` to
`csv2parquet` at once:

    # On one long line:
    csv2parquet data.csv data.parquet --column-map "First Column" "Primary Column" "Another Column" "Special Name" --types "First Column" "INT" "Another Column" "FLOAT"
    
    # Split across lines, for readability:
    csv2parquet data.csv data.parquet \
        --column-map "First Column" "Primary Column" "Another Column" "Special Name" \
        --types "First Column" "INT" "Another Column" "FLOAT"

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

 * Python 3 (version 3.5 or later).
 * A quick-and-easy installation of [Apache Drill](https://drill.apache.org), version 1.4 or 1.5 - see below.

There are no other dependencies. You can simply copy the `csv2parquet` script wherever you'd like, and run it.

If you do not currently have Drill installed, simply
[download the tarball](https://drill.apache.org/download/), uncompress
it, and add its `bin` directory in your `$PATH`. No additional setup is
needed. (`cvs2parquet` just uses the `drill-embedded` executable.)

Currently, `csv2parquet` runs on OS X and Linux. It has not been tested
on Windows, though Windows support is intended, and I appreciate
comments, pull requests, etc. to support Windows users.

Regarding Python versions: Note that Python 3 safely installs
alongside Python 2 with no conflict: even the executables are named
differently ("python" for 2.7, and "python3" for 3.x). So you can
[simply install it](https://www.python.org/downloads/) to run
`csv2parquet` today on any system you control.

# Future Work

In terms of priority:

 * Adding certain important features, including:
   - delimiters other than commas
   - CSV files without header lines
 * Running `csv2parquet` on Windows

# About and Contact

Written by [Aaron Maxwell](http://redsymbol.net). Contact him at amax@redsymbol.net.

Licensed under GPLv3.

For bug reports, please run with the `--debug` option (see
"Troubleshooting" above), and email the `script`, `script_stderr` and
`script_stdout` files to the author, along with a description of what
happened, and a CSV file that will reproduce the error.
