import pandas as pd
from config import engine

import pandas as pd
from config import engine

def extraer_datos() -> pd.DataFrame:
    query = """
    SELECT 
        f.id AS factura_id,
        f.total,
        f.fecha_emision,
        f.pagada,
        
        c.nombre AS cliente,
        c.email AS cliente_email,
        c.telefono AS cliente_telefono,
        c.direccion AS cliente_direccion,
        c.fecha_registro AS cliente_fecha_registro,
        
        o.descripcion_falla,
        o.estado AS orden_estado,
        o.fecha_inicio,
        o.fecha_fin,
        
        e.tipo AS equipo_tipo,
        e.marca AS equipo_marca,
        e.modelo AS equipo_modelo,
        e.serial AS equipo_serial,
        e.estado AS equipo_estado,
        e.fecha_ingreso AS equipo_fecha_ingreso,
        
        t.nombre AS tecnico,
        t.especialidad AS tecnico_especialidad,
        t.telefono AS tecnico_telefono,
        t.email AS tecnico_email,
        t.activo AS tecnico_activo
        
    FROM Facturas f
    LEFT JOIN Clientes c ON f.id_cliente = c.id
    LEFT JOIN OrdenesServicio o ON f.id_orden = o.id
    LEFT JOIN Equipos e ON o.id_equipo = e.id
    LEFT JOIN Tecnicos t ON o.id_tecnico = t.id;
    """
    
    df = pd.read_sql(query, engine)
    return df
