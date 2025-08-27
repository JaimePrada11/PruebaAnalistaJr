import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 7)

def graficar_avanzado(res):
    
    # ----- Ventas por cliente -----
    plt.figure()
    top_clientes = res["ventas_cliente"].head(15)  # top 15 clientes
    sns.barplot(
        x="total_facturado", 
        y="cliente", 
        data=top_clientes, 
        color="mediumseagreen",  # usar color directo en lugar de palette
        dodge=False
    )
    plt.title("Top Clientes por Ventas", fontsize=16)
    plt.xlabel("Total Facturado")
    plt.ylabel("Cliente")
    for index, value in enumerate(top_clientes["total_facturado"]):
        plt.text(value, index, f"${value:,.0f}", va="center")
    plt.tight_layout()
    plt.savefig("reportes/ventas_cliente.png", dpi=300)
    plt.close()

    # ----- Ventas por técnico -----
    plt.figure()
    top_tecnicos = res["ventas_tecnico"].head(15)
    sns.barplot(
        x="total_facturado", 
        y="tecnico", 
        data=top_tecnicos, 
        color="royalblue",
        dodge=False
    )
    plt.title("Top Técnicos por Ventas", fontsize=16)
    plt.xlabel("Total Facturado")
    plt.ylabel("Técnico")
    for index, value in enumerate(top_tecnicos["total_facturado"]):
        plt.text(value, index, f"${value:,.0f}", va="center")
    plt.tight_layout()
    plt.savefig("reportes/ventas_tecnico.png", dpi=300)
    plt.close()

    # ----- Ventas por tipo de equipo -----
    plt.figure()
    sns.barplot(
        x="total_facturado", 
        y="equipo_tipo", 
        data=res["ventas_equipo"], 
        color="orangered",
        dodge=False
    )
    plt.title("Ventas por Tipo de Equipo", fontsize=16)
    plt.xlabel("Total Facturado")
    plt.ylabel("Tipo de Equipo")
    for index, value in enumerate(res["ventas_equipo"]["total_facturado"]):
        plt.text(value, index, f"${value:,.0f}", va="center")
    plt.tight_layout()
    plt.savefig("reportes/ventas_equipo.png", dpi=300)
    plt.close()

    # ----- Facturas pagadas vs pendientes -----
    plt.figure()
    colores = sns.color_palette("pastel")
    plt.pie(
        res["facturas_pagadas"]["total_facturado"], 
        labels=res["facturas_pagadas"]["pagada"].astype(str), 
        autopct="%1.1f%%", 
        startangle=140, 
        colors=colores, 
        textprops={'fontsize':12}
    )
    plt.title("Facturas Pagadas vs Pendientes", fontsize=16)
    plt.tight_layout()
    plt.savefig("reportes/facturas_pagadas.png", dpi=300)
    plt.close()

    # ----- Ventas mensuales -----
    plt.figure()
    sns.lineplot(
        x=res["ventas_mensual"]["mes"].astype(str), 
        y="total_facturado", 
        data=res["ventas_mensual"], 
        marker="o",
        color="purple"
    )
    plt.title("Ventas Mensuales", fontsize=16)
    plt.xlabel("Mes")
    plt.ylabel("Total Facturado")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("reportes/ventas_mensual.png", dpi=300)
    plt.close()

    # ----- Ventas por día de la semana -----
    plt.figure()
    sns.barplot(
        x="dia_semana", 
        y="total_facturado", 
        data=res["ventas_dia_semana"], 
        color="goldenrod",
        dodge=False
    )
    plt.title("Ventas por Día de la Semana", fontsize=16)
    plt.xlabel("Día de la Semana")
    plt.ylabel("Total Facturado")
    for index, value in enumerate(res["ventas_dia_semana"]["total_facturado"]):
        plt.text(index, value, f"${value:,.0f}", ha="center", va="bottom")
    plt.tight_layout()
    plt.savefig("reportes/ventas_dia_semana.png", dpi=300)
    plt.close()
