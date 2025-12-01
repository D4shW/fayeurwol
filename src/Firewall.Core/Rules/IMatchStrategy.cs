namespace FirewallSingular.Rules
{
    public interface IMatchStrategy
    {
        bool IsMatch(PacketContext context);
    }
}
