import sys

class Input:
    """
    The Class Input allows typing data with the keyboard interactively.
    Supported types: String, Int, Float (Double), Boolean, Char
    """

    @staticmethod
    def read_char():
        """
        Reads a valid char value from the console.
        :return: The typed char
        """
        ok = False
        res = ''

        while not ok:
            try:
                line = input()
                if len(line) > 0:
                    res = line[0]
                    ok = True
                else:
                    # If empty line (just enter), try again or consider it invalid
                    pass
            except Exception:
                print("This is not a valid character. Try again")
        return res

    @staticmethod
    def read_string():
        """
        Reads a String from the console.
        :return: The typed string
        """
        try:
            return input()
        except Exception:
            return "There is a problem. Try again."

    @staticmethod
    def read_int():
        """
        Reads a valid integer value from the console.
        :return: The typed integer value
        """
        ok = False
        res = -1

        while not ok:
            try:
                s = input()
                if s.lower().startswith("0x"):
                    res = int(s, 16)
                else:
                    res = int(s)
                ok = True
            except ValueError:
                print("This is not a valid number. Try again")
        return res

    @staticmethod
    def read_double():
        """
        Reads a valid double (float) value from the console.
        :return: The typed double value
        """
        ok = False
        res = -1.0

        while not ok:
            try:
                res = float(input())
                ok = True
            except ValueError:
                print("This is not a valid number. Try again")
        return res

    @staticmethod
    def read_boolean():
        """
        Reads a valid boolean value from the console.
        :return: True if the typed value is 'true' (case insensitive), False otherwise.
        """
        ok = False
        res = False

        while not ok:
            try:
                s = input().lower()
                if s == 'true':
                    res = True
                    ok = True
                elif s == 'false':
                    res = False
                    ok = True
                else:
                    print("This is not a valid boolean. Try again")
            except Exception:
                print("This is not a valid boolean. Try again")
        return res
