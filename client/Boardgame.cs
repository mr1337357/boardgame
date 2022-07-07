using System;

using System.Windows.Forms;

namespace Boardgame
{
	public class Boardgame : Form
	{
		
		public Boardgame()
		{
			InitializeGui();
		}
		
		private void InitializeGui()
		{
            this.PerformLayout();
		}
		
		public static void Main(String[] args)
		{
			//System.Windows.Forms.Application
			Application.EnableVisualStyles();
			Application.SetCompatibleTextRenderingDefault(false);
			Application.Run(new Boardgame());
		}
	}
}
