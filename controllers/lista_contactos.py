import web
import sqlite3
import os

render = web.template.render('views', base='layout')

class ListaContactos:

    def obtenerContactos(self):
        conn = None
        try:
            # Esto localiza la base de datos de forma automática sin importar dónde ejecutes el comando
            base_dir = os.path.dirname(os.path.abspath(_file_))
            db_path = os.path.abspath(os.path.join(base_dir, '..', 'bootstrap', 'sql', 'agenda.db'))
            
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            cursor.execute("SELECT * FROM contactos;")
            
            contactos = []
            for row in cursor.fetchall():
                contacto = {
                    'id_contacto': row[0],
                    'nombre': row[1],
                    'primer_apellido': row[2],
                    'segundo_apellido': row[3],
                    'email': row[4],
                    'telefono': row[5]
                }
                contactos.append(contacto)
                
            return contactos
            
        except sqlite3.Error as error:
            print(f"ERROR 100: {error.args}")
            return []
        except Exception as error:
            print(f"ERROR 101: {error.args}")
            return []
        finally:
            if conn:
                conn.close()

    def GET(self):
        contactos = self.obtenerContactos()
        print(contactos)
        return render.lista_contactos(contactos)