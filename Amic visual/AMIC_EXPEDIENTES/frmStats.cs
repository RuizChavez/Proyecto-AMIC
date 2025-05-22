
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms.DataVisualization.Charting;
using System.Windows.Forms;
using System.Xml.Linq;

namespace AMIC
{
    public partial class frmStats : Form
    {
        public Series series_ChartSemaforo;
        public Series series_ChartDias;
        public Series series_ChartCrimenes;

        public string[] fecha;
        public int[] numDelitos;
        public string[] nom_Delitos;
        public int[] cantidad_Del;

        public int alto;
        public int ancho;

        public string legend1 = "";
        public string legend2 = "";
        public string legend3 = "";

        public string color1 = "";
        public string color2 = "";
        public string color3 = "";

        public DataPoint point_S01;
        public DataPoint point_S02;
        public DataPoint point_S03;

        List<string> delitos;
        List<object> dataList;
        public frmStats()
        {
            TopLevel = false;
            this.Dock = DockStyle.Fill;
            InitializeComponent();
            dpInicio.Value = new DateTime(2023, 1, 1);
            delitos = new List<string>()
            {
                "DELITO",
                "ABANDONO DE PERSONAS",
                "ABIGEATO POR ALTERACION DE MARCAS",
                "ABIGEATO POR POSESION, TRANSPORTE O SACRIFICIO",
                "ABIGEATOS",
                "ABORTO",
                "ABUSO DE AUTORIDAD",
                "ABUSO DE CONFIANZA",
                "ABUSOS DESHONESTOS",
                "ACC AUTOMOVILISTICOS",
                "ACC FERROVIARIO",
                "ACCIDENTE AEREO",
                "ADULTERIO",
                "ALLANAMIENTO DE MORADA",
                "ALTA DE ELEMENTO A LA COORPORACION",
                "AMENAZAS",
                "AMOTINAMIENTO",
                "ARMAS DECOMISADAS",
                "ASALTO",
                "ASALTO EN TENTATIVA",
                "BIGAMIA",
                "CALUMNIA",
                "CATEO",
                "CHANTAJE",
                "CITATORIOS ENTREGA",
                "COBRO INDEBIDO DE UN FUNCIONARIO (CONCUSION)",
                "COHECHO",
                "COMISION DE SERVICIO",
                "CORRUPCION DE MENORES",
                "DAÑOS",
                "DELITO COMETIDO EN LA ADMINISTRACION DE JUSTICIA",
                "DELITO CONTRA EL TRABAJO Y LA PREVENSION SOCIAL",
                "DELITO DE SUJETO A CONCURSO",
                "DELITOS DE ABOGADOS PATRONOS Y LITIGANTES",
                "DESALOJO",
                "DESPOJO",
                "DIFAMACION",
                "DROGA DECOMISADA",
                "EJERCICIO ABUSIVO DE FUNCIONES",
                "ENCUBRIMIENTO",
                "ESTUPRO",
                "EVASION DE PRESOS",
                "EXHUMACION",
                "EXPOSICION DE INFANTES",
                "EXTORSION",
                "FALSA ALARMA BANCARIA",
                "FALSEDAD EN DECLARACIONES",
                "FALSIFICACION",
                "FILTROS DE REVISION",
                "FRAUDE GENERICO",
                "FUGA DE REOS",
                "HOMICIDIO CULPOSO",
                "HOMICIDIO EN TENTATIVA",
                "HOMICIDIOS",
                "HOMICIDIOS RESUELTOS",
                "HOSTIGAMIENTO SEXUAL",
                "INCESTO",
                "INCUMPLIMIENTO DE OBLIGACIONES FAMILIARES",
                "INF LEY ALCOHOLES",
                "INF LEY GANADERIA",
                "INHUMACION",
                "INJURIAS",
                "INTIMIDACION",
                "INVASION",
                "LENOCINIO",
                "LESIONES",
                "LESIONES TUMULTUARIAS CON ARMAS",
                "LEVANTAMIENTO DE HUELLAS",
                "LOCALIZACION DE EXPLOSIVOS",
                "LOCALIZACION DE OSAMENTA HUMANA",
                "LOCALIZACION DE PISTA CLANDESTINA",
                "MUERTE ANIMALES (EXTRAÑA)",
                "MUERTE POR ENFRENTAMIENTO",
                "PECULADO",
                "PERSONAS DETENIDAS",
                "PERSONAS EXTRAVIADAS",
                "PLANTIOS LOCALIZADOS",
                "PLANTON",
                "PORNOGRAFIA INFANTIL",
                "PRIVACION ILEGAL DE LA LIBERTAD",
                "PROFANACION DE CADAVER",
                "RAPTOS",
                "RECEPCION DE ORDEN DE APREHENSION",
                "RESPONSABILIDAD MEDICA Y TECNICA",
                "RIÑA, ASONADA O MOTIN",
                "ROBO CON VIOLENCIA (NO INCLUYE ASALTOS)",
                "ROBO DE INFANTE",
                "ROBO EN CONDICION DE CATASTROFE O DESASTRE",
                "ROBO SIMPLE (SIN FORZAR NADA)",
                "SECUESTRO",
                "SOBORNO A FUNCIONARIOS PUBLICOS (COHECHO)",
                "SUICIDIO",
                "SUPOSICION, SUPRESION, OCULTACION Y SUBSTITUCION",
                "TRAFICO DE ARMAS PROHIBIDAS",
                "TRAFICO DE INFLUENCIA",
                "TRASLADOS",
                "TRATA DE PERSONAS",
                "ULTRAJES A LA MORAL PUBLICA",
                "USO INDEBIDO DE ATRIBUCIONES Y FACULTADES",
                "USURPACION",
                "VARIACION DEL DOMICILIO",
                "VARIACION DEL NOMBRE",
                "VEHICULO ROBADO",
                "VEHICULO INVESTIGACION",
                "VEHICULO TRASLADO",
                "VENTA CLANDESTINA",
                "VIOLACION",
                "VIOLACION DE GARANTIAS INDIVIDUALES",
                "VIOLACION DE TUMULO",
                "VIOLENCIA INTRAFAMILIAR"
            };

            series_ChartSemaforo = new Series("datos")
            {
                ChartType = SeriesChartType.Pie
            };

            series_ChartDias = new Series("datos")
            {
                ChartType = SeriesChartType.SplineArea,
                BackGradientStyle = GradientStyle.LeftRight,
                BackSecondaryColor = Color.Aqua
            };

            series_ChartCrimenes = new Series("datos")
            {
                ChartType = SeriesChartType.Doughnut
            };

            point_S01 = new DataPoint(0, 1);
            point_S02 = new DataPoint(0, 1);
            point_S03 = new DataPoint(0, 1);

            dataList = new List<object>();

        }

