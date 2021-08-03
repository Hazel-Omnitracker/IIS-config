lineasMod = [
    '    </location>\n',
    '                    <virtualDirectory path="/" physicalPath="C:\\Omnitracs\\sylectus-trunk\\GPS411" />\n',
    '                </application>\n'
]

archivo = open("C:\\Windows\\System32\\inetsrv\\config\\applicationHost.config", "r")

lineas = archivo.readlines()

archivo.close()

archivo = open("C:\\Windows\\System32\\inetsrv\\config\\applicationHost.config", "w")

count = 0
for element in  lineas:
    archivo.write(element)
    if element == lineasMod[2]:
        #This counter is used to control when inserting the lines of the WebServices
        count += 1
    if element == lineasMod[0]:
        #This part adds the lines to configure the Web Site
        archivo.write('    <location path="Sylectus">\n')
        archivo.write('        <system.webServer>\n')
        archivo.write('            <asp appAllowDebugging="true" enableParentPaths="true" scriptErrorSentToBrowser="true" />\n')
        archivo.write('        </system.webServer>\n')
        archivo.write('    </location>\n')
    elif element == lineasMod[1]:
        #This part adds the lines to include the Virtual Directories
        archivo.write('                    <virtualDirectory path="/AccountingImportFiles" physicalPath="\\gps003qdev.int.sylectus.com\\d$\\gps411\\Accounting\\Importfiles" />\n')
        archivo.write('                    <virtualDirectory path="/Documentation" physicalPath="\\gps003qdev.int.sylectus.com \\d$\\gps411\\Documentation" />\n')
        archivo.write('                    <virtualDirectory path="/PaperworkImages" physicalPath="C:\\GPS411\\Paperwork" />\n')
        archivo.write('                    <virtualDirectory path="/PCMilerGIFs" physicalPath="C:\\inetpub\\wwwroot\\GPS\\GPS411\\PCMilerGIFs" />\n')
        archivo.write('                    <virtualDirectory path="/Prophesy" physicalPath="C:\\GPS411\\Prophesy" />\n')
        archivo.write('                    <virtualDirectory path="/Uploads" physicalPath="C:\\GPS411\\Uploads" />\n')
    elif element == lineasMod[2] and count == 2:
        #This part adds the lines to convert the folder WebServices to Application
        archivo.write('                <application path="/WebServices" applicationPool="Sylectus">\n')
        archivo.write('                    <virtualDirectory path="/" physicalPath="C:\Omnitracs\sylectus-trunk\GPS411\WebServices" />\n')
        archivo.write('                </application>\n')

archivo.close()