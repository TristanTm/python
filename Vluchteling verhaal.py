def vraag1():

    print("Gelukkig je hebt het gehaald, de taliban kan ons hier niet vinden, ze weten niks van deze schuilplek. \n Het is hier wel te onveilig voor je, je kan hier niet langer blijven.")

    Vraag1 = input("Wat is je plan? A) Vluchten B) niks doen en verstoppen? C) Terug vechten tegen de taliban? ").lower()
   
    if Vraag1 == "a": 
        vraag2()
    elif Vraag1 == "b":
        print("Oh oke, nou dat was het dan hopelijk overleven we het")
    elif Vraag1 == "c":
        vraag3()


def vraag2():

        print("Oke vliegtuig of auto? het is jou keuze! ")
        Vraag2 = input(" A) Auto B) Vliegtuig ").lower()
    
        if Vraag2 == "a": 
            print("Oke we kunnen de auto pakken die voor ons huis staat")
        
        elif Vraag2 == "b":
            print("Oke top we gaan zo snel mogelijk naar het vliegveld")



def vraag3():

        print("oke we vechten terug! Gaan we andere mensen zoeken of gaan we alleen vechten?")
        Vraag2 = input(" A) Alleen B) Andere zoeken ").lower()
    
        if Vraag2 == "a": 
            pass
        elif Vraag2 == "b":
            pass 


def vraag4():

        print("Oke we gaan zoeken! ")
        Vraag2 = input(" A) Auto B) Vliegtuig ").lower()
    
        if Vraag2 == "a": 
            pass
        
        elif Vraag2 == "b":
            pass

            




      
            

vraag1()








    
    
    
  
    
    
    
    




