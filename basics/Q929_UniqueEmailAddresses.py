class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # will there be invalid email address? e.g. no @, start with +
        unique_email_addresses = set()
        for email in emails:
            local_name, domain_name = email.split("@")
            new_local_name = local_name.split('+', 1)[0].replace('.', '')
            unique_email_addresses.add(f"{new_local_name}@{domain_name}")
        return len(unique_email_addresses)

# a.b@x.com
# ab@x.com
# a.b+c@x.com
# a.b+c+d@x.com