class Solution:
    def strongPasswordChecker(self, s: str) -> int:

        @lru_cache(None)
        def dp(index, numOfCh, hasLower, hasUpper, hasDigit, lastChr, secondLastChr):
            if numOfCh > 20:
                return sys.maxsize

            if index == n:
                if numOfCh >= 6 and hasLower and hasUpper and hasDigit:
                    return 0
                else:
                    return sys.maxsize

            ans = sys.maxsize

            c = s[index]

            # keep
            if c != lastChr or c != secondLastChr:
                ans = min(ans, dp(index + 1, numOfCh + 1,
                                  hasLower or c.islower(),
                                  hasUpper or c.isupper(),
                                  hasDigit or c.isdigit(),
                                  c,
                                  lastChr))

            # insert lower case
            ans = min(ans, dp(index, numOfCh + 1,
                              True,
                              hasUpper,
                              hasDigit,
                              'y' if lastChr == 'z' else 'z',
                              lastChr) + 1)

            # insert upper case
            ans = min(ans, dp(index, numOfCh + 1,
                              hasLower,
                              True,
                              hasDigit,
                              'Y' if lastChr == 'Z' else 'Z',
                              lastChr) + 1)

            # insert digit
            ans = min(ans, dp(index, numOfCh + 1,
                              hasLower,
                              hasUpper,
                              True,
                              '8' if lastChr == '9' else '8',
                              lastChr) + 1)

            # delete
            ans = min(ans, dp(index + 1, numOfCh,
                              hasLower,
                              hasUpper,
                              hasDigit,
                              lastChr,
                              secondLastChr) + 1)

            # change to lower case
            ans = min(ans, dp(index + 1, numOfCh + 1,
                              True,
                              hasUpper,
                              hasDigit,
                              'y' if lastChr == 'z' else 'z',
                              lastChr) + 1)

            # change to upper case
            ans = min(ans, dp(index + 1, numOfCh + 1,
                              hasLower,
                              True,
                              hasDigit,
                              'Y' if lastChr == 'Z' else 'Z',
                              lastChr) + 1)

            # change digit
            ans = min(ans, dp(index + 1, numOfCh + 1,
                              hasLower,
                              hasUpper,
                              True,
                              '8' if lastChr == '9' else '8',
                              lastChr) + 1)

            return ans

        n = len(s)

        if n == 0:
            return 6

        return dp(0, 0, False, False, False, '', '')
