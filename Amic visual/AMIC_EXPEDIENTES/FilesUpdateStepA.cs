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
    public partial class FilesUpdateStepA : Form
    {
        public FilesUpdateStepA()
        {
            TopLevel = false;
            this.Dock = DockStyle.Fill;
            InitializeComponent();
        }

        public void setFechaEmi(int year, int month, int day)
        {
            dpFechaEmi.Value = new DateTime(year, month, day);
        }

        public void setFechaRec(int year, int month, int day)
        {
            dpFechaRec.Value = new DateTime(year, month, day);
        }

        public void setFechaCum(int year, int month, int day)
        {
            dpFechaCumpli.Value = new DateTime(year, month, day);
        }

        public void LimitDay(int year, int month, int day)
        {
            dpFechaCumpli.MaxDate = new DateTime(year, month, day);
            dpFechaEmi.MaxDate = new DateTime(year, month, day);
            dpFechaRec.MaxDate = new DateTime(year, month, day);
        }

        private void roundedPanel1_Resize(object sender, EventArgs e)
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
