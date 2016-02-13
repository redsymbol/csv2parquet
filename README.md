# csv2parquet - Create Parquet files from CSV

This simple tool creates Parquet files from CSV input. It requires [Apache Drill](https://drill.apache.org) to be installed.

Credit for this goes to Tugdual "Tug" Grall"; csv2parquet essentially
automates the process he documents in [Convert a CSV File to Apache
Parquet With
Drill](http://tgrall.github.io/blog/2015/08/17/convert-csv-file-to-apache-parquet-dot-dot-dot-with-drill/).

# Installation

You must install the following on your system:

 * [Apache Drill](https://drill.apache.org). I have only tested with version 1.5, but believe 1.4 will work as well.
 * Python 3 (version 3.4 or later).

There are no other dependencies. You can simply move the csv2parquet script wherever you'd like, and run it.

