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
    public partial class FilesRead : Form
    {
        public FilesRead()
        {
            TopLevel = false;
            this.Dock = DockStyle.Fill;
            InitializeComponent();
        }

        private void roundedPanel1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void FilesRead_ResizeEnd(object sender, EventArgs e)
        {
            cbxAgencia.Invalidate();
            cbxBase.Invalidate();
            cbxDelito.Invalidate(); 
            cbxStatus.Invalidate(); 
            this.Refresh();
        }
    }
}
