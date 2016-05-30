using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Caesar
{
    class Caesar
    {
        public int Offset { get; set; }
        public string Input { get; set; }

        public string Encode()
        {
            string output = "";

            // Case sensitive
            foreach (char letter in Input)
            {
                //Debug.WriteLine(letter);
                char curr;
                if (letter >= 'a' && letter <= 'z')
                {
                    curr = (char)((int)letter + Offset);

                    if (curr > 'z')
                    {
                        int difference = (int)curr - (int)'z';
                        curr = (char) ((int)'a' + difference - 1);
                    }
                }
                else if (letter >= 'A' && letter <= 'Z')
                {
                    curr = (char)((int)letter + Offset);

                    if (curr > 'Z')
                    {
                        int difference = (int)curr - (int)'Z';
                        curr = (char)((int)'A' + difference - 1);
                    }
                }
                else
                {
                    curr = letter;
                }
                output = output + curr;
            }

            return output;
        }

        public string Decode()
        {
            string output = "";

            // Case sensitive
            foreach (char letter in Input)
            {
                // Debug.WriteLine(letter);
                char curr;
                if (letter >= 'a' && letter <= 'z')
                {
                    curr = (char)((int)letter - Offset);

                    if (curr < 'a')
                    {
                        int difference = (int)curr - (int)'a';
                        curr = (char)((int)'z' + difference + 1);
                    }
                }
                else if (letter >= 'A' && letter <= 'Z')
                {
                    curr = (char)((int)letter - Offset);

                    if (curr < 'A')
                    {
                        int difference = (int)curr - (int)'A';
                        curr = (char)((int)'Z' + difference + 1);
                    }
                }
                else
                {
                    curr = letter;
                }
                output = output + curr;
            }

            return output;
        }
    }
}
