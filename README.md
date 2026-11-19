# lab-regex

Starter code for the **Redacted (regular expressions)** lab in CSCI 40.

[Course assignment](https://csci40.rtealwitter.com/regex/lab.html)

The sample tickets are fictional. The phone numbers and email addresses are public admissions-office contacts for the seven Claremont Colleges, checked in November 2026. Each record links to its source in `contact_source`. The Social Security and card numbers are made-up test data.

## What this program does

`lab_regex.py` holds twelve small functions that each use one regular
expression to find, count, or hide a pattern in text: digits, phone
numbers, hashtags, @-mentions, URLs, email addresses, Social Security
numbers, and 16-digit card numbers.

`review_packet.py` reads the fictional support tickets in
`support_tickets.json` and runs them through those functions, in four
stages:

- `inspect` — does the message contain digits? what are they? what does
  the message look like with every digit masked?
- `index` — pull out the phone numbers (and their area codes), URLs,
  hashtags, and mentions.
- `validate` — check whether the ticket's contact field is a single
  well-formed email address.
- `redact` — replace emails and SSNs in the message, and mask all but
  the last four digits of the card number.

## Project structure

- `lab_regex.py` — the twelve functions to complete, each with doctests.
- `review_packet.py` — reads `support_tickets.json` and prints a report
  using the functions above. You don't need to change this file.
- `support_tickets.json` — fictional sample support tickets.
- `test_lab_regex.py` — extra checks for edge cases beyond the doctests.

## How to run it

```
python review_packet.py
```

or just one stage at a time:

```
python review_packet.py --stage inspect
python review_packet.py --stage index
python review_packet.py --stage validate
python review_packet.py --stage redact
```

Expect ticket `demo-001`'s contact to be valid, `demo-002`'s to be
invalid (it has extra text after the email), `demo-001`'s card to
become `************5678`, and the redacted message to keep its
ordinary words untouched — only the email, SSN, and card change.

## How to run the tests

```
python -m doctest lab_regex.py
python test_lab_regex.py
```

The first command runs the doctests already written inside
`lab_regex.py` (no output means they all passed; add `-v` to see
every test). The second runs extra edge-case checks and prints
`All checks passed!` when everything works.

## A known limitation

`find_mentions` looks for `@` followed by letters/digits/underscores,
exactly like its doctest shows. That means it also picks up the `@cmc`
inside an email address like `admission@cmc.edu`, not just a real
`@cmc` mention elsewhere in the message. Telling those apart needs a
regex feature (a "lookbehind") beyond what this lab's doctests ask
for, so — like the module docstring in `review_packet.py` says — this
is a demonstration of the specified patterns, not a complete,
production-ready redaction tool.
