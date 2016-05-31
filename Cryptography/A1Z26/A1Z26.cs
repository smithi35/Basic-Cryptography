using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace A1Z26
{
    class A1Z26
    {
        public string Input { get; set; }

        private string GetPosition(char letter, int offset)
        {
            int value = (int)letter - offset;
            return value.ToString();
        }

        public string Encode()
        {
            string output = "";
            foreach (char letter in Input)
            {
                if (letter >= 'a' && letter <= 'z')
                {
                    if (!output.Equals(""))
                    {
                        output = output + '-';
                    }
                    string position = GetPosition(letter, 96);
                    output = output + position;
                }
                else if (letter >= 'A' && letter <= 'Z')
                {
                    if (!output.Equals(""))
                    {
                        output = output + '-';
                    }
                    string position = GetPosition(letter, 64);
                    output = output + position;
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
            string letter = "";

            foreach (char curr in Input)
            {
                if (curr >= '0' && curr <= '9')
                {
                    letter = letter + curr;
                }
                else
                {
                    if (!letter.Equals(""))
                    {
                        int value = int.Parse(letter);
                        value = value + 64;
                        output = output + (char)value;
                    }
                    if (!curr.Equals('-'))
                    {
                        output = output + curr;
                    }

                    letter = "";
                }
            }

            if (!letter.Equals(""))
            {
                int value = int.Parse(letter);
                value = value + 64;
                output = output + (char)value;
            }

            return output;
        }
    }
}
