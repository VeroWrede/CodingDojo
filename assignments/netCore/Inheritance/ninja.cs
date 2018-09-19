using System;

namespace Inheritance {

    public class Ninja : Human 
    {
        public Ninja(string person) : base(person)
        {
            dexterity = 175;
        }

        public void steal(object obj)
        {
            health += 10;
        }

        public void get_away()
        {
            health -= 15;
        }

    }
}