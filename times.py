input_data = open('input.txt','r')
data = input_data.read()
output_data = open('output.txt','w')
data = data.split('-')
a= int(data[0])
a1=a*3600
b= int(data[1])
b1=b*60
c= int(data[2])
d=(a1+b1+c)
output_data.write(str(d))
output_data.close()
input_data.close()