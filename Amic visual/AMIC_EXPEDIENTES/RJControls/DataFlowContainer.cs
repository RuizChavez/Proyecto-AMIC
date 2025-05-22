using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Drawing.Printing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AMIC
{
    public partial class DataFlowContainer : Panel
    {
        public int borderRadius = 0;
        private Label label;
        public RJButton btnDelete;
        private Color backColor = Color.WhiteSmoke;
        private Color borderColor = Color.MediumSlateBlue;
        public int borderSize = 0;

        public DataFlowContainer(string data, Size size, Padding margin, Color backColor, Font font, int borderRadious, int border)
        {
            this.Size = size;
            this.Font = font;
            this.Margin = margin;
            this.BackColor = backColor;

            btnDelete = new RJButton();
            label = new Label();

            btnDelete.Size = new Size()
            {
                Width = this.Size.Height - 2 * this.Padding.All,
                Height = this.Size.Height - 2 * this.Padding.All
            };         
            label.Size = new Size() { 
                Width = this.Size.Width-btnDelete.Size.Width-3*this.Padding.All,
                Height = this.Size.Height - 2 * this.Padding.All
            };

            btnDelete.Location = new Point()
            {
                X = 2 * Padding.All + label.Size.Width,
                Y = Padding.All,
            };
            label.Location = new Point()
            {
                X = Padding.All,
                Y = Padding.All,
            };
          

            borderSize = border;
            borderRadius = borderRadious;

            this.BorderStyle = BorderStyle.None;
            this.SuspendLayout();

            label.Text = data;
            label.AutoSize = false;
            label.BackColor = Color.Transparent;
            //label.Location = new Point((this.MinimumSize.Width-label.Width)/2, (this.MinimumSize.Height - label.Height) / 2);
            label.TextAlign = ContentAlignment.MiddleCenter;
            //label.Dock = DockStyle.Fill;

            btnDelete.BackColor = Color.FromArgb(122, 8, 10);
            btnDelete.AccessibleDescription = data;
            btnDelete.Image = AMIC.Properties.Resources.cruz;

            this.Controls.Add(label);
            this.Controls.Add(btnDelete);
        }

        private GraphicsPath GetFigurePath(Rectangle rect, int radius)
        {
            GraphicsPath path = new GraphicsPath();
            float curveSize = radius * 2F;

            path.StartFigure();
            path.AddArc(rect.X, rect.Y, curveSize, curveSize, 180, 90);
            path.AddArc(rect.Right - curveSize, rect.Y, curveSize, curveSize, 270, 90);
            path.AddArc(rect.Right - curveSize, rect.Bottom - curveSize, curveSize, curveSize, 0, 90);
            path.AddArc(rect.X, rect.Bottom - curveSize, curveSize, curveSize, 90, 90);
            path.CloseFigure();
            return path;
        }

        protected override void OnPaint(PaintEventArgs pevent)
        {
            base.OnPaint(pevent);


            Rectangle rectSurface = this.ClientRectangle;
            Rectangle rectBorder = Rectangle.Inflate(rectSurface, -borderSize, -borderSize);
            int smoothSize = 2;
            if (borderSize > 0)
                smoothSize = borderSize;

            if (borderRadius > 2) //Rounded button
            {
                using (GraphicsPath pathSurface = GetFigurePath(rectSurface, borderRadius))
                using (GraphicsPath pathBorder = GetFigurePath(rectBorder, borderRadius - borderSize))
                using (Pen penSurface = new Pen(this.Parent.BackColor, smoothSize))
                using (Pen penBorder = new Pen(borderColor, borderSize))
                {
                    pevent.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
                    //Button surface
                    this.Region = new Region(pathSurface);
                    //Draw surface border for HD result
                    pevent.Graphics.DrawPath(penSurface, pathSurface);

                    //Button border                    
                    if (borderSize >= 1)
                        //Draw control border
                        pevent.Graphics.DrawPath(penBorder, pathBorder);
                }
            }
            else //Normal button
            {
                pevent.Graphics.SmoothingMode = SmoothingMode.None;
                //Button surface
                this.Region = new Region(rectSurface);
                //Button border
                if (borderSize >= 1)
                {
                    using (Pen penBorder = new Pen(borderColor, borderSize))
                    {
                        penBorder.Alignment = PenAlignment.Inset;
                        pevent.Graphics.DrawRectangle(penBorder, 0, 0, this.Width - 1, this.Height - 1);
                    }
                }
            }
        }
        protected override void OnHandleCreated(EventArgs e)
        {
            base.OnHandleCreated(e);
            this.Parent.BackColorChanged += new EventHandler(Container_BackColorChanged);
        }

        private void Container_BackColorChanged(object sender, EventArgs e)
        {
            this.Invalidate();
        }
        private void Button_Resize(object sender, EventArgs e)
        {
            if (borderRadius > this.Height)
                borderRadius = this.Height;
        }
    }
}
