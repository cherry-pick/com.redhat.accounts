#!/usr/bin/python3

import getopt
import os
import pwd
import subprocess
import sys

import varlink

service = varlink.Service(
    vendor='Red Hat',
    product='Accounts Manager',
    version='1',
    interface_dir=os.path.dirname(__file__)
)


def account_from_pw(pw):
    return {
        'name': pw.pw_name,
        'uid': pw.pw_uid,
        'gid': pw.pw_gid,
        'full_name': pw.pw_gecos.split(',')[0],
        'home': pw.pw_dir,
        'shell': pw.pw_shell
    }


class AccountCreationFailed(varlink.VarlinkError):
    def __init__(self, field):
        varlink.VarlinkError.__init__(self, {'error': 'com.redhat.accounts.CreationFailed',
                                             'parameters': {'field': field}})


class ServiceRequestHandler(varlink.RequestHandler):
    service = service


@service.interface('com.redhat.accounts')
class Accounts:
    def GetAll(self):
        return {'accounts': [account_from_pw(pw) for pw in pwd.getpwall()]}

    def GetByUid(self, uid):
        return {'account': account_from_pw(pwd.getpwuid(uid))}

    def GetByName(self, name):
        return {'account': account_from_pw(pwd.getpwnam(name))}

    def Add(self, account):
        if not 'name' in account:
            raise varlink.InvalidParameter('name')

        name = account['name']

        command = ['useradd']
        if 'uid' in account:
            command.append('-u')
            command.append(str(account['uid']))
        if 'gid' in account:
            command.append('-g')
            command.append(str(account['gid']))
        if 'home' in account:
            command.append('-d')
            command.append(account['home'])
        if 'shell' in account:
            command.append('-s')
            command.append(account['shell'])

        command.append(name)
        r = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if r.returncode == 4:
            raise AccountCreationFailed('uid')
        elif r.returncode == 9:
            raise AccountCreationFailed('name')
        elif r.returncode != 0:
            raise AccountCreationFailed()

        if 'full_name' in account:
            subprocess.run(['chfn', '-f', account['full_name'], name], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        return {'account': account_from_pw(pwd.getpwnam(name))}


def run_server(address):
    with varlink.ThreadingServer(address, ServiceRequestHandler) as server:
        print("Listening on", server.server_address)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


def usage():
    print('Usage: %s [--varlink=<varlink address>]' % sys.argv[0], file=sys.stderr)


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "", ["help", "varlink="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    address = None
    client_mode = False

    for opt, arg in opts:
        if opt == "--help":
            usage()
            sys.exit(0)
        elif opt == "--varlink":
            address = arg

    if not address:
        usage()
        sys.exit(2)

    run_server(address)

    sys.exit(0)
