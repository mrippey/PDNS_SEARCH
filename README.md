# PDNS_SEARCH

> PDNS_SEARCH utilizes Farsight's DNSDB database to search for hosts associated with an IPv4 address. IP addresses with over 100 hosts are ignored, while any addresses with less than 100 are printed (maybe written to a file later) to possibly be added to a blocklist.
<!--
> Basic JavaScript specific YARA rules are courtesy of imp0rtp3:
 - https://github.com/imp0rtp3/js-yara-rules


![](screenshot.png)
-->
<!---
## Installation

OS X & Linux:

```sh
npm install my-crazy-module --save
```

Windows:

```sh
edit autoexec.bat
```
--->
## Usage example

```python
python passive_dns_lookup.py --ip '1.2.3.4'
python passive_dns_lookup.py --file '/some/path/to/a file of/ip addresses
```
<!---
A few motivating and useful examples of how your product can be used. Spice this up with code blocks and potentially more screenshots.

_For more examples and usage, please refer to the [Wiki][wiki]._

## Development setup

Describe how to install all development dependencies and how to run an automated test-suite of some kind. Potentially do this for multiple platforms.

```sh
make install
npm test
```
--->
## Release History
<!---
* 0.2.1
    * CHANGE: Update docs (module code remains unchanged)
* 0.2.0
    * CHANGE: Remove `setDefaultXYZ()`
    * ADD: Add `init()`
* 0.1.1
    * FIX: Crash when calling `baz()` (Thanks @GenerousContributorName!) 
* 0.1.0
    * The first proper release
    * CHANGE: Restructure files, add database connection
-->
* 0.0.1
    * Work in progress

## About

Your Name – [@nahamike01](https://twitter.com/nahamike01) 

Distributed under the GNU GPL v3.0 license. See ``LICENSE`` for more information.

[https://github.com/yourname/github-link](https://github.com/mrippey/)
