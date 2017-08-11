import re

class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """

        if IP == None:
            return "Neither"

        v4dec = '([0-9]{1,3})'
        v4regx = v4dec + '\.' + v4dec + '\.' + v4dec + '\.' + v4dec

        v6dec = '([0-9A-Fa-f]{0,4})'
        v6regx = v6dec + ':' + v6dec + ':' + v6dec + ':' + v6dec + ':' + v6dec + ':' + v6dec + ':' + v6dec + ':' + v6dec

        m = re.match(v4regx, IP)
        if m != None:
            a1 = m.group(1)
            a2 = m.group(2)
            a3 = m.group(3)
            a4 = m.group(4)

            def check_digit(d):
                if (d != '0' and d.startswith('0')) or (int(d) > 255):
                    return False
                return True

            if not check_digit(a1) or not check_digit(a2) or not check_digit(a3) or not check_digit(a4):
                return "Neither"

            return "IPv4"

        m = re.match(v6regx, IP)
        if m != None:
            return 'IPv6'

        return 'Neither'


s = Solution()
def test_addresses():

    ip = ''
    assert s.validIPAddress(ip) == 'Neither'

    ip = None
    assert s.validIPAddress(ip) == 'Neither'

    ip = '192.168.01.1'
    assert s.validIPAddress(ip) == 'Neither'

    ip = '255.255.255.256'
    assert s.validIPAddress(ip) == 'Neither'

    ip = '256.255.255.255'
    assert s.validIPAddress(ip) == 'Neither'

    ip = '255.256.255.255'
    assert s.validIPAddress(ip) == 'Neither'

    ip = '255.255.256.255'
    assert s.validIPAddress(ip) == 'Neither'

    ip = '255.255.255.256'
    assert s.validIPAddress(ip) == 'Neither'


    ip = '2a5.255.255.255'
    assert s.validIPAddress(ip) == 'Neither'

    ip = '075.255.255.255'
    assert s.validIPAddress(ip) == 'Neither'

    ip = '0x8.255.255.255'
    assert s.validIPAddress(ip) == 'Neither'

    ip = '0x8.255.255'
    assert s.validIPAddress(ip) == 'Neither'


    ip = '255.255.255.255'
    assert s.validIPAddress(ip) == 'IPv4'

    ip = "2001:0db8:85a3:::8A2E:0370:7334"
    assert s.validIPAddress(ip) == 'IPv6'

    ip = "2001:0db8:85a3::0:8A2E:0370:7334"
    assert s.validIPAddress(ip) == 'IPv6'

    ip = "2001:0db8:85a3:0:0:8A2E:0370:7334"
    assert s.validIPAddress(ip) == 'IPv6'

    ip = "2001:0db8:85a3::8A2E:0370:7334"
    assert s.validIPAddress(ip) == 'Neither'
