from django.http import HttpResponse
from  django.shortcuts import render, redirect

def home(request):
    data = {}
    
    if request.method=='POST':
        # Sunject 1
        omk = float(request.POST.get('omk'))
        fmk = float(request.POST.get('fmk'))
        percentage = (omk*100)/fmk
        fgpa = percentage/25
        gpa = "{:.1f}".format(fgpa)
        pr = request.POST.get('pr')
        pr2 = request.POST.get('pr2')
        pr3 = request.POST.get('pr3')
        pr4 = request.POST.get('pr4')
        pr5 = request.POST.get('pr5')
        pr6 = request.POST.get('pr6')
        gpoint6 = ''
        gpa6 = ''
        omk6 = 0
        fmk6 = 0
        finalgrade6 = ''
        
        gpointp = ''
        gpointp2 = ''
        gpointp3 = ''
        gpointp4 = ''
        gpointp5 = ''
        gpointp6 = ''
        gpap = ''
        gpap2 = ''
        gpap3 = ''
        gpap4 = ''
        gpap5 = ''
        gpap6 = ''
        omkp = 0
        omkp2 = 0
        omkp3 = 0
        omkp4 = 0
        omkp5 = 0
        omkp6 = 0
        fmkp = 0
        fmkp2 = 0
        fmkp3 = 0
        fmkp4 = 0
        fmkp5 = 0
        fmkp6 = 0
        if pr!='pr':
            omkp = float(request.POST.get('omkp'))
            fmkp = float(request.POST.get('fmkp'))
            percentagep = (omkp*100)/fmkp
            fgpap = percentagep/25
            gpap = "{:0.1f}".format(fgpap)
        
            ogp = omk+omkp
            fgp = fmk + fmkp
            percentfun = (ogp*100)/fgp
            gpointp = check(percentagep)
        else:
            percentfun= percentage
        
        gpoint = check(percentage)
        finalgrade = check(percentfun)
            
        # Sunject 2
        omk2 = float(request.POST.get('omk2'))
        fmk2 = float(request.POST.get('fmk2'))
        percentage2 = (omk2*100)/fmk2
        fgpa2 = percentage2/25
        gpa2 = "{:.1f}".format(fgpa2)
       
        if pr2 !='pr2':
            omkp2 = float(request.POST.get('omkp2'))
            fmkp2 = float(request.POST.get('fmkp2'))
            percentagep2 = (omkp2*100)/fmkp2
            fgpap2 = percentagep2/25
            gpap2 = "{:.1f}".format(fgpap2)
        
            ogp2 = omk2+omkp2
            fgp2 = fmk2 + fmkp2
            percentfun2 = (ogp2*100)/fgp2
            gpointp2 = check(percentagep2)
        else:
            percentfun2 = percentage2
        gpoint2 = check(percentage2)
        finalgrade2 = check(percentfun2)
            
        # Sunject 3
        omk3 = float(request.POST.get('omk3'))
        fmk3 = float(request.POST.get('fmk3'))
        percentage3 = (omk3*100)/fmk3
        fgpa3 = percentage3/25
        gpa3 = "{:.1f}".format(fgpa3)
        if pr3 != 'pr3':
            omkp3 = float(request.POST.get('omkp3'))
            fmkp3 = float(request.POST.get('fmkp3'))
            percentagep3 = (omkp3*100)/fmkp3
            fgpap3 = percentagep3/25
            gpap3 = "{:.2f}".format(fgpap3)
            
            
            ogp3 = omk3+omkp3
            fgp3 = fmk3 + fmkp3
            percentgp3 = (ogp3*100)/fgp3
            
            gpointp3 = check(percentagep3)
        else:
            percentgp3 =percentage3
        gpoint3 = check(percentage3)
        finalgrade3 = check(percentgp3)
        
        # Sunject 4
        omk4 = float(request.POST.get('omk4'))
        fmk4 = float(request.POST.get('fmk4'))
        percentage4 = (omk4*100)/fmk4
        fgpa4 = percentage4/25
        gpa4 = "{:.1f}".format(fgpa4)
        if pr4 != 'pr4':
            omkp4 = float(request.POST.get('omkp4'))
            fmkp4 = float(request.POST.get('fmkp4'))
            percentagep4 = (omkp4*100)/fmkp4
            fgpap4 = percentagep4/25
            gpap4 = "{:.1f}".format(fgpap4)
            
            
            ogp4 = omk4+omkp4
            fgp4 = fmk4 + fmkp4
            percentgp4 = (ogp4*100)/fgp4
            
            gpointp4 = check(percentagep4)
        else:
            percentgp4 = percentage4  
        gpoint4 = check(percentage4)
        finalgrade4 = check(percentgp4)  
        
        # Sunject 5
        omk5 = float(request.POST.get('omk5'))
        fmk5 = float(request.POST.get('fmk5'))
        percentage5 = (omk5*100)/fmk5
        fgpa5 = percentage5/25
        gpa5 = "{:.1f}".format(fgpa5)
        if pr5 != 'pr5':
            omkp5 = float(request.POST.get('omkp5'))
            fmkp5 = float(request.POST.get('fmkp5'))
            percentagep5 = (omkp5*100)/fmkp5
            fgpap5 = percentagep5/25
            gpap5 = "{:.1f}".format(fgpap5)
            
            
            ogp5 = omk5+omkp5
            fgp5 = fmk5 + fmkp5
            percentgp5 = (ogp5*100)/fgp5
            
            gpointp5 = check(percentagep5)
        else:
            percentgp5 = percentage5
        gpoint5 = check(percentage5)
        finalgrade5 = check(percentgp5)
            
        # Sunject 6
        optional = request.POST.get('optionals')
        if optional != 'optional':
            omk6 = float(request.POST.get('omk6'))
            fmk6 = float(request.POST.get('fmk6'))
            percentage6 = (omk6*100)/fmk6
            fgpa6 = percentage6/25
            gpa6 = "{:.1f}".format(fgpa6)
            if pr6 != 'pr6':
                omkp6 = float(request.POST.get('omkp6'))
                fmkp6 = float(request.POST.get('fmkp6'))
                percentagep6 = (omkp6*100)/fmkp6
                fgpap6 = percentagep6/25
                gpap6 = "{:.1f}".format(fgpap6)
                
                
                ogp6 = omk6+omkp6
                fgp6 = fmk6 + fmkp6
                percentgp6 = (ogp6*100)/fgp6
                
                gpointp6 = check(percentagep6)
            else:
                percentgp6 = percentage6
            gpoint6 = check(percentage6)
            finalgrade6 = check(percentgp6)
        
        final = omk + omkp + omk2 + omkp2 + omk3 + omkp3 + omk4 + omkp4 + omk5 + omkp5 + omk6 + omkp6
        full =  fmk + fmkp + fmk2 + fmkp2 + fmk3 + fmkp3 + fmk4 + fmkp4 + fmk5 + fmkp5 + fmk6 + fmkp6
        ftotal_grade = ((final*100)/full)/25
        total_grade = "{:.1f}".format(ftotal_grade)
        data = {
            'name' : request.POST.get('name'),
            'dofbs': request.POST.get('dofbs'),
            'dofad': request.POST.get('dofad'),
            'reg': request.POST.get('reg'),
            'smb': request.POST.get('smb'),
            'doebs': request.POST.get('doebs'),
            'doead': request.POST.get('doead'),
            'doi': request.POST.get('doi'),
            'subjects': [
                {'scode': request.POST.get('scode'),
                'sname': request.POST.get('sname'),
                'ch':request.POST.get('ch'),
                'gpa': gpa,
                'gpoint': gpoint,
                
                
                'scodep': request.POST.get('scodep'),
                'snamep': request.POST.get('snamep'),
                'chp':request.POST.get('chp'),
                'gpointp': gpointp,
                'gpap': gpap,
                'finalgrade': finalgrade,
                },
                
                {'scode': request.POST.get('scode2'),
                'sname': request.POST.get('sname2'),
                'ch':request.POST.get('ch2'),
                'gpa': gpa2,
                'gpoint': gpoint2,
                
                'scodep': request.POST.get('scodep2'),
                'snamep': request.POST.get('snamep2'),
                'chp':request.POST.get('chp2'),
                'gpap': gpap2,
                'gpointp': gpointp2,
                'finalgrade': finalgrade2,
                },
            
                {'scode': request.POST.get('scode3'),
                    'sname': request.POST.get('sname3'),
                    'ch':request.POST.get('ch3'),
                    'gpa': gpa3,
                    'gpoint': gpoint3,
                    
                    'scodep': request.POST.get('scodep3'),
                    'snamep': request.POST.get('snamep3'),
                    'chp':request.POST.get('chp3'),
                    'gpap': gpap3,
                    'gpointp': gpointp3,
                    'finalgrade': finalgrade3,
                },
                {'scode': request.POST.get('scode4'),
                    'sname': request.POST.get('sname4'),
                    'ch':request.POST.get('ch4'),
                    'gpa': gpa4,
                    'gpoint': gpoint4,
                    
                    'scodep': request.POST.get('scodep4'),
                    'snamep': request.POST.get('snamep4'),
                    'chp':request.POST.get('chp4'),
                    'gpap': gpap4,
                    'gpointp': gpointp4,
                    'finalgrade': finalgrade4,
                },
                {'scode': request.POST.get('scode5'),
                    'sname': request.POST.get('sname5'),
                    'ch':request.POST.get('ch5'),
                    'gpa': gpa5,
                    'gpoint': gpoint5,
                    
                    'scodep': request.POST.get('scodep5'),
                    'snamep': request.POST.get('snamep5'),
                    'chp':request.POST.get('chp5'),
                    'gpap': gpap5,
                    'gpointp': gpointp5,
                    'finalgrade': finalgrade5,
                },
                {'scode': request.POST.get('scode6'),
                    'sname': request.POST.get('sname6'),
                    'ch':request.POST.get('ch6'),
                    'gpa': gpa6,
                    'gpoint': gpoint6,
                    
                    'scodep': request.POST.get('scodep6'),
                    'snamep': request.POST.get('snamep6'),
                    'chp':request.POST.get('chp6'),
                    'gpap': gpap6,
                    'gpointp': gpointp6,
                    'finalgrade': finalgrade6,
                },
            ],
            'total_grade': total_grade
                
        }
        return render(request,'index.html', data)
    return render(request,'form.html' , data)

def check(values):
    if values >= 90 and values <= 100:
        return 'A+'
    elif values >= 80 and values < 90 :
        return 'A'
    elif values >= 70 and values < 80:
        return 'B+'
    elif values >= 60 and values < 70:
        return 'B'
    elif values >= 50 and values < 60:
        return 'C+'
    elif values >= 40 and values < 50:
        return 'C'
    elif values >= 30 and values < 40:
        return 'D+'
    elif values >= 20 and values < 30:
        return 'D'
    elif values >= 0 and values < 20:
        return 'E'
    else:
        return 'not'
    