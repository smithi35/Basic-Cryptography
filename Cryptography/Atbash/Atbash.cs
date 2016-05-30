using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Atbash
{
    class Atbash
    {
        public string Input { get; set; }

        public char AtbashCipher(char letter, int offset)
        {
            int temp = (int)letter - offset;
            int index = 25 - temp + offset;
            return (char)index;
        }

        public string Encode()
        {
            string output = "";

            foreach (char letter in Input)
            {
                char result;
                int offset;

                if (letter >= 'a' && letter <= 'z')
                {
                    offset = 97;
                    result = AtbashCipher(letter, offset);
                }
                else if (letter >= 'A' && letter <= 'Z')
                {
                    offset = 65;
                    result = AtbashCipher(letter, offset);
                }
                else
                {
                    result = letter;
                }
                output = output + result;
            }
            return output;
        }

        public string Decode()
        {
            return Encode();
        }
    }
}
