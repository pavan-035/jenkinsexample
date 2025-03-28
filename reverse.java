// C# program to reverse a number
using System;

class GfG {
    static int reverseDigits(int n) {
        int revNum = 0;
        while (n > 0) {
            revNum = revNum * 10 + n % 10;
            n = n / 10;
        }
        return revNum;
    }

    public static void Main() {
        int num = 4562;
        Console.Write(reverseDigits(num));
    }
}
