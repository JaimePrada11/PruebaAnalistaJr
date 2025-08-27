import logging
import os
import pandas as pd
from datetime import datetime

# Carpeta base
os.makedirs("reportes", exist_ok=True)
os.makedirs("logs", exist_ok=True)

# Carpeta por fecha (opcional)
fecha_hoy = datetime.now().strftime("%Y-%m-%d")
reportes_path = os.path.join("reportes", fecha_hoy)
logs_path = os.path.join("logs", fecha_hoy)
os.makedirs(reportes_path, exist_ok=True)
os.makedirs(logs_path, exist_ok=True)

# Logging
logging.basicConfig(
    filename=os.path.join(logs_path, "pipeline.log"),
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def log_info(msg: str):
    logging.info(msg)
    print(msg)

def log_error(msg: str):
    logging.error(msg)
    print(msg)

def guardar_resultados(resultados: dict):
    """Guarda resultados en CSV y Excel de manera robusta"""
    excel_path = os.path.join(reportes_path, "reportes_completos.xlsx")
    
    with pd.ExcelWriter(excel_path, engine='xlsxwriter') as writer:
        for key, df in resultados.items():
            try:
                # CSV
                csv_file = os.path.join(reportes_path, f"{key}.csv")
                df.to_csv(csv_file, index=False)
                
                # Excel
                sheet_name = key[:31]  # limite de Excel
                df.to_excel(writer, sheet_name=sheet_name, index=False)
                
                log_info(f"Guardado exitoso: {key}")
            except Exception as e:
                log_error(f"Error guardando {key}: {e}")
