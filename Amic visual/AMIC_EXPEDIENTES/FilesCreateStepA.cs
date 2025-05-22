using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Windows.Forms.DataVisualization.Charting;

namespace AMIC
{
    public partial class FilesCreateStepA : Form
    {
        public FilesCreateStepA()
        {
            TopLevel = false;
            this.Dock = DockStyle.Fill;
            InitializeComponent();

        }

        public void LimitDay(int year, int month, int day)
        {
            dpFechaCumpli.MaxDate = new DateTime(year, month, day);
            dpFechaEmi.MaxDate = new DateTime(year, month, day);
            dpFechaRec.MaxDate = new DateTime(year, month, day);
        }

        private void FilesCreateStepA_Resize(object sender, EventArgs e)
        {
            this.Refresh();
            cbxDepto.Invalidate();
            cbxAgencia.Invalidate();
            cbxClasificacionHecho.Invalidate();
            cbxColaboracion.Invalidate();
            cbxStatus.Invalidate();
        }
    }
}
