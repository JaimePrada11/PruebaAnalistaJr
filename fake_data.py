import argparse
import random
from datetime import timedelta, date
from faker import Faker
from config import Base, engine, Session  # en lugar de SessionLocal
from models import Cliente, Equipo, Tecnico, OrdenServicio, Repuesto, Factura, orden_repuesto

fake = Faker("es_CO")

def create_massive_realistic_data(num_clientes=2000, num_equipos=5000, num_tecnicos=50, num_repuestos=200, num_ordenes=8000, num_facturas=6000):
    """
    Genera datos masivos y realistas con algunos problemas para practicar limpieza de datos
    """
    session = Session()
    
    try:
        print("🚀 Iniciando generación masiva de datos...")
        
        # === REPUESTOS REALISTAS ===
        print("📦 Creando repuestos...")
        repuestos_data = [
            # Laptops
            {"nombre": "Pantalla LCD 15.6\"", "descripcion": "Pantalla LED para laptops 15.6 pulgadas", "precio": 150.000, "categoria": "pantallas"},
            {"nombre": "Pantalla LCD 14\"", "descripcion": "Pantalla LED para laptops 14 pulgadas", "precio": 135.000, "categoria": "pantallas"},
            {"nombre": "Teclado Español", "descripcion": "Teclado en español para laptop", "precio": 45.000, "categoria": "teclados"},
            {"nombre": "Teclado Inglés", "descripcion": "Teclado en inglés para laptop", "precio": 40.000, "categoria": "teclados"},
            {"nombre": "Batería Li-ion 6 celdas", "descripcion": "Batería recargable 6 celdas", "precio": 80.000, "categoria": "baterias"},
            {"nombre": "Batería Li-ion 4 celdas", "descripcion": "Batería recargable 4 celdas", "precio": 65.000, "categoria": "baterias"},
            {"nombre": "Cargador 65W", "descripcion": "Cargador original 65W", "precio": 55.000, "categoria": "cargadores"},
            {"nombre": "Cargador 90W", "descripcion": "Cargador original 90W", "precio": 70.000, "categoria": "cargadores"},
            {"nombre": "Memoria RAM 8GB DDR4", "descripcion": "Memoria RAM 8GB DDR4 2400MHz", "precio": 120.000, "categoria": "memorias"},
            {"nombre": "Memoria RAM 16GB DDR4", "descripcion": "Memoria RAM 16GB DDR4 2400MHz", "precio": 220.000, "categoria": "memorias"},
            {"nombre": "SSD 256GB", "descripcion": "Disco sólido 256GB SATA", "precio": 180.000, "categoria": "discos"},
            {"nombre": "SSD 512GB", "descripcion": "Disco sólido 512GB SATA", "precio": 320.000, "categoria": "discos"},
            {"nombre": "HDD 1TB", "descripcion": "Disco duro mecánico 1TB", "precio": 200.000, "categoria": "discos"},
            {"nombre": "Tarjeta Madre", "descripcion": "Placa base para laptop", "precio": 450.000, "categoria": "componentes"},
            {"nombre": "Ventilador CPU", "descripcion": "Ventilador para procesador", "precio": 35.000, "categoria": "componentes"},
            {"nombre": "Pasta Térmica", "descripcion": "Pasta térmica para CPU", "precio": 8.000, "categoria": "componentes"},
            
            # Celulares
            {"nombre": "Pantalla Táctil iPhone", "descripcion": "Pantalla táctil original iPhone", "precio": 200.000, "categoria": "pantallas"},
            {"nombre": "Pantalla Táctil Samsung", "descripcion": "Pantalla táctil Samsung Galaxy", "precio": 180.000, "categoria": "pantallas"},
            {"nombre": "Batería iPhone", "descripcion": "Batería original iPhone", "precio": 85.000, "categoria": "baterias"},
            {"nombre": "Batería Samsung", "descripcion": "Batería original Samsung", "precio": 75.000, "categoria": "baterias"},
            {"nombre": "Cargador USB-C", "descripcion": "Cargador USB-C rápido", "precio": 25.000, "categoria": "cargadores"},
            {"nombre": "Cargador Lightning", "descripcion": "Cargador Lightning original", "precio": 30.000, "categoria": "cargadores"},
            {"nombre": "Auricular interno", "descripcion": "Auricular para llamadas", "precio": 15.000, "categoria": "audio"},
            {"nombre": "Altavoz", "descripcion": "Altavoz interno celular", "precio": 20.000, "categoria": "audio"},
            {"nombre": "Cámara trasera", "descripcion": "Cámara principal trasera", "precio": 90.000, "categoria": "camaras"},
            {"nombre": "Cámara frontal", "descripcion": "Cámara frontal selfie", "precio": 45.000, "categoria": "camaras"},
            
            # Impresoras
            {"nombre": "Toner Negro HP", "descripcion": "Toner negro original HP", "precio": 180.000, "categoria": "toners"},
            {"nombre": "Toner Color HP", "descripcion": "Toner color original HP", "precio": 220.000, "categoria": "toners"},
            {"nombre": "Toner Negro Canon", "descripcion": "Toner negro original Canon", "precio": 170.000, "categoria": "toners"},
            {"nombre": "Cartucho Negro Epson", "descripcion": "Cartucho de tinta negro Epson", "precio": 45.000, "categoria": "cartuchos"},
            {"nombre": "Cartucho Color Epson", "descripcion": "Cartucho de tinta color Epson", "precio": 55.000, "categoria": "cartuchos"},
            {"nombre": "Fusor HP", "descripcion": "Unidad fusora HP LaserJet", "precio": 350.000, "categoria": "componentes"},
            {"nombre": "Rodillo HP", "descripcion": "Rodillo de transferencia HP", "precio": 120.000, "categoria": "componentes"},
            {"nombre": "Cabezal Epson", "descripcion": "Cabezal de impresión Epson", "precio": 280.000, "categoria": "componentes"},
            
            # Cables y accesorios
            {"nombre": "Cable HDMI", "descripcion": "Cable HDMI 1.5m", "precio": 15.000, "categoria": "cables"},
            {"nombre": "Cable USB 3.0", "descripcion": "Cable USB 3.0 tipo A-B", "precio": 12.000, "categoria": "cables"},
            {"nombre": "Cable Ethernet", "descripcion": "Cable red RJ45 Cat6", "precio": 8.000, "categoria": "cables"},
            {"nombre": "Adaptador WiFi USB", "descripcion": "Adaptador inalámbrico USB", "precio": 35.000, "categoria": "redes"},
            {"nombre": "Hub USB 4 puertos", "descripcion": "Hub USB 4 puertos", "precio": 25.000, "categoria": "accesorios"},
        ]
        
        repuestos = []
        for i, repuesto_data in enumerate(repuestos_data * 5):  # Multiplicamos por 5 para más variedad
            precio = repuesto_data["precio"]
            stock = random.randint(0, 150)
            
            # Introducir algunos problemas realistas (10% de los casos)
            if random.random() < 0.1:
                if random.random() < 0.3:  # Precios inconsistentes
                    precio = precio * random.uniform(0.7, 1.5)
                if random.random() < 0.2:  # Stock negativo por error sistema
                    stock = -random.randint(1, 5)
                    
            nombre = repuesto_data["nombre"]
            if i > len(repuestos_data):  # Para las copias, agregar variaciones
                variaciones = [" - Genérico", " Compatible", " Original", " Remanufacturado"]
                nombre += random.choice(variaciones)
                
            # Problemas en nombres (5% de casos)
            if random.random() < 0.05:
                nombre = f"  {nombre}  " if random.random() < 0.5 else nombre.upper()
                
            repuesto = Repuesto(
                nombre=nombre,
                descripcion=repuesto_data["descripcion"],
                precio=precio,
                stock=stock
            )
            session.add(repuesto)
            if len(repuestos) < num_repuestos:
                repuestos.append(repuesto)
                
        # === TÉCNICOS REALISTAS ===
        print("👨‍🔧 Creando técnicos...")
        especialidades_reales = [
            "Hardware de Computadoras", "Reparación de Celulares", "Impresoras y Escáneres", 
            "Redes y Conectividad", "Software y Sistemas", "Electrónica General",
            "Soldadura de Componentes", "Recuperación de Datos"
        ]
        
        nombres_tecnicos = [
            "Carlos Rodríguez", "Ana García", "Miguel Torres", "Laura Martínez", "David López",
            "Carmen Ruiz", "Javier Moreno", "Patricia Jiménez", "Roberto Álvarez", "María Herrera",
            "Fernando Castro", "Isabel Vargas", "Antonio Ramos", "Cristina Mendoza", "Luis Guerrero",
            "Elena Navarro", "José Romero", "Pilar Iglesias", "Manuel Delgado", "Rosa Santos"
        ]
        
        tecnicos = []
        for i in range(num_tecnicos):
            nombre = random.choice(nombres_tecnicos) if i < 20 else fake.name()
            especialidad = random.choice(especialidades_reales)
            
            # Algunos técnicos sin especialidad (realista)
            if random.random() < 0.1:
                especialidad = None
                
            telefono = fake.phone_number()
            email = fake.email()
            
            # Problemas realistas en emails (3% de casos)
            if random.random() < 0.03:
                email = email.replace("@", "_at_") if random.random() < 0.5 else f"{nombre.lower().replace(' ', '.')}@empresa.com"
                
            fecha_contratacion = fake.date_between(start_date='-5y', end_date='-1m')
            activo = True if random.random() > 0.05 else False  # 5% inactivos
            
            tecnico = Tecnico(
                nombre=nombre,
                especialidad=especialidad,
                telefono=telefono,
                email=email,
                fecha_contratacion=fecha_contratacion,
                activo=activo
            )
            session.add(tecnico)
            tecnicos.append(tecnico)
            
        session.flush()  # Guardar técnicos y repuestos primero
        
        # === CLIENTES MASIVOS ===
        print("👥 Creando clientes...")
        clientes = []
        batch_size = 500
        
        for batch in range(0, num_clientes, batch_size):
            batch_clientes = []
            for i in range(batch, min(batch + batch_size, num_clientes)):
                nombre = fake.name()
                email = fake.unique.email()
                telefono = fake.phone_number()
                direccion = fake.address()
                fecha_registro = fake.date_between(start_date='-3y', end_date='today')
                
                # Problemas realistas pero no excesivos (5% de casos)
                if random.random() < 0.05:
                    if random.random() < 0.3:  # Espacios extra
                        nombre = f"  {nombre}  "
                    if random.random() < 0.2:  # Direcciones inconsistentes
                        direccion = direccion.upper()
                    if random.random() < 0.1:  # Emails con formato raro
                        email = email.replace(".", "_")
                        
                try:
                    cliente = Cliente(
                        nombre=nombre,
                        email=email,
                        telefono=telefono,
                        direccion=direccion,
                        fecha_registro=fecha_registro
                    )
                    batch_clientes.append(cliente)
                except Exception:
                    continue
                    
            session.add_all(batch_clientes)
            session.flush()
            clientes.extend(batch_clientes)
            print(f"   Creados {len(clientes)} clientes...")
            
        # === EQUIPOS MASIVOS ===
        print("💻 Creando equipos...")
        tipos_equipos = {
            "Laptop": ["HP", "Dell", "Lenovo", "Asus", "Acer", "Toshiba"],
            "Celular": ["Samsung", "Apple", "Huawei", "Xiaomi", "LG", "Motorola"],
            "Impresora": ["HP", "Canon", "Epson", "Brother"],
            "Tablet": ["Samsung", "Apple", "Lenovo"],
            "Desktop": ["HP", "Dell", "Lenovo"]
        }
        
        estados_equipo = ["En reparación", "Reparado", "Entregado", "Pendiente"]
        equipos = []
        
        for batch in range(0, num_equipos, batch_size):
            batch_equipos = []
            for i in range(batch, min(batch + batch_size, num_equipos)):
                cliente = random.choice(clientes)
                tipo = random.choice(list(tipos_equipos.keys()))
                marca = random.choice(tipos_equipos[tipo])
                
                # Modelos realistas
                if tipo == "Laptop":
                    modelo = f"{marca} {random.choice(['Pavilion', 'Inspiron', 'ThinkPad', 'Aspire'])}"
                elif tipo == "Celular":
                    modelo = f"{marca} {random.choice(['Galaxy S21', 'iPhone 12', 'P40', 'Redmi Note'])}"
                else:
                    modelo = f"{marca} {random.choice(['Pro', 'Standard', 'Elite'])}"
                    
                serial = fake.bothify(text='??######??')
                estado = random.choice(estados_equipo)
                fecha_ingreso = fake.date_between(start_date='-2y', end_date='today')
                
                # Problemas realistas (3% de casos)
                if random.random() < 0.03:
                    if random.random() < 0.5:  # Estados inconsistentes
                        estado = estado.lower()
                    if random.random() < 0.3:  # Modelos con espacios
                        modelo = f"  {modelo}  "
                        
                try:
                    equipo = Equipo(
                        id_cliente=cliente.id,
                        tipo=tipo,
                        marca=marca,
                        modelo=modelo,
                        serial=serial,
                        fecha_ingreso=fecha_ingreso,
                        estado=estado
                    )
                    batch_equipos.append(equipo)
                except Exception:
                    continue
                    
            session.add_all(batch_equipos)
            session.flush()
            equipos.extend(batch_equipos)
            print(f"   Creados {len(equipos)} equipos...")
            
        # === ÓRDENES DE SERVICIO MASIVAS ===
        print("📋 Creando órdenes de servicio...")
        fallas_por_tipo = {
            "Laptop": ["No enciende", "Pantalla rota", "Teclado no funciona", "Batería no carga", 
                      "Sobrecalentamiento", "Lento", "No detecta disco duro", "RAM defectuosa"],
            "Celular": ["Pantalla táctil dañada", "No carga", "No enciende", "Cámara borrosa",
                       "Micrófono no funciona", "Altavoz dañado", "Botones no responden"],
            "Impresora": ["No imprime", "Atasco papel", "Calidad impresión mala", "No conecta WiFi",
                         "Error toner", "Ruido extraño", "No escanea"],
            "Tablet": ["Pantalla rota", "No carga", "Lenta", "No conecta WiFi"],
            "Desktop": ["No enciende", "Pantalla azul", "Lento", "Ruido ventilador"]
        }
        
        estados_orden = ["Pendiente", "En proceso", "Completada", "Cancelada"]
        ordenes = []
        
        for batch in range(0, num_ordenes, batch_size):
            batch_ordenes = []
            for i in range(batch, min(batch + batch_size, num_ordenes)):
                equipo = random.choice(equipos)
                tecnico = random.choice([t for t in tecnicos if t.activo])  # Solo técnicos activos
                
                tipo_equipo = equipo.tipo
                if tipo_equipo in fallas_por_tipo:
                    descripcion_falla = random.choice(fallas_por_tipo[tipo_equipo])
                else:
                    descripcion_falla = "Falla general del equipo"
                    
                estado = random.choice(estados_orden)
                fecha_inicio = fake.date_between(start_date='-1y', end_date='today')
                
                # Fechas de fin lógicas
                fecha_fin = None
                if estado == "Completada":
                    fecha_fin = fecha_inicio + timedelta(days=random.randint(1, 30))
                elif estado == "Cancelada" and random.random() < 0.5:
                    fecha_fin = fecha_inicio + timedelta(days=random.randint(1, 15))
                    
                # Problemas realistas (2% de casos)
                if random.random() < 0.02:
                    if random.random() < 0.5:  # Fechas ilógicas
                        if fecha_fin:
                            fecha_fin = fecha_inicio - timedelta(days=1)
                    if random.random() < 0.3:  # Descripciones problemáticas
                        descripcion_falla = descripcion_falla.upper()
                        
                orden = OrdenServicio(
                    id_equipo=equipo.id,
                    id_tecnico=tecnico.id,
                    descripcion_falla=descripcion_falla,
                    estado=estado,
                    fecha_inicio=fecha_inicio,
                    fecha_fin=fecha_fin
                )
                batch_ordenes.append(orden)
                
            session.add_all(batch_ordenes)
            session.flush()
            ordenes.extend(batch_ordenes)
            print(f"   Creadas {len(ordenes)} órdenes...")
            
            # Asociar repuestos a algunas órdenes
            for orden in batch_ordenes:
                if random.random() < 0.4:  # 40% tienen repuestos
                    num_repuestos_orden = random.randint(1, 3)
                    repuestos_seleccionados = random.sample(repuestos, min(num_repuestos_orden, len(repuestos)))
                    for repuesto in repuestos_seleccionados:
                        orden.repuestos.append(repuesto)
                        
        # === FACTURAS MASIVAS ===
        print("💰 Creando facturas...")
        for batch in range(0, num_facturas, batch_size):
            batch_facturas = []
            for i in range(batch, min(batch + batch_size, num_facturas)):
                if i < len(ordenes):
                    orden = ordenes[i]
                    cliente = orden.equipo.cliente
                    
                    # Calcular total realista basado en tipo de equipo
                    base_prices = {
                        "Laptop": random.uniform(80000, 300000),
                        "Celular": random.uniform(50000, 200000),
                        "Impresora": random.uniform(30000, 150000),
                        "Tablet": random.uniform(60000, 180000),
                        "Desktop": random.uniform(70000, 250000)
                    }
                    
                    total = base_prices.get(orden.equipo.tipo, 100000)
                    
                    # Agregar costo de repuestos
                    if orden.repuestos:
                        total += sum([r.precio for r in orden.repuestos])
                        
                    fecha_emision = orden.fecha_inicio + timedelta(days=random.randint(0, 5))
                    
                    # Estado de pago realista
                    if orden.estado == "Completada":
                        pagada = True if random.random() > 0.1 else False  # 90% pagadas
                    else:
                        pagada = False if random.random() > 0.05 else True  # 5% pagadas anticipadamente
                        
                    # Problemas realistas (1% de casos)
                    if random.random() < 0.01:
                        if random.random() < 0.5:  # Totales negativos por error
                            total = -abs(total)
                        if random.random() < 0.3:  # Fechas futuras
                            fecha_emision = date.today() + timedelta(days=random.randint(1, 10))
                            
                    factura = Factura(
                        id_orden=orden.id,
                        id_cliente=cliente.id,
                        total=total,
                        fecha_emision=fecha_emision,
                        pagada=pagada
                    )
                    batch_facturas.append(factura)
                    
            session.add_all(batch_facturas)
            print(f"   Creadas {len(batch_facturas)} facturas...")
            
        session.commit()
        
        print(f"\n✅ DATOS MASIVOS CREADOS EXITOSAMENTE:")
        print(f"   - {len(clientes):,} clientes")
        print(f"   - {len(tecnicos):,} técnicos") 
        print(f"   - {len(equipos):,} equipos")
        print(f"   - {len(repuestos):,} repuestos")
        print(f"   - {len(ordenes):,} órdenes de servicio")
        print(f"   - ~{num_facturas:,} facturas")
        
        print(f"\n🔍 PROBLEMAS INCLUIDOS PARA ANÁLISIS:")
        print(f"   - ~5% de registros con problemas de formato")
        print(f"   - ~2% con inconsistencias lógicas")
        print(f"   - ~1% con valores imposibles")
        print(f"   - Datos realistas basados en negocio real")
        print(f"   - Relaciones coherentes entre entidades")
        
    except Exception as e:
        session.rollback()
        print(f"❌ Error: {e}")
        raise
    finally:
        session.close()

def main():
    parser = argparse.ArgumentParser(description='Generar datos masivos realistas para el sistema de reparaciones')
    parser.add_argument('--clientes', type=int, default=2000, help='Número de clientes (default: 2000)')
    parser.add_argument('--equipos', type=int, default=5000, help='Número de equipos (default: 5000)')
    parser.add_argument('--tecnicos', type=int, default=50, help='Número de técnicos (default: 50)')
    parser.add_argument('--repuestos', type=int, default=200, help='Número de repuestos (default: 200)')
    parser.add_argument('--ordenes', type=int, default=8000, help='Número de órdenes (default: 8000)')
    parser.add_argument('--facturas', type=int, default=6000, help='Número de facturas (default: 6000)')
    
    args = parser.parse_args()
    
    print("🎯 GENERADOR DE DATOS MASIVOS PARA PRÁCTICA DE ANÁLISIS")
    print("=" * 60)
    
    create_massive_realistic_data(
        num_clientes=args.clientes,
        num_equipos=args.equipos, 
        num_tecnicos=args.tecnicos,
        num_repuestos=args.repuestos,
        num_ordenes=args.ordenes,
        num_facturas=args.facturas
    )

if __name__ == "__main__":
    main()