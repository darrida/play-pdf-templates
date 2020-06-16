
import weasyprint
for _ in range(1,11):
    weasyprint.HTML('1.html').write_pdf('tmp/1.pdf')