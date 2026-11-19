'''Starter functions for the Redacted lab.'''

import re


def has_digit(text):
    '''
    Return True if text contains at least one digit, and False otherwise.

    >>> has_digit('Campus visit #42 booked')
    True
    >>> has_digit('no numbers here')
    False
    '''
    # re.search looks through the whole string for one match. If it
    # does not find one, it gives back None instead of a match.
    match = re.search(r'\d', text)

    if match:
        return True
    else:
        return False


def find_numbers(text):
    '''
    Return a list of every run of consecutive digits in text, as strings.

    >>> find_numbers('I booked 2 tours for 10 visitors')
    ['2', '10']
    >>> find_numbers('no numbers here')
    []
    '''
    # the '+' means "one or more", so '10' counts as one match, not two.
    numbers = re.findall(r'\d+', text)
    return numbers


def mask_digits(text):
    '''
    Return text with every digit replaced by a capital 'X'.

    >>> mask_digits('call 909-621-8088')
    'call XXX-XXX-XXXX'
    >>> mask_digits('no digits')
    'no digits'
    '''
    # re.sub finds every match of the pattern and swaps it for the
    # second argument. Everything else in the text stays the same.
    masked_text = re.sub(r'\d', 'X', text)
    return masked_text


def find_hashtags(text):
    '''
    Return a list of the hashtags in text, each without its leading '#'.

    >>> find_hashtags('Campus visit today! #CMC #Claremont #CMC')
    ['CMC', 'Claremont', 'CMC']
    >>> find_hashtags('no tags in this one')
    []
    '''
    # the parentheses mark a "capture group". findall only gives back
    # what is inside the parentheses, so the '#' itself gets left out.
    hashtags = re.findall(r'#(\w+)', text)
    return hashtags


def find_mentions(text):
    '''
    Return a list of the @-handles in text, each without its leading '@'.

    >>> find_mentions('thank you @cmc and @pomona, see you soon @cmc')
    ['cmc', 'pomona', 'cmc']
    >>> find_mentions('nobody is mentioned here')
    []
    '''
    # same idea as find_hashtags, just looking for '@' instead of '#'.
    mentions = re.findall(r'@(\w+)', text)
    return mentions


def find_urls(text):
    '''
    Return a list of the http and https URLs in text.

    >>> find_urls('read more at https://www.cmc.edu today and http://www.pomona.edu')
    ['https://www.cmc.edu', 'http://www.pomona.edu']
    >>> find_urls('no links in this tweet')
    []
    '''
    # the '?' means the letter right before it is optional, so this
    # pattern matches both 'http://' and 'https://'.
    urls = re.findall(r'https?://\S+', text)
    return urls


def find_phone_numbers(text):
    '''
    Return a list of the US phone numbers in text, in XXX-XXX-XXXX form.

    >>> find_phone_numbers('call 909-621-8088 or 800-770-1333 today')
    ['909-621-8088', '800-770-1333']
    >>> find_phone_numbers('no phone number here')
    []
    '''
    # \d{3} means "exactly three digits", so this reads as:
    # three digits, a dash, three digits, a dash, four digits.
    phone_numbers = re.findall(r'\d{3}-\d{3}-\d{4}', text)
    return phone_numbers


def area_code(phone):
    '''
    Return the three-digit area code of a XXX-XXX-XXXX phone number.

    >>> area_code('909-621-8088')
    '909'
    >>> area_code('800-770-1333')
    '800'
    '''
    # putting parentheses around the first \d{3} captures just those
    # three digits, so .group(1) can read that piece back out alone.
    match = re.match(r'(\d{3})-\d{3}-\d{4}', phone)
    first_group = match.group(1)
    return first_group


def redact_emails(text):
    '''
    Return text with every email address replaced by the string '[REDACTED]'.

    >>> redact_emails('reach me at admission@cmc.edu or admission@hmc.edu')
    'reach me at [REDACTED] or [REDACTED]'
    >>> redact_emails('this line has no email')
    'this line has no email'
    '''
    # an email here is word-characters, then @, then word-characters,
    # then a literal dot, then more word-characters (the ".edu" part).
    redacted_text = re.sub(r'\w+@\w+\.\w+', '[REDACTED]', text)
    return redacted_text


def redact_ssns(text):
    '''
    Return text with every US Social Security number masked as 'XXX-XX-XXXX'.

    >>> redact_ssns('SSN 123-45-6789 on file')
    'SSN XXX-XX-XXXX on file'
    >>> redact_ssns('no ssn in this record')
    'no ssn in this record'
    '''
    # an SSN is three digits, a dash, two digits, a dash, four digits.
    masked_text = re.sub(r'\d{3}-\d{2}-\d{4}', 'XXX-XX-XXXX', text)
    return masked_text


def mask_last_four(card):
    '''
    Return a 16-digit card number with all but its last four digits masked by '*'.

    >>> mask_last_four('1234567812345678')
    '************5678'
    >>> mask_last_four('4111111111111111')
    '************1111'
    '''
    # a 16-digit card number is 12 digits, then the last 4 digits.
    # this just replaces those first 12 digits with 12 stars, and
    # leaves the last 4 digits where they are.
    masked_card = re.sub(r'\d{12}', '************', card)
    return masked_card


def is_valid_email(s):
    '''
    Return True if the whole string s is a single valid-looking email address.

    >>> is_valid_email('admission@cmc.edu')
    True
    >>> is_valid_email('not-an-email')
    False
    >>> is_valid_email('admission@cmc.edu and some extra text')
    False
    >>> is_valid_email('admission@cmc.edu' + chr(10))
    False
    '''
    # fullmatch checks the pattern against the ENTIRE string, not just
    # part of it. That is why extra text, or an extra line, fails here.
    match = re.fullmatch(r'\w+@\w+\.\w+', s)

    if match:
        return True
    else:
        return False
