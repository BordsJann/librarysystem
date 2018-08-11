using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Trip.Classess;
using System.Media;
using WMPLib;

namespace Trip
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Application Starting");
            PublicClass pc = new PublicClass();

            TimeSpan alarmTime = new TimeSpan(5, 30, 0);
            TimeSpan stopAlarm = new TimeSpan(6, 0, 0);

            AlarmClock clock = new AlarmClock(alarmTime, stopAlarm);
            clock.Alarm += (sender, e) => pc.Alarm();
            
        }
    }
}
