import sys
from smith_waterman import Smithwaterman

a, b = Smithwaterman().water("alpha beta gamma", "betaphni gamma gamma")

print(a)
print(b)