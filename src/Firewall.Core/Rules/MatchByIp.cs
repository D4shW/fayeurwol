using System.Net;

namespace FirewallSingular.Rules
{
    public class MatchByIp : IMatchStrategy
    {
        public IPAddress TargetIp { get; }
        public bool MatchSource { get; }
        public bool MatchDestination { get; }

        public MatchByIp(string ip, bool matchSource = true, bool matchDestination = false)
        {
            TargetIp = IPAddress.Parse(ip);
            MatchSource = matchSource;
            MatchDestination = matchDestination;
        }

        public bool IsMatch(PacketContext context)
        {
            if (MatchSource && context.SourceIp.Equals(TargetIp))
                return true;

            if (MatchDestination && context.DestinationIp.Equals(TargetIp))
                return true;

            return false;
        }
    }
}
