def analisis_avanzado(df):
    resultados = {}

    # VALIDACIONES
    resultados["filas_totales"] = len(df)
    resultados["filas_problema"] = df["fila_problematica"].sum()
    resultados["porcentaje_problema"] = (resultados["filas_problema"] / resultados["filas_totales"]) * 100
    resultados["facturas_negativas"] = df[df["total"] < 0].shape[0]
    resultados["facturas_cero"] = df[df["total"] == 0].shape[0]
                                                

    # KPIS 

    resultados["total_facturado"] = df["total"].sum()
    resultados["facturas_promedio"] = df["total"].mean()
    resultados["factura_max"] = df["total"].max()
    resultados["factura_min"] = df["total"].min()

    
    # Facturas por cliente
    resultados["ventas_cliente"] = df.groupby("cliente")["total"].agg(
        total_facturado="sum",
        factura_promedio="mean",
        factura_max="max",
        factura_min="min",
        cantidad_facturas="count"
    ).reset_index().sort_values("total_facturado", ascending=False)


    # Facturas por técnico
    resultados["ventas_tecnico"] = df.groupby("tecnico")["total"].agg(
        total_facturado="sum",
        promedio="mean",
        cantidad_facturas="count",
        max_factura="max",
        min_factura="min"
    ).reset_index().sort_values("total_facturado", ascending=False)
    
    # Facturas por tipo de equipo
    resultados["ventas_equipo"] = df.groupby("equipo_tipo")["total"].agg(
        total_facturado="sum",
        promedio="mean",
        cantidad_facturas="count"
    ).reset_index().sort_values("total_facturado", ascending=False)


    # Facturas pagadas vs pendientes
    resultados["facturas_pagadas"] = df.groupby("pagada")["total"].agg(
        total_facturado="sum",
        cantidad_facturas="count"
    ).reset_index()

    # Ventas mensuales
    resultados["ventas_mensual"] = df.groupby("mes")["total"].agg(
        total_facturado="sum",
        promedio="mean",
        cantidad="count"
    ).reset_index()

    # Ventas por día de la semana
    dias_semana = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    resultados["ventas_dia_semana"] = df.groupby("dia_semana")["total"].agg(
        total_facturado="sum",
        promedio="mean",
        cantidad="count"
    ).reindex(dias_semana).reset_index()

    return resultados
