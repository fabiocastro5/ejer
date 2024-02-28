class Empleado:
    def __init__(self, dni, nombre, apellido, añoIngreso):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.añoIngreso = añoIngreso

    def getSalario(self):
        pass  # Implementar en las clases derivadas

class EmpleadoSalarioFijo(Empleado):
    def __init__(self, dni, nombre, apellido, añoIngreso, sueldoBasico, añosEmpresa):
        super().__init__(dni, nombre, apellido, añoIngreso)
        self.sueldoBasico = sueldoBasico
        self.añosEmpresa = añosEmpresa

    def getSalario(self):
        if self.añosEmpresa < 2:
            return self.sueldoBasico
        elif 2 <= self.añosEmpresa <= 5:
            return self.sueldoBasico * 1.05
        else:
            return self.sueldoBasico * 1.10

class EmpleadoComision(Empleado):
    def __init__(self, dni, nombre, apellido, añoIngreso, salarioMinimo, clientesCaptados, montoPorCliente):
        super().__init__(dni, nombre, apellido, añoIngreso)
        self.salarioMinimo = salarioMinimo
        self.clientesCaptados = clientesCaptados
        self.montoPorCliente = montoPorCliente

    def getSalario(self):
        salario = self.clientesCaptados * self.montoPorCliente
        return max(salario, self.salarioMinimo)

# Crear 4 empleados (ejemplo)
empleados = [
    EmpleadoSalarioFijo("111", "Juan", "Pérez", 2018, 2000,),
    EmpleadoComision("222", "María", "Gómez", 2019, 1000, 18, 48),
    EmpleadoComision("333", "Elena", "Ramirez", 2017, 1000, 17, 50),
    EmpleadoSalarioFijo("444", "Juan", "Pérez", 2015, 2000,),
]
# Método para mostrar salarios
def mostrarSalarios(empleados):
    for emp in empleados:
        print(f"{emp.nombre} {emp.apellido}: ${emp.getSalario():.2f}")

mostrarSalarios(empleados)
def empleadoConMasClientes(empleados):
    max_clientes = -1
    empleado_max_clientes = None
    for emp in empleados:
        if isinstance(emp, EmpleadoComision) and emp.clientesCaptados > max_clientes:
            max_clientes = emp.clientesCaptados
            empleado_max_clientes = emp
    return empleado_max_clientes

empleado_max_clientes = empleadoConMasClientes(empleados)
if empleado_max_clientes:
    print(f"Empleado con más clientes captados: {empleado_max_clientes.nombre} {empleado_max_clientes.apellido}")
else:
    print("No hay empleados a comisión en la lista.")
