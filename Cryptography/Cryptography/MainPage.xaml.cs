using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices.WindowsRuntime;
using Windows.Foundation;
using Windows.Foundation.Collections;
using Windows.UI.Xaml;
using Windows.UI.Xaml.Controls;
using Windows.UI.Xaml.Controls.Primitives;
using Windows.UI.Xaml.Data;
using Windows.UI.Xaml.Input;
using Windows.UI.Xaml.Media;
using Windows.UI.Xaml.Navigation;

using Cryptography.Business;
using System.Diagnostics;

// The Blank Page item template is documented at http://go.microsoft.com/fwlink/?LinkId=391641

namespace Cryptography
{
    /// <summary>
    /// An empty page that can be used on its own or navigated to within a Frame.
    /// </summary>
    public sealed partial class MainPage : Page
    {
        public MainPage()
        {
            this.InitializeComponent();

            this.NavigationCacheMode = NavigationCacheMode.Required;

            Caesar.Click += caesar;
            Atbash.Click += atbash;
            A1Z26.Click += a1z26;
            Vigenere.Click += vigenere;
        }

        /// <summary>
        /// Invoked when this page is about to be displayed in a Frame.
        /// </summary>
        /// <param name="e">Event data that describes how this page was reached.
        /// This parameter is typically used to configure the page.</param>
        protected override void OnNavigatedTo(NavigationEventArgs e)
        {
            // TODO: Prepare page for display here.

            // TODO: If your application contains multiple pages, ensure that you are
            // handling the hardware Back button by registering for the
            // Windows.Phone.UI.Input.HardwareButtons.BackPressed event.
            // If you are using the NavigationHelper provided by some templates,
            // this event is handled for you.
        }

        public void caesar(object sender, RoutedEventArgs e)
        {
            var offset = key.Text;
            var crypt = textBox.Text;
            Debug.WriteLine("offset = {0}, text = {1}", offset, crypt);

            try
            {
                int numberOffset = int.Parse(offset);

                Caesar cipher = new Caesar
                {
                    Offset = numberOffset,
                    Input = crypt
                };

                var output = cipher.Caesar_Cipher();
                textBox.Text = output;
            }
            catch (FormatException)
            {
                key.Text = "Offset must be an integer";
            }
        }

        public void atbash(object sender, RoutedEventArgs e)
        {
            var crypt = textBox.Text;
            Debug.WriteLine("text = {0}", crypt);

            Atbash cipher = new Atbash
            {
                Input = crypt
            };
            textBox.Text = cipher.AtbashCipher();
        }

        public void a1z26(object sender, RoutedEventArgs e)
        {
            var crypt = textBox.Text;
            Debug.WriteLine("text = {0}", crypt);

            A1Z26 cipher = new A1Z26
            {
                Input = crypt
            };
            textBox.Text = cipher.A1Z26Cipher();
        }

        //TODO: Encrypting or Decrypting!
        public void vigenere(object sender, RoutedEventArgs e)
        {
            var vigenere = key.Text;
            var crypt = textBox.Text;
            Debug.WriteLine("offset = {0}, text = {1}", vigenere, crypt);

            Vigenere cipher = new Vigenere
            {
                Input = crypt,
                Key = vigenere
            };
            textBox.Text = cipher.VigenereCipher();
        }
    }
}
