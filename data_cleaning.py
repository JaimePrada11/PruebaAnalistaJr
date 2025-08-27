import pandas as pd

def limpiar_transformar(df: pd.DataFrame) -> pd.DataFrame:
    # Eliminacion de duplicados
    df = df.drop_duplicates()

    # Conversion de tipos y manejo de nulos
    df["total"] = df["total"].fillna(0).astype(float)
    df["fecha_emision"] = pd.to_datetime(df["fecha_emision"])
    df["pagada"] = df["pagada"].astype(bool)

    # Columnas temporales
    df["mes"] = df["fecha_emision"].dt.to_period("M")
    df["dia_semana"] = df["fecha_emision"].dt.day_name()
    
    # Marcar errores y anomalías
    df["cliente_faltante"] = df["cliente"].isna()
    df["equipo_tipo_faltante"] = df["equipo_tipo"].isna()
    df["tecnico_faltante"] = df["tecnico"].isna()
    
    df["total_negativo"] = df["total"] < 0
    df["fecha_futura"] = df["fecha_emision"] > pd.Timestamp.today()

    # Marcar filas problemáticas
    df["fila_problematica"] = (
        df["cliente_faltante"] |
        df["equipo_tipo_faltante"] |
        df["tecnico_faltante"] |
        df["total_negativo"] |
        df["fecha_futura"]
    )

    return df
