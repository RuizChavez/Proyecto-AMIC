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
    public partial class UsersCreate : Form
    {
        public int id;
        public UsersCreate()
        {
            TopLevel = false;
            InitializeComponent();
            this.Dock = DockStyle.Fill;
            this.Refresh();
        }

        private void UsersCreate_Resize(object sender, EventArgs e)
        {
            this.Refresh();
        }

        private void roundedPanel1_Resize(object sender, EventArgs e)
        {
            this.Refresh();
        }

        private void UsersCreate_Load(object sender, EventArgs e)
        {
            this.Refresh();
        }
        int Id
        {
            set
            {
                id = value;
            }
        }
    }
}
