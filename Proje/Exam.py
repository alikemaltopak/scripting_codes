import os
import pdfplumber
txt_name = "exam.txt"
if os.path.exists(txt_name) != True:

    with open(txt_name,"w") as txt:

        with pdfplumber.open("/Users/alikemaltopak/Library/CloudStorage/OneDrive-Kişisel/VSCODE_PY/Grade_Lists_midterm1.pdf") as pdf:        # Pdf name or path
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    lines = text.splitlines(True)
                    for line in lines:
                        txt.write(line)
else:


    import matplotlib.pyplot as plt
    def get_list(file_name):
        with open(file_name,"r") as file:
            ceng_grades = []
            cengstd = 0
            ehm_grads = []
            ehmstd = 0
            kimmüh_grades = []
            kim_mühstd = 0
            foton_grades = []
            fotonstd = 0
            enerji_grades = []
            enerjistd = 0
            makine_grades = []
            makinestd = 0
            biomüh_grades = []
            biomühstd = 0
            mbg_grades = []
            mbgstd = 0
            fizik_grades = []
            fizikstd = 0
            malzeme_grades = []
            malzemestd = 0
            mimar_grades = []
            mimarstd = 0
            şbp_grades = []
            şbpstd = 0
            entas_grades = []
            entasstd = 0
            mat_grades = []
            matstd = 0
            gıda_grades = []
            gıdastd = 0
            inşat_grades = []
            inşatstd = 0

            for line in file:
                line = line.strip()
                liste = line.split()
                stdID = liste[0]
                try:
                    grades = liste[1]
                except Exception:
                    grades = "not available because of did'n join the exam."
                seperate_stdID = f"{stdID[:3]},{stdID[3:6]},{stdID[6:]}"
                newstdID = stdID.replace(stdID,seperate_stdID).split(",")
                std_year = newstdID[0]
                std_dprt = newstdID[1]
                std_arng = newstdID[2]
                if std_dprt == "201":
                    try:
                        ceng_grades.append(int(grades))
                    except Exception:
                        pass
                    cengstd += 1
                if std_dprt == "206":
                    try:
                        ehm_grads.append(int(grades))
                    except Exception:
                        pass
                    ehmstd += 1
                if std_dprt == "202":
                    try:
                        kimmüh_grades.append(int(grades))
                    except Exception:
                        pass
                    kim_mühstd += 1
                if std_dprt == "105":
                    try:
                        foton_grades.append(int(grades))
                    except Exception:
                        pass
                    fotonstd += 1
                if std_dprt == "209":
                    try:
                        enerji_grades.append(int(grades))
                    except Exception:
                        pass
                    enerjistd += 1
                if std_dprt == "203":
                    try:
                        makine_grades.append(int(grades))
                    except Exception:
                        pass
                    makinestd += 1
                if std_dprt == "210":
                    try:
                        biomüh_grades.append(int(grades))
                    except Exception:
                        pass
                    biomühstd += 1
                if std_dprt == "104":
                    try:
                        mbg_grades.append(int(grades))
                    except Exception:
                        pass
                    mbgstd += 1
                if std_dprt == "101":
                    try:
                        fizik_grades.append(int(grades))
                    except Exception:
                        pass
                    fizikstd += 1
                if std_dprt == "208":
                    try:
                        malzeme_grades.append(int(grades))
                    except Exception:
                        pass
                    malzemestd += 1
                if std_dprt == "301":
                    try:
                        mimar_grades.append(int(grades))
                    except Exception:
                        pass
                    mimarstd += 1
                if std_dprt == "302":
                    try:
                        şbp_grades.append(int(grades))
                    except Exception:
                        pass
                    şbpstd += 1
                if std_dprt == "303":
                    try:
                        entas_grades.append(int(grades))
                    except Exception:
                        pass
                    entasstd += 1
                if std_dprt == "103":
                    try:
                        mat_grades.append(int(grades))
                    except Exception:
                        pass
                    matstd += 1
                if std_dprt == "205":
                    try:
                        gıda_grades.append(int(grades))
                    except Exception:
                        pass
                    gıdastd += 1
                if std_dprt == "204":
                    try:
                        inşat_grades.append(int(grades))
                    except Exception:
                        pass
                    inşatstd += 1

        return std_year,std_arng,ceng_grades,cengstd,ehm_grads,ehmstd,kimmüh_grades,kim_mühstd,foton_grades,fotonstd,enerji_grades,enerjistd,makine_grades,makinestd,biomüh_grades,biomühstd,mbg_grades,mbgstd,fizik_grades,fizikstd,malzeme_grades,malzemestd,mimar_grades,mimarstd,şbp_grades,şbpstd,entas_grades,entasstd,mat_grades,matstd,gıda_grades,gıdastd,std_dprt,inşat_grades,inşatstd

    def calculate_avg():
        data = get_list("/Users/alikemaltopak/Library/CloudStorage/OneDrive-Kişisel/VSCODE_PY/exam.txt")            # Here
        department = input("Enter your department code: ")
        dprt_avg = []
        try:
            cengavg = sum(data[2])/data[3]
            dprt_avg.append(cengavg)
        except:
            cengavg = 0
            dprt_avg.append(cengavg)
        try:
            ehmavg = sum(data[4])/data[5]
            dprt_avg.append(ehmavg)
        except:
            ehmavg = 0
            dprt_avg.append(ehmavg)
        try:    
            kimmüh_avg = sum(data[6])/data[7]
            dprt_avg.append(kimmüh_avg)
        except:
            kimmüh_avg = 0
            dprt_avg.append(kimmüh_avg)
        try:
            fotonavg = sum(data[8])/data[9]
            dprt_avg.append(fotonavg)
        except:
            fotonavg = 0
            dprt_avg.append(fotonavg)
        try:
            enerjiavg = sum(data[10])/data[11]
            dprt_avg.append(enerjiavg)
        except:
            enerjiavg = 0
            dprt_avg.append(enerjiavg)
        try:
            makineavg = sum(data[12])/data[13]
            dprt_avg.append(makineavg)
        except:
            makineavg = 0
            dprt_avg.append(makineavg)
        try:
            biomüh_avg = sum(data[14])/data[15]
            dprt_avg.append(biomüh_avg)
        except:
            biomüh_avg = 0
            dprt_avg.append(biomüh_avg)
        try:
            mbgavg = sum(data[16])/data[17]
            dprt_avg.append(mbgavg)
        except:
            mbgavg = 0
            dprt_avg.append(mbgavg)
        try:
            fizikavg = sum(data[18])/data[19]
            dprt_avg.append(fizikavg)
        except:
            fizikavg = 0
            dprt_avg.append(fizikavg)
        try:
            malzemeavg = sum(data[20])/data[21]
            dprt_avg.append(malzemeavg)
        except:
            malzemeavg = 0
            dprt_avg.append(malzemeavg)
        try:
            mimaravg = sum(data[22])/data[23]
            dprt_avg.append(mimaravg)
        except:
            mimaravg = 0
            dprt_avg.append(mimaravg)
        try:
            şbpavg = sum(data[24])/data[25]
            dprt_avg.append(şbpavg)
        except:
            şbpavg = 0
            dprt_avg.append(şbpavg)
        try:
            entasavg = sum(data[26])/data[27]
            dprt_avg.append(entasavg)
        except:
            entasavg = 0
            dprt_avg.append(entasavg)
        try:
            matavg = sum(data[28])/data[29]
            dprt_avg.append(matavg)
        except:
            matavg = 0
            dprt_avg.append(matavg)
        try:
            gıdaavg = sum(data[30])/data[31]
            dprt_avg.append(gıdaavg)
        except:
            gıdaavg = 0
            dprt_avg.append(gıdaavg)
        try:
            inşatavg = sum(data[33])/data[34]
            dprt_avg.append(inşatavg)
        except:
            inşatavg = 0
            dprt_avg.append(inşatavg)

        
        if department == "201" and cengavg != 0:
            print(f"\nFor this exam bilgisayar ortalaması {cengavg}\n")
        elif department == "201" and data[3] == 0:
            print("\nThere is no ceng student in the exam.\n")
        if department == "206" and ehmavg != 0:
            print(f"\nFor this exam ehm ortalaması {ehmavg}\n")
        elif department == "206" and data[5] == 0:
            print("\nThere is no ehm student in the exam.\n")
        if department == "202" and kimmüh_avg != 0:
            print(f"\nFor this exam1 kimya mühendisliği ortalaması {kimmüh_avg}\n")
        elif department == "202" and data[7] == 0:
            print("\nThere is no kimya müh student in the exam.\n")
        if department == "105" and fotonavg != 0:
            print(f"\nFor this exam fotonik ortalaması {fotonavg}\n")
        elif department == "105" and data[9] == 0:
            print("\nThere is no fotonik student in the exam.\n")
        if department == "209" and enerjiavg != 0:
            print(f"\nFor this exam enerji müh ortalaması {enerjiavg}\n")
        elif department == "209" and data[11] == 0:
            print("\nThere is no enerji müh student in the exam.\n")
        if department == "203" and makineavg != 0:
            print(f"\nFor this exam makine müh ortalaması {makineavg}\n")
        elif department == "203" and data[13] == 0:
            print("\nThere is no makine müh student in the exam.\n")
        if department == "210" and biomüh_avg != 0:
            print(f"\nFor this exam biyo müh ortalaması {biomüh_avg}\n")
        elif department == "210" and data[15] == 0:
            print("\nThere is no biyo müh student in the exam.\n")
        if department == "104" and mbgavg != 0:
            print(f"\nFor this exam mbg ortalaması {mbgavg}\n")
        elif department == "104" and data[17] == 0:
            print("\nThere is no mbg student in the exam.\n")
        if department == "101" and fizikavg != 0:
            print(f"\nFor this exam fizik ortalaması {fizikavg}\n")
        elif department == "101" and data[19] == 0:
            print("\nThere is no fizik student in the exam.\n")
        if department == "208" and malzemeavg != 0:
            print(f"\nFor this exam malzeme ortalaması {malzemeavg}\n")
        elif department == "208" and data[21] == 0:
            print("\nThere is no malzeme student in the exam.\n")
        if department == "301" and mimaravg != 0:
            print(f"\nFor this exam mimar ortalaması {mimaravg}\n")
        elif department == "301" and data[23] == 0:
            print("\nThere is no mimar student in the exam.\n")
        if department == "302" and şbpavg != 0:
            print(f"\nFor this exam şbp ortalaması {şbpavg}\n")
        elif department == "302" and data[25] == 0:
            print("\nThere is no şbp student in the exam.\n")
        if department == "303" and entasavg != 0:
            print(f"\nFor this exam entas ortalaması {entasavg}\n")
        elif department == "303" and data[27] == 0:
            print("\nThere is no entas student in the exam.\n")
        if department == "103" and matavg != 0:
            print(f"\nFor this exam matematik ortalaması {matavg}\n")
        elif department == "103" and data[29] == 0:
            print("\nThere is no matematik student in the exam.\n")
        if department == "205" and gıdaavg != 0:
            print(f"\nFor this exam gıda müh ortalaması {gıdaavg}\n")
        elif department == "205" and data[31] == 0:
            print("\nThere is no gıda müh student in the exam.\n")
        if department == "204" and inşatavg != 0:
            print(f"\nFor this exam inşaat müh ortalaması {inşatavg}\n")
        elif department == "204" and data[34] == 0:
            print("\nThere is no inşaat müh student in the exam.\n")
        return dprt_avg

    def totalavg(file_name):
        with open(file_name,"r") as file:
            total_grades = []
            for line in file:
                line = line.strip()
                liste = line.split()
                try:
                    grades = liste[1]
                except Exception:
                    grades = "not available because of did'n join the exam."
                try: 
                    total_grades.append(int(grades))
                except Exception:
                    pass
            result = sum(total_grades)/len(total_grades)
            return f"\nFor this exam university average is {result}\n"

    def see_yourgrade(file_name):
        with open(file_name,"r") as file:
            std_ID = input("Enter your student ID: ").strip()
            finde_grade = " "
            for line in file:
                line = line.strip()
                liste = line.split()
                stdnum = liste[0]
                try:
                    grade = liste[1]
                except Exception:
                    grade = "not available because of did'n join the exam."
                if std_ID == stdnum:
                    finde_grade = grade
                    break
            if std_ID == stdnum:
                print(f"Your grade is {finde_grade}\n")
            else:
                print("\nID not fount in file:\n")
        return finde_grade

    
    def see_arangemet(file_name):
        try:
            finde_grade = int(see_yourgrade(file_name))
        except Exception:
            finde_grade = 0
        queue = 1
        with open(file_name,"r") as file:
            for line in file:
                line = line.strip()
                liste = line.split()
                try:
                    grades = int(liste[1])
                except Exception:
                    grades = 0
                if finde_grade <= int(grades):
                    queue += 1
        return f"Your  university arangement is {queue}\n"

    def see_dep_arangement(file_name):
        finde_grade = int(see_yourgrade(file_name))
        queue = 1
        std_dprt_input = input("Enter your department code: ")
        with open(file_name,"r") as file:
            for line in file:
                line = line.strip()
                liste = line.split()
                stdID = liste[0] 
                seperate_stdID = f"{stdID[:3]},{stdID[3:6]},{stdID[6:]}"
                newstdID = stdID.replace(stdID,seperate_stdID).split(",")
                dprtcode = newstdID[1]
                try:
                    grades = liste[1] 
                except Exception:
                    grades = 0
                if std_dprt_input == dprtcode and finde_grade <= int(grades):
                    queue += 1
        return f"Your  department arangement is {queue}\n"

    def graph():
        x = ["ceng","ehm","kimmüh","foton","enerji","makine","biomüh","mbg","fizik","malzeme","mimar","şbp","entas","mat","gıda","inşaat"]
        y = calculate_avg()
        plt.bar(x,y,0.5)
        plt.show()

            
    while True:

        islem = int(input("1: See the average of exam.\n2: See your department average and graph\n3: See your grade\n4: See your university arangemen\n5: See your department arangement\n6: Exit\n"))

        if islem == 1:
            print(totalavg("/Users/alikemaltopak/Library/CloudStorage/OneDrive-Kişisel/VSCODE_PY/exam.txt"))            # Here
        elif islem == 2:
            graph()
        elif islem == 3:
            see_yourgrade("/Users/alikemaltopak/Library/CloudStorage/OneDrive-Kişisel/VSCODE_PY/exam.txt")           # Here
        elif islem == 4:
            print(see_arangemet("/Users/alikemaltopak/Library/CloudStorage/OneDrive-Kişisel/VSCODE_PY/exam.txt"))           # Here
        elif islem == 5:
            print(see_dep_arangement("/Users/alikemaltopak/Library/CloudStorage/OneDrive-Kişisel/VSCODE_PY/exam.txt"))          # Here
        else:
            break