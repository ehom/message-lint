# message_lint

`message_lint` checks each message for localizability (L12y) issues.

## What it looks for

| `message_lint` checks each message if it...                     | L12y Issues                    |
|-----------------------------------------------------------------|--------------------------------|
| begins with `,` or `.`                                          | Text Fragments                 |
| begins with one of the following: `and` `or`                    |                                |
| ends with `,`                                                   |                                |
| ends with one of the following: `the` `to` `by` `on` `and` `or` |                                |
|                                                                 |                                |
| contains `{placeholder}` preceded by                            | Articles before placeholders   |   
| `a` `an` `a(n)` or `the`                                        |                                |
|                                                                 |                                |
| contains `{placeholder}%` `{0}%`                                | Percentage Formatting          |
|                                                                 |                                |
| contains one of the following: `http://` `https://`             | URIs/URLs embedded in messages | 
| `<a href="...">...</a>`                                         |                                |
|                                                                 |                                |
| contains `{placeholder}` followed by:                           | Lack of Pluralization          |
| `year` `month` `week` `day`                                     |                                |
| `hour` `min` `sec`                                              |                                |
| `groups` `issues` `users` `people` `other` `boards` `spaces`    |                                |
|                                                                 |                                |
| contains placeholder that uses a number `{[0-9]+}`              | Non-named placeholders         | 
|                                                                 |                                |
| contains any of following:                                      | use of ASCII Punctuation Chars |
| `'` apostrophe (U+0027)                                         |                                |
| `"` double quote (U+0022)                                       |                                | 
| `...` 3 periods (U+002E)                                        |                                |

## Install dependencies
% `cd message_lint`

% `pip install -r requirements.txt`

## First, do this

*message_lint %* `bin/message_lint --help`

```
usage: message_lint [-h] [-o OUTPUT_FOLDER] [-v] files [files ...]

lint a list of message resource files

positional arguments:
  files                 list of files to be linted

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT_FOLDER, --output_folder OUTPUT_FOLDER
                        folder where the report files will be written to.
  -v, --version         show program's version number and exit

Thanks for using message_lint!

%
```

## Diagram

![Alt text here](images/message_lint_diagram.svg)


## Now try out the test files

You must pass JSON message files and Java (message) Properties files to `message_lint`.

By default, the lint reports will be generated and located in the same directory 
as the test_files under `message_lint_reports`.

The lint reports will only be generated in `.json` format.

Here are some example command lines:

### Example 1.1

When you run the following command line, `message_lint` will examine each message in `test_files\test.json` 
and generate a report of localizability issues if any. By default, the lint reports will be generated and located in 
the same directory as the `test_files` but in `message_lint_reports`

*message_lint %* `bin/message_lint test_files\test.json`

### Example 1.2

You can also pass it more than one file.

*message_lint %* `bin/message_lint test_files\test.json test_files\test.properties`

A lint report will be generated for each message resource file.

### Example 2

You can specify a custom output folder where the lint reports will go. 

*message_lint %* `bin/message_lint test.json test.properties --output_folder ..\output`

The lint reports for this next command will located in `output\message_lint_reports`


---
