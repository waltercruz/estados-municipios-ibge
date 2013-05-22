import lxml.html as html
import glob
import sys
f = open('municipios.sql','w+')

arquivos = glob.glob('estados/*')
sql = []

#arquivos = ['estados/sp.html']
for arquivo in arquivos:
	doc = html.parse(arquivo)
	estadoNode = doc.xpath('//h1')
	estadoName = estadoNode[0].text.split('-')[0]
	estadoSigla = estadoNode[0].text.split('-')[1].strip()

	for i in doc.xpath("//*[@class='nome']"):
		municipioNome = i.text
		municipioId = i.getnext().text
		sql.append('INSERT INTO municipios (codigo,nome,estado) VALUES ('+ municipioId +',"'+municipioNome+'","'+estadoSigla+'");')

#print sql
f.write('\n'.join(sql).encode('utf8'))
