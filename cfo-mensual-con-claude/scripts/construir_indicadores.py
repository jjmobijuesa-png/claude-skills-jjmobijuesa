# -*- coding: utf-8 -*-
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.chart import PieChart, BarChart, LineChart, Reference
from openpyxl.chart.label import DataLabelList
from openpyxl.utils import get_column_letter

FLUJO=r"E:\vars\var 11-11 Finanza Integral\03 Flujo de Caja\Flujo de Efectivo 2026.xlsx"
wb=openpyxl.load_workbook(FLUJO)
if 'Indicadores' in wb.sheetnames: del wb['Indicadores']
ws=wb.create_sheet('Indicadores', 0)  # primera hoja

NAVY='1F3864'; BLUE='2E5496'; LGREY='D9E1F2'; GREEN='C6EFCE'; RED='FFC7CE'; AMBER='FFEB9C'; GOLD='FFF2CC'; HDRG='BDD7EE'
GREENF='006100'; REDF='9C0006'; AMBERF='9C6500'
thin=Side(style='thin',color='BFBFBF')
def st(c,bold=False,size=10,color='000000',fill=None,align='left',fmt=None,wrap=False,border=True):
    c.font=Font(bold=bold,size=size,color=color); c.alignment=Alignment(horizontal=align,vertical='center',wrap_text=wrap)
    if fill:c.fill=PatternFill('solid',fgColor=fill)
    if fmt:c.number_format=fmt
    if border:c.border=Border(left=thin,right=thin,top=thin,bottom=thin)

# ===== DATOS REALES 2026 (ene-jul) =====
M=['ENE','FEB','MAR','ABR','MAY','JUN','JUL']
ing=[5928.69,2700,2800,3450,2700,2700,2700]
egr=[4060.58,2731.60,2769.24,3508.11,2857.62,3252.79,3496.30]
gper=[494.55,184.20,250.60,361.80,137.70,757.70,883.90]
gfin=[45.00,4.50,4.50,3.60,0.00,4.10,5.20]
ginv=[160.70,24.10,10.50,233.00,40.00,23.00,40.00]
deu=[3156.00,2244.90,2244.90,2589.90,2244.90,2244.90,2343.80]
mm=[249.33,278.50,263.20,323.50,435.10,227.20,228.71]
n=len(M)
sum_=lambda a: round(sum(a),2)
Ting=sum_(ing); Tegr=sum_(egr); Tdeu=sum_(deu)
Tgper=sum_(gper); Tgfin=sum_(gfin); Tginv=sum_(ginv); Tmm=sum_(mm)
Gop = Tgper+Tgfin+Tginv+Tmm            # gasto operativo (sin deuda)
FlujoOp = Ting - Gop                    # caja disponible para deuda
DSCR = FlujoOp/Tdeu if Tdeu else 0
carga = Tdeu/Ting if Ting else 0
margen = (Ting-Tegr)/Ting if Ting else 0
ahorro = 3228.69; tasa_aho = ahorro/Ting
cob_op = Ting/Gop if Gop else 0
saldo_disp = 880.79; gasto_mes = Tegr/n
runway = saldo_disp/gasto_mes if gasto_mes else 0

r=1
ws.merge_cells(start_row=r,start_column=1,end_row=r,end_column=8)
st(ws.cell(r,1,'INDICADORES DE CONTROL DE FLUJO Y BANCABILIDAD - 2026'),bold=True,size=14,color='FFFFFF',fill=NAVY,align='center'); ws.row_dimensions[r].height=24
r+=1
ws.merge_cells(start_row=r,start_column=1,end_row=r,end_column=8)
st(ws.cell(r,1,'Base real ene-jul 2026 (7 meses). Doctrina: los bancos financian CAPACIDAD DE PAGO (flujo de caja), no utilidad ni EBITDA.'),size=9,fill=LGREY,align='center')
r+=2

# ===== PANEL BANCABILIDAD =====
st(ws.cell(r,1,'PANEL DE BANCABILIDAD (semaforo)'),bold=True,size=12,color='FFFFFF',fill=BLUE)
for c in range(2,9): st(ws.cell(r,c,''),fill=BLUE)
r+=1
for i,h in enumerate(['INDICADOR','VALOR','UMBRAL BANCA','ESTADO','LECTURA']):
    st(ws.cell(r,1+i if i<4 else 5,h),bold=True,fill=HDRG,align='center')
