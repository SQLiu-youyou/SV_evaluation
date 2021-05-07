import sys

if __name__ == '__main__':
    file  = open('gt.vcf','w')
    with open(sys.argv[1],'r') as g:
        for line in g:
            if line[0] == '#':
                file.write(line)
            if line[0] !='#':
                a = line.split('\t')
                if a[0] == '1' or  a[0] == '3' or a[0] == '5' or a[0] == '7' or a[0] == '9' or a[0] == '11' or a[0] == '13' or a[0] == '15' or a[0] == '17' or a[0] == '19' or a[0] == '21' :
                    file.write(line.strip()+'\t'+'GT'+'\t'+'0/1'+'\n')
                else:
                    file.write(line.strip() + '\t' + 'GT' + '\t' + '1/1'+'\n')




