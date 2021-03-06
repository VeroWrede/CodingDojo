using System;

namespace Inheritance {
    public class Wizard : Human 
    {
        public Wizard(string person) : base(person) 
        {  
            health = 50;
            intelligence = 25;
            name = person;
        }

        public void heal() 
        {
            health += 15;
        }

        public void firebal(object obj)
        {
            Human foe = obj as Human;
            Random rand = new Random();
            foe.health -= rand.Next(20, 51);
        }
    }
}