ws.merge_cells(start_row=r,start_column=5,end_row=r,end_column=8)
r+=1
def kpi(nombre, valor, valfmt, umbral, ok, lectura):
    global r
    st(ws.cell(r,1,nombre),bold=True)
    st(ws.cell(r,2,valor),align='center',fmt=valfmt)
    st(ws.cell(r,3,umbral),align='center')
    estado = 'VERDE' if ok=='v' else ('AMBAR' if ok=='a' else 'ROJO')
    fill = GREEN if ok=='v' else (AMBER if ok=='a' else RED)
    fcol = GREENF if ok=='v' else (AMBERF if ok=='a' else REDF)
    st(ws.cell(r,4,estado),bold=True,align='center',fill=fill,color=fcol)
    ws.merge_cells(start_row=r,start_column=5,end_row=r,end_column=8)
    st(ws.cell(r,5,lectura),size=9,wrap=True,align='left'); ws.row_dimensions[r].height=30
    r+=1
kpi('DSCR (cobertura del servicio de deuda)', round(DSCR,2), '0.00', '>= 1.20', 'r' if DSCR<1.2 else ('a' if DSCR<1.35 else 'v'),
    'Flujo operativo / servicio de deuda. En 1.0 apenas se paga la deuda: sin colchon, el banco no presta.')
kpi('Carga de deuda / ingreso', carga, '0.0%', '<= 40%', 'r' if carga>0.4 else ('a' if carga>0.3 else 'v'),
    'La deuda absorbe el 74% del ingreso. La banca exige por debajo de 40% para dar credito.')
kpi('Margen de caja libre', margen, '0.0%', '>= 10%', 'r' if margen<0.05 else ('a' if margen<0.1 else 'v'),
    'Lo que sobra tras cubrir todo. Apenas 1%: el sistema vive al filo cada mes.')
kpi('Tasa de ahorro', tasa_aho, '0.0%', '>= 20%', 'a' if tasa_aho>=0.1 else 'r',
    'Motor del Sistema del 1%. El 14% actual proviene de un aporte unico de enero, no es recurrente.')
kpi('Cobertura operativa (sin deuda)', round(cob_op,2), '0.00', '>= 1.5', 'v' if cob_op>=1.5 else 'r',
    'Ingreso / gasto operativo. 4x: la operacion es sana; el problema es 100% la deuda.')
kpi('Runway (meses de caja)', round(runway,2), '0.00', '>= 3.0', 'r' if runway<1 else ('a' if runway<3 else 'v'),
    'Meses que la caja disponible cubre. Menos de 1 mes: liquidez critica.')
r+=1
ws.merge_cells(start_row=r,start_column=1,end_row=r,end_column=8)
st(ws.cell(r,1,'VEREDICTO: NO bancable hoy. La operacion es sana (cobertura 4x) pero la deuda la asfixia (DSCR ~1.0, carga 74%). '
             'Palanca unica: convertir lotes en caja para amortizar deuda -> DSCR sube, carga baja -> bancable.'),
   bold=True,size=10,fill=GOLD,wrap=True,align='left'); ws.row_dimensions[r].height=42
r+=2

# ===== MATRIZ CATEGORIA x MES (reconstruida, real) =====
mat_start=r
st(ws.cell(r,1,'MATRIZ DE EGRESOS POR CATEGORIA x MES (real ene-jul)'),bold=True,size=11,color='FFFFFF',fill=BLUE)
for c in range(2,9): st(ws.cell(r,c,''),fill=BLUE)
r+=1
st(ws.cell(r,1,'CATEGORIA'),bold=True,fill=HDRG)
for i,mn in enumerate(M): st(ws.cell(r,2+i,mn),bold=True,fill=HDRG,align='center')
st(ws.cell(r,2+n,'TOTAL'),bold=True,fill=HDRG,align='center')
r+=1
cats=[('Gastos Personales',gper),('Gastos Financieros',gfin),('Gastos Inversion',ginv),('Servicio de Deuda',deu),('Hogar/Familia',mm)]
matrix_first=r
for nombre,arr in cats:
    st(ws.cell(r,1,nombre))
    for i,v in enumerate(arr): st(ws.cell(r,2+i,round(v,2)),align='right',fmt='#,##0')
    st(ws.cell(r,2+n,round(sum(arr),2)),bold=True,align='right',fmt='#,##0',fill=GOLD)
    r+=1
matrix_last=r-1
# fila total e ingreso
st(ws.cell(r,1,'TOTAL EGRESOS'),bold=True,fill=LGREY)
for i in range(n): st(ws.cell(r,2+i,round(egr[i],2)),bold=True,align='right',fmt='#,##0',fill=LGREY)
st(ws.cell(r,2+n,round(Tegr,2)),bold=True,align='right',fmt='#,##0',fill=LGREY)
tot_egr_row=r; r+=1
st(ws.cell(r,1,'TOTAL INGRESOS'),bold=True,fill=GREEN)
for i in range(n): st(ws.cell(r,2+i,round(ing[i],2)),bold=True,align='right',fmt='#,##0',fill=GREEN,color=GREENF)
st(ws.cell(r,2+n,round(Ting,2)),bold=True,align='right',fmt='#,##0',fill=GREEN,color=GREENF)
tot_ing_row=r; r+=1
# carga de deuda mensual (%)
st(ws.cell(r,1,'Carga de deuda % (deuda/ingreso)'),bold=True)
for i in range(n):
    cg=deu[i]/ing[i] if ing[i] else 0
    st(ws.cell(r,2+i,cg),align='right',fmt='0%',color=(REDF if cg>0.4 else '000000'))
st(ws.cell(r,2+n,carga),bold=True,align='right',fmt='0%',fill=GOLD)
carga_row=r; r+=2

# ===== GRAFICOS =====
# 1) Pie distribucion egresos (categorias TOTAL)
pie=PieChart(); pie.title="Distribucion de Egresos (ene-jul)"
labels=Reference(ws, min_col=1, min_row=matrix_first, max_row=matrix_last)
data=Reference(ws, min_col=2+n, min_row=matrix_first, max_row=matrix_last)
pie.add_data(data, titles_from_data=False); pie.set_categories(labels)
pie.dataLabels=DataLabelList(); pie.dataLabels.showPercent=True; pie.height=7.5; pie.width=11
ws.add_chart(pie, f"A{r}")
# 2) Barras ingreso vs egreso vs deuda mensual
bar=BarChart(); bar.type="col"; bar.title="Ingreso vs Egreso vs Servicio de Deuda (mensual)"
cats_ref=Reference(ws, min_col=2, max_col=1+n, min_row=matrix_first-1, max_row=matrix_first-1)
ing_ref=Reference(ws, min_col=2, max_col=1+n, min_row=tot_ing_row, max_row=tot_ing_row)
egr_ref=Reference(ws, min_col=2, max_col=1+n, min_row=tot_egr_row, max_row=tot_egr_row)
deu_ref=Reference(ws, min_col=2, max_col=1+n, min_row=matrix_first+3, max_row=matrix_first+3)  # fila Servicio de Deuda
for ref,nm in [(ing_ref,'Ingreso'),(egr_ref,'Egreso'),(deu_ref,'Servicio Deuda')]:
    bar.add_data(ref, titles_from_data=False)
bar.set_categories(cats_ref)
bar.series[0].tx=None
bar.height=7.5; bar.width=14; bar.gapWidth=60
ws.add_chart(bar, f"D{r}")
r_after_charts=r+16

# 3) Linea carga de deuda %
line=LineChart(); line.title="Carga de deuda mensual (%)"
lr=Reference(ws, min_col=2, max_col=1+n, min_row=carga_row, max_row=carga_row)
line.add_data(lr, titles_from_data=False); line.set_categories(cats_ref)
line.height=6.5; line.width=12
ws.add_chart(line, f"A{r_after_charts}")

# ===== COMPARATIVO MULTIANUAL EGRESOS =====
r2=r_after_charts+14
st(ws.cell(r2,1,'EVOLUCION DE EGRESOS ANUALES (2023-2026)'),bold=True,size=11,color='FFFFFF',fill=BLUE)
for c in range(2,5): st(ws.cell(r2,c,''),fill=BLUE)
r2+=1
st(ws.cell(r2,1,'Año'),bold=True,fill=HDRG); st(ws.cell(r2,2,'Egreso total'),bold=True,fill=HDRG,align='center')
st(ws.cell(r2,3,'Servicio deuda'),bold=True,fill=HDRG,align='center'); st(ws.cell(r2,4,'Deuda %'),bold=True,fill=HDRG,align='center')
r2+=1
multiyr=[('2023',4525,0),('2024',6708,1985),('2025',42563,24644),('2026 (proy)',33854,22893)]
my_first=r2
for yr,e,d in multiyr:
    st(ws.cell(r2,1,yr)); st(ws.cell(r2,2,e),align='right',fmt='#,##0'); st(ws.cell(r2,3,d),align='right',fmt='#,##0')
    st(ws.cell(r2,4,(d/e if e else 0)),align='right',fmt='0%',color=(REDF if (d/e if e else 0)>0.4 else '000000'))
    r2+=1
my_last=r2-1
barY=BarChart(); barY.type="col"; barY.title="Egresos vs Servicio de Deuda por año"
catY=Reference(ws, min_col=1, min_row=my_first, max_row=my_last)
dY=Reference(ws, min_col=2, max_col=3, min_row=my_first-1, max_row=my_last)
barY.add_data(dY, titles_from_data=True); barY.set_categories(catY); barY.height=6.5; barY.width=12
ws.add_chart(barY, f"D{r_after_charts+14}")
r2+=1

# ===== PUENTE AL SISTEMA DEL 1% =====
st(ws.cell(r2,1,'PUENTE AL SISTEMA DE MULTIPLICACION DE RIQUEZA (1%)'),bold=True,size=11,color='FFFFFF',fill=NAVY)
for c in range(2,9): st(ws.cell(r2,c,''),fill=NAVY)
r2+=1
puente=[
 'Fase 1 (Aseguramiento) exige EXCEDENTE recurrente para las 5 cuentas. Hoy el margen de caja libre es ~1%: no hay excedente estable que asignar.',
 'Requisito de entrada: subir DSCR a >=1.2 y bajar carga de deuda a <40%. Ambos dependen de amortizar deuda con la venta de lotes.',
 'Meta de tasa de ahorro >=20% para alimentar la Cuenta de Multiplicacion. Recurrente, no aportes unicos.',
 'Regla del 1%: cada $1 de excedente debe generar >=$0.12/año pasivo. Solo aplica una vez exista excedente (tras sanear deuda).',
 'Secuencia correcta: (1) vender lotes -> caja; (2) amortizar/refinanciar deuda vencida; (3) DSCR y carga sanos = bancable; (4) recien ahi arranca el flujo circular del 1%.',
]
for t in puente:
    ws.merge_cells(start_row=r2,start_column=1,end_row=r2,end_column=8)
    st(ws.cell(r2,1,t),size=9,wrap=True,align='left'); ws.row_dimensions[r2].height=28; r2+=1

# formato
ws.column_dimensions['A'].width=34
for col in 'BCDEFGH': ws.column_dimensions[col].width=11
ws.sheet_view.showGridLines=False
ws.page_setup.orientation='portrait'; ws.page_setup.paperSize=9; ws.sheet_properties.pageSetUpPr.fitToPage=True; ws.page_setup.fitToWidth=1; ws.page_setup.fitToHeight=0

# ordenar hojas
order=['Indicadores','Flujo 2026','Resumen Bancario','Conciliacion','Reglas']
wb._sheets.sort(key=lambda s: order.index(s.title) if s.title in order else 99)
wb.save(FLUJO)
print('OK Indicadores. DSCR=%.2f carga=%.1f%% margen=%.1f%% cob_op=%.2f runway=%.2f'%(DSCR,carga*100,margen*100,cob_op,runway))
print('Hojas:', wb.sheetnames)
