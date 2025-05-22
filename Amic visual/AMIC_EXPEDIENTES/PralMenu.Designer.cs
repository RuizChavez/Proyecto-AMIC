namespace AMIC
{
    partial class PralMenu
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
            this.flpMenu = new System.Windows.Forms.FlowLayoutPanel();
            this.btnStats = new AMIC.RJButton();
            this.btnFiles = new AMIC.RJButton();
            this.btnUsers = new AMIC.RJButton();
            this.panel1 = new System.Windows.Forms.Panel();
            this.flowLayoutPanel2 = new System.Windows.Forms.FlowLayoutPanel();
            this.btnClose = new AMIC.RJButton();
            this.pnlPral = new System.Windows.Forms.Panel();
            this.dmFiles = new CustomControls.RJControls.RJDropdownMenu(this.components);
            this.itemFilesCreate = new System.Windows.Forms.ToolStripMenuItem();
            this.itemFilesRead = new System.Windows.Forms.ToolStripMenuItem();
            this.dmUsers = new CustomControls.RJControls.RJDropdownMenu(this.components);
            this.itemUsersCreate = new System.Windows.Forms.ToolStripMenuItem();
            this.itemUsersRead = new System.Windows.Forms.ToolStripMenuItem();
            this.flpMenu.SuspendLayout();
            this.panel1.SuspendLayout();
            this.flowLayoutPanel2.SuspendLayout();
            this.dmFiles.SuspendLayout();
            this.dmUsers.SuspendLayout();
            this.SuspendLayout();
            // 
            // flpMenu
            // 
            this.flpMenu.BackColor = System.Drawing.Color.MediumSlateBlue;
            this.flpMenu.Controls.Add(this.btnStats);
            this.flpMenu.Controls.Add(this.btnFiles);
            this.flpMenu.Controls.Add(this.btnUsers);
            this.flpMenu.FlowDirection = System.Windows.Forms.FlowDirection.TopDown;
            this.flpMenu.Location = new System.Drawing.Point(0, 52);
            this.flpMenu.Name = "flpMenu";
            this.flpMenu.Padding = new System.Windows.Forms.Padding(0, 20, 0, 0);
            this.flpMenu.Size = new System.Drawing.Size(200, 450);
            this.flpMenu.TabIndex = 3;
            // 
            // btnStats
            // 
            this.btnStats.BackColor = System.Drawing.Color.MediumSlateBlue;
            this.btnStats.BackgroundColor = System.Drawing.Color.MediumSlateBlue;
            this.btnStats.BorderColor = System.Drawing.Color.PaleVioletRed;
            this.btnStats.BorderRadius = 0;
            this.btnStats.BorderSize = 0;
            this.btnStats.FlatAppearance.BorderSize = 0;
            this.btnStats.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnStats.ForeColor = System.Drawing.Color.White;
            this.btnStats.Location = new System.Drawing.Point(0, 20);
            this.btnStats.Margin = new System.Windows.Forms.Padding(0);
            this.btnStats.Name = "btnStats";
            this.btnStats.Size = new System.Drawing.Size(200, 50);
            this.btnStats.TabIndex = 6;
            this.btnStats.Text = "Estadisticas";
            this.btnStats.TextColor = System.Drawing.Color.White;
            this.btnStats.UseVisualStyleBackColor = false;
            // 
            // btnFiles
            // 
            this.btnFiles.BackColor = System.Drawing.Color.MediumSlateBlue;
            this.btnFiles.BackgroundColor = System.Drawing.Color.MediumSlateBlue;
            this.btnFiles.BorderColor = System.Drawing.Color.PaleVioletRed;
            this.btnFiles.BorderRadius = 0;
            this.btnFiles.BorderSize = 0;
            this.btnFiles.FlatAppearance.BorderSize = 0;
            this.btnFiles.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnFiles.ForeColor = System.Drawing.Color.White;
            this.btnFiles.Location = new System.Drawing.Point(0, 70);
            this.btnFiles.Margin = new System.Windows.Forms.Padding(0);
            this.btnFiles.Name = "btnFiles";
            this.btnFiles.Size = new System.Drawing.Size(200, 50);
            this.btnFiles.TabIndex = 4;
            this.btnFiles.Text = "Expedientes";
            this.btnFiles.TextColor = System.Drawing.Color.White;
            this.btnFiles.UseVisualStyleBackColor = false;
            this.btnFiles.Click += new System.EventHandler(this.btnFiles_Click);
            // 
            // btnUsers
            // 
            this.btnUsers.BackColor = System.Drawing.Color.MediumSlateBlue;
            this.btnUsers.BackgroundColor = System.Drawing.Color.MediumSlateBlue;
            this.btnUsers.BorderColor = System.Drawing.Color.PaleVioletRed;
            this.btnUsers.BorderRadius = 0;
            this.btnUsers.BorderSize = 0;
            this.btnUsers.FlatAppearance.BorderSize = 0;
            this.btnUsers.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnUsers.ForeColor = System.Drawing.Color.White;
            this.btnUsers.Location = new System.Drawing.Point(0, 120);
            this.btnUsers.Margin = new System.Windows.Forms.Padding(0);
            this.btnUsers.Name = "btnUsers";
            this.btnUsers.Size = new System.Drawing.Size(200, 50);
            this.btnUsers.TabIndex = 5;
            this.btnUsers.Text = "Usuarios";
            this.btnUsers.TextColor = System.Drawing.Color.White;
            this.btnUsers.UseVisualStyleBackColor = false;
            this.btnUsers.Click += new System.EventHandler(this.btnUsers_Click);
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.flpMenu);
            this.panel1.Controls.Add(this.flowLayoutPanel2);
            this.panel1.Controls.Add(this.pnlPral);
            this.panel1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.panel1.Location = new System.Drawing.Point(0, 0);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(1000, 502);
            this.panel1.TabIndex = 5;
            // 
            // flowLayoutPanel2
            // 
            this.flowLayoutPanel2.BackColor = System.Drawing.SystemColors.ActiveCaptionText;
            this.flowLayoutPanel2.Controls.Add(this.btnClose);
            this.flowLayoutPanel2.FlowDirection = System.Windows.Forms.FlowDirection.RightToLeft;
            this.flowLayoutPanel2.Location = new System.Drawing.Point(0, 0);
            this.flowLayoutPanel2.Name = "flowLayoutPanel2";
            this.flowLayoutPanel2.Size = new System.Drawing.Size(1000, 52);
            this.flowLayoutPanel2.TabIndex = 4;
            // 
            // btnClose
            // 
            this.btnClose.BackColor = System.Drawing.Color.Black;
            this.btnClose.BackgroundColor = System.Drawing.Color.Black;
            this.btnClose.BorderColor = System.Drawing.Color.PaleVioletRed;
            this.btnClose.BorderRadius = 0;
            this.btnClose.BorderSize = 0;
            this.btnClose.FlatAppearance.BorderSize = 0;
            this.btnClose.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnClose.ForeColor = System.Drawing.Color.White;
            this.btnClose.Location = new System.Drawing.Point(931, 0);
            this.btnClose.Margin = new System.Windows.Forms.Padding(0);
            this.btnClose.Name = "btnClose";
            this.btnClose.Size = new System.Drawing.Size(69, 52);
            this.btnClose.TabIndex = 0;
            this.btnClose.Text = "Cerrar Sesion";
            this.btnClose.TextColor = System.Drawing.Color.White;
            this.btnClose.UseVisualStyleBackColor = false;
            // 
            // pnlPral
            // 
            this.pnlPral.Location = new System.Drawing.Point(200, 52);
            this.pnlPral.Name = "pnlPral";
            this.pnlPral.Size = new System.Drawing.Size(800, 450);
            this.pnlPral.TabIndex = 5;
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
            this.dmFiles.Size = new System.Drawing.Size(157, 48);
            // 
            // itemFilesCreate
            // 
            this.itemFilesCreate.Name = "itemFilesCreate";
            this.itemFilesCreate.Size = new System.Drawing.Size(156, 22);
            this.itemFilesCreate.Text = "Capturar nuevo";
            // 
            // itemFilesRead
            // 
            this.itemFilesRead.Name = "itemFilesRead";
            this.itemFilesRead.Size = new System.Drawing.Size(156, 22);
            this.itemFilesRead.Text = "Listar";
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
            this.dmUsers.Size = new System.Drawing.Size(121, 48);
            // 
            // itemUsersCreate
            // 
            this.itemUsersCreate.Name = "itemUsersCreate";
            this.itemUsersCreate.Size = new System.Drawing.Size(120, 22);
            this.itemUsersCreate.Text = "Registrar";
            // 
            // itemUsersRead
            // 
            this.itemUsersRead.Name = "itemUsersRead";
            this.itemUsersRead.Size = new System.Drawing.Size(120, 22);
            this.itemUsersRead.Text = "Listar";
            // 
            // PralMenu
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1000, 502);
            this.Controls.Add(this.panel1);
            this.Margin = new System.Windows.Forms.Padding(2);
            this.Name = "PralMenu";
            this.Text = "frmMenu";
            this.flpMenu.ResumeLayout(false);
            this.panel1.ResumeLayout(false);
            this.flowLayoutPanel2.ResumeLayout(false);
            this.dmFiles.ResumeLayout(false);
            this.dmUsers.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        public System.Windows.Forms.FlowLayoutPanel flpMenu;
        public RJButton btnStats;
        public RJButton btnFiles;
        public RJButton btnUsers;
        public System.Windows.Forms.Panel panel1;
        public System.Windows.Forms.FlowLayoutPanel flowLayoutPanel2;
        public CustomControls.RJControls.RJDropdownMenu dmFiles;
        public System.Windows.Forms.ToolStripMenuItem itemFilesCreate;
        public System.Windows.Forms.ToolStripMenuItem itemFilesRead;
        public CustomControls.RJControls.RJDropdownMenu dmUsers;
        public System.Windows.Forms.ToolStripMenuItem itemUsersCreate;
        public System.Windows.Forms.ToolStripMenuItem itemUsersRead;
        public System.Windows.Forms.Panel pnlPral;
        public RJButton btnClose;
    }
}