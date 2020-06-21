"""
"Python Data Representations".
Find differences in file contents.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    """
    The function should return the index
    of the first character that differs between the two lines. 
    """
    one=len(line1)
    two=len(line2)
    if one!=two:
        s=min(one,two)
        for i in range(s):
            if line1[i]!=line2[i]:
                return i
    return IDENTICAL
#This is only for testing
print(singleline_diff("my13ed", "2my"))
