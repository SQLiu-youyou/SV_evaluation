import sys


if __name__ == '__main__':
    file = open('chm1.vcf', 'w')
    with open(sys.argv[1], 'r') as f:
        for line in f:
            a = line.split('\t')
            if a[3] == 'deletion':
                del_length = int(a[2])-int(a[1])+1
                file.write(a[0]+'\t'+a[1]+'\t'+'nssv13699237'+'\t'+'A'+'\t'+'<DEL>'+'\t'+'.'+'\t'+'.'+'\t'+'SVTYPE=DEL;END='+a[2]+';SVLEN=-'+str(del_length)+'\n')
            if a[3] == 'insertion':
                ins_length = len(a[4])
                file.write(a[0] + '\t' + a[2] + '\t' + 'nssv13699237' + '\t' + 'A' + '\t' + '<INS>' + '\t' + '.' + '\t' + '.' + '\t' + 'SVTYPE=INS;END=' +a[2] + ';SVLEN=' +str(ins_length)+ '\n')
            if a[3] == 'tandem duplication':
                dup_length = int(a[2])-int(a[1])+1
                file.write(a[0] + '\t' + a[1] + '\t' + 'nssv13699237' + '\t' + 'A' + '\t' + '<DUP>' + '\t' + '.' + '\t' + '.' + '\t' + 'SVTYPE=DUP;END=' +a[2] + ';SVLEN=' + str(dup_length) + '\n')
            if a[3] == 'inversion':
                inv_length = int(a[2])-int(a[1])+1
                file.write(a[0] + '\t' + a[1] + '\t' + 'nssv13699237' + '\t' + 'A' + '\t' + '<INV>' + '\t' + '.' + '\t' + '.' + '\t' + 'SVTYPE=INV;END=' +a[2] + ';SVLEN=' + str(inv_length) + '\n')



