namespace AMIC
{
    partial class FilesUpdate
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
            this.pnlFileCreate = new System.Windows.Forms.Panel();
            this.SuspendLayout();
            // 
            // pnlFileCreate
            // 
            this.pnlFileCreate.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.pnlFileCreate.Dock = System.Windows.Forms.DockStyle.Fill;
            this.pnlFileCreate.Location = new System.Drawing.Point(0, 0);
            this.pnlFileCreate.Name = "pnlFileCreate";
            this.pnlFileCreate.Size = new System.Drawing.Size(1080, 720);
            this.pnlFileCreate.TabIndex = 0;
            // 
            // FilesCreate
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1080, 720);
            this.Controls.Add(this.pnlFileCreate);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.Margin = new System.Windows.Forms.Padding(2);
            this.Name = "FilesCreate";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "frmCaptura";
            this.ResumeLayout(false);

        }

        #endregion

        public System.Windows.Forms.Panel pnlFileCreate;
    }
}