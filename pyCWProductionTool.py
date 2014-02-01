# -*- coding: utf-8 -*-
import sys, os, codecs
delimiter = 'þþ'
BegID = "Begno"
d2 = r"þ"
TextPath = "TextPath"
NativeFile = "NativeFile"
#CustodianField = "Author"
#f = codecs.open("GS-CFTC-001.dat", "r", "utf-8")
#count = 0
#Custodians = []
header = None
OriginalDatFile = "GS-CFTC-001.dat"
Fields = []
Custodians = []

def map(maplist):
	mapcount = 0
	for i in maplist:
		print i.encode("utf-8")+"	"+str(mapcount)
		mapcount = mapcount + 1
	result = raw_input()
	result2 = maplist[int(result)]
	result2 = result2.encode("utf-8")
	#print int(result)
	return int(result), result2

def opt_parse(imagefiles,c):
	for image in imagefiles:
		count = 0
		f = open("GS-CFTC-001.opt", "r")
		#print "working on "+image+" now"
		linecount = f.readlines()
		for litr in range(0, len(linecount)):
			line = linecount[litr]
			line = line.strip()
			i = line.split(',')
			
			if i[0] == str(image):

				if i[6] == '':
					i[6] = 0
				dir = i[2].split('\\')
				dir2 = '\\'.join(dir[2:-1])
				#for i in line.split(','):
				if int(i[6]) >= 1:
					count = int(i[6])
					if not os.path.exists(".\\\""+c+"\"\\"+dir2):
						#print ".\\"+c+"\\"+dir2
						os.system("MKDIR .\\\""+c+"\"\\"+dir2)
					#print "copy file "+str(i[0])+" #"+str(count)+"to "+dir2
					#print "COPY .\\"+'\\'.join(dir[2:])+" .\\\""+c+"\"\\"+dir2
					os.system("COPY .\\"+'\\'.join(dir[2:])+" .\\\""+c+"\"\\"+dir2)
					#os.system("COPY "+i[2]+" .\\\""+c+"\"\\"+dir2)
					#os.system("MKDIR "+dir2)
					count = count - 1 #number of files to copy
			elif count >> 0:
				dir = i[2].split('\\')
				dir2 = '\\'.join(dir[2:-1])
				#print count
				#print "HERE?"
				if not os.path.exists(".\\\""+c+"\"\\"+dir2):
					#print ".\\"+c+"\\"+dir2
					os.system("MKDIR .\\\""+c+"\"\\"+dir2)
				#print "copy file "+str(i[0])+" #"+str(count)+"to "+dir2
				#print "COPY .\\"+'\\'.join(dir[2:])+" .\\\""+c+"\"\\"+dir2
				os.system("COPY .\\"+'\\'.join(dir[2:])+" .\\\""+c+"\"\\"+dir2)
				count = count - 1
		f.close
	
def GetLines(feildIndex, field, d2):	
	#print Fields
	count = 0
	f = codecs.open(OriginalDatFile, "r", "utf-8")
	for line in f:
		#print line.encode("utf-8")
		#line.split(delimiter.decode("utf-8"))
		if count == 0:
			count = count+1
		elif count >> 0:
			for i in line.split(delimiter.decode("utf-8")):
				if i.startswith(d2.decode("utf-8")):
					i = i[1:]
				elif i.endswith(d2.decode("utf-8")):
					i = i[:-1]
				if i == field:
					lines.append(line)
				count = count + 1
				
def GetCustodian(FieldIndex, OriginalDatFile, d2, delimiter, Custodians):
	print FieldIndex
	f = codecs.open(OriginalDatFile, "r", "utf-8")
	count = 0
	FieldCount = 0
	for line in f:
		if count == 0:
			count = count + 1
		else:
			line2 = line.split(delimiter.decode("utf-8"))
			#print line2[FieldIndex].encode("utf-8")
			if	line2[FieldIndex].encode("utf-8") not in Custodians:
					Custodians.append(line2[FieldIndex])
					count = count + 1

	choice = map(Custodians)
	return choice[1]
	
