# This program is intended to construct a series of small NFA's
# for use in a seperate program to construct larger NFA's

# References:
# https://swtch.com/~rsc/regexp/regexp1.html


stack = [] # NFA Store

def postfix_to_nfa(post_fix):
    for i, token in enumerate(post_fix):
        if