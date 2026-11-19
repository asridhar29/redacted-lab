"""Extra checks for lab_regex.py, beyond the doctests in that file.

Run with:
    python test_lab_regex.py

Each check uses a plain assert statement. If every assert passes,
nothing is printed except the final "All checks passed!" message.
If one fails, Python stops and shows which line failed.
"""

from lab_regex import (
    has_digit,
    find_numbers,
    mask_digits,
    find_hashtags,
    find_mentions,
    find_urls,
    find_phone_numbers,
    area_code,
    redact_emails,
    redact_ssns,
    mask_last_four,
    is_valid_email,
)


# has_digit should say False when there really is no digit anywhere.
assert has_digit('no numbers at all, just letters') is False

# find_numbers should treat a run of digits as one string, not several.
assert find_numbers('room 123, locker 4') == ['123', '4']

# mask_digits should leave non-digit characters alone.
assert mask_digits('2 cats, 3 dogs') == 'X cats, X dogs'

# find_hashtags and find_mentions should return [] when there are none.
assert find_hashtags('no tags here') == []
assert find_mentions('no mentions here') == []

# find_hashtags and find_mentions keep duplicates in the order they appear.
assert find_hashtags('#a #b #a') == ['a', 'b', 'a']
assert find_mentions('@x @y @x') == ['x', 'y', 'x']

# find_urls should find both http and https links in the same text.
assert find_urls('try http://a.com and https://b.com') == ['http://a.com', 'https://b.com']

# find_phone_numbers should keep duplicate phone numbers, in order.
same_number_twice = find_phone_numbers('call 909-621-8088 or 909-621-8088')
assert same_number_twice == ['909-621-8088', '909-621-8088']

# area_code reads the first three digits of a phone number.
assert area_code('909-621-8088') == '909'

# redact_emails should leave text with no email address unchanged.
assert redact_emails('no email in this sentence') == 'no email in this sentence'

# redact_ssns should leave text with no SSN unchanged.
assert redact_ssns('no ssn in this sentence') == 'no ssn in this sentence'

# mask_last_four should always keep exactly the last four digits visible.
assert mask_last_four('0000000000001111') == '************1111'

# is_valid_email should reject a string with two email addresses in it.
assert is_valid_email('a@b.com c@d.com') is False

# is_valid_email should accept a plain, single, well-formed address.
assert is_valid_email('admissions@pomona.edu') is True

print('All checks passed!')
