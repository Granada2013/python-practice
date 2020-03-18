"""
Write a function which makes a list of strings representing all of the ways you can balance n pairs of parentheses

Examples:
balanced_parens(0) => [""]
balanced_parens(1) => ["()"]
balanced_parens(2) => ["()()","(())"]
balanced_parens(3) => ["()()()","(())()","()(())","(()())","((()))"]
"""

from functools import lru_cache

@lru_cache(maxsize=None)
def balanced_parens(n):
    if n == 0: return [""]
    elif n == 1: return ["()"]
    else:
        res = []
        for elem in balanced_parens(n - 1):
            res.extend([elem[:i] + "()" + elem[i:] for i in range(len(elem))])
    return list(set(res))

