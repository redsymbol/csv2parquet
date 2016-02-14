# csv2parquet: Create Parquet files from CSV

This simple tool creates Parquet files from CSV input. It requires [Apache Drill](https://drill.apache.org) to be installed.

Much credit for this goes to Tugdual "Tug" Grall"; `csv2parquet`
essentially automates the process he documents in [Convert a CSV File
to Apache Parquet With
Drill](http://tgrall.github.io/blog/2015/08/17/convert-csv-file-to-apache-parquet-dot-dot-dot-with-drill/).

# Usage

```csv2parquet CSV_INPUT PARQUET_OUTPUT [--column-names ...]```

`csv_input` is a CSV file, whose first line defines the column names.
`parquet_output` is the Parquet output (i.e., directory in which one or
more Parquet files are written.)

To see Drill logs and other intermediate files, add the `--debug` option.

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

(A CSV column name may not be valid as a Parquet column name - for
example, a header name with a period, like "Min. Investment". In this
situation, you *must* use `--column-names` to provide a valid column
name, or edit the source CSV file.)

# Installation

Your system must have:

 * [Apache Drill](https://drill.apache.org), version 1.4 or later.
 * Python 3 (version 3.5 or later).

There are no other dependencies. You can simply copy the `csv2parquet` script wherever you'd like, and run it.

Currently, `csv2parquet` runs on OS X and Linux. It has not been tested
on Windows, though Windows support is intended, and I appreciate
comments, pull requests, etc. to support Windows users.

# Future Work

In terms of priority:

 * Adding certain important features, including:
   - type casting
   - delimiters other than comma
 * Running `csv2parquet` on Windows.
 * Porting to work on versions of Python earlier than 3.5.

# About

Written by Aaron Maxwell - amax at redsymbol dot net

Licensed under GPLv3.

