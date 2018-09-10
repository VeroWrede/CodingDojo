using System;

namespace Basic13
{
    class Program
    {
        static void Main(string[] args)
        {

            Avg(new int[] {255, 7890 ,123 ,43 ,6 ,1});
            Console.WriteLine("Hello World!");
        }

        public static void OddArr(int num) {
            
            for (int i = 0; i <= num; i++) {
                if (i % 2 != 0) {
                    Console.WriteLine(i);
                };
            };
        }

        public static void Avg(int[] arr) {
            int temp = 0;
            foreach (int num in arr) {
                temp += num;
            };
            int len = arr.Length;
            int result = temp / len;
            Console.WriteLine(result);
        }

        public static void Max(int[] arr) {
            int temp = arr[0];
            foreach(int num in arr) {
                if (num > temp) {
                    temp = num;
                };
            };
            Console.WriteLine(temp);
        }

        public static void IterArr(int[] arr) {
            foreach (int num in arr) {
                Console.WriteLine(num);
            };
        }

        public static void SumNums(int num) {
            int temp = 0;
            for (int i = 0; i <= num; i++) {
                Console.WriteLine(i);
                temp += i;
                Console.WriteLine(temp);
            };
        }

        public static void PrintNums(int num) {
            for (int i = 0; i <= num; i++) {
                Console.WriteLine(i);
            };
        }

        public static void PrintOddNums(int num) {
            for (int i = 0; i <= num; i++) {
                if (i % 2 != 0) {
                    Console.WriteLine(i);
                };
            };
        }
    }
}
