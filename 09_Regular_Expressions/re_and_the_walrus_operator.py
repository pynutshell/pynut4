"""
The introduction of the := operator in Python 3.8 established support for a
successive-match idiom in Python similar to one that’s common in Perl. In
this idiom, a series of if-elif branches tests a string against different
regular expressions. In Perl, the if ($var =~ /regExpr/) statement both
evaluates the regular expression and saves the successful match in the
variable var.

if    ($statement =~ /I love (\w+)/) {
  print "He loves $1\n";
}
elsif ($statement =~ /Ich liebe (\w+)/) {
  print "Er liebt $1\n";
}
elsif ($statement =~ /Je t\'aime (\w+)/) {
  print "Il aime $1\n";
}

"""
# Prior to Python 3.8, this behavior of evaluate-and-store was not possible
# in a single statement, so developers would have to use a cumbersome cascade
# of nested if-else statements:
import re
statement = "Ich liebe Maria"

m = re.match("I love (\w+)", statement)
if m:
    print(f"He loves {m.group(1)}")
else:
    m = re.match("Ich liebe (\w+)", statement)
    if m:
        print(f"Er liebt {m.group(1)}")
    else:
        m = re.match("Je t'aime (\w+)", statement)
        if m:
            print(f"Il aime {m.group(1)}")

# Using the := operator, this code simplifies to:
if m := re.match(r"I love (\w+)", statement):
    print(f"He loves {m.group(1)}")

elif m := re.match(r"Ich liebe (\w+)", statement):
    print(f"Er liebt {m.group(1)}")

elif m := re.match(r"Je t'aime (\w+)", statement):
    print(f"Il aime {m.group(1)}")


# Example taken from regex - Match groups in Python - Stack Overflow
# (https://stackoverflow.com/questions/2554185/match-groups-in-python/2555047)
