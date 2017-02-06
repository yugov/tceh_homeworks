# Есть класс, который выводи информацию в консоль: `Printer`, у него есть метод: log(*values).
# Написать класс FormattedPrinter, который выводит в консоль информацию, окружая ее строками из *

class Printer(object):
    def log(self, *text):
        mytext = ''
        self.text = text
        for t in text:
            mytext += ' ' + t
        print(mytext)
        return mytext


class FormattedPrinter(object):
    def flog(self, ftext):
        self.ftext = ftext
        print(15 * '*' + '\n' + '*', self.ftext, '*\n' + 15 * '*')
        return


text1 = Printer()

text2 = FormattedPrinter()
text2.flog(text1.log('text123', 'test321'))