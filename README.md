# message-res-lint


## Install Dependencies
% `cd message-lint`

% `pip install -r requirements.txt`

## Table of Lint Rules

| Localizability (L12y) Issues   | Details                                                         |
|--------------------------------|-----------------------------------------------------------------|
| Text Fragments                 | begins with `,` or `.`                                          |
|                                | begins with one of the following: `and` `or`                    |
|                                | ends with `,`                                                   |
|                                | ends with one of the following: `the` `to` `by` `on` `and` `or` |
| Articles before placeholders   | contains `{placeholder}` preceded by                            |
|                                | `a` `an` `an` or `the`                                          |
| Percentage Formatting          | contains `{placeholder}%` `{0}%`                                |
| URIs/URLs embedded in messages | contains one of the following: `http://` `https://`             |
|                                | `<a href="...">...</a>`                                         |
| Lack of Pluralization          | contains `{placeholder}` followed by:                           |
|                                | `year` `month` `week` `day`                                     |
|                                | `hour` `min` `sec`                                              |
|                                | `groups` `issues` `users` `people` `other` `boards` `spaces`    |
| Non-named placeholders         | contains placeholder that uses a number `{[0-9]+}`              |
| use of ASCII Punctuation Chars | contains any of following:                                      |
|                                | `'` apostrophe (U+0027)                                         |
|                                | `"` double quote (U+0022)                                       |
|                                | `...` 3 periods (U+002E)                                        |

## How to Run

% `message-lint/bin/str-res-lint filename1.json filename2.properties`

When you run the above command line, `message_lint` will scan each message for localizability issues.
