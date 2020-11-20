from tkinter import *
from tkinter import messagebox
import sqlite3
import enum

class Cliente:
    def __init__(self, nombre, direccion, telefono, email):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
    
    def __str__(self):
        return "Nombre:{}\nDireccion:{}\nTelefono:{}\nEmail:{}".format(self.nombre, self.direccion, self.telefono, self.email)

class Cuenta:
    def __init__(self, id_cliente, valor, num_tarjeta, ):
        self.id_cliente = id_cliente
        self.valor = valor
        self.num_tarjeta = num_tarjeta
    
    def __str__(self):
        return "IdCliente:{}\nValorDisponible:{}\nNumero Tarjeta:{}".format(self.id_cliente, self.valor, self.num_tarjeta)

class Pedido:
    def __init__(self, total, estadoPedido):
        self.total = total
        self.estadoPedido = EstadosPedidos()

class EstadosPedidos(enum.Enum):
   pendiente = 1
   pagado = 2
   servido = 3
   confirmado = 4
   rechazado = 5



#CONEXION CREACION BASE DE DATOS
def creacion_base():
    conn = sqlite3.connect("BASEDATOSIA")
    curs = conn.cursor()
    #curs.execute("CREATE TABLE CLIENTES (NOMBRE VARCHAR(75), DIRECCION VARCHAR(200), TELEFONO VARCHAR(10), EMAIL VARCHAR(75))")
    #curs.execute("create table if not exists CLIENTE(id integer primary key autoincrement,nombre varchar(100) not null,direccion varchar(100) not null,telefono varchar(10) not null,correo varchar(150) not null);")
    #curs.execute("create table if not exists CUENTA(id integer primary key autoincrement, id_cliente integer, valor integer, num_tarjeta varchar(50) not null, foreign key(id_cliente) references cliente(id));")
    conn.close()




def registrar_clientes():
    newWindow = Toplevel(root)

    lblTitulo = Label(newWindow, text = "Registro Cliente")

    lblNombre = Label(newWindow, text = "Nombres: ")
    nombre = StringVar()
    txtNombre = Entry(newWindow, width=15, textvariable=nombre)

    lblDireccion = Label(newWindow, text = "Direccion: ")
    direccion = StringVar()
    txtDireccion = Entry(newWindow, width=15, textvariable=direccion)

    lblTelefono = Label(newWindow, text = "Telefono: ")
    telefono = StringVar()
    txtTelefono = Entry(newWindow, width=15, textvariable=telefono)

    lblEmail = Label(newWindow, text = "Correo: ")
    email = StringVar()
    txtEmail = Entry(newWindow, width=15, textvariable=email)

    buttonExample = Button(newWindow, text = "CREAR CLIENTE", command=lambda: creacion(nombre.get(), direccion.get(), telefono.get(), email.get()))

    lblTitulo.pack()
    lblNombre.pack()
    txtNombre.pack()

    lblDireccion.pack()
    txtDireccion.pack()
    
    lblTelefono.pack()
    txtTelefono.pack()

    lblEmail.pack()
    txtEmail.pack()

    buttonExample.pack()
    root.withdraw()

    def creacion(n, d, t, e):
        cli = Cliente(n, d, t, e)
        conn = sqlite3.connect("BASEDATOSIA")
        curs = conn.cursor()
        if((n != "") and (d != "") and (t != "") and (e != "")):
            curs.execute("INSERT INTO CLIENTES(nombre, direccion, telefono, correo) VALUES('"+cli.nombre+"','"+cli.direccion+"','"+cli.telefono+"','"+cli.email+"')")
            conn.commit()
            conn.close()
            messagebox.showinfo('Advertencia', 'Creado Correctamente')
            nombre.set("")
            direccion.set("")
            telefono.set("")
            email.set("")
        else:
            messagebox.showinfo('Advertencia', 'Campos Vacios')
            conn.close()

