using System;

namespace Phone 
{
    public class Galaxy : Phone, IRingable
    {
         public string versionNumber;
        public int batteryPercentage;
        public string carrier;
        public string ringTone;
        public Galaxy (string versionNumber, int batteryPercentage, string carrier, string ringTone) : base(versionNumber, batteryPercentage, carrier, ringTone) 
        {}
        
        public string Ring()
        {
            return($"... {ringTone} ...");
        }
        public string Unlock()
        {
            return($"Galaxy {versionNumber} is unlocked with fingerprint");
        }

        public override void DisplayInfo()
        {
            Console.WriteLine("########################");
            Console.WriteLine("Galaxy ", versionNumber);
            Console.WriteLine("Battery Percentage ", batteryPercentage);
            Console.WriteLine("CArrier ", carrier);
            Console.WriteLine("Ring Tone ", ringTone);
            Console.WriteLine("########################");
        }

    }
}