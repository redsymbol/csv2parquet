# csv2parquet - Create Parquet files from CSV

This simple tool creates Parquet files from CSV input. It requires [Apache Drill](https://drill.apache.org) to be installed.

Much credit for this goes to Tugdual "Tug" Grall"; csv2parquet
essentially automates the process he documents in [Convert a CSV File
to Apache Parquet With
Drill](http://tgrall.github.io/blog/2015/08/17/convert-csv-file-to-apache-parquet-dot-dot-dot-with-drill/).

# Installation

Your system must have:

 * [Apache Drill](https://drill.apache.org), version 1.4 or later.
 * Python 3 (version 3.5 or later).

There are no other dependencies. You can simply move the csv2parquet script wherever you'd like, and run it.

Currently, csv2parquet runs on OS X and Linux. It has not been tested
on Windows, though Windows support is intended, and I appreciate
comments, pull requests, etc. to help add Windows support.

# Future Work

In terms of priority:

 * Adding certain important features, including:
   - validation of header names
   - mapping CSV headers to custom Parquet column names
   - type casting
   - delimiters other than comma
 * Running csv2parquet on Windows.
 * Porting to work on versions of Python earlier than 3.5.

# About

Written by Aaron Maxwell - amax at redsymbol dot net

Licensed under GPLv3.

