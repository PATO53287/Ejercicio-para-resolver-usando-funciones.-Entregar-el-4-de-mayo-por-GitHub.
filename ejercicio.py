# --- 1. LAS HERRAMIENTAS (FUNCIONES) ---

def calcular_objetivo_ml(peso, actividad):
    # Usamos el PESO que entra por el paréntesis
    meta = peso * 35 
    
    # Usamos ESTRUCTURAS DE CONTROL (if/elif) para decidir el ajuste
    if actividad == "bajo":
        meta = meta * 0.90
    elif actividad == "alto":
        meta = meta * 1.10
        
    return meta # El RETURN devuelve el número final

def obtener_estado(consumo, objetivo):
    # Comparamos números para decidir qué mensaje mostrar
    if consumo < objetivo:
        porcentaje = ((objetivo - consumo) / objetivo) * 100
        return f"Te falta un {porcentaje:.1f}%" 
    elif consumo == objetivo:
        return "Objetivo alcanzado"
    else:
        porcentaje = ((consumo - objetivo) / objetivo) * 100
        return f"Excedido en {porcentaje:.1f}%"

        # --- 2. EL MOTOR DEL PROGRAMA (WHILE Y DICCIONARIOS) ---

personas = [] # Esta es la LISTA (nuestro archivador)

while True: # BUCLE infinito para cargar mucha gente
    try:
        # INPUTS: Capturamos datos del usuario
        peso_ingresado = float(input("Peso (0 para salir): "))
        if peso_ingresado == 0:
            break # El BREAK detiene el bucle
            
        actividad_ingresada = input("Actividad (bajo/medio/alto): ").lower().strip()
        consumo_ingresado = float(input("Consumo en ml: "))

        # Llamamos a las FUNCIONES y guardamos sus resultados en variables
        meta_final = calcular_objetivo_ml(peso_ingresado, actividad_ingresada)
        estado_final = obtener_estado(consumo_ingresado, meta_final)

        # Creamos el DICCIONARIO (La "ficha" de la persona)
        usuario = {
            "peso": peso_ingresado,
            "meta": meta_final,
            "estado": estado_final
        }
        
        # Guardamos la ficha en la LISTA con .APPEND
        personas.append(usuario)
        
        print(f"Meta: {meta_final}ml | {estado_final}")

    except ValueError:
        # El EXCEPT atrapa errores si el usuario no escribe números
        print("Error: Ingresa números válidos.")

# --- 3. EL CIERRE (RECORRER LA LISTA) ---

print("\n--- RESUMEN FINAL ---")
for p in personas: # El FOR recorre cada ficha en la lista
    print(f"Peso: {p['peso']}kg - Meta: {p['meta']:.0f}ml - {p['estado']}")
