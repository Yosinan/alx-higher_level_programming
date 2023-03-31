#!/usr/bin/python3
# a Python script that fetches https://alx-intranet.hbtn.io/status
 """ fetch the given url """

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        respon = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(respon)))
        print("\t- content: {}".format(respon))
        print("\t- utf8 content: {}".format(respon.decode("UTF-8")))
