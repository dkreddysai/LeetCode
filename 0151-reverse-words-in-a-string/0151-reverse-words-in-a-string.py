class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=s.split()
        reverse_words=words[::-1]
        reversed_string=' '.join(reverse_words)
        return reversed_string

        