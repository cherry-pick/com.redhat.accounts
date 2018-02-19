from distutils.core import setup

setup(
    name = "com.redhat.accounts",
    version = "1",
    author = "Lars Karlitski",
    author_email = "lars@karlitski.net",
    url = "https://github.com/varlink/com.redhat.accounts",
    license = "ASL2.0",
    data_files = [
        ('lib/com.redhat', [
            'src/accounts.py',
            'src/com.redhat.accounts.varlink'
        ])
    ]
)
