
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Diagnostics.CodeAnalysis;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Runtime.Serialization;
using System.Text.RegularExpressions;
using System.Text;
using System;

class Result
{

    /*
     * Complete the 'timeConversion' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts STRING s as parameter.
     */

    public static string timeConversion(string s)
    {
        var dt = DateTime.ParseExact(s, "hh:mm:sstt", CultureInfo.InvariantCulture);
        return $"{dt:HH:mm:ss}";
    }

}

class Solution
{
    public static void Main(string[] args)
    {
        string result = Result.timeConversion("12:00:00AM");
        Console.WriteLine(result);
    }
}
