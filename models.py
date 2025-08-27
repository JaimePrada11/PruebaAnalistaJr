from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Boolean, Table
from sqlalchemy.orm import relationship, declarative_base
from datetime import date
from config import Base, engine

orden_repuesto = Table(
    'orden_repuesto',
    Base.metadata,
    Column('id_orden_servicio', Integer, ForeignKey('OrdenesServicio.id'), primary_key=True),
    Column('id_repuesto', Integer, ForeignKey('Repuestos.id'), primary_key=True)
)

class Cliente(Base):
    __tablename__ = 'Clientes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    telefono = Column(String(20), nullable=True)
    direccion = Column(String(255), nullable=True)
    fecha_registro = Column(Date, default=date.today)

    equipos = relationship("Equipo", back_populates="cliente")
    facturas = relationship("Factura", back_populates="cliente")

class Equipo(Base):
    __tablename__ = 'Equipos'
    id = Column(Integer, primary_key=True, autoincrement=True)  
    id_cliente = Column(Integer, ForeignKey('Clientes.id'), nullable=False)
    tipo = Column(String(100), nullable=False)   # Laptop, celular, Impresora
    marca = Column(String(50), nullable=False)
    modelo = Column(String(100), nullable=True)
    serial = Column(String(100), unique=True, nullable=False)
    fecha_ingreso = Column(Date, default=date.today)
    estado = Column(String(50), nullable=False)  # En reparación, Reparado, Entregado

    cliente = relationship("Cliente", back_populates="equipos")
    ordenes_servicio = relationship("OrdenServicio", back_populates="equipo")

class Tecnico(Base):
    __tablename__ = 'Tecnicos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    especialidad = Column(String(100), nullable=True)  # Hardware, Software, Redes
    telefono = Column(String(20), nullable=True)
    email = Column(String(100), unique=True, nullable=False)
    fecha_contratacion = Column(Date, default=date.today)
    activo = Column(Boolean, default=True)

    ordenes_servicio = relationship("OrdenServicio", back_populates="tecnico")

class OrdenServicio(Base):
    __tablename__ = 'OrdenesServicio'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_equipo = Column(Integer, ForeignKey('Equipos.id'), nullable=False)
    id_tecnico = Column(Integer, ForeignKey('Tecnicos.id'), nullable=False)
    descripcion_falla = Column(String(255), nullable=False)
    estado = Column(String(50), nullable=False)  # Pendiente, En proceso, Completada
    fecha_inicio = Column(Date, default=date.today)
    fecha_fin = Column(Date, nullable=True)

    equipo = relationship('Equipo', back_populates='ordenes_servicio')
    tecnico = relationship('Tecnico', back_populates='ordenes_servicio')
    repuestos = relationship('Repuesto', secondary=orden_repuesto, back_populates='ordenes')
    factura = relationship('Factura', back_populates='orden', uselist=False)

class Repuesto(Base):
    __tablename__ = 'Repuestos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String(255), nullable=True)
    precio = Column(Float, nullable=False)
    stock = Column(Integer, default=0)

    ordenes = relationship('OrdenServicio', secondary=orden_repuesto, back_populates='repuestos')


class Factura(Base):
    __tablename__ = 'Facturas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_orden = Column(Integer, ForeignKey('OrdenesServicio.id'), nullable=False)
    id_cliente = Column(Integer, ForeignKey('Clientes.id'), nullable=False)
    total = Column(Float, nullable=False)
    fecha_emision = Column(Date, default=date.today)
    pagada = Column(Boolean, default=False)

    orden = relationship('OrdenServicio', back_populates='factura')
    cliente = relationship('Cliente', back_populates='facturas')


Base.metadata.create_all(engine)