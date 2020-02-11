


class EmailManager:
    import re
    rule = re.compile(r'\S{1,20}@stevens\.edu')

    def __init__(self):
        self.emails_ = set()

    def __repr__(self):
        return '{}'.format(self.emails_)

    def update(self, emails):
        self.emails_.update(emails)

    def extract(self, content):
        emails = self.rule.findall(content)
        self.emails_.update(emails)


if __name__ == '__main__':
    test = EmailManager()
    content = 'as  sfsfsf.sfsf@stevens.edu <a> asf@stevens.edu'
    test.extract(content)
    test
