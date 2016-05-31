using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Vigenere
{
    class Vigenere
    {
        private List<List<char>> Alphabets;
        private List<char> Default;
        private string Key;

        public string GetKey()
        {
            return Key;
        }
        public void SetKey(string value)
        {
            Debug.WriteLine(value);
            string temp = value;
            temp = temp.ToUpper();
            Debug.WriteLine("Temp = " + temp);
            string key = "";

            foreach (char letter in temp)
            {
                Debug.WriteLine("Letter = " + letter);
                if (letter >= 'A' || letter <= 'Z')
                {
                    key = key + letter;
                }
            }

            Key = key;
            setAlphabets();
        }

        public string Input { get; set; }

        private void setAlphabets()
        {
            Debug.WriteLine("Set Alphabets");
            Alphabets = new List<List<char>>();
            
            foreach (char letter in Key)
            {
                List<char> list = new List<char>();
                int start = (int)letter;

                for (int i = 0; i < 25; i++)
                {
                    char curr = (char)start;
                    list.Add(curr);
                    start = start + 1;

                    if (start > (int)'Z')
                    {
                        start = (int)'A';
                    }
                }

                Alphabets.Add(list);
            }

            Default = new List<char>();
            for (int i = 0; i < 25; i++)
            {
                Default.Add((char)(65 + i));
            }
        }

        public string Encode()
        {
            string output = "";
            Input = Input.ToUpper();
            int index = 0;

            foreach (char letter in Input)
            {
                if (letter >= 'A' && letter <= 'Z')
                {
                    List<char> curr = Alphabets[index];

                    int value = (int)letter - 65;
                    char nextChar = curr[value];
                    output = output + nextChar;

                    index++;
                    if (index == Alphabets.Count)
                    {
                        index = 0;
                    }
                }
                else
                {
                    output = output + letter;
                }
            }
            return output;
        }

        public string Decode()
        {
            string output = "";
            Input = Input.ToUpper();
            int index = 0;

            foreach (char letter in Input)
            {
                if (letter >= 'A' && letter <= 'Z')
                {
                    List<char> curr = Alphabets[index];

                    int value = 0;
                    for (int i = 0; i < curr.Count; i++ )
                    {
                        char item = curr[i];
                        if (letter == item)
                        {
                            value = i;
                        }
                    }

                    output = output + Default[value];

                    index++;
                    if (index == Alphabets.Count)
                    {
                        index = 0;
                    }
                }
                else
                {
                    output = output + letter;
                }
            }
            return output;
        }
    }
}