def getFields(header, OriginalDatFile, d2, delimiter):
	FieldCount = 0 
	t = []
	f = codecs.open(OriginalDatFile, "r", "utf-8")
	header = f.readline()
	y = header.strip().split(delimiter.decode("utf-8"))
	for i in y:
		if i.startswith(d2.decode("utf-8")):
			i = i[1:]
		elif i.endswith(d2.decode("utf-8")):
			i = i[:-1]
		t.append(i)
		#print str(FieldCount)+"\t"+i.encode("utf-8")
		#if i == CustodianField:
		#	CustodianField = FieldCount
		#	print "\nAuthor is "+str(FieldCount)
		FieldCount = FieldCount + 1
	#print "Print Selection: "+result = raw_input()
	f.close()
	return t

def buildLists(CustodianField, BegField, OriginalDatFile, NativeFile, TextPath, d2, delimiter, custodian):
	f = codecs.open(OriginalDatFile, "r", "utf-8")
	os.system("MKDIR \""+str(custodian)+"\"")
	n = codecs.open(".\\"+custodian+"\\"+custodian+".dat", "w", "utf-8")
	count = 0
	Begs = []
	for line in f:
		t = []
		if count == 0:
			count = count+1
		elif count >> 0:
			for i in line.split(delimiter.decode("utf-8")):
				if i.startswith(d2.decode("utf-8")):
					i = i[1:]
				elif i.endswith(d2.decode("utf-8")):
					i = i[:-1]
				if i == custodian:
					for j in line.split(delimiter.decode("utf-8")):
						if j.startswith(d2.decode("utf-8")):
							j = j[1:]
							j = j.strip().replace(u'\xfe','')
							Begs.append(j)
						elif j.endswith(d2.decode("utf-8")):
							j = j[:-1]
							j = j.strip().replace(u'\xfe','')
						t.append(j)
						
					n.write(line)
					
					dirA = t[NativeFile[0]].replace(u'\xfe','').strip().split('\\')
					dirA2 = '\\'.join(dirA[2:-1])
					dirB = t[TextPath[0]].replace(u'\xfe','').strip().split('\\')
					dirB2 = '\\'.join(dirB[2:-1])
					
					#Natives
					if not os.path.exists(".\\\""+custodian+"\"\\"+dirA2):
						os.system("MKDIR .\\\""+custodian+"\"\\"+dirA2)
					os.system("COPY "+'\\'.join(dirA[2:])+" "+"\""+custodian+"\"\\"+'\\'.join(dirA[2:]))
					
					#Texts
					if not os.path.exists(".\\\""+custodian+"\"\\"+dirB2):
						os.system("MKDIR .\\\""+custodian+"\"\\"+dirB2)
					os.system("COPY "+'\\'.join(dirB[2:])+" "+"\""+custodian+"\"\\"+'\\'.join(dirB[2:]))
			count = count + 1
	n.close()
	opt_parse(Begs,custodian)

		


	
Fields = getFields(header, OriginalDatFile, d2, delimiter) 
count = 0
for Field in Fields:
	if Field == TextPath:
		TextPath = [count, TextPath]
	if Field == NativeFile:
		NativeFile = [count, NativeFile]
	count = count + 1

		
	
print "Please Seltect your Custodian Field"
CustodianField = map(Fields)

#choose beg field
print "Please Seltect your Beg Field"
BegField = map(Fields)

#choose custodian
print "Please Seltect your Custodian"
custodian = GetCustodian(CustodianField[0], OriginalDatFile, d2, delimiter, Custodians)
buildLists(CustodianField, BegField, OriginalDatFile, NativeFile, TextPath, d2, delimiter, custodian)
#custodian = Custodians[custodian]

#write dat file


'''
----------Here start workign on printing. Pull files from custodian, then pass to opt.
os.system("MKDIR \""+str(custodian)+"\"")
f = codecs.open(OriginalDatFile, "r", "utf-8")
n = codecs.open(".\\"+custodian+"\\"+custodian+".dat", "w", "utf-8")

for line in f:
	#print line.encode("utf-8")
	#line.split(delimiter.decode("utf-8"))
	if count == 0:
		count = count+1
	elif count >> 0:
		for i in line.split(delimiter.decode("utf-8")):
			if i.startswith(d2.decode("utf-8")):
				i = i[1:]
			elif i.endswith(d2.decode("utf-8")):
				i = i[:-1]
			if i == c:
				n.write(line)
			count = count + 1
#n.close()

'''
