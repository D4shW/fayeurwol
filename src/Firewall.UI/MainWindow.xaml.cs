using System.Windows;
using FirewallSingular.Core;   // si ton PacketFilterEngine est ici
using FirewallSingular.Rules;

namespace Firewall.UI
{
    public partial class MainWindow : Window
    {
        private readonly PacketFilterEngine _engine;

        public MainWindow()
        {
            InitializeComponent();

            var subject = new TrafficSubject();
            subject.Subscribe(new UiTrafficObserver(TrafficList));

            _engine = new PacketFilterEngine(new WfpUserModeAdapter(), subject);
            _engine.Start();
        }
    }

    public class UiTrafficObserver : ITrafficObserver
    {
        private readonly System.Windows.Controls.ListBox _list;

        public UiTrafficObserver(System.Windows.Controls.ListBox list)
        {
            _list = list;
        }

        public void OnEvent(string evt, object? payload)
        {
            Application.Current.Dispatcher.Invoke(() =>
            {
                _list.Items.Add($"{evt}: {payload}");
            });
        }
    }
}
