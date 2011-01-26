'''
Created on Dec 7, 2010

@author: sstafford
'''
import re;

x = "School cop";

# Test out negative lookahead regex
print(re.sub("c(?!o)", "C", x));
