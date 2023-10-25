class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s or len(s) < 2:
            return False
        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                # push it to the stack
                stack.append(c)
            else:
                # if the stack is empty there is no opening bracket to match
                if not stack:
                    return False
                last = stack.pop()
                # if the character is a closing bracket and the last element
                # in the stack is not the corresponding opening bracket
                if c == ')' and last != '(':
                    return False
                if c == ']' and last != '[':
                    return False
                if c == '}' and last != '{':
                    return False
        # if the stack is empty it means
        # that all the brackets were matched
        return not stack