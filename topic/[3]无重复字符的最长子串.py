# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#  
# 
#  示例 3: 
# 
#  
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 5 * 10⁴ 
#  s 由英文字母、数字、符号和空格组成 
#  
#  Related Topics 哈希表 字符串 滑动窗口 👍 7047 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution2:
    def lengthOfLongestSubstring2(self, s: str) -> int:
        m = dict()
        ret = ll = 0
        for c in s:
            if c in m:
                ll = 0
                m = dict()
                m[c] = 1
                ll += 1
                ret = max(ret, ll)
                continue
            else:
                ll += 1

            m[c] = 1
            ret = max(ret, ll)

        return ret


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        occ = set()
        rk = -1
        ans = 0

        for i in range(n):
            if i != 0:
                occ.remove(s[i - 1])

            while rk + 1 < n and s[rk + 1] not in occ:
                occ.add(s[rk + 1])
                rk += 1
            ans = max(ans, rk - i + 1)

        return ans


# s = Solution()
# print(s.lengthOfLongestSubstring("abcabcbb"))

# x = set(['a', 'b'])
# x.add('c')
# print(x)

# leetcode submit region end(Prohibit modification and deletion)