        public string[] Nom_Delitos
        {
            set
            {
                nom_Delitos = value;
            }
        }
        public int[] Cantidad_Del
        {
            set
            {
                cantidad_Del = value;
                series_ChartCrimenes.Points.Clear();
                chart_Crimenes.Series.Clear();
                for (int i = 0; i < cantidad_Del.Length; i++)
                {
                    series_ChartCrimenes.Points.AddXY(nom_Delitos[i], cantidad_Del[i]);
                    series_ChartCrimenes.IsValueShownAsLabel = false;
                }
                chart_Crimenes.Series.Add(series_ChartCrimenes);
                chart_Crimenes.Update();
            }
        }

        public string[] Fecha
        {
            set
            {
                fecha = value;
            }
        }
        public int[] NumDelitos
        {
            set
            {
                numDelitos = value;

                if (numDelitos.Length == 0)
                {
                    chart_Dias.Titles.Clear();
                    chart_Dias.Titles.Add("Sin registros");
                    chart_Dias.Titles[0].Text = "No hay registros :c";
                    chart_Dias.Titles[0].Visible = true;
                    chart_Dias.Update();
                }
                else
                {
                    chart_Dias.Series.Clear();
                    series_ChartDias.Points.Clear();
                    for (int i = 0; i < numDelitos.Length; i++)
                    {
                        if (dpInicio.Equals(dpEnd))
                        {
                            series_ChartDias.ChartType = SeriesChartType.Column;
                        }

                        series_ChartDias.Points.AddXY(fecha[i], numDelitos[i]);
                        series_ChartDias.IsValueShownAsLabel = false;

                    }

                    chart_Dias.Titles.Clear();
                    chart_Dias.Titles.Add("Si hay registros c:");
                    chart_Dias.Titles[0].Text = "Delitos Registrados entre: " + dpInicio.Value.ToString() + " y " + dpEnd.Value.ToString();
                    chart_Dias.Titles[0].Visible = true;
                    chart_Dias.Update();

                    chart_Dias.Series.Add(series_ChartDias);
                    chart_Dias.Update();
                }
            }
        }

        public int Ancho
        {
            set
            {
                ancho = value;
            }
        }

        public int Alto
        {
            set
            {
                alto = value;
            }
        }

        public int Point_S01
        {
            set
            {
                point_S01 = new DataPoint(0, value)
                {
                    Color = Color.FromName(color1),
                    LegendText = legend1,
                    IsValueShownAsLabel = true
                };
            }
        }

        public int Point_S02
        {
            set
            {
                point_S02 = new DataPoint(0, value)
                {
                    Color = Color.FromName(color2),
                    LegendText = legend2,
                    IsValueShownAsLabel = true
                };
            }
        }

        public int Point_S03
        {
            set
            {
                point_S03 = new DataPoint(0, value)
                {
                    Color = Color.FromName(color3),
                    LegendText = legend3,
                    IsValueShownAsLabel = true
                    //AxisLabel = "No trabajadas"
                };

                series_ChartSemaforo.Points.Add(point_S01);
                series_ChartSemaforo.Points.Add(point_S02);
                series_ChartSemaforo.Points.Add(point_S03);
                chart_Semaforo.Series.Add(series_ChartSemaforo);
            }
        }

        public void frmStats_ResizeEnd(object sender, EventArgs e)
        {
        }

        private void roundedPanel6_Paint(object sender, PaintEventArgs e)
        {

        }

        private void roundedPanel7_Paint(object sender, PaintEventArgs e)
        {

        }

        private void roundedPanel2_Paint(object sender, PaintEventArgs e)
        {

        }

        private void chart_Semaforo_Click(object sender, EventArgs e)
        {

        }

        private void frmStats_Resize(object sender, EventArgs e)
        {

            this.Refresh();
        }
    }
}

