class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for mail in emails:
            local , domain = mail.split("@")
            local = local.split("+")[0].replace(".","")
            seen.add(local + "@" + domain)
        return len(seen)
