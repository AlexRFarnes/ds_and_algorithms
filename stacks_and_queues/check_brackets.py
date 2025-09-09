# check_brackets.py

from stack_linked_list import Stack


def check_brackets(expression: str) -> bool:
    """Check if the brackets in the expression are balanced.

    Args:
        expression (str): The input expression containing brackets.
                          It may include other characters as well."""
    stack = Stack()
    pairs = {")": "(", "}": "{", "]": "["}
    for ch in expression:
        if ch in pairs.values():  # If it's one of '(', '{', '['
            stack.push(ch)
        elif ch in pairs:  # If it's one of ')', '}', ']'
            if stack.size == 0 or stack.pop() != pairs[ch]:
                return False
    return stack.size == 0


if __name__ == "__main__":

    sl = (
        "{(foo)(bar)}[hello](((this)is)a)test",
        "{(foo)(bar)}[hello](((this)is)atest",
        "{(foo)(bar)}[hello](((this)is)a)test))",
    )
    for s in sl:
        m = check_brackets(s)
        print("{}: {}".format(s, m))
