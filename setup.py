from distutils.core import setup

setup(
    name = "com.redhat.system",
    version = "1",
    author = "Lars Karlitski",
    author_email = "lars@karlitski.net",
    url = "https://github.com/varlink/com.redhat.system",
    license = "ASL2.0",
    data_files = [
        ('lib/com.redhat.system', [
            'accounts/accounts.py',
            'accounts/com.redhat.system.accounts.varlink'
        ])
    ]
)
