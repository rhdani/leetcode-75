"""Given a string ``s`` possibly containing unmatched parentheses,
remove the minimum number of parentheses so the result is valid.

This implementation runs in O(n) time and O(n) space: we track indices
of unmatched opens and closes, then build the final string skipping them.
"""

def min_remove_parentheses(s):
    open_stack = []         # indices of unmatched '('
    invalid_indices = set() # indices of unmatched ')'

    for i, ch in enumerate(s):
        if ch == '(':
            open_stack.append(i)
        elif ch == ')':
            if open_stack:
                open_stack.pop()
            else:
                invalid_indices.add(i)

    # any remaining '(' indices are unmatched
    invalid_indices.update(open_stack)

    # build result skipping invalid indices
    return ''.join(ch for i, ch in enumerate(s) if i not in invalid_indices)

def main():
    inputs = ["ar)ab(abc)abd(", "a)rt)lm(ikgh)", "aq)xy())qf(a(ba)q)", 
    "(aw))kk())(w(aa)(bv(wt)r)",  "(qi)(kl)((y(yt))(r(q(g)s)"]
    for i in range(len(inputs)):
        print(i + 1, ". Input: \"", inputs[i], "\"", sep="")
        print("   Valid parentheses, after minimum removal: \"", \
         min_remove_parentheses(inputs[i]), "\"", sep="")
        print("-" * 100)

if __name__ == "__main__":
    main()
