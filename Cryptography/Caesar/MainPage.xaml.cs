using System;
using System.Collections.Generic;
using System.Diagnostics;
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

// The Blank Page item template is documented at http://go.microsoft.com/fwlink/?LinkId=391641

namespace Caesar
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

            Encode.Click += encode;
            Decode.Click += decode;
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

        public void encode(object o, RoutedEventArgs e)
        {
            var offsetText = Offset.Text;

            try
            {
                int offset = int.Parse(offsetText);
                string text = Textbox.Text;

                Caesar c = new Caesar
                {
                    Offset = offset,
                    Input = text
                };

                Textbox.Text = c.Encode();
            }
            catch (FormatException)
            {
                Debug.WriteLine("Invalid offset number");
            }
            catch (OverflowException)
            {
                Debug.WriteLine("Received invalid offset number");
            }
            
        }

        public void decode(object o, RoutedEventArgs e)
        {
            var offsetText = Offset.Text;

            try
            {
                int offset = int.Parse(offsetText);
                string text = Textbox.Text;

                Caesar c = new Caesar
                {
                    Offset = offset,
                    Input = text
                };

                Textbox.Text = c.Decode();
            }
            catch (FormatException)
            {
                Debug.WriteLine("Invalid offset number");
                Offset.Text = "Invalid entry, offset must be a number.";
            }
        }
    }
}
