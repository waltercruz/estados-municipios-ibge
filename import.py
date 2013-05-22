import lxml.html as html
import glob
import sys
f = open('municipios.sql','w+')

estados = {'AC':'1',
		   'AL':'2',
		   'AM':'3',
		   'AP':'4',
		   'BA':'5',
		   'CE':'6',
		   'DF':'7',
		   'ES':'8',
		   'GO':'9',
		   'MA':'10',
		   'MG':'11',
		   'MS':'12',
		   'MT':'13',
		   'PA':'14',
		   'PB':'15',
		   'PE':'16',
		   'PI':'17',
		   'PR':'18',
		   'RJ':'19',
		   'RN':'20',
		   'RO':'21',
		   'RR':'22',
		   'RS':'23',
		   'SC':'24',
		   'SE':'25',
		   'SP':'26',
		   'TO':'27'}

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
		try:
			sql.append('INSERT INTO municipios (codigo,nome,fk_estado) VALUES ('+ str(int(municipioId)) +',"'+municipioNome+'","'+estados[estadoSigla]+'");')
		except:
			pass
			#print(municipioId+ '-'+ estadoSigla)
#print sql
f.write('\n'.join(sql).encode('utf8'))
