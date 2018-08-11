using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using WMPLib;

namespace Trip.Classess
{
    #region Properties

    #endregion

    public class PublicClass
    {
        public void Alarm()
        {
            WindowsMediaPlayer myplayer = new WindowsMediaPlayer();
            myplayer.URL = AppDomain.CurrentDomain.BaseDirectory + "alarm.mp3";
            myplayer.controls.play();
        }
    }
}
