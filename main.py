import tkinter as tk
from tkinter import ttk


master = tk.Tk()
master.geometry('500x500')
master.title('wiki citation wizard')

last1_var = tk.StringVar()
first1_var = tk.StringVar()
last2_var = tk.StringVar()
first2_var = tk.StringVar()
title_var = tk.StringVar()
url_var = tk.StringVar()
source_date_var = tk.StringVar()
journal_var = tk.StringVar()
volume_var = tk.StringVar()
issue_var = tk.StringVar()
pages_var = tk.StringVar()


def citation_submit():

    last1 = last1_var.get()
    first1 = first1_var.get()
    last2 = last2_var.get()
    first2 = first2_var.get()
    title = title_var.get()
    url = url_var.get()
    source_date = source_date_var.get()
    journal = journal_var.get()
    volume = volume_var.get()
    issue = issue_var.get()
    pages = pages_var.get()

    # data transformer 1
    transformer1 = [{'label': 'last1', 'entry_data': last1},
                    {'label': 'first1', 'entry_data': first1},
                    {'label': 'last2', 'entry_data': last2},
                    {'label': 'first2', 'entry_data': first2},
                    {'label': 'title', 'entry_data': title},
                    {'label': 'url', 'entry_data': url},
                    {'label': 'source_date', 'entry_data': source_date},
                    {'label': 'journal', 'entry_data': journal},
                    {'label': 'volume', 'entry_data': volume},
                    {'label': 'issue', 'entry_data': issue},
                    {'label': 'pages', 'entry_data': pages}]

    # conditional enforcer:
    # filter out entries containing str('x')
    # outputs to a sequentially formatted filtered_input[{}]
    filtered_inputs = []
    for i in transformer1:
        if i['entry_data'] != 'x':
            filtered_inputs.append({'label': i['label'], 'entry_data': i['entry_data']})

    # adaptive citation engine:
    citations_proper = []
    for j in filtered_inputs:
        if j['label'] == 'last1':
            citations_proper.append({'prefix': 'last1=', 'entry_data': j['entry_data'], 'suffix': ' | '})
        elif j['label'] == 'first1':
            citations_proper.append({'prefix': 'first1=', 'entry_data': j['entry_data'], 'suffix': ' | '})
        elif j['label'] == 'last2':
            citations_proper.append({'prefix': 'last2=', 'entry_data': j['entry_data'], 'suffix': ' | '})
        elif j['label'] == 'first2':
            citations_proper.append({'prefix': 'first2=', 'entry_data': j['entry_data'], 'suffix': ' | '})
        elif j['label'] == 'title':
            citations_proper.append({'prefix': 'title=', 'entry_data': j['entry_data'], 'suffix': ' | '})
        elif j['label'] == 'url':
            citations_proper.append({'prefix': 'url=', 'entry_data': j['entry_data'], 'suffix': ' | '})
        elif j['label'] == 'source_date':
            citations_proper.append({'prefix': 'source-date=', 'entry_data': j['entry_data'], 'suffix': ' | '})
        elif j['label'] == 'journal':
            citations_proper.append({'prefix': 'journal=', 'entry_data': j['entry_data'], 'suffix': ' | '})
        elif j['label'] == 'volume':
            citations_proper.append({'prefix': 'volume=', 'entry_data': j['entry_data'], 'suffix': ' | '})
        elif j['label'] == 'issue':
            citations_proper.append({'prefix': 'issue=', 'entry_data': j['entry_data'], 'suffix': ' | '})
        elif j['label'] == 'pages':
            citations_proper.append({'prefix': 'pages=', 'entry_data': j['entry_data'], 'suffix': ''})
        else:
            print('error')

    # data transformer 2
    # looking for a pure list
    transformer2 = []
    for x in citations_proper:
        transformer2.append(x['prefix'])
        transformer2.append(x['entry_data'])
        transformer2.append(x['suffix'])

    final_citation = ''.join(transformer2)

    print('final_citation:')
    print('<ref>{{cite journal |', final_citation, '}}</ref>')

    last1_var.set('')
    first1_var.set('')
    last2_var.set('')
    first2_var.set('')
    title_var.set('')
    url_var.set('')
    source_date_var.set('')
    journal_var.set('')
    volume_var.set('')
    issue_var.set('')
    pages_var.set('')


# all entry fields and labels creation
label_ln1 = tk.Label(master, text='last name 1')
entry_ln1 = ttk.Entry(master, textvariable=last1_var)

label_fn1 = tk.Label(master, text='first name 1')
entry_fn1 = ttk.Entry(master, textvariable=first1_var)

label_ln2 = tk.Label(master, text='last name 2')
entry_ln2 = ttk.Entry(master, textvariable=last2_var)

label_fn2 = tk.Label(master, text='first name 2')
entry_fn2 = ttk.Entry(master, textvariable=first2_var)

label_tit = tk.Label(master, text='title')
entry_tit = ttk.Entry(master, textvariable=title_var)

label_url = tk.Label(master, text='url')
entry_url = ttk.Entry(master, textvariable=url_var)

label_sd = tk.Label(master, text='source-date')
entry_sd = ttk.Entry(master, textvariable=source_date_var)

label_jour = tk.Label(master, text='journal')
entry_jour = ttk.Entry(master, textvariable=journal_var)

label_vol = tk.Label(master, text='volume')
entry_vol = ttk.Entry(master, textvariable=volume_var)

label_iss = tk.Label(master, text='issue')
entry_iss = ttk.Entry(master, textvariable=issue_var)

label_pgs = tk.Label(master, text='pages')
entry_pgs = ttk.Entry(master, textvariable=pages_var)

# Button calling submit_citation()
button1 = ttk.Button(master, text='Cite', command=citation_submit, compound=tk.TOP)

# placing the label and entry with grid
label_ln1.grid(row=0, column=0)
label_fn1.grid(row=1, column=0)
label_ln2.grid(row=2, column=0)
label_fn2.grid(row=3, column=0)
label_tit.grid(row=4, column=0)
label_url.grid(row=5, column=0)
label_sd.grid(row=6, column=0)
label_jour.grid(row=7, column=0)
label_vol.grid(row=8, column=0)
label_iss.grid(row=9, column=0)
label_pgs.grid(row=10, column=0)

entry_ln1.grid(row=0, column=1)
entry_fn1.grid(row=1, column=1)
entry_ln2.grid(row=2, column=1)
entry_fn2.grid(row=3, column=1)
entry_tit.grid(row=4, column=1)
entry_url.grid(row=5, column=1)
entry_sd.grid(row=6, column=1)
entry_jour.grid(row=7, column=1)
entry_vol.grid(row=8, column=1)
entry_iss.grid(row=9, column=1)
entry_pgs.grid(row=10, column=1)

button1.grid(row=10, column=3)

label_legend = tk.Label(master, text='NOTICE: populate all null fields with the character: x')
label_legend.place(relx=0.5, rely=0.7, anchor='center')

master.mainloop()