def crear_cuenta(n):
    def creacion_cuenta(c, v, nt):
        cue = Cuenta(c, v, nt)
        print(type(cue.id_cliente))
        print(type(cue.valor))
        print(type(cue.num_tarjeta))
        conn = sqlite3.connect("BASEDATOSIA")
        curs = conn.cursor()
        if((c != None) and (v != None) and (nt != "")):
            curs.execute("INSERT INTO CUENTA(id_cliente, valor, num_tarjeta) VALUES("+str(cue.id_cliente)+","+str(cue.valor)+",'"+cue.num_tarjeta+"')")
            conn.commit()
            conn.close()
            messagebox.showinfo('Advertencia', 'Creado Correctamente')
            valor.set("")
            numTarjeta.set("")
        else:
            messagebox.showinfo('Advertencia', 'Campos Vacios')
            conn.close()

    
    if (n != " "):
        conn = sqlite3.connect("BASEDATOSIA")
        curs = conn.cursor()
        curs.execute("SELECT ID, NOMBRE FROM CLIENTES WHERE NOMBRE = '" + n +"';" )
        v = curs.fetchall()
        codigo_cliente = v[0][0]
        nombre_cliente = v[0][1]
        conn.commit()
        conn.close()
        
        if (nombre_cliente == n):
            
            newWindow2 = Toplevel(root)
            lblTitulo = Label(newWindow2, text = "Crear Cuentas")

            lblCod = Label(newWindow2, text = "Codigo Cliente")
            lblCodigoCliente = Label(newWindow2, text = codigo_cliente)

            lblValor = Label(newWindow2, text = "Valor Disponible: ")
            valor = IntVar()
            txtValor = Entry(newWindow2, width=20, textvariable=valor)

            lblNumeroTarjeta = Label(newWindow2, text = "Numero Tarjeta: ")
            numTarjeta = StringVar()
            txtNumTarjeta = Entry(newWindow2, width=20, textvariable=numTarjeta)

            buttonExample = Button(newWindow2, text = "CREAR CUENTA", command=lambda : creacion_cuenta(codigo_cliente, valor.get(), numTarjeta.get()))

            lblTitulo.pack()

            lblCod.pack()
            lblCodigoCliente.pack()
            lblValor.pack()
            txtValor.pack()

            lblNumeroTarjeta.pack()
            txtNumTarjeta.pack()

            buttonExample.pack()
            root.withdraw()
        else:
            messagebox.showinfo('Advertencia', 'Nombre Incorrecto')
    else:
        messagebox.showinfo('Advertencia', 'Campos Vacios')

def aumentar_cuenta(n):
    def aumentar_valor(c, v, nt):
        cue = Cuenta(c, v, nt)
        print(type(cue.id_cliente))
        print(type(cue.valor))
        print(type(cue.num_tarjeta))
        conn = sqlite3.connect("BASEDATOSIA")
        curs = conn.cursor()
        if((c != None) and (v != None) and (nt != "")):
            curs.execute("UPDATE CUENTA SET VALOR = "+ str(cue.valor) +" WHERE num_tarjeta = '"+ cue.num_tarjeta +"'")
            conn.commit()
            conn.close()
            messagebox.showinfo('Advertencia', 'Creado Correctamente')
            valor.set("")
        else:
            messagebox.showinfo('Advertencia', 'Campos Vacios')
            conn.close()


    if n != " ":
        conn = sqlite3.connect("BASEDATOSIA")
        curs = conn.cursor()
        curs.execute("SELECT * FROM CUENTA WHERE num_tarjeta = '" + n +"';" )
        v = curs.fetchall()
        id_cuenta = v[0][0]
        valor_cuenta = v[0][2]
        nume_tarj = v[0][3]
        conn.commit()
        conn.close()
        if (nume_tarj == n):
        
            newWindow2 = Toplevel(root)

            lblTitulo = Label(newWindow2, text = "Aumentar Valor")

            lblNum= Label(newWindow2, text = "Numero de Tarjeta: ")
            lblNumeTarj = Label(newWindow2, text = nume_tarj)

            lblValoAc= Label(newWindow2, text = "Valor Actual: ")
            lblValoAct = Label(newWindow2, text = valor_cuenta)

            lblValor = Label(newWindow2, text = "Valor a Aumentar: ")
            valor = IntVar()
            txtValor = Entry(newWindow2, width=20, textvariable=valor)

            buttonExample = Button(newWindow2, text = "AUMENTAR", command=lambda : aumentar_valor(id_cuenta, valor.get() + valor_cuenta, nume_tarj))

            lblTitulo.pack()

            lblNum.pack()
            lblNumeTarj.pack()

            lblValoAc.pack()
            lblValoAct.pack()

            lblValor.pack()
            txtValor.pack()

            buttonExample.pack()
            root.withdraw()
        else:
            messagebox.showinfo('Advertencia', 'Numero de Tarjeta Incorrecto')
    else:
        messagebox.showinfo('Advertencia', 'Campos Vacios')


if __name__ == '__main__':
    root = Tk()
    root.title("COMPRAS")
    root.resizable(1, 1)
    root.geometry("700x700")

    abrir_ingreso = Button(root, text = "Ingreso clientes", command=lambda: registrar_clientes())
    abrir_ingreso.grid(row=1, column=1)

    nom = StringVar()
    txtNom = Entry(root, width=30, textvariable=nom)
    txtNom.grid(row=3, column=1)
    abrir_cuenta = Button(root, text = "Crear Cuenta", command=lambda: crear_cuenta(nom.get()))
    abrir_cuenta.grid(row=3, column=2)

    val = StringVar()
    txtVal = Entry(root, width=30, textvariable=val)
    txtVal.grid(row=5, column=1)
    aumentar_valor = Button(root, text = "Aumentar Valor", command=lambda: aumentar_cuenta(val.get()))
    aumentar_valor.grid(row=5, column=2)

    val = StringVar()
    txtVal = Entry(root, width=30, textvariable=val)
    txtVal.grid(row=5, column=1)
    aumentar_valor = Button(root, text = "Aumentar Valor", command=lambda: aumentar_cuenta(val.get()))
    aumentar_valor.grid(row=5, column=2)

    root.mainloop()