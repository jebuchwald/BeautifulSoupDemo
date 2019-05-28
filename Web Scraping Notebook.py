#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup as soup
from urllib.request import urlopen


# In[2]:


# Opening a webpage (wiki_url) as a variable (wiki_data)
# Reading the webpage variable (wiki_data) and assigning the contents to a variable (wiki_html)
# Closing the webpage data
wiki_url = 'https://en.wikipedia.org/wiki/Genome'
wiki_data = urlopen(wiki_url)
wiki_html = wiki_data.read()
wiki_data.close()

# Creating page_soup variable which contains the data read off the website
# This is accomplished by using BeautifulSoup (imported in as soup) with the first argument being the variable to be parsed and the second being teh
page_soup = soup(wiki_html, 'html.parser')
print(page_soup)


# In[3]:


genome_table = page_soup.findAll('table', {'class': 'wikitable sortable'})
print(genome_table)


# In[4]:


genome_table = genome_table[0]
headers = genome_table.findAll('th',{})
print(headers)


# In[5]:


header_titles = []
for header in headers:
    header_titles.append(header.text[:-1])
print(header_titles)


# In[6]:


all_rows = genome_table.findAll('tr', {})
print(all_rows)


# In[7]:


data = all_rows[1:]
print(data)


# In[8]:


first_row = data[0]
first_row_data = first_row.findAll('td', {})
print(first_row_data)


# In[9]:


data_texts = []
for data_text in first_row_data:
    data_texts.append(data_text.text[:-1])
print(data_texts)


# In[10]:


table_rows = []
for row in data:
    table_row = []
    row_data = row.findAll('td', {})
    for data_point in row_data:
        table_row.append(data_point.text[:-1])
    table_rows.append(table_row)
print(table_rows)


# In[11]:


filename = 'genome_table.csv'
f = open(filename, 'w', encoding='utf-8')

header_string = ''
for title in header_titles:
    header_string += title + ','
header_string = header_string[:-1]
header_string += '\n'

f.write(header_string)

for row in table_rows:
    row_string = ''
    for column in row:
        column_string = column.replace(',','')
        column_string = column.replace(',','')
        row_string += column_string + ','
    row_string = row_string[:-1]
    row_string += '\n'
    
    f.write(row_string)


# In[12]:


filename = 'GenomeWikipedia.htm'
f = open(filename, 'r', encoding='utf-8')

new_soup = soup(f, 'html.parser')
print(new_soup.h1)


# In[13]:


print(new_soup.findAll('table',{'class': 'wikitable sortable'}))


# In[14]:


print(page_soup.h1)


# In[16]:


references_lists_raw = page_soup.findAll('ol', {'class': 'references'})
print(references_lists_raw)


# In[20]:


references_lists = references_lists_raw[0].findAll('li', {})

all_references = []
for list_item in references_lists:
    references = []
    for reference in list_item.findAll('a', {}):
        references.append(reference['href'])
    all_references.append(references)
    
print(all_references)


# In[ ]:




