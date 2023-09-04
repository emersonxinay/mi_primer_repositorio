# emerson espinoza aguirre - 3g
import sesion 

# bloques de prueba 
if __name__ == "__main__":
    # ingresar datos dinamicos para sesión
    user = input("ingrese su usuario: ")
    contra = input("ingrese su contraseña: ")
    # invocar a la funcion del modulo sesión 
    sesion.login(user, contra )  