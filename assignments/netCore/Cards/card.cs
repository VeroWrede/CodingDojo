// public class Card 
// {
//     public string stringVal { get; set}
//     public string suit { get; set }
//     public int val { get; set }
// }

public class Deck 
{
    public string cards { get; set }

    public Deck (Card[] cards)
    {
        if (cards.Distinct().Length < 52)
        {
            Console.WriteLine("this is not a ful Deck!");
        };
    }
}