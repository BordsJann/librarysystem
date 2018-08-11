using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Timers;

namespace Trip.Classess
{

    public class AlarmClock
    {
        #region Properties

        private EventHandler alarmEvent;
        private Timer timer;
        private TimeSpan alarmTime;
        private TimeSpan stopAlarm;
        private bool enabled;

        #endregion

        public AlarmClock(TimeSpan alarmTime,TimeSpan stopAlarmTime)
        {
            this.alarmTime = alarmTime;
            this.stopAlarm = stopAlarmTime;

            timer = new Timer();
            timer.Elapsed +=  (sender, e) => timer_Elapsed(sender, e);
            timer.Interval = 1000;
            timer.Start();

            enabled = true;

            //timer_Elapsed(this, null);
        }

        static void timer_Elapsed(object sender, ElapsedEventArgs e)
        {
            PublicClass pc = new PublicClass();
            pc.Alarm();
        }

        protected virtual void OnAlarm()
        {
            if (alarmEvent != null)
            {
                PublicClass pc = new PublicClass();
                pc.Alarm();
            }
                //alarmEvent(this, EventArgs.Empty);
        }


        public event EventHandler Alarm
        {
            add { alarmEvent += value; }
            remove { alarmEvent -= value; }
        }

    }
}
