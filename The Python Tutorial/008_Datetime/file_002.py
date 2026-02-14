# In Python, the date object from the datetime module provides ways to format dates
# as strings in custom formats using the strftime() method.
"""
Common Format Codes:
--------------------
%Y  - Year with century as a decimal number (e.g., 2025)
%y  - Year without century as a zero-padded decimal number (e.g., 25)
%m  - Month as a zero-padded decimal number (01-12)
%B  - Full month name (e.g., July)
%b  - Abbreviated month name (e.g., Jul)
%d  - Day of the month as a zero-padded decimal number (01-31)
%A  - Full weekday name (e.g., Wednesday)
%a  - Abbreviated weekday name (e.g., Wed)
%H  - Hour (24-hour clock) as a zero-padded decimal number (00-23)
%I  - Hour (12-hour clock) as a zero-padded decimal number (01-12)
%p  - Locale’s AM or PM
%M  - Minute as a zero-padded decimal number (00-59)
%S  - Second as a zero-padded decimal number (00-59)

%f  - Microsecond as a decimal number, zero‑padded on the left (000000–999999)
%j  - Day of the year as a zero‑padded decimal number (001–366)
%U  - Week number of the year (Sunday as the first day of the week) as a zero‑padded decimal (00–53)
%W  - Week number of the year (Monday as the first day of the week) as a zero‑padded decimal (00–53)
%w  - Weekday as a decimal number (0=Sunday, 6=Saturday)
%G  - ISO 8601 year with century corresponding to the ISO week number (see %V)
%u  - ISO 8601 weekday as a decimal number (1=Monday, 7=Sunday)
%V  - ISO 8601 week number of the year (01–53)
%z  - UTC offset in the form ±HHMM (e.g., +0530)
%Z  - Time zone name or abbreviation (e.g., UTC, IST)
%c  - Locale’s appropriate date and time representation (e.g., ‘Wed Jul 16 14:30:00 2025’)
%x  - Locale’s appropriate date representation (e.g., ‘07/16/25’)
%X  - Locale’s appropriate time representation (e.g., ‘14:30:00’)
%%  - A literal '%' character
"""
from datetime import date

d = date(2025, 7, 16)
print(d.strftime("%B %d, %Y"))  # July 16, 2025
print(d.strftime("%d/%m/%y"))  # 16/07/25
