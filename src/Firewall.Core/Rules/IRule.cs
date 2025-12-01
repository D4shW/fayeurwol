namespace FirewallSingular.Rules
{
    public interface IRule
    {
        string Name { get; }
        IAction Action { get; }

        bool Evaluate(PacketContext context);
    }
}
