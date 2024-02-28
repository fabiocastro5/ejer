class FabricaInstrumentos:
    def __init__(self):
        self.sucursales = []

    def listarInstrumentos(self):
        for sucursal in self.sucursales:
            for instrumento in sucursal.instrumentos:
                instrumento.mostrarDatos()

    def instrumentosPorTipo(self, tipo):
        instrumentos_filtrados = []
        for sucursal in self.sucursales:
            for instrumento in sucursal.instrumentos:
                if instrumento.tipo == tipo:
                    instrumentos_filtrados.append(instrumento)
        return instrumentos_filtrados

    def borrarInstrumento(self, ID):
        for sucursal in self.sucursales:
            for instrumento in sucursal.instrumentos:
                if instrumento.ID == ID:
                    sucursal.instrumentos.remove(instrumento)

    def porcInstrumentosPorTipo(self, nombre_sucursal):
        porcentajes = {}
        sucursal = next((s for s in self.sucursales if s.nombre == nombre_sucursal), None)
        if sucursal:
            total = len(sucursal.instrumentos)
            tipos = {}
            for instrumento in sucursal.instrumentos:
                if instrumento.tipo in tipos:
                    tipos[instrumento.tipo] += 1
                else:
                    tipos[instrumento.tipo] = 1
            for tipo, cantidad in tipos.items():
                porcentaje = (cantidad / total) * 100
                porcentajes[tipo] = porcentaje
        return porcentajes

class Sucursal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.instrumentos = []

    def agregarInstrumento(self, instrumento):
        self.instrumentos.append(instrumento)

class Instrumento:
    def __init__(self, ID, precio, tipo):
        self.ID = ID
        self.precio = precio
        self.tipo = tipo

    def mostrarDatos(self):
        print(f"ID: {self.ID}, Precio: {self.precio}, Tipo: {self.tipo}")

# Ejemplo de uso
fabrica = FabricaInstrumentos()

sucursal1 = Sucursal("Sucursal A")
sucursal1.agregarInstrumento(Instrumento("001", 100, "Cuerda"))
sucursal1.agregarInstrumento(Instrumento("002", 150, "Viento"))

sucursal2 = Sucursal("Sucursal B")
sucursal2.agregarInstrumento(Instrumento("003", 200, "Percusión"))
sucursal2.agregarInstrumento(Instrumento("004", 120, "Cuerda"))

fabrica.sucursales.append(sucursal1)
fabrica.sucursales.append(sucursal2)

fabrica.listarInstrumentos()

instrumentos_cuerda = fabrica.instrumentosPorTipo("Cuerda")
for instrumento in instrumentos_cuerda:
    instrumento.mostrarDatos()

fabrica.borrarInstrumento("003")
fabrica.listarInstrumentos()

porcentajes_sucursal = fabrica.porcInstrumentosPorTipo("Sucursal B")
print(porcentajes_sucursal)

    
    
   