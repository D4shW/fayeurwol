namespace FirewallSingular.Rules
{
    public class SimpleRule : IRule
    {
        public string Name { get; }
        public IAction Action { get; }
        public IMatchStrategy Strategy { get; }

        public SimpleRule(string name, IAction action, IMatchStrategy strategy)
        {
            Name = name;
            Action = action;
            Strategy = strategy;
        }

        public bool Evaluate(PacketContext context)
        {
            return Strategy.IsMatch(context);
        }
    }
}
