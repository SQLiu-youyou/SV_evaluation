python bed_vcf.py chm1.bed
cat head.txt chm1.vcf > chm1_head.vcf
rm chm1.vcf
python vcf_vcfgt.py chm1_head.vcf
rm chm1_head.vcf
mv gt.vcf TOTAL.chm1.vcf
