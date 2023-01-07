# message_lint

`message_lint` scans each message for localizability (L12y) issues.

## What `message_lint` looks for 

| `message_lint` checks each message if it...                     | L12y Issues                    |
|-----------------------------------------------------------------|--------------------------------|
| begins with `,` or `.`                                          | Text Fragments                 |
| begins with one of the following: `and` `or`                    |                                |
| ends with `,`                                                   |                                |
| ends with one of the following: `the` `to` `by` `on` `and` `or` |                                |
| contains `{placeholder}` preceded by                            | Articles before placeholders   |   
| `a` `an` `an` or `the`                                          |                                |
| contains `{placeholder}%` `{0}%`                                | Percentage Formatting          |                                     
| contains one of the following: `http://` `https://`             | URIs/URLs embedded in messages | 
| `<a href="...">...</a>`                                         |                                |
| contains `{placeholder}` followed by:                           | Lack of Pluralization          |
| `year` `month` `week` `day`                                     |                                |
| `hour` `min` `sec`                                              |                                |
| `groups` `issues` `users` `people` `other` `boards` `spaces`    |                                |
| contains placeholder that uses a number `{[0-9]+}`              | Non-named placeholders         | 
| contains any of following:                                      | use of ASCII Punctuation Chars |
| `'` apostrophe (U+0027)                                         |                                |
| `"` double quote (U+0022)                                       |                                | 
| `...` 3 periods (U+002E)                                        |                                |

## Install dependencies
% `cd message_lint`

% `pip install -r requirements.txt`

## How to Run

You can pass JSON message files and Java (message) Properties files to `message_lint`.

The lint reports for `test.json` will be located in the same directory under `message_lint_reports`

% `message_lint/bin/message_lint --files test.json test.properties`

You can also pass it an output folder where the lint reports will go. The lint reports for this next command will 
located in `output\message_lint_reports`

% `message-lint/bin/message_lint --files test.json test.properties --dest ..\output`

% `message-lint/bin/message_lint --help`

```
usage: message_lint [-h] --files FILES [FILES ...] [--dest DEST]

lint a list of message resource files

optional arguments:
  -h, --help            show this help message and exit
  --files FILES [FILES ...]
                        list of files to be linted
  --dest DEST           folder where the report files will be written to.
```
