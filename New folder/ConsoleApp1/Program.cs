using System.IO.Pipelines;

public class Solution
{
    public bool checkIfAnagrams(string str1, string str2)
    {
        var charOccurenceMap1 = new Dictionary<char, int>();
        var charOccurenceMap2 = new Dictionary<char, int>();

        foreach (char c1 in str1)
        {
            if (charOccurenceMap1.ContainsKey(c1))
            {
                charOccurenceMap1[c1]++;
            }
            else
            {
                charOccurenceMap1[c1] = 1;
            }
        }

        foreach (char c2 in str2)
        {
            if (charOccurenceMap1.ContainsKey(c2))
            {
                charOccurenceMap1[c2]++;
            }
            else
            {
                charOccurenceMap1[c2] = 1;
            }
        }

        if (charOccurenceMap1.Count != charOccurenceMap2.Count)
        {
            return false;
        }

        var result1 = charOccurenceMap1.Keys.All (x => charOccurenceMap1[x] == charOccurenceMap2[x]); 
        var result2 = charOccurenceMap2.Keys.All (x => charOccurenceMap1[x] == charOccurenceMap2[x]); 

        return result1 && result2;
    }

    static void Main(string[] args)
    {

        var pairs = new[]
        {
            ("listen", "silent"),
            ("earth", "heart"),
            ("angel", "glean"),
            ("vase", "save"),
            ("cinema", "iceman"),
            ("elbow", "below"),
            ("state", "taste"),
            ("night", "thing"),
            ("dusty", "study"),
            ("inch", "chin")
        };

        var solution = new Solution();
        foreach (var (str1, str2) in pairs)
        {
            bool areAnagrams = solution.checkIfAnagrams(str1, str2);
            Console.WriteLine($"Are '{str1}' and '{str2}' anagrams? {areAnagrams}");
        }
    }
}



