import numpy as np
import pickle
import justpy as jp
import requests

#Chance_of_Admit
@jp.SetRoute('/home')
def home():
    wp = jp.WebPage()
    div = jp.Div(a= wp, classes='bg-gray-100 text-center',style=' height: 620px; width: 1350px;')
    jp.Label(a=div,text='Welcome to the Admission Chance Predictor',
             style='font-weight: bold; font-size:40px; margin-top:5px;')
    maindiv1 = jp.Div(a=div,style='')
    maindiv2 = jp.Div(a=maindiv1, classes='bg-red-100 text grid-cols-2')

    div1 = jp.Div(a=maindiv2, classes='bg-green-300 ',style='height: 450px; width: 600px; padding-top:20px;')
    maindiv3 = jp.Div(a=maindiv2, classes='bg-gray-200 text white',style='height: 50px; font-size:20px')
    resultlbl = jp.Label(a=maindiv3,text='HEllO')
    jp.Label(a=div1,text='Select Your Grades',style='font-weight: bold; font-size:20px;')
    div2 = jp.Div(a=div1, classes='bg grid grid-cols-2',style='height: 400px;  width: 600px;padding-top:0px;')
    lbl_div =jp.Div(a=div2, classes='bg-blue-0 ')
    input_div = jp.Div(a=div2, classes='bg-red-0')

    labels =["English Exam Type","English Score","GRE","University Rating (1-5):","SOP (1-5):"
        ,"LOR (1-5):","GPA (1-5):","Number of Published Papers:"]
    for label in labels:
        jp.Label(a=lbl_div, text=label,style='margin-top:5px;')
        jp.Br(a=lbl_div)
        jp.Br(a=lbl_div)


    eng_sel =make_selector(parent=input_div,txts=["IELTS","TOEFL"], vals=[1,2])
    jp.Br(a=input_div)
    eng_grad = jp.Input(a=input_div, text="Hello", classes='form-input',
                        style='margin-top:5px;',value=7.5, placeholder='English Exam Score ')
    jp.Br(a=input_div)
    gre_grad = jp.Input(a=input_div, text="Hello", classes='form-input',
                        style='margin-top:5px;',value=320, placeholder='GRE Score ')
    jp.Br(a=input_div)
    uni_sel = make_selector(parent=input_div,txts=["1","2","3","4","5"],vals=[1,2,3,4,5])
    jp.Br(a=input_div)
    sop_sel= make_selector(parent=input_div,txts=["1","2","3","4","5"],vals=[1,2,3,4,5])
    jp.Br(a=input_div)
    lor_sel = make_selector(parent=input_div,txts=["1","2","3","4","5"],vals=[1,2,3,4,5])
    jp.Br(a=input_div)
    gpa = jp.Input(a=input_div, text="Hello",classes='form-input',value=3.7,style='width:100px; margin-top:5px;',  placeholder='GPA ')
    jp.Br(a=input_div)
    noa = jp.Input(a=input_div, text="Hello",classes='form-input',value=0,style='width:200px; margin-top:5px;', placeholder='Number of Papers ')
    div_grades = jp.Div(a=div, classes='bg-green-200 text-center',style=' height: 50px; width: 600px;')

    jp.Button(a=div_grades, text='Prediction', click=predict_chance, eng_sel=eng_sel,
              eng_grad= eng_grad, gre_grad=gre_grad, uni_sel=uni_sel, sop_sel=sop_sel, lor_sel=lor_sel,
              gpa=gpa, noa=noa,resultlbl=resultlbl,
              classes='btn btn bg-blue-500 border border-yellow-500 m-2 py-1 '
                      'px-4 rounded hover:bg-red-500 text-white ')
    return wp


def predict_chance(widget , msg):
    #req = requests.get("http://127.0.0.1:8001/api?w=1")
    #result = req.json()
    if widget.eng_sel.value == '1':
        loaded_model = pickle.load(open('models/ielts_model.pkl','rb'))
    else:
        loaded_model = pickle.load_model(open('models/toefl_model.pkl','rb'))

    sample =(np.array([[int(widget.gre_grad.value),float(widget.eng_grad.value),
                                            int(widget.uni_sel.value), int(widget.sop_sel.value),
                                            int(widget.lor_sel.value), float(widget.gpa.value),
                                            int(widget.noa.value)]]))
    result = loaded_model.predict(sample)
    widget.resultlbl.text = result

def make_selector(parent,txts,vals):
    sel = jp.Select(a=parent,classes='form-input',style='margin-top:2px;')
    for index,txt in enumerate(txts):
        sel.add(jp.Option(value=vals[index], text=txt))
    return sel


jp.justpy(home)

