# message-res-lint


## Install Dependencies
% `cd message-lint`

% `pip install -r requirements.txt`

## Table of Lint Rules

| Localizability (L12y) Issues   | Details                                                                           |
|--------------------------------|-----------------------------------------------------------------------------------|
| Text Fragments                 | begins with `,` or `.`                                                            |
|                                | ends with a comma                                                                 |
|                                | begins with one of the following: `and` `or`                                      |
|                                | ends with one of the following: `the` `to` `by` `on` `and` `or`                   |
| Articles before placeholders   | contains the {placeholder}, a {placeholder}, an {placeholder}, a(n) {placeholder} |
| Percentage Formatting          | contains `{placeholder}%` `{0}%`                                                  |
| URIs/URLs detected             | contains one of the following: `http://` `https://`  `<a href="...">...</a>`      |
| Lack of Pluralization          | contains a placeholder followed by: `month` `year` `week` `day` `hour` `minutes`  |
| use of ASCII Punctuation Chars | contains apostrophe (U+0027), double quote (U+0022), and 3 period (U+002E) chars  |

## How to Run

% `message-lint/bin/str-res-lint filename1.json filename2.properties`

When you run the above command line, `message_lint` will scan each message for localizability issues.
