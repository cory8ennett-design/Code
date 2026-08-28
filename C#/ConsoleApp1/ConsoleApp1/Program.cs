public class Solution
{
    public string GetSolution(string input)
    {
        var arr = input.ToCharArray();

        for (int i = arr.Length - 1; i >= 0; i--)
        {
            Console.WriteLine(arr[i]);
        }

        return input;
    }

    public static void Main(string[] args)
    {
        var s = new Solution().GetSolution("Hellow world");
        Console.WriteLine(s);
    }
}