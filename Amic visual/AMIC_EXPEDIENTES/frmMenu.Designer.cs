namespace AMIC
{
    partial class frmMenu
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(frmMenu));
            this.pnlForm = new System.Windows.Forms.Panel();
            this.flowLayoutPanel1 = new System.Windows.Forms.FlowLayoutPanel();
            this.btnStats = new AMIC.RJButton();
            this.btnFiles = new AMIC.RJButton();
            this.btnUsers = new AMIC.RJButton();
            this.btnCerrarSesion = new AMIC.RJButton();
            this.pnlMenu = new System.Windows.Forms.Panel();
            this.btnListar = new AMIC.RJButton();
            this.pbxLogo = new AMIC.RJCircularPictureBox();
            this.dmUsers = new CustomControls.RJControls.RJDropdownMenu(this.components);
            this.itemUsersCreate = new System.Windows.Forms.ToolStripMenuItem();
            this.itemUsersRead = new System.Windows.Forms.ToolStripMenuItem();
            this.dmFiles = new CustomControls.RJControls.RJDropdownMenu(this.components);
            this.itemFilesCreate = new System.Windows.Forms.ToolStripMenuItem();
            this.itemFilesRead = new System.Windows.Forms.ToolStripMenuItem();
            this.flowLayoutPanel1.SuspendLayout();
            this.pnlMenu.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pbxLogo)).BeginInit();
            this.dmUsers.SuspendLayout();
            this.dmFiles.SuspendLayout();
            this.SuspendLayout();
            // 
            // pnlForm
            // 
            this.pnlForm.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.pnlForm.Dock = System.Windows.Forms.DockStyle.Right;
            this.pnlForm.Location = new System.Drawing.Point(267, 0);
            this.pnlForm.Margin = new System.Windows.Forms.Padding(4);
            this.pnlForm.Name = "pnlForm";
            this.pnlForm.Size = new System.Drawing.Size(1440, 886);
            this.pnlForm.TabIndex = 13;
            // 
            // flowLayoutPanel1
            // 
            this.flowLayoutPanel1.Controls.Add(this.btnStats);
            this.flowLayoutPanel1.Controls.Add(this.btnFiles);
            this.flowLayoutPanel1.Controls.Add(this.btnUsers);
            this.flowLayoutPanel1.Controls.Add(this.btnCerrarSesion);
            this.flowLayoutPanel1.FlowDirection = System.Windows.Forms.FlowDirection.TopDown;
            this.flowLayoutPanel1.Location = new System.Drawing.Point(0, 219);
            this.flowLayoutPanel1.Margin = new System.Windows.Forms.Padding(4);
            this.flowLayoutPanel1.Name = "flowLayoutPanel1";
            this.flowLayoutPanel1.Size = new System.Drawing.Size(267, 378);
            this.flowLayoutPanel1.TabIndex = 10;
            // 
            // btnStats
            // 
            this.btnStats.AccessibleName = "Análisis";
            this.btnStats.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(80)))), ((int)(((byte)(60)))), ((int)(((byte)(60)))));
            this.btnStats.BackgroundColor = System.Drawing.Color.FromArgb(((int)(((byte)(80)))), ((int)(((byte)(60)))), ((int)(((byte)(60)))));
            this.btnStats.BorderColor = System.Drawing.Color.PaleVioletRed;
            this.btnStats.BorderRadius = 0;
            this.btnStats.BorderSize = 0;
            this.btnStats.FlatAppearance.BorderSize = 0;
            this.btnStats.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnStats.Font = new System.Drawing.Font("Lucida Sans Unicode", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnStats.ForeColor = System.Drawing.Color.White;
            this.btnStats.Image = global::AMIC.Properties.Resources.grafico_pastel_alt;
            this.btnStats.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.btnStats.Location = new System.Drawing.Point(0, 0);
            this.btnStats.Margin = new System.Windows.Forms.Padding(0);
            this.btnStats.Name = "btnStats";
            this.btnStats.Padding = new System.Windows.Forms.Padding(13, 0, 13, 0);
            this.btnStats.Size = new System.Drawing.Size(267, 74);
            this.btnStats.TabIndex = 3;
            this.btnStats.Text = "Análisis";
            this.btnStats.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.btnStats.TextColor = System.Drawing.Color.White;
            this.btnStats.UseVisualStyleBackColor = false;
            // 
            // btnFiles
            // 
            this.btnFiles.AccessibleName = "Expedientes";
            this.btnFiles.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(80)))), ((int)(((byte)(60)))), ((int)(((byte)(60)))));
            this.btnFiles.BackgroundColor = System.Drawing.Color.FromArgb(((int)(((byte)(80)))), ((int)(((byte)(60)))), ((int)(((byte)(60)))));
            this.btnFiles.BorderColor = System.Drawing.Color.PaleVioletRed;
            this.btnFiles.BorderRadius = 0;
            this.btnFiles.BorderSize = 0;
            this.btnFiles.FlatAppearance.BorderSize = 0;
            this.btnFiles.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnFiles.Font = new System.Drawing.Font("Lucida Sans Unicode", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnFiles.ForeColor = System.Drawing.Color.White;
            this.btnFiles.Image = global::AMIC.Properties.Resources.archivar_factura;
            this.btnFiles.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.btnFiles.Location = new System.Drawing.Point(0, 74);
            this.btnFiles.Margin = new System.Windows.Forms.Padding(0);
            this.btnFiles.Name = "btnFiles";
            this.btnFiles.Padding = new System.Windows.Forms.Padding(13, 0, 13, 0);
            this.btnFiles.Size = new System.Drawing.Size(267, 74);
            this.btnFiles.TabIndex = 4;
            this.btnFiles.Text = "Expedientes";
            this.btnFiles.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.btnFiles.TextColor = System.Drawing.Color.White;
            this.btnFiles.UseVisualStyleBackColor = false;
            this.btnFiles.Click += new System.EventHandler(this.btnFiles_Click);
            // 
            // btnUsers
            // 
            this.btnUsers.AccessibleName = "Usuarios";
            this.btnUsers.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(80)))), ((int)(((byte)(60)))), ((int)(((byte)(60)))));
            this.btnUsers.BackgroundColor = System.Drawing.Color.FromArgb(((int)(((byte)(80)))), ((int)(((byte)(60)))), ((int)(((byte)(60)))));
            this.btnUsers.BorderColor = System.Drawing.Color.PaleVioletRed;
            this.btnUsers.BorderRadius = 0;
            this.btnUsers.BorderSize = 0;
            this.btnUsers.FlatAppearance.BorderSize = 0;
            this.btnUsers.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnUsers.Font = new System.Drawing.Font("Lucida Sans Unicode", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnUsers.ForeColor = System.Drawing.Color.White;
            this.btnUsers.Image = global::AMIC.Properties.Resources.usuarios;
            this.btnUsers.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.btnUsers.Location = new System.Drawing.Point(0, 148);
            this.btnUsers.Margin = new System.Windows.Forms.Padding(0);
            this.btnUsers.Name = "btnUsers";
            this.btnUsers.Padding = new System.Windows.Forms.Padding(13, 0, 13, 0);
            this.btnUsers.Size = new System.Drawing.Size(267, 74);
            this.btnUsers.TabIndex = 5;
            this.btnUsers.Text = "Usuarios";
            this.btnUsers.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.btnUsers.TextColor = System.Drawing.Color.White;
            this.btnUsers.UseVisualStyleBackColor = false;
            this.btnUsers.Click += new System.EventHandler(this.btnUsers_Click);
            // 
            // btnCerrarSesion
            // 
            this.btnCerrarSesion.AccessibleName = "Cerrar sesión";
            this.btnCerrarSesion.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(80)))), ((int)(((byte)(60)))), ((int)(((byte)(60)))));
            this.btnCerrarSesion.BackgroundColor = System.Drawing.Color.FromArgb(((int)(((byte)(80)))), ((int)(((byte)(60)))), ((int)(((byte)(60)))));
            this.btnCerrarSesion.BorderColor = System.Drawing.Color.PaleVioletRed;
            this.btnCerrarSesion.BorderRadius = 0;
            this.btnCerrarSesion.BorderSize = 0;
            this.btnCerrarSesion.FlatAppearance.BorderSize = 0;
            this.btnCerrarSesion.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnCerrarSesion.Font = new System.Drawing.Font("Lucida Sans Unicode", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnCerrarSesion.ForeColor = System.Drawing.Color.White;
            this.btnCerrarSesion.Image = global::AMIC.Properties.Resources.salida;
            this.btnCerrarSesion.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.btnCerrarSesion.Location = new System.Drawing.Point(0, 222);
            this.btnCerrarSesion.Margin = new System.Windows.Forms.Padding(0);
            this.btnCerrarSesion.Name = "btnCerrarSesion";
            this.btnCerrarSesion.Padding = new System.Windows.Forms.Padding(13, 0, 13, 0);
            this.btnCerrarSesion.Size = new System.Drawing.Size(267, 74);
            this.btnCerrarSesion.TabIndex = 8;
            this.btnCerrarSesion.Text = "Cerrar sesión";
            this.btnCerrarSesion.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.btnCerrarSesion.TextColor = System.Drawing.Color.White;
            this.btnCerrarSesion.UseVisualStyleBackColor = false;
            // 
            // pnlMenu
            // 
            this.pnlMenu.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(80)))), ((int)(((byte)(60)))), ((int)(((byte)(60)))));
            this.pnlMenu.Controls.Add(this.btnListar);
            this.pnlMenu.Controls.Add(this.pbxLogo);
            this.pnlMenu.Controls.Add(this.flowLayoutPanel1);
            this.pnlMenu.Location = new System.Drawing.Point(0, 0);
            this.pnlMenu.Margin = new System.Windows.Forms.Padding(4);
            this.pnlMenu.Name = "pnlMenu";
            this.pnlMenu.Size = new System.Drawing.Size(267, 886);
            this.pnlMenu.TabIndex = 14;
            // 
            // btnListar
            // 
            this.btnListar.AccessibleName = "Listar";
            this.btnListar.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(80)))), ((int)(((byte)(60)))), ((int)(((byte)(60)))));
            this.btnListar.BackgroundColor = System.Drawing.Color.FromArgb(((int)(((byte)(80)))), ((int)(((byte)(60)))), ((int)(((byte)(60)))));
            this.btnListar.BorderColor = System.Drawing.Color.PaleVioletRed;
            this.btnListar.BorderRadius = 0;
            this.btnListar.BorderSize = 0;
            this.btnListar.FlatAppearance.BorderSize = 0;
            this.btnListar.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnListar.Font = new System.Drawing.Font("Lucida Sans Unicode", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.btnListar.ForeColor = System.Drawing.Color.White;
            this.btnListar.Image = global::AMIC.Properties.Resources.menu_1;
            this.btnListar.ImageAlign = System.Drawing.ContentAlignment.MiddleLeft;
            this.btnListar.Location = new System.Drawing.Point(0, 626);
            this.btnListar.Margin = new System.Windows.Forms.Padding(0);
            this.btnListar.Name = "btnListar";
            this.btnListar.Padding = new System.Windows.Forms.Padding(13, 0, 13, 0);
            this.btnListar.Size = new System.Drawing.Size(267, 74);
            this.btnListar.TabIndex = 11;
            this.btnListar.Text = "Listar";
            this.btnListar.TextAlign = System.Drawing.ContentAlignment.MiddleRight;
            this.btnListar.TextColor = System.Drawing.Color.White;
            this.btnListar.UseVisualStyleBackColor = false;
            this.btnListar.Click += new System.EventHandler(this.btnListar_Click);
            // 
            // pbxLogo
            // 
            this.pbxLogo.BorderCapStyle = System.Drawing.Drawing2D.DashCap.Flat;
            this.pbxLogo.BorderColor = System.Drawing.Color.RoyalBlue;
            this.pbxLogo.BorderColor2 = System.Drawing.Color.HotPink;
            this.pbxLogo.BorderLineStyle = System.Drawing.Drawing2D.DashStyle.Solid;
            this.pbxLogo.BorderSize = 0;
            this.pbxLogo.GradientAngle = 50F;
            this.pbxLogo.Image = global::AMIC.Properties.Resources.logo;
            this.pbxLogo.Location = new System.Drawing.Point(47, 25);
            this.pbxLogo.Margin = new System.Windows.Forms.Padding(4);
            this.pbxLogo.Name = "pbxLogo";
            this.pbxLogo.Size = new System.Drawing.Size(173, 173);
            this.pbxLogo.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pbxLogo.TabIndex = 9;
            this.pbxLogo.TabStop = false;
            // 
            // dmUsers
            // 
            this.dmUsers.ImageScalingSize = new System.Drawing.Size(20, 20);
            this.dmUsers.IsMainMenu = false;
            this.dmUsers.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.itemUsersCreate,
            this.itemUsersRead});
            this.dmUsers.MenuItemHeight = 25;
            this.dmUsers.MenuItemTextColor = System.Drawing.Color.Empty;
            this.dmUsers.Name = "dmUsers";
            this.dmUsers.PrimaryColor = System.Drawing.Color.Empty;
            this.dmUsers.Size = new System.Drawing.Size(138, 52);
            // 
            // itemUsersCreate
            // 
            this.itemUsersCreate.Name = "itemUsersCreate";
            this.itemUsersCreate.Size = new System.Drawing.Size(137, 24);
            this.itemUsersCreate.Text = "Registrar";
            // 
            // itemUsersRead
            // 
            this.itemUsersRead.Name = "itemUsersRead";
            this.itemUsersRead.Size = new System.Drawing.Size(137, 24);
            this.itemUsersRead.Text = "Listar";
            // 
            // dmFiles
            // 
            this.dmFiles.ImageScalingSize = new System.Drawing.Size(20, 20);
            this.dmFiles.IsMainMenu = false;
            this.dmFiles.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.itemFilesCreate,
            this.itemFilesRead});
            this.dmFiles.MenuItemHeight = 25;
            this.dmFiles.MenuItemTextColor = System.Drawing.Color.Empty;
            this.dmFiles.Name = "dmFiles";
            this.dmFiles.PrimaryColor = System.Drawing.Color.Empty;
            this.dmFiles.Size = new System.Drawing.Size(180, 52);
            // 
            // itemFilesCreate
            // 
            this.itemFilesCreate.Name = "itemFilesCreate";
            this.itemFilesCreate.Size = new System.Drawing.Size(179, 24);
            this.itemFilesCreate.Text = "Capturar nuevo";
            // 
            // itemFilesRead
            // 
            this.itemFilesRead.Name = "itemFilesRead";
            this.itemFilesRead.Size = new System.Drawing.Size(179, 24);
            this.itemFilesRead.Text = "Listar";
            // 
            // frmMenu
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1707, 886);
            this.Controls.Add(this.pnlMenu);
            this.Controls.Add(this.pnlForm);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.Name = "frmMenu";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "frmMenu";
            this.Resize += new System.EventHandler(this.ResponisveEnd);
            this.flowLayoutPanel1.ResumeLayout(false);
            this.pnlMenu.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.pbxLogo)).EndInit();
            this.dmUsers.ResumeLayout(false);
            this.dmFiles.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion
        private RJCircularPictureBox pbxLogo;
        private System.Windows.Forms.FlowLayoutPanel flowLayoutPanel1;
        private System.Windows.Forms.Panel pnlMenu;
        public CustomControls.RJControls.RJDropdownMenu dmUsers;
        public System.Windows.Forms.ToolStripMenuItem itemUsersCreate;
        public System.Windows.Forms.ToolStripMenuItem itemUsersRead;
        public CustomControls.RJControls.RJDropdownMenu dmFiles;
        public System.Windows.Forms.ToolStripMenuItem itemFilesCreate;
        public System.Windows.Forms.ToolStripMenuItem itemFilesRead;
        public RJButton btnStats;
        public RJButton btnFiles;
        public RJButton btnUsers;
        public RJButton btnCerrarSesion;
        public RJButton btnListar;
        public System.Windows.Forms.Panel pnlForm;
    }
}