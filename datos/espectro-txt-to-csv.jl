# Script para convertir los ficheros TXT del espectrógrafo a formato CSV.
# Autor: Alfredo Sánchez Alberca (asaber@ceu.es)

using Glob

# Directorio que contiene los ficheros con los espectros.
input_dir = "datos/espectros-variabilidad-01-08-2025"
if !isdir(input_dir)
    error("El directorio $input_dir no existe.")
end
# Obtenemos todos los ficheros con extensión .TXT en el directorio.
txt_files = Glob.glob("*.TXT", input_dir)

for input_file in txt_files
    # Cambiamos la extensión de los ficheros generados a csv.
    output_file = replace(input_file, r"\.TXT$" => ".csv")

    lines = readlines(input_file)

    # Eliminamos líneas 1 a 5 y 7 a 8 (índices 1:5 y 7:8 después de eliminar las primeras 5).
    filtered_lines = vcat(lines[6], lines[9:end])

    # Reemplazamos coma por punto para los decimales.
    filtered_lines = replace.(filtered_lines, ',' => '.')
    # Reemplazamos punto y coma por coma para formato CSV.
    filtered_lines = replace.(filtered_lines, ';' => ',')

    # Guardamos el resultado.
    open(output_file, "w") do io
        for line in filtered_lines
            println(io, strip(line))
        end
    end

    println("Archivo CSV generado: $output_file")
end