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
    public partial class frmMenu : Form
    {
        List<RJButton> buttons;
        RJButton actualBtn;
        bool listar = true;

        Color focusBtn = Color.White;
        Color princBtn = Color.FromArgb(80, 60, 60);

        bool estado = false;
        int dif_tamano = 0;

        public frmMenu()
        {
            InitializeComponent();
            buttons = new List<RJButton>()
            {
                btnStats, btnCerrarSesion, btnFiles, btnListar, btnUsers
            };

            actualBtn = btnListar;

            foreach (RJButton button in buttons)
            {
                if (button.AccessibleName != "Listar")
                {
                    button.Click += btn_Click;
                }
            }

            pnlForm.Controls.Clear();
        }

        private void btnListar_Click(object sender, EventArgs e)
        {
            if (listar)
            {
                pnlMenu.Size = new Size(pnlMenu.Size.Width / 2, pnlMenu.Size.Height);
                pnlForm.Size = new Size(pnlForm.Size.Width + pnlMenu.Size.Width, pnlForm.Height);
                pnlForm.Location = new Point(pnlForm.Location.X - pnlMenu.Size.Width, pnlForm.Location.Y);
                pbxLogo.Size = new Size(4 * pbxLogo.Size.Width / 6, 4 * pbxLogo.Size.Height / 6);
                pbxLogo.Location = new Point((pnlMenu.Size.Width - pbxLogo.Size.Width) / 2, pbxLogo.Location.Y + 10);
                foreach (RJButton btn in buttons)
                {
                    btn.Size = new Size(btn.Size.Width / 2, btn.Size.Height);
                    btn.ImageAlign = ContentAlignment.MiddleCenter;
                    btn.Text = String.Empty;
                }
                listar = false;
            }
            else
            {
                pnlForm.Location = new Point(pnlForm.Location.X + pnlMenu.Size.Width, pnlForm.Location.Y);
                pnlMenu.Size = new Size(pnlMenu.Size.Width * 2, pnlMenu.Size.Height);
                pnlForm.Size = new Size(pnlForm.Size.Width - pnlMenu.Size.Width / 2, pnlForm.Height);
                pbxLogo.Size = new Size(6 * pbxLogo.Size.Width / 4, 6 * pbxLogo.Size.Height / 4);
                pbxLogo.Location = new Point((pnlMenu.Size.Width - pbxLogo.Size.Width) / 2, pbxLogo.Location.Y - 10);
                foreach (RJButton btn in buttons)
                {
                    btn.Size = new Size(btn.Size.Width * 2, btn.Size.Height);
                    btn.ImageAlign = ContentAlignment.MiddleLeft;
                    btn.Text = btn.AccessibleName;
                }
                listar = true;
            }
        }

        private void btn_Click(object sender, EventArgs e)
        {
            actualBtn.BackColor = princBtn;
            actualBtn = sender as RJButton;
            actualBtn.BackColor = focusBtn;
        }

        private void btnFiles_Click(object sender, EventArgs e)
        {
            dmFiles.Show(btnFiles, btnFiles.Width, 0);
        }

        private void btnUsers_Click(object sender, EventArgs e)
        {
            dmUsers.Show(btnUsers, btnUsers.Width, 0);
        }

        private void AjustarTamano()
        {
            dif_tamano = this.Width - pnlMenu.Size.Width;
            if (this.WindowState == FormWindowState.Maximized)
            {
                pnlMenu.Size = new Size(pnlMenu.Size.Width, this.Height);
                pnlForm.Size = new Size(dif_tamano, this.Height);
                pnlForm.Location = new Point(pnlMenu.Size.Width, pnlForm.Location.Y);
                pnlForm.ToString();
                estado = true;
            }
            else if (this.WindowState == FormWindowState.Normal)
            {
                if (estado)
                {
                    pnlForm.Location = new Point(pnlMenu.Size.Width, pnlForm.Location.Y);
                    pnlMenu.Size = new Size(pnlMenu.Size.Width, this.Height);
                    pnlForm.Size = new Size(dif_tamano, this.Height);
                    estado = false;
                }
            }
        }

        private void ResponisveEnd(object sender, EventArgs e)
        {
            AjustarTamano();
        }
    }
}


