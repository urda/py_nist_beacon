#! /usr/bin/env python

import requests
from requests.exceptions import RequestException

from py_nist_beacon.nist_beacon_value import NistBeaconValue


class NistRandomnessBeacon(object):
    NIST_BASE_URL = "https://beacon.nist.gov/rest/record"

    @classmethod
    def last_record(cls):
        try:
            r = requests.get("{}/last".format(cls.NIST_BASE_URL))
            return NistBeaconValue.from_xml(r.text)
        except RequestException:
            return None


if __name__ == '__main__':
    pass
