import re
a = 'i have a dog'
print(re.match('i',a))
print(re.search('dog',a))
print(re.findall("\d",a))
print(re.sub('dog','cat',a))
print(re.split(' ',a))

b = '1 plus 2 equals 3'
print(re.findall('\d+',b))    #цифры, повторяющиеся 1 или более раз
print(re.findall('\w+',b))  #слова, повторяющиеся 1 или более раз
print(re.findall('\s+',b))  #пробелы, повторяющиеся 1 или более раз
print(re.findall('\d{3}',b))  #цифры, повторяющиеся 3 раза

c = 'The rain in Spain stays mainly in the plain'
print(re.findall('p*',c))   #буква p, повторяющаяся 0 или более раз
print(re.findall('a.n',c))  #буква a, за которой следует любой символ, за которым следует буква n

d = 'we are the champions'
print(re.findall('^we', d))  #слово, начинающееся с 'we'
print(re.findall('champions$', d))  #слово, заканчивающееся на 'champions'
print(re.findall('^we.*champions$', d))  #строка, начинающаяся с 'we' и заканчивающаяся на 'champions'

e = 'my email is'
print(re.findall('my|is',e)) #слова 'my' или 'is'

f = 'name: John, age: 30, city: New York'
print(re.findall('name:\s*(\w+),\s*age:\s*(\d+),\s*city:\s*(\w+\s*\w*)', f)) #поиск шаблона и извлечение данных

g = 'cat , scat , cat , catapult'
print(re.findall(r'\bcat\b',g)) #поиск слова 'cat' как отдельного слова, а не как части других слов (например, 'scat' или 'catapult')

h = 'aaa12314scd215sef22safc2'
print(re.findall('(\d{4})',h)) #поиск последовательности из 4 цифр в строке
print(re.findall('(\d{3})',h)) #поиск последовательности из 3 цифр в строке
print(re.findall('(\d{2})',h)) #поиск последовательности из 2 цифр в строке

i = 'suyefcgisubgv, 6464 64 usybfvicsu4567890, 985264  esrdtfyguhijo,98765'
pattern = re.compile(r'(\w+),\s*(\d+)') #компиляция шаблона для поиска слов, за которыми следует запятая и число
print(pattern.findall(i)) #поиск всех совпадений шаблона в строке и возвращение их в виде списка кортежей, где каждый кортеж содержит найденные группы (слово и число)
print(pattern.search(i))    #поиск первого совпадения шаблона в строке и возвращение объекта Match, который содержит информацию о найденном совпадении (слово и число)

j = '....,,/..'
pattern_2 = '.'
print(re.escape(j)) #экранирование всех специальных символов в строке, чтобы они воспринимались как обычные символы при использовании в регулярных выражениях