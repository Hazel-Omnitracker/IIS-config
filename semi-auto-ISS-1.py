lineasMod = [
    '            <add name=".NET v4.5" managedRuntimeVersion="v4.0" />\n'
]

archivo = open("C:\\Windows\\System32\\inetsrv\\config\\applicationHost.config", "r")

lineas = archivo.readlines()

archivo.close()

archivo = open("C:\\Windows\\System32\\inetsrv\\config\\applicationHost.config", "w")

for element in  lineas:
    archivo.write(element)
    if element == lineasMod[0]:
        archivo.write('            <add name="Sylectus" autoStart="true" enable32BitAppOnWin64="true" managedRuntimeVersion="v4.0" managedPipelineMode="Classic">\n')
        archivo.write('                <processModel pingResponseTime="00:15:00" />\n')
        archivo.write('            </add>\n')
archivo.close()