package String;
/*
# Author: Madhur Gupta
# Github: github.com/guptamadhur
# Project: HackerRank Java
# Created on: 28-09-2020 13:53
*/

/*
    Problem Statement
    Two strings are anagrams if they are permutations of each other. For example, “aaagmnrs” is an anagram of “anagrams”.
    Given an array of strings, remove each string that is an anagram of an earlier string,
    then return the remaining array in sorted order.

    For example, given the strings s = ['code', 'doce', 'ecod', 'framer', 'frame'], the strings 'doce' and 'ecod'
    are both anagrams of 'code' so they are removed from the list. The words 'frame' and 'framer' are not anagrams
    due to the extra 'r' in 'framer', so they remain. The final list of strings in alphabetical order is
    ['code', 'frame', 'framer'].

    Function Description
    Complete the function funWithAnagrams in the editor below.
    It must return a list of strings in alphabetical order, ascending.

    funWithAnagrams has the following parameters:

    s[s[0],...s[n-1]]: an array of strings
    Constraints
    1 ≤ n ≤ 1000
    1 ≤ |s[i]| ≤ 1000
    Each string s[i] is made up of characters in the range ascii[a-z]

    Sample Input For Custom Testing

    4
    code
    aaagmnrs
    anagrams
    doce
    Sample Output

    aaagmnrs
    code
    Explanation
    aaagmnrs and anagrams are anagrams, code and doce are anagrams. After sorting aaagmnrs comes first.
*/

import java.util.*;

public class Fun_with_Anagrams {
    public static void main(String[] args) {
        //List<String> a = Arrays.asList("code", "doce", "ecod", "framer", "frame");
        List<String> a = Arrays.asList("code", "aaagmnrs", "anagrams", "doce");
        System.out.println(funWithAnagrams(a));
    }

    private static List<String> funWithAnagrams(List<String> s) {
        List<String> ans = new LinkedList<>();
        Set<String> found = new HashSet<>();
        for (int i = 0; i < s.size(); i++) {
            String word = s.get(i);
            String key = key(word);
            if (!found.contains(key)) {
                ans.add(word);
                found.add(key);
            }
        }
        Collections.sort(ans);
        return ans;
    }

    private static String key(String words) {
        char[] chars = words.toCharArray();
        Arrays.sort(chars);
        return new String(chars);
    }
}
