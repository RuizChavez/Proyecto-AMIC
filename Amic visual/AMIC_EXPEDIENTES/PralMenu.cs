using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AMIC
{
    public partial class PralMenu : Form
    {
        public PralMenu()
        {
            InitializeComponent();
        }

        private void btnFiles_Click(object sender, EventArgs e)
        {
            dmFiles.Show(btnFiles,btnFiles.Width,0);
        }

        private void btnUsers_Click(object sender, EventArgs e)
        {
            dmUsers.Show(btnUsers,btnUsers.Width,0);
        }
    }
}
