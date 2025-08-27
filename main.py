from data_extraction import extraer_datos
from data_cleaning import limpiar_transformar
from analisis import analisis_avanzado
from visualizacion import graficar_avanzado
from utils import log_info, log_error, guardar_resultados
from config import engine

def main(query=None):
    try:
        log_info("Pipeline iniciado")
        
        df = extraer_datos()
        log_info(f"Datos extraídos: {len(df)} filas")
        if df.empty:
            log_error("No se extrajeron datos. Terminando pipeline.")
            return
        
        df = limpiar_transformar(df)
        log_info("Datos limpiados y transformados")
        
        resultados = analisis_avanzado(df)
        log_info("Análisis completado")
        
        guardar_resultados(resultados)
        log_info("Resultados guardados en CSV y Excel")
        
        graficar_avanzado(resultados)
        log_info("Gráficos generados correctamente")
        
        log_info("Pipeline finalizado exitosamente")
        
    except Exception as e:
        log_error(f"Error en pipeline: {e}")

if __name__ == "__main__":
    main()
