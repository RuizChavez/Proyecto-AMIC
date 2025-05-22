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
    public partial class FilesUpdateStepB : Form
    {
        public List<string> listDelitos;
        public List<string> listImputados;
        public List<string> listOfendidos;
        public FilesUpdateStepB()
        {
            TopLevel = false;
            this.Dock = DockStyle.Fill;
            InitializeComponent();

            listDelitos = new List<string>();
            listImputados = new List<string>();
            listOfendidos = new List<string>();
        }

        public void flpDelitosAdd(string data)
        {
            DataFlowContainer dfc = new DataFlowContainer(data,
                new Size(260, 24),
                new Padding(0),
                Color.White,
                new Font(FontFamily.GenericSansSerif, 8),
                5,
                0);
            dfc.btnDelete.Click += btnDelete_Click;
            dfc.AccessibleDescription = data;
            flpDelitos.Controls.Add(dfc);

            listDelitos.Add(data);
        }

        public void flpImputadosAdd(string data)
        {
            DataFlowContainer dfc = new DataFlowContainer(data,
                new Size(260, 20),
                new Padding(0),
                Color.White,
                new Font(FontFamily.GenericSansSerif, 8),
                5,
                0);
            dfc.btnDelete.Click += btnDelete_Click;
            dfc.AccessibleDescription = data;
            flpImputados.Controls.Add(dfc);

            listImputados.Add(data);
        }

        public void flpOfendidosAdd(string data)
        {
            DataFlowContainer dfc = new DataFlowContainer(data,
                new Size(260, 20),
                new Padding(0),
                Color.White,
                new Font(FontFamily.GenericSansSerif, 8),
                5,
                0);
            dfc.btnDelete.Click += btnDelete_Click;
            dfc.AccessibleDescription = data;
            flpOfendidos.Controls.Add(dfc);

            listOfendidos.Add(data);
        }

        private void btnDelete_Click(object sender, EventArgs e)
        {
            RJButton btn = sender as RJButton;

            string ad = btn.Parent.Parent.AccessibleDescription;
            MessageBox.Show(ad);

            for (int i = 0; i < btn.Parent.Parent.Controls.Count; i++)
            {
                if (btn.Parent.Parent.Controls[i].AccessibleDescription == btn.AccessibleDescription)
                {
                    btn.Parent.Parent.Controls.RemoveAt(i);
                    break;
                }
            }
            List<string> list = new List<string>();

            if (ad == "Delitos")
            {
                list = listDelitos;
            }
            else if (ad == "Imputados")
            {
                list = listImputados;
            }
            else if (ad == "Ofendidos")
            {
                list = listOfendidos;
            }

            for (int i = 0; i < list.Count; i++)
            {
                if (list[i] == btn.AccessibleDescription)
                {
                    list.RemoveAt(i);
                    break;
                }
            }

            if (ad == "Delitos")
            {
                listDelitos = list;
            }
            else if (ad == "Imputados")
            {
                listImputados = list;
            }
            else if (ad == "Ofendidos")
            {
                listOfendidos = list;
            }
        }

        private void FilesUpdateStepB_Resize(object sender, EventArgs e)
        {
            this.Refresh();
            cbxDelito.Invalidate();
        }

        private void FilesUpdateStepB_Load(object sender, EventArgs e)
        {
            this.Refresh();
            cbxDelito.Invalidate();
        }
    }
}
