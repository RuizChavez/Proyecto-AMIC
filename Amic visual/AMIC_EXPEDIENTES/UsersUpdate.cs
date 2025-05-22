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
    public partial class UsersUpdate : Form
    {
        public int id;
        public UsersUpdate()
        {
            TopLevel = false;
            this.Dock = DockStyle.Fill;
            InitializeComponent();
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
