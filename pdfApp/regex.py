import re


name_regex = re.compile(r'\n[A-Z]+(?:\s+[A-Z]+)*\b')

phoneNumber_regex = re.compile(r'^Mobile :[\s\d{11}]+$')

dob_regex = re.compile(r'^Date of Birth:[\s\d+/[a-zA-z+]/\d{4}]+$')

email_regex = re.compile(r'''(
	[._%+-a-zA-z0-9]+
	@
	[a-zA-z0-9.-]+
	\.[a-zA-Z]{2,4}
	)''', re.VERBOSE